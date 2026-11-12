import logging

import openai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.llm import generate_answer
from app.schemas import AskRequest, AskResponse

logger = logging.getLogger(__name__)

app = FastAPI(title="Citewise")

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    # Users get a short, generic message; the real cause goes to the server log.
    # Order matters: subclasses (e.g. APITimeoutError) must come before their parents.
    try:
        answer = generate_answer(question=request.question)
    except (openai.AuthenticationError, openai.PermissionDeniedError):
        logger.exception("OpenAI rejected our credentials")
        raise HTTPException(
            status_code=500,
            detail="The service is misconfigured. Please try again later.",
        )
    except openai.RateLimitError:
        logger.exception("OpenAI rate limit or quota exceeded")
        raise HTTPException(
            status_code=503,
            detail="The service is busy. Please try again in a moment.",
        )
    except openai.APITimeoutError:
        logger.exception("OpenAI request timed out")
        raise HTTPException(
            status_code=504,
            detail="The answer took too long. Please try again.",
        )
    except openai.APIConnectionError:
        logger.exception("Could not connect to OpenAI")
        raise HTTPException(
            status_code=502,
            detail="Could not reach the AI service. Please try again.",
        )
    except openai.APIError:
        logger.exception("OpenAI request failed")
        raise HTTPException(
            status_code=502,
            detail="The AI service returned an error. Please try again.",
        )

    return AskResponse(answer=answer)

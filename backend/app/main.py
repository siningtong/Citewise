from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import AskRequest, AskResponse

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
    # Placeholder until the LLM is connected in stage 2.
    return AskResponse(answer=f"You asked: {request.question}")

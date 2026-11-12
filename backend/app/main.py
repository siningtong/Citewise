from fastapi import FastAPI

from app.schemas import AskRequest, AskResponse

app = FastAPI(title="Citewise")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    # Placeholder until the LLM is connected in stage 2.
    return AskResponse(answer=f"You asked: {request.question}")

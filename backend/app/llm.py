from openai import OpenAI

from app.config import settings

SYSTEM_PROMPT = (
    "You are a helpful assistant. Answer clearly and concisely. "
    "If you don't know the answer, say so instead of guessing."
)

# Created once and shared by every request.
client = OpenAI(api_key=settings.openai_api_key.get_secret_value())


def generate_answer(question: str) -> str:
    response = client.responses.create(
        model=settings.openai_model,
        instructions=SYSTEM_PROMPT,
        input=question,
    )
    return response.output_text

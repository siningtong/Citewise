from openai import OpenAI

from app.config import settings

SYSTEM_PROMPT = (
    "You are a helpful assistant. Answer clearly and concisely. "
    "If you don't know the answer, say so instead of guessing."
)

# Created once and shared by every request.
# The SDK default read timeout is 10 minutes; a user won't wait that long.
client = OpenAI(
    api_key=settings.openai_api_key.get_secret_value(),
    timeout=30.0,
)


def generate_answer(question: str) -> str:
    response = client.responses.create(
        model=settings.openai_model,
        instructions=SYSTEM_PROMPT,
        input=question,
    )
    return response.output_text

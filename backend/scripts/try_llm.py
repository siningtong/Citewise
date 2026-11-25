"""Send one question to OpenAI and print the answer.

Run from the backend/ directory:
    python -m scripts.try_llm
"""

from openai import OpenAI

from app.config import settings

client = OpenAI(api_key=settings.openai_api_key.get_secret_value())

response = client.responses.create(
    model=settings.openai_model,
    instructions="Answer in one short sentence.",
    input="What is RAG?",
)

print(response.output_text)

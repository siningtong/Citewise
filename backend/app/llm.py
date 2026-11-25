import logging
import time

from openai import OpenAI

from app.config import settings

logger = logging.getLogger(__name__)

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
    start = time.perf_counter()
    response = client.responses.create(
        model=settings.openai_model,
        instructions=SYSTEM_PROMPT,
        input=question,
        reasoning={"effort": settings.openai_reasoning_effort},
    )
    latency_ms = (time.perf_counter() - start) * 1000

    # Log usage and timing only, never the question or answer text.
    usage = response.usage
    if usage is not None:
        logger.info(
            "OpenAI call model=%s effort=%s input_tokens=%d output_tokens=%d "
            "reasoning_tokens=%d latency_ms=%.0f",
            settings.openai_model,
            settings.openai_reasoning_effort,
            usage.input_tokens,
            usage.output_tokens,
            usage.output_tokens_details.reasoning_tokens,
            latency_ms,
        )

    return response.output_text

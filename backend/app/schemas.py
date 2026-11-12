from pydantic import BaseModel, ConfigDict, Field


class AskRequest(BaseModel):
    # Strip leading/trailing whitespace so "   " counts as empty.
    model_config = ConfigDict(str_strip_whitespace=True)

    question: str = Field(min_length=1, max_length=1000)


class AskResponse(BaseModel):
    answer: str

from pydantic import BaseModel


class TranscribeResponse(BaseModel):

    success: bool

    language: str

    language_probability: float

    transcript: str
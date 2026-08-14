from pydantic import BaseModel


class DetectResponse(BaseModel):

    success: bool

    sound: str

    confidence: float

    is_emergency: bool

    next_action: str
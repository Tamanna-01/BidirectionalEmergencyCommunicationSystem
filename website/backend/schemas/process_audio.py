from pydantic import BaseModel
from typing import Optional


class ProcessAudioResponse(BaseModel):
    """
    Response returned by the complete EchoSafe AI pipeline.
    """

    success: bool

    # Model 1
    sound: str
    confidence: float
    is_emergency: bool

    # Model 2
    transcript: Optional[str] = None

    # Model 3
    simplified_text: Optional[str] = None

    # Performance
    processing_time_ms: float
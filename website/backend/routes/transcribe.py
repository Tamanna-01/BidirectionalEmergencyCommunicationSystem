import os
import shutil
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException

from schemas.transcribe import TranscribeResponse
from services.whisper_service import WhisperService

router = APIRouter(
    prefix="/transcribe",
    tags=["Speech To Text"]
)


@router.post(
    "/",
    response_model=TranscribeResponse
)
async def transcribe_audio(
    file: UploadFile = File(...)
):

    if not file.filename.lower().endswith(".wav"):
        raise HTTPException(
            status_code=400,
            detail="Only WAV files are supported."
        )

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    try:

        with temp_file as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = WhisperService.transcribe(
            temp_file.name
        )

        return TranscribeResponse(
            success=True,
            language=result["language"],
            language_probability=result["language_probability"],
            transcript=result["transcript"]
        )

    finally:

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
import os
import shutil
import tempfile
import time

from fastapi import APIRouter, File, HTTPException, UploadFile

from schemas.process_audio import ProcessAudioResponse
from services.emergency_detection_service import EmergencyDetectionService
from services.whisper_service import WhisperService
from services.flant5_service import FlanT5Service


router = APIRouter(
    prefix="/process-audio",
    tags=["Complete AI Pipeline"]
)


@router.post(
    "/",
    response_model=ProcessAudioResponse
)
async def process_audio(
    file: UploadFile = File(...)
):
    """
    Complete EchoSafe AI Pipeline

    Audio
        ↓
    Emergency Detection
        ↓
    If Emergency
            ↓
        Whisper STT
            ↓
        FLAN-T5 Simplification
    """

    start_time = time.perf_counter()

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

        audio_path = temp_file.name

        # ----------------------------------------------------
        # Model 1 : Emergency Sound Detection
        # ----------------------------------------------------

        detection = EmergencyDetectionService.detect(audio_path)

        # ----------------------------------------------------
        # No Emergency
        # ----------------------------------------------------

        if not detection["is_emergency"]:

            elapsed = round(
                (time.perf_counter() - start_time) * 1000,
                2
            )

            return ProcessAudioResponse(
                success=True,

                sound=detection["sound"],
                confidence=detection["confidence"],
                is_emergency=False,

                transcript=None,
                simplified_text=None,

                processing_time_ms=elapsed
            )

        # ----------------------------------------------------
        # Model 2 : Whisper Speech-to-Text
        # ----------------------------------------------------

        whisper_result = WhisperService.transcribe(audio_path)

        transcript = whisper_result["transcript"]

        # ----------------------------------------------------
        # Model 3 : FLAN-T5 Simplification
        # ----------------------------------------------------

        simplified = FlanT5Service.simplify(
            transcript
        )

        elapsed = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        return ProcessAudioResponse(
            success=True,

            sound=detection["sound"],
            confidence=detection["confidence"],
            is_emergency=True,

            transcript=transcript,
            simplified_text=simplified,

            processing_time_ms=elapsed
        )

    finally:

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
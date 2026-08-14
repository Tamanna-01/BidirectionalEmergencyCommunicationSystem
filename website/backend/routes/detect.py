import os
import shutil
import tempfile

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from schemas.detect import DetectResponse

from services.audio_processor import AudioProcessor
from services.embedding_service import EmbeddingService
from services.classifier_service import ClassifierService
from services.emergency_detection_service import EmergencyDetectionService

router = APIRouter(
    prefix="/detect",
    tags=["Emergency Detection"]
)


@router.post(
    "/",
    response_model=DetectResponse
)
async def detect_sound(
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
            shutil.copyfileobj(
                file.file,
                buffer
            )

        result = EmergencyDetectionService.detect(
            temp_file.name
        )

        return DetectResponse(
            success=True,
            sound=result["sound"],
            confidence=result["confidence"],
            is_emergency=result["is_emergency"],
            next_action=result["next_action"]
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
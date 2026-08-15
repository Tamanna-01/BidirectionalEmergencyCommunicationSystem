from fastapi import APIRouter, File, UploadFile, HTTPException
import time

from services.gesture_service import process_gesture_video


router = APIRouter()


@router.post("/gesture-detection")
async def gesture_detection(
    file: UploadFile = File(...)
):
    """
    Process an uploaded gesture video
    using Model 3.
    """

    start_time = time.perf_counter()

    try:

        # ----------------------------------------------------
        # Validate file
        # ----------------------------------------------------

        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="No video file provided."
            )

        # ----------------------------------------------------
        # Validate extension
        # ----------------------------------------------------

        allowed_extensions = {
            ".mp4",
            ".webm",
            ".mov",
            ".avi",
            ".mkv",
        }

        filename = file.filename

        extension = (
            "." + filename.split(".")[-1].lower()
            if "." in filename
            else ""
        )

        if extension not in allowed_extensions:

            raise HTTPException(
                status_code=400,
                detail=(
                    "Unsupported video format. "
                    "Please upload MP4, WebM, MOV, AVI, "
                    "or MKV."
                )
            )

        # ----------------------------------------------------
        # Read uploaded video
        # ----------------------------------------------------

        video_bytes = await file.read()

        if not video_bytes:

            raise HTTPException(
                status_code=400,
                detail="Uploaded video is empty."
            )

        # ----------------------------------------------------
        # Process video
        # ----------------------------------------------------

        result = process_gesture_video(
            video_bytes,
            filename
        )

        # ----------------------------------------------------
        # Processing time
        # ----------------------------------------------------

        processing_time_ms = (
            time.perf_counter() - start_time
        ) * 1000

        # ----------------------------------------------------
        # Response
        # ----------------------------------------------------

        return {
            "success": True,

            "gesture": result["gesture"],

            "confidence": result["confidence"],

            "recognized": result["recognized"],

            "processing_time_ms": round(
                processing_time_ms,
                2
            ),
        }

    except HTTPException:
        raise

    except Exception as exc:

        print(
            "Gesture detection error:",
            str(exc)
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "Gesture detection failed: "
                f"{str(exc)}"
            )
        )

    finally:

        await file.close()
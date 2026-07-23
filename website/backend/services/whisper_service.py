from core.model_manager import ModelManager


class WhisperService:

    @staticmethod
    def transcribe(audio_path: str):

        segments, info = ModelManager.whisper.transcribe(
            audio_path,
            beam_size=5,
            language="en"
        )

        transcript = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return {
            "language": info.language,
            "language_probability": round(info.language_probability, 3),
            "transcript": transcript.strip()
        }
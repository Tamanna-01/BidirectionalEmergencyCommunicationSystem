from services.audio_processor import AudioProcessor
from services.embedding_service import EmbeddingService
from services.classifier_service import ClassifierService


class EmergencyDetectionService:
    """
    Executes the complete Emergency Sound Detection pipeline.

    Pipeline:
        Audio File
            ↓
        Audio Preprocessing
            ↓
        YAMNet Embeddings
            ↓
        Fine-tuned Classifier
            ↓
        Prediction
    """

    @staticmethod
    def detect(audio_path: str) -> dict:
        """
        Detect emergency sound from an audio file.

        Parameters
        ----------
        audio_path : str
            Path to the WAV audio file.

        Returns
        -------
        dict
            {
                "sound": str,
                "confidence": float,
                "is_emergency": bool,
                "next_action": str
            }
        """

        # Step 1: Preprocess audio
        waveform = AudioProcessor.preprocess(audio_path)

        # Step 2: Extract embeddings
        embedding = EmbeddingService.extract(waveform)

        # Step 3: Predict sound class
        prediction = ClassifierService.predict(embedding)

        return prediction
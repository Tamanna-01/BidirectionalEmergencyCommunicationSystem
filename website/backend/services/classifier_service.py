import numpy as np

from core.model_manager import ModelManager


class ClassifierService:

    @staticmethod
    def predict(embedding):

        embedding = np.expand_dims(
            embedding,
            axis=0
        )

        prediction = ModelManager.emergency_classifier.predict(
            embedding,
            verbose=0
        )[0]

        index = np.argmax(prediction)

        sound = str(
            ModelManager.class_names[index]
        )

        confidence = round(
            float(prediction[index] * 100),
            2
        )

        is_emergency = sound != "Ambient_Noise"

        next_action = (
            "speech_to_text"
            if is_emergency
            else "continue_monitoring"
        )

        return {
            "sound": sound,
            "confidence": confidence,
            "is_emergency": is_emergency,
            "next_action": next_action
        }
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from faster_whisper import WhisperModel

from core.config import (
    MODEL1_PATH,
    CLASS_NAMES_PATH,
    WHISPER_MODEL_DIR,
    GESTURE_MODEL_PATH,
)

from core.model_manager import ModelManager

# Import the custom FLAN loader
from services.flant5_service import load_model as load_flan_model


def load_models():

    # -------------------------------------------------------
    # YAMNet
    # -------------------------------------------------------

    print("=" * 60)
    print("Loading YAMNet...")

    ModelManager.yamnet = hub.load(
        "https://tfhub.dev/google/yamnet/1"
    )

    print("✓ YAMNet Loaded")

    # -------------------------------------------------------
    # Emergency Classifier - Model 1
    # -------------------------------------------------------

    print("=" * 60)
    print("Loading Emergency Classifier...")

    ModelManager.emergency_classifier = tf.keras.models.load_model(
        MODEL1_PATH,
        compile=False
    )

    ModelManager.class_names = np.load(
        CLASS_NAMES_PATH,
        allow_pickle=True
    )

    ModelManager.model1_loaded = True

    print("✓ Emergency Sound Model Loaded")

    # -------------------------------------------------------
    # Whisper
    # -------------------------------------------------------

    print("=" * 60)
    print("Loading Whisper...")

    ModelManager.whisper = WhisperModel(
        str(WHISPER_MODEL_DIR),
        device="cpu",
        compute_type="int8"
    )

    ModelManager.whisper_loaded = True

    print("✓ Whisper Loaded")

    # -------------------------------------------------------
    # FLAN-T5 - Model 2
    # -------------------------------------------------------

    print("=" * 60)
    print("Loading FLAN-T5...")

    load_flan_model()

    ModelManager.model2_loaded = True

    print("✓ FLAN-T5 Loaded")

    # -------------------------------------------------------
    # ISL Gesture Recognition - Model 3
    # -------------------------------------------------------

    print("=" * 60)
    print("Loading ISL Gesture Recognition Model...")

    ModelManager.gesture_model = tf.keras.models.load_model(
        GESTURE_MODEL_PATH,
        compile=False,
    )

    ModelManager.model3_loaded = True

    print("✓ ISL Gesture Recognition Model Loaded")

    print(
        f"✓ Gesture Model Input Shape: "
        f"{ModelManager.gesture_model.input_shape}"
    )

    print(
        f"✓ Gesture Model Output Shape: "
        f"{ModelManager.gesture_model.output_shape}"
    )

    # -------------------------------------------------------
    # Complete
    # -------------------------------------------------------

    print("=" * 60)
    print("All AI Models Loaded Successfully!")
    print("=" * 60)
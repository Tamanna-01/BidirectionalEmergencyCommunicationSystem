import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

from faster_whisper import WhisperModel

from core.config import (
    MODEL1_PATH,
    CLASS_NAMES_PATH,
    WHISPER_MODEL_DIR
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
    # Emergency Classifier
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
    # FLAN-T5
    # -------------------------------------------------------

    load_flan_model()

    print("=" * 60)
    print("All AI Models Loaded Successfully!")
    print("=" * 60)
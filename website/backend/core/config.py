from pathlib import Path


# ============================================================
# Project Directories
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(exist_ok=True)


# ============================================================
# Model 1 - Emergency Sound Detection
# ============================================================

MODEL1_PATH = (
    r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project"
    r"\ProjectCode\BidirectionalEmergencyCommunicationSystem"
    r"\model1\emergency_sound_model.h5"
)

CLASS_NAMES_PATH = (
    r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project"
    r"\ProjectCode\BidirectionalEmergencyCommunicationSystem"
    r"\model1\class_names.npy"
)


# ============================================================
# Model 2 - FLAN-T5 Emergency Phrase Simplification
# ============================================================

MODEL2_PATH = (
    r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project"
    r"\ProjectCode\BidirectionalEmergencyCommunicationSystem"
    r"\model2\best-emergency-simplifier"
)


# ============================================================
# Whisper
# ============================================================

WHISPER_MODEL_DIR = (
    r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project"
    r"\ProjectCode\BidirectionalEmergencyCommunicationSystem"
    r"\whispermodel\faster-whisper"
)


# ============================================================
# FLAN-T5 Local Model
# ============================================================

BASE_FLAN_MODEL_PATH = (
    r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project"
    r"\ProjectCode\BidirectionalEmergencyCommunicationSystem"
    r"\flant_model_local"
)


# ============================================================
# Model 3 - Indian Sign Language Recognition
# ============================================================

GESTURE_MODEL_PATH = (
    r"C:\Users\Tamanna Shaw\Downloads\IIIT-Dharwad\Project"
    r"\ProjectCode\BidirectionalEmergencyCommunicationSystem"
    r"\model3\action.keras"
)


# ============================================================
# Gesture Recognition Configuration
# ============================================================

GESTURE_SEQUENCE_LENGTH = 90

GESTURE_FEATURES_PER_FRAME = 126

GESTURE_CONFIDENCE_THRESHOLD = 0.80


GESTURE_ACTIONS = [
    "HELP",
    "CALL_AMBULANCE",
    "FIRE",
    "CALL_DOCTOR",
    "STOP_DANGER",
]
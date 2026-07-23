from pathlib import Path

# ==========================
# Project Directories
# ==========================

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(exist_ok=True)

# ==========================
# Model Paths
# Update these paths according to your machine
# ==========================

MODEL1_PATH = r"C:\\Users\\Tamanna Shaw\\Downloads\\IIIT-Dharwad\\Project\\ProjectCode\\BidirectionalEmergencyCommunicationSystem\\model1\\emergency_sound_model.h5"

CLASS_NAMES_PATH = r"C:\\Users\\Tamanna Shaw\\Downloads\\IIIT-Dharwad\\Project\\ProjectCode\\BidirectionalEmergencyCommunicationSystem\\model1\\class_names.npy"

MODEL2_PATH = r"C:\\Users\\Tamanna Shaw\\Downloads\\IIIT-Dharwad\\Project\\ProjectCode\\BidirectionalEmergencyCommunicationSystem\\model2\\best-emergency-simplifier"

WHISPER_MODEL_DIR = r"C:\\Users\\Tamanna Shaw\\Downloads\\IIIT-Dharwad\\Project\\ProjectCode\\BidirectionalEmergencyCommunicationSystem\\whispermodel\\faster-whisper"

BASE_FLAN_MODEL_PATH = r"C:\\Users\\Tamanna Shaw\\Downloads\\IIIT-Dharwad\\Project\\ProjectCode\\BidirectionalEmergencyCommunicationSystem\\flant_model_local"
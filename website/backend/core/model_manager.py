class ModelManager:
    """
    Stores all loaded AI models in memory.
    """

    # -----------------------------
    # Model 1 - Emergency Detection
    # -----------------------------
    yamnet = None
    emergency_classifier = None
    class_names = None

    # -----------------------------
    # Whisper
    # -----------------------------
    whisper = None

    # -----------------------------
    # Model 2 - FLAN-T5
    # -----------------------------
    flan_model = None
    flan_tokenizer = None

    # -----------------------------
    # Model 3 - ISL Gesture Recognition
    # -----------------------------
    gesture_model = None

    # -----------------------------
    # Status
    # -----------------------------
    model1_loaded = False
    whisper_loaded = False
    model2_loaded = False
    model3_loaded = False
class ModelManager:
    """
    Stores all loaded AI models in memory.
    """

    # -----------------------------
    # Model 1
    # -----------------------------
    yamnet = None
    emergency_classifier = None
    class_names = None

    # -----------------------------
    # Whisper
    # -----------------------------
    whisper = None

    # -----------------------------
    # Model 2
    # -----------------------------
    flan_model = None
    flan_tokenizer = None

    # -----------------------------
    # Status
    # -----------------------------
    model1_loaded = False
    whisper_loaded = False
    model2_loaded = False
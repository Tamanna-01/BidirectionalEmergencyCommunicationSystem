import os

from safetensors.torch import load_file
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from core.config import MODEL2_PATH, BASE_FLAN_MODEL_PATH
from core.model_manager import ModelManager


def load_model():
    """
    Load the fine-tuned FLAN-T5 model.
    """

    print("=" * 50)
    print("Loading FLAN-T5...")

    # Load tokenizer from fine-tuned model
    ModelManager.flan_tokenizer = AutoTokenizer.from_pretrained(
        MODEL2_PATH
    )

    # Load base FLAN-T5 architecture
    ModelManager.flan_model = AutoModelForSeq2SeqLM.from_pretrained(
        BASE_FLAN_MODEL_PATH
    )

    # Load fine-tuned weights
    safetensor_path = os.path.join(
        MODEL2_PATH,
        "model.safetensors"
    )

    state_dict = load_file(safetensor_path)

    ModelManager.flan_model.load_state_dict(
        state_dict,
        strict=False
    )

    ModelManager.model2_loaded = True

    print("✓ FLAN-T5 Loaded")
    print("=" * 50)


class FlanT5Service:

    @staticmethod
    def simplify(text: str) -> str:

        if text is None or text.strip() == "":
            return ""

        tokenizer = ModelManager.flan_tokenizer
        model = ModelManager.flan_model

        # SAME PROMPT USED DURING TRAINING
        prompt = (
            "Simplify this emergency instruction into concise, actionable phrases:"
            f"{text}"
        )

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=128
        )

        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=32,
            num_beams=4,
            early_stopping=True
        )

        result = tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return result.strip()
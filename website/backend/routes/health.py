from fastapi import APIRouter

from core.model_manager import ModelManager

router = APIRouter()


@router.get("/health")
def health():

    return {

        "status": "running",

        "model1_loaded": ModelManager.model1_loaded,

        "model2_loaded": ModelManager.model2_loaded

    }
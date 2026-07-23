from contextlib import asynccontextmanager

from fastapi import FastAPI

from routes.health import router as health_router

from routes.detect import router as detect_router

from services.model_loader import load_models

from routes.transcribe import router as transcribe_router

from routes.process_audio import router as process_audio_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting EchoSafe...")
    load_models()

    print("All AI models loaded successfully!")

    yield

    print("Shutting down EchoSafe...")


app = FastAPI(
    title="EchoSafe API",
    version="1.0.0",
    description="AI Powered Emergency Communication System",
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(detect_router)
app.include_router(transcribe_router)
app.include_router(process_audio_router)


@app.get("/")
def home():
    return {
        "application": "EchoSafe",
        "version": "1.0.0"
    }
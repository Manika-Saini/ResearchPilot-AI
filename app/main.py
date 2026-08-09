from fastapi import FastAPI

from app.api.routes.health import router as health_router


app = FastAPI(
    title="ResearchPilot AI",
    description="AI-powered research assistant for analyzing and interacting with research papers.",
    version="0.1.0"
)

app.include_router(health_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to ResearchPilot AI",
        "status": "running"
    }

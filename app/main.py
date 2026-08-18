from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.users import router as users_router

app = FastAPI(
    title="ResearchPilot AI",
    description="AI-powered research assistant backend",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(users_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to ResearchPilot AI",
        "status": "running"
    }

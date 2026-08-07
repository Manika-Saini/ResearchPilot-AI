from fastapi import FastAPI

app = FastAPI(
    title="ResearchPilot AI",
    description="AI-powered research assistant for analyzing and interacting with research papers.",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to ResearchPilot AI",
        "status": "running"
    }
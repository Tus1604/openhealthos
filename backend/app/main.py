from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ImmuCore",
    description="Privacy focused personal health operating system.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": "ImmuCore",
        "database": "connected"
    }


@app.get("/")
def read_root():
    return {"message": "Welcome to ImmuCore! Your FastAPI server is running perfectly."}
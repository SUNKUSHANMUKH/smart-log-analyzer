from fastapi import FastAPI
import random
from ai_analyzer.analyzer import analyze_log

app = FastAPI()

from fastapi.responses import FileResponse

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/simulate")
def simulate():
    events = [
        "INFO: User login successful",
        "ERROR: Database connection timeout",
        "CRITICAL: Service crashed unexpectedly"
    ]

    log = random.choice(events)

    print("🔥 Calling AI with:", log)

    analysis = analyze_log(log)

    return {
        "log": log,
        "analysis": analysis
    }
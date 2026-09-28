from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="POC Kubernetes API")

@app.get("/")
def root():
    return {
        "application": "poc-kubernetes",
        "status": "running"
    }

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

Instrumentator().instrument(app).expose(app)

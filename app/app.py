from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "k8s-poc",
        "message": "Kubernetes local funcionando!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/ready")
def ready():
    return {"status": "ready"}

@app.route("/metrics")
def metrics():
    return "# Metrics endpoint\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

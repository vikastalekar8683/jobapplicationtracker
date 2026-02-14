from fastapi import FastAPI
import os
import sys

# Ensure the root directory is in sys.path so we can import 'backend'
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.main import app

# Keep the connection alive for serverless function (optional, not strictly necessary for Vercel)
# Adjust root path for Vercel if needed
if os.environ.get("VERCEL"):
    # If routed via rewrites like /api/* -> /api/index.py, the path received by app includes /api.
    # So we tell FastAPI the root path is /api so it strips it for route matching.
    app.root_path = "/api"

# Serve the app
# Use 'app' variable directly as Vercel detects it.

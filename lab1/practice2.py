============================================================
Practice 2 — Running FastAPI via Python Script
============================================================
from fastapi import FastAPI
import uvicorn

# TODO: Initialize a FastAPI app instance
app = FastAPI()

# TODO: Complete the main block below to run the app
if __name__ == "__main__":
    # TODO: Call uvicorn.run() with:
    #       - app  → your FastAPI instance
    #       - host → "127.0.0.1"
    #       - port → 8080
    uvicorn.run(app, host="127.0.0.1", port=8080)
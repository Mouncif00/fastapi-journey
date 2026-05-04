from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mini Project 4 Running"}
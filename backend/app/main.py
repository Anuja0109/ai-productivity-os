from fastapi import FastAPI
from app.core.database import engine

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running 🚀"}

@app.get("/db-check")
def db_check():
    try:
            connection = engine.connect()
            return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "error": str(e)}
from fastapi import FastAPI
from env import SETTINGS

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

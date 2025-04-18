from fastapi import FastAPI
import random

app = FastAPI()

#127.0.0.1:8000
@app.get("/")
async def root():
    return  {"message": "Hello World"}

@app.get("/teste")
async def ola():
    return  {"message": True, "num_aleatorio": random.randint(0, 100)}
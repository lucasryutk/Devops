from fastapi import FastAPI

app = FastAPI()

@app.get("/endpoint1")
async def root():
    return  {"message": "Hello World"}

@app.get("/endpoint2")
async def ola():
    return  {"message": "deu certo"}
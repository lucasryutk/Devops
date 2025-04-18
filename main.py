from fastapi import FastAPI

app = FastAPI()

#127.0.0.1:8000
@app.get("/")
async def root():
    return  {"message": "Hello World"}

@app.get("/teste")
async def ola():
    return  {"message": "deu certo"}
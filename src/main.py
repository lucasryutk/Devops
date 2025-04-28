from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

#127.0.0.1:8000
@app.get("/")
async def root():
    return  {"message": "Hello World"}

@app.get("/teste")
async def funcaoteste():
    return  {"message": True, "num_aleatorio": random.randint(0, 1000)}

@app.post("/estudante/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.get("/estudante/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudante/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

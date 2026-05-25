from fastapi import FastAPI
from app.schemas import Cadastro, ResponseSchema, Cadastro_carro


app = FastAPI()


database = []


@app.get("/")
async def home():
    return{
        "status": "success",
         "message": "welcone to the course."
    }


@app.post("/cadastrar", response_model=ResponseSchema)
async def criar_cadastro(payload: Cadastro):
    dados = {
        "nome": payload.nome,
        "cpf": payload.cpf,
        "data_nascimento": payload.data_nascimento,
        "telefone": payload.telefone
    }

    database.append(dados)
    return{
        "status": "success"
    }

@app.get("/cadastros", response_model=list[Cadastro])
async def listar_cadastros():
    return database

@app.post("/cadastrar_carro")
async def cadastrar_carro(payload: Cadastro_carro):
    dados = {
        "modelo": payload.modelo,
        "marca": payload.marca,
        "placa": payload.placa,
        "ano": payload.ano
    }

    database.append(dados)
    return database
    

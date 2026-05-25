from pydantic import (BaseModel)
from typing import Optional

class Cadastro(BaseModel):
    nome: str
    cpf: str
    data_nascimento: str
    telefone: str
    
class ResponseSchema(BaseModel):
    status: str
    message : Optional[str] = None

class Cadastro_carro(BaseModel):
    modelo: str
    marca: str
    placa: str
    ano: int

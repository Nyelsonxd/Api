# Passo a passo
## 1. Configuração do ambiente
- Instale o Python 3.12
- Crie um ambiente virtual:
  ```bash
  py -3.12 -m venv venv
  ```
- Ative o ambiente virtual:
  - No Windows:
    ```bash
    venv\Scripts\activate
    ```
  - No macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
## 2. Instalação das dependências
- Instale as dependências necessárias:
  ```bash
  pip install -r requirements.txt
  ```
- Caso sem o requirements.txt, instale as seguintes bibliotecas:
  ```bash
  pip install fastapi uvicorn
  ```
## 3. Dicas de Inicialização
- Diretórios padrões:
  - `app/`: Contém o código da aplicação.
    - `main.py`: Ponto de entrada da aplicação.
      - Importar o FastAPI e criar uma instância da aplicação.
        ```python
          from fastapi import FastAPI

          app = FastAPI()

          @app.get("/")
          async def read_root():
              return {"Hello": "World"}
        ```
    - `schemas.py`: Definição dos modelos de dados.
      - Importar BaseModel do Pydantic e criar modelos de dados.
        ```python
          from pydantic import BaseModel

          class Item(BaseModel):
              name: str
              price: float
              is_offer: bool = None
        ```
## 4. Execução da aplicação
- Execute a aplicação usando o Uvicorn:
  ```bash
  uvicorn app.main:app --reload
  ```
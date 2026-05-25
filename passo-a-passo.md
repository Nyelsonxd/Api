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

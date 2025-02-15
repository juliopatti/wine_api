# wine_api
Repositório destinado ao trabalho da disciplina de Confecção de APIs da pós-graduação em Sistemas e Agentes Inteligentes da UFG.

# Windows Tutorial
## Ambiente desenvolvido com Python 3.11.9

Para instalação em Windows, siga os passos abaixo:

1. Clone o diretório:
    ```bash
    git clone <URL_DO_REPOSITÓRIO>
    ```
2. Entre na pasta do projeto pelo terminal:
    ```bash
    cd wine_api
    ```
3. Crie um ambiente virtual:
    ```bash
    python3.11 -m venv venv
    ```
4. Ative o ambiente virtual:
    ```bash
    .\venv\Scripts\activate
    ```
5. Atualize o pip (boa prática):
    ```bash
    python.exe -m pip install --upgrade pip
    ```
6. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
7. Crie um arquivo `.env` com os campos `FLASK_APP`, `FLASK_DEBUG`, `API_TOKEN` ou outros que julgar necessário:
    ```env
    # Exemplo para debug
    FLASK_APP=app
    FLASK_DEBUG=1
    API_TOKEN=XXXXXX
    ```
    **OBS:** Não deixe sua `API_TOKEN` visível no código!

## Rodar a API localmente

Na pasta do projeto, você pode subir a API localmente com o comando:
```bash
flask run
```
Por padrão, você deve ver a mensagem informando que a aplicação está rodando em `http://127.0.0.1:5000`.

## Documentação pelo Swagger

Você pode obter mais detalhes da documentação pelo Swagger quando a API estiver rodando localmente. A documentação está configurada para estar em `http://127.0.0.1:5000/swagger-ui`.



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



# Linux/MAC Tutorial (Gerado pelo Copilot)

## Ambiente desenvolvido com Python 3.11.9

### Instalação no Linux e macOS

Siga os passos abaixo para instalar em um ambiente Linux ou macOS:

1. Clone o diretório:
    ```bash
    git clone <URL_DO_REPOSITÓRIO>
    ```
2. Entre na pasta do projeto pelo terminal:
    ```bash
    cd wine_api
    ```
3. Crie um ambiente virtual:
    ```bash
    python3.11 -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Linux:
        ```bash
        source venv/bin/activate
        ```
    - No macOS:
        ```bash
        source venv/bin/activate
        ```
5. Atualize o pip (boa prática):
    ```bash
    python -m pip install --upgrade pip
    ```
6. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
7. Crie um arquivo `.env` com os campos `FLASK_APP`, `FLASK_DEBUG`, `API_TOKEN` ou outros que julgar necessário:
    ```env
    # Exemplo para debug
    FLASK_APP=app
    FLASK_DEBUG=1
    API_TOKEN=XXXXXX
    ```
    **OBS:** Não deixe sua `API_TOKEN` visível no código!

## Rodar a API localmente

Na pasta do projeto, você pode subir a API localmente com o comando:
```bash
flask run
```
Por padrão, você deve ver a mensagem informando que a aplicação está rodando em `http://127.0.0.1:5000`.

## Documentação pelo Swagger

Você pode obter mais detalhes da documentação pelo Swagger quando a API estiver rodando localmente. A documentação está configurada para estar em `http://127.0.0.1:5000/swagger-ui`.


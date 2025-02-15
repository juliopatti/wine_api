# wine_api
Repositorio destinado ao trabalho da disciplina de confecção de APIs da pós-graduação de Sistemas e Agentes Inteligentes da UFG

# Ambiente desenvolvido com Python 3.11.9
Para instação em windows, por exemplo, voce pode seguir os seguintes passos:

 1- Clone o diretório
 2- entre na pasta do projeto pelo terminal
 3- Crie um ambiente virtual
    - python3.11 -m venv venv
 4- Ative o ambiente virtual
    - .\venv\Scripts\activate
 5- É uma boa pratica atualizar o pip
    - python.exe -m pip install --upgrade pip
 6- Instale as dependências
    - pip install -r requirements.txt
 7- crie um arquivo ".env" para os campos FLASK_APP, FLASK_DEBUG, API_TOKEN ou demais que julgar necessário
    Ex: caso esteja debugando
    FLASK_APP=app
    FLASK_DEBUG=1
    API_TOKEN=XXXXXX

8- OBS: Não deixe sua API_TOKEN visível no código!

# Rodar a API localmente
Na pasta do projeto, voce pode subir a API localmente pelo comando:
    - flask run
 
 Por padrão, voce deve receber a mensagem que está rodando em http://127.0.0.1:5000

# Voce pode obter mais detalhes da documentação pelo Swagger, quando a API estiver rodando localmente.
Foi configurado para estar em http://127.0.0.1:5000/swagger-ui


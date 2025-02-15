from dotenv import load_dotenv
from flask_smorest import abort
import os

def verify_authorization(token_api):
    if os.getenv("API_TOKEN")!=token_api:
        abort(401, message="API TOKEN inválido!")




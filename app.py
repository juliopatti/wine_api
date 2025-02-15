from flask import Flask, request
from flask_smorest import Api
import pickle
import pandas as pd
from resources.recommendation import blp as RecommendationBluePrint
from resources.predict_class import blp as PredictionBluePrint
from resources.regression import blp as RegressionBluePrint

def create_app():
    app = Flask(__name__)
    app.config['API_TITLE'] = "Wine API"
    app.config['API_VERSION'] = "v3"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" # http://127.0.0.1:5000/swagger-ui
    app.config["OPENAPI_SWAGGER_UI_URL"] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    app.config["PROPAGATE_EXCEPTIONS"] = True

    api = Api(app)
    api.register_blueprint(RecommendationBluePrint)
    api.register_blueprint(PredictionBluePrint)
    api.register_blueprint(RegressionBluePrint)
    
    return app

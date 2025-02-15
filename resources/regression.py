from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
import logging
from ml_models.models import RegressionWineModel
from schemas import BlindClassificationWine, RegressPredictionOutput, RegressPredictionInput
from utils import verify_authorization
import os


blp = Blueprint("Regression", __name__, description="Predição da nota de um vinho [0 a 10]")

@blp.route("/regression") # http://127.0.0.1:5000/predict
class RegressionWinePredictor(MethodView):
    @blp.arguments(RegressPredictionInput) 
    @blp.response(201, RegressPredictionOutput)
    def post(self, request_data):    
        
        # Verificação de segurança
        logging.info('\nVerificacao de Seguranca no RegressionWinePredictor')
        verify_authorization(request.headers.get('Authorization'))
        
        df_sample = pd.DataFrame([request_data])
        predict_model = RegressionWineModel('regression_model.pkl')
        
        logging.info('\n\n\nPredicao do modelo de REGRESSAO\n\n\n')
        pred = predict_model.predict(df_sample)
        return pred.to_dict(orient='records')[0]
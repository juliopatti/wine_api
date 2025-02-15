from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
import logging
from ml_models.models import WineModel
from schemas import BlindClassificationWine, ClassifierPredictionWineOutput, ClassifierPredictionWineInput
from utils import verify_authorization
import os

blp = Blueprint("Prediction", __name__, description="Predizer se um vinho é bom ou ruim.")

@blp.route("/predict") # http://127.0.0.1:5000/predict
class WinePredictor(MethodView):
    @blp.arguments(ClassifierPredictionWineInput)     
    @blp.response(201, ClassifierPredictionWineOutput)
    def post(self, request_data):   
        
        # Verificação de segurança
        logging.info('\nVerificacao de Seguranca no WinePredictor')
        verify_authorization(request.headers.get('Authorization'))
        
        df_sample = pd.DataFrame([request_data])
        predict_model = WineModel('predict_model.pkl')
        
        logging.info('Predicao do modelo WinePredictor')
        pred = predict_model.predict(df_sample)
        return pred




from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
from ml_models.models import WineModel
from schemas import BlindClassificationWine, ClassifierPredictionWineOutput, ClassifierPredictionWineInput

blp = Blueprint("Prediction", __name__, description="Predizer se um vinho é bom ou ruim.")

@blp.route("/predict") # http://127.0.0.1:5000/predict
class WinePredictor(MethodView):
    @blp.arguments(ClassifierPredictionWineInput)     
    @blp.response(201, ClassifierPredictionWineOutput)
    def post(self, request_data):    
        df_sample = pd.DataFrame([request_data])
        predict_model = WineModel('predict_model.pkl')
        pred = predict_model.predict(df_sample)
        return pred


from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
from ml_models.models import RegressionWineModel
from schemas import BlindClassificationWine, RegressPredictionOutput, RegressPredictionInput


blp = Blueprint("Regression", __name__, description="Predição da nota de um vinho [0 a 10]")

@blp.route("/regression") # http://127.0.0.1:5000/predict
class RegressionWinePredictor(MethodView):
    @blp.arguments(RegressPredictionInput) 
    @blp.response(201, RegressPredictionOutput)
    def post(self, request_data):    
        df_sample = pd.DataFrame([request_data])
        predict_model = RegressionWineModel('regression_model.pkl')
        pred = predict_model.predict(df_sample)
        return pred.to_dict(orient='records')[0]
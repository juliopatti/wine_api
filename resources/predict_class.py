from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
from ml_models.models import WineModel
from schemas import BlindClassificationWine, WineClassified

blp = Blueprint("Prediction", __name__, description="Prediction of a good, or not, wine")

@blp.route("/predict") # http://127.0.0.1:5000/predict
class WinePredictor(MethodView):
    @blp.arguments(WineClassified)        # Obs preferi permitir os campos dos classificados
    @blp.response(201, WineClassified)
    def post(self, request_data):    
        # request_data = request.get_json()
        df_sample = pd.DataFrame([request_data])
        predict_model = WineModel('predict_model.pkl')
        pred = predict_model.predict(df_sample)[0]
        request_data["bin_pred"] = int(pred)
        return request_data


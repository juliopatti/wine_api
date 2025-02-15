from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
from ml_models.models import WineModel


blp = Blueprint("Prediction", __name__, description="Prediction of a good, or not, wine")

@blp.route("/predict") # http://127.0.0.1:5000/predict
class WinePredictor(MethodView):
    def post(self):    
        request_data = request.get_json()
        df_sample = pd.DataFrame([request_data])
        predict_model = WineModel('predict_model.pkl')
        pred = predict_model.predict(df_sample)[0]
        request_data["PRED"] = int(pred)
        return request_data, 201


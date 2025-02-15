from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
from ml_models.models import RegressionWineModel
from schemas import BlindClassificationWine, WineClassified


blp = Blueprint("Regression", __name__, description="Prediction the quality of a wine")

@blp.route("/regression") # http://127.0.0.1:5000/predict
class RegressionWinePredictor(MethodView):
    @blp.arguments(WineClassified)        # Obs preferi permitir os campos dos classificados
    @blp.response(201, WineClassified)
    def post(self, request_data):    
        # request_data = request.get_json()
        df_sample = pd.DataFrame([request_data])
        predict_model = RegressionWineModel('regression_model.pkl')
        pred = predict_model.predict(df_sample)[0]
        request_data["quality_regression_pred"] = round(pred,1)
        return request_data
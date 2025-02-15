from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
from ml_models.models import WineModel


blp = Blueprint("Recommendation", __name__, description="Operations with dropper wines recomendation")

@blp.route("/recomendation") # http://127.0.0.1:5000/recomendation
class WineDropper(MethodView):
    def post(self):
        request_data = request.get_json()
        df_sample = pd.DataFrame([request_data])
        recomendation_model = WineModel('recommendation_model.pkl')
        pred = recomendation_model.predict(df_sample)[0]
        if pred==0:
            answer = 'Cilada Bino! Não recomendo este vinho.'
        else:
            answer = 'Glória Pires: Não sei opinar/O vinho pode ser bom, ou não, segundo os critérios adotados'
        request_data["Recomendation"] = answer
        return request_data, 201
        


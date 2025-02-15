from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import pandas as pd
import logging
from ml_models.models import WineModel
from schemas import BlindClassificationWine, RecommendationInput, RecommendationOutput
from utils import verify_authorization
import os

refuse_rec = 'Cilada Bino! Não recomendo este vinho.'
neutral_rec = 'Glória Pires: Não sei opinar/O vinho pode ser bom, ou não, segundo os critérios adotados'

blp = Blueprint("Recommendation", __name__, description="Não recomendar o vinho ou não opinar.")

@blp.route("/recomendation") # http://127.0.0.1:5000/recomendation
class WineDropper(MethodView):
    @blp.arguments(RecommendationInput) 
    @blp.response(201, RecommendationOutput)
    def post(self, request_data):
        
        # Verificação de segurança
        logging.info('\nVerificacao de Seguranca no WineDropper')
        verify_authorization(request.headers.get('Authorization'))
        df_sample = pd.DataFrame([request_data])
        recomendation_model = WineModel('recommendation_model.pkl')
        
        logging.info('Predicao do modelo de recomendação')
        pred_df = recomendation_model.predict(df_sample)
        pred_df.loc[pred_df['bin_pred']==1, 'bin_pred'] = neutral_rec
        pred_df.loc[pred_df['bin_pred']==0, 'bin_pred'] = refuse_rec
        pred_df['recommendation'] = pred_df['bin_pred'].copy()
        pred_df.drop(columns=['bin_pred'], inplace=True)
        
        return pred_df.to_dict(orient='records')[0]
        


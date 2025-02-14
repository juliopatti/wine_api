from flask import Flask, request
import pickle
import pandas as pd

app = Flask(__name__)


path_predict_model = "ml_models/predict_model.pkl"
with open(path_predict_model, "rb") as arquivo:
    predict_model = pickle.load(arquivo)
    
path_predict_model = "ml_models/recomendation_model.pkl"
with open(path_predict_model, "rb") as arquivo:
    recomendation_model = pickle.load(arquivo)
    
features = ["fixed acidity", "volatile acidity", "citric acid", 
            "residual sugar","chlorides", "free sulfur dioxide", 
            "total sulfur dioxide", "density","pH", "sulphates", 
            "alcohol"]

@app.post("/predict") # /recomendation
def pred_wine():     
    request_data = request.get_json()
    df_sample = pd.DataFrame([request_data])[features]
    pred = predict_model.predict(df_sample)[0]
    request_data["PRED"] = int(pred)
    return request_data, 201

@app.post("/recomendation") # /recomendation
def wine_dropper():     
    request_data = request.get_json()
    df_sample = pd.DataFrame([request_data])[features]
    pred = recomendation_model.predict(df_sample)[0]
    if pred==0:
        answer = 'Cilada Bino! Não recomendo este vinho.'
    else:
        answer = 'Glória Pires: Não sei opinar/O vinho pode ser bom, ou não, segundo os critérios adotados'
    request_data["Recomendation"] = answer
    return request_data, 201

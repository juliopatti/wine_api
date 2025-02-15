import pickle
import os


this_dir = os.path.dirname(os.path.abspath(__file__))

def load_model(path_model):
    with open(path_model, "rb") as arquivo:
        model = pickle.load(arquivo)
    return model

features = ["fixed_acidity", "volatile_acidity", "citric_acid", 
            "residual_sugar","chlorides", "free_sulfur_dioxide", 
            "total_sulfur_dioxide", "density", "pH", "sulphates", 
            "alcohol"]


# Binary
class WineModel:
    def __init__(self, filename):
        self.name = filename.replace('.pkl', '')
        self.model = load_model(f'{this_dir}/{filename}')
        self.features = features
        self.classes_meaning = {'0': 'not good wine.', 
                                '1':'good_wine'}
        
    def predict(self, sample):
        sample_features = sample[self.features]
        return self.model.predict(sample_features)
    
    def predict_proba(self, sample):
        sample_features = sample[self.features]
        return self.model.predict_proba(sample_features)
    
    
# Regression
class RegressionWineModel:
    def __init__(self, filename):
        self.name = filename.replace('.pkl', '')
        self.model = load_model(f'{this_dir}/{filename}')
        self.features = features
        
    def predict(self, sample):
        sample_features = sample[self.features]
        return self.model.predict(sample_features)
    
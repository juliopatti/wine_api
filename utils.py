import pickle

def load_model(path_model):
    with open(path_model, "rb") as arquivo:
        model = pickle.load(arquivo)
    return model
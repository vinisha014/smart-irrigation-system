import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

def predict_irrigation(data):
    return int(model.predict([data])[0])
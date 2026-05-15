import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# 🔥 Improved dataset with forecast
data = {
    "moisture": [10, 20, 30, 40, 50, 60, 25, 35],
    "temperature": [30, 32, 34, 36, 38, 40, 33, 37],
    "humidity": [40, 50, 60, 70, 80, 90, 55, 65],
    "rainfall": [0, 0, 0, 1, 1, 1, 0, 1],
    "rain_forecast": [0, 0, 1, 1, 1, 1, 1, 1],
    "irrigation": [1, 1, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

X = df[["moisture", "temperature", "humidity", "rainfall", "rain_forecast"]]
y = df["irrigation"]

model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("Model trained with weather forecast!")
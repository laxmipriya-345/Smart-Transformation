import numpy as np
import pandas as pd
import joblib
import os
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load correct model
model = load_model(os.path.join(BASE_DIR, "ml_model", "lstm_model.h5"))

scaler = joblib.load(os.path.join(BASE_DIR, "ml_model", "scaler.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "ml_model", "type_encoder.pkl"))

def predict_lstm(data_dict):

    df = pd.DataFrame([data_dict])

    df["Type"] = encoder.transform(df["Type"])

    features = [
        "Type",
        "Air temperature [K]",
        "Process temperature [K]",
        "Rotational speed [rpm]",
        "Torque [Nm]",
        "Tool wear [min]"
    ]

    X = df[features]

    X_scaled = scaler.transform(X)

    X_scaled = X_scaled.reshape((1, X_scaled.shape[1], 1))

    prediction = model.predict(X_scaled)

    return float(prediction[0][0])
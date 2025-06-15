import streamlit as st
import os
import joblib
import gdown

# Configuración desde secrets
MODEL_CONFIG = st.secrets.get("model", {})
MODEL_ENV = MODEL_CONFIG.get("env", "local")
MODEL_ID = MODEL_CONFIG.get("gdrive_id", None)
MODEL_PATH = MODEL_CONFIG.get("model_path", "sentiment_model.pkl")
MODEL_URL = f"https://drive.google.com/uc?id={MODEL_ID}" if MODEL_ID else None

def download_model():
    print(f"Modo: {MODEL_ENV}")
    if not os.path.exists(MODEL_PATH):
        if MODEL_ENV == "cloud" and MODEL_URL:
            print(f"Descargando modelo desde Google Drive a {MODEL_PATH}...")
            gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
        elif MODEL_ENV == "cloud" and not MODEL_URL:
            raise ValueError("Modo 'cloud' pero no se proporcionó el gdrive_id.")
        else:
            raise FileNotFoundError(
                f"Modo 'local' pero el archivo '{MODEL_PATH}' no se encontró."
            )

@st.cache_resource
def load_model():
    download_model()
    return joblib.load(MODEL_PATH)

def predict_sentiment(model, text):
    return model.predict([text])[0]

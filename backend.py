import streamlit as st
import os
import joblib
import gdown
import streamlit as st
MODEL_PATH = "sentiment_stacking_model.pkl"
MODEL_ID = st.secrets["model"]["gdrive_id"]
MODEL_URL = f"https://drive.google.com/uc?id={MODEL_ID}"

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("🔽 Descargando modelo desde Google Drive...")
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

@st.cache_resource  # ✅ Esto es recomendable
def load_model():
    download_model()
    return joblib.load(MODEL_PATH)

def predict_sentiment(model, text):
    return model.predict([text])[0]

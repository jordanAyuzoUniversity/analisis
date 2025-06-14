import streamlit as st
from frontend import render_interface
from backend import load_model, predict_sentiment

# Configuración general de la página
st.set_page_config(page_title="Sentiment Predictor", layout="centered")

# Cargar el modelo una sola vez
model = load_model()

# Renderizar interfaz principal
render_interface(model, predict_sentiment)

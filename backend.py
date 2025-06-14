import joblib
import streamlit as st

@st.cache_resource
def load_model():
    return joblib.load("sentiment_stacking_model.pkl")

def predict_sentiment(model, text):
    return model.predict([text])[0]

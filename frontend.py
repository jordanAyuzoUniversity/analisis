import streamlit as st

def render_interface(model, predict_fn):
    st.markdown("<h1 style='text-align: center;'>💬 Chat de Análisis de Sentimientos</h1>", unsafe_allow_html=True)

    # Estilo CSS personalizado para burbujas derecha/izquierda
    st.markdown("""
        <style>
            .chat-container { margin-bottom: 1rem; }

            .user-message {
                background-color: #d0ebff;
                color: black;
                padding: 0.8rem 1rem;
                border-radius: 10px;
                max-width: 70%;
                margin: 0.5rem 0 0.5rem auto;
                text-align: left;
                clear: both;
                float: right;
            }

            .bot-message-positive {
                background-color: #d4edda;
                color: black;
                padding: 0.8rem 1rem;
                border-radius: 10px;
                max-width: 70%;
                margin: 0.5rem auto 0.5rem 0;
                text-align: left;
                clear: both;
                float: left;
            }

            .bot-message-negative {
                background-color: #f8d7da;
                color: black;
                padding: 0.8rem 1rem;
                border-radius: 10px;
                max-width: 70%;
                margin: 0.5rem auto 0.5rem 0;
                text-align: left;
                clear: both;
                float: left;
            }

            .emoji {
                font-weight: bold;
                margin-right: 0.5rem;
            }
        </style>
    """, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar el historial
    for entry in st.session_state.chat_history:
        st.markdown(
            f"<div class='chat-container'><div class='user-message'>"
            f"<span class='emoji'>👤</span>{entry['user']}</div></div>", 
            unsafe_allow_html=True
        )

        # Determinar clase según sentimiento
        bot_class = "bot-message-positive" if "✅" in entry["bot"] else "bot-message-negative"

        st.markdown(
            f"<div class='chat-container'><div class='{bot_class}'>"
            f"<span class='emoji'>🤖</span>{entry['bot']}</div></div>", 
            unsafe_allow_html=True
        )

    user_input = st.chat_input("Escribe tu mensaje para analizar el sentimiento...")

    if user_input:
        prediction = predict_fn(model, user_input)
        sentiment = "Positivo" if prediction == 1 else "Negativo"
        icon = "✅" if prediction == 1 else "❌"
        response = f"{icon} Sentimiento ** {sentiment.upper()} **"

        st.session_state.chat_history.append({
            "user": user_input,
            "bot": response
        })

        st.rerun()

    if st.button("🧹 Limpiar conversación"):
        st.session_state.chat_history = []
        st.rerun()

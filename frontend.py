import streamlit as st

def render_interface(model, predict_fn):
    st.markdown("""
        <style>
            .sticky-title {
                position: sticky;
                top: 0;
                background-color: inherit;
                z-index: 100;
                padding: 0.5rem 0;
                text-align: center;
                font-size: 1.5rem;
                font-weight: 600;
                border-bottom: 1px solid #ccc;
            }
        </style>
        <div class="sticky-title">Chat de Análisis de Sentimientos</div>
    """, unsafe_allow_html=True)

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

            .bot-message-positive, .bot-message-negative, .bot-message-welcome {
                background-color: #e2e3e5;
                color: black;
                padding: 0.8rem 1rem;
                border-radius: 10px;
                max-width: 70%;
                margin: 0.5rem auto 0.5rem 0;
                text-align: left;
                clear: both;
                float: left;
            }

            .bot-message-positive { background-color: #d4edda; }
            .bot-message-negative { background-color: #f8d7da; }

            .emoji {
                font-weight: bold;
                margin-right: 0.5rem;
            }
        </style>
    """, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar mensaje inicial si el historial está vacío
    if not st.session_state.chat_history:
        st.session_state.chat_history.append({
            "user": None,
            "bot": "👋 ¡Hola! Soy un modelo de análisis de sentimientos basado en *stacking*. Escribe una opinión y te diré si es positiva o negativa."
        })

    # Mostrar el historial
    for entry in st.session_state.chat_history:
        if entry["user"] is not None:
            st.markdown(
                f"<div class='chat-container'><div class='user-message'>{entry['user']}</div></div>",
                unsafe_allow_html=True
            )

        bot_class = "bot-message-welcome"
        if "✅" in entry["bot"]:
            bot_class = "bot-message-positive"
        elif "❌" in entry["bot"]:
            bot_class = "bot-message-negative"

        st.markdown(
            f"<div class='chat-container'><div class='{bot_class}'>{entry['bot']}</div></div>",
            unsafe_allow_html=True
        )

    user_input = st.chat_input("Escribe tu mensaje para analizar el sentimiento...")

    if user_input:
        prediction = predict_fn(model, user_input)
        sentiment = "Positivo" if prediction == 1 else "Negativo"
        icon = "✅" if prediction == 1 else "❌"
        response = f"{icon} Sentimiento <strong>{sentiment.upper()}</strong>"

        st.session_state.chat_history.append({
            "user": user_input,
            "bot": response
        })
        st.rerun()

    if st.button("🧹 Limpiar conversación"):
        st.session_state.chat_history = []
        st.rerun()

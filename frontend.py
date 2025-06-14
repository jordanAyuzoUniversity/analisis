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
        # Si el usuario escribe /info
        if user_input.strip().lower() == "/info":
            info_msg = (
                "📘 <strong>Información del modelo:</strong><br>"
                "Este es un modelo de análisis de sentimientos desarrollado con la técnica "
                "<em>stacking</em>. Fue creado como parte de un proyecto académico para la "
                "materia <strong>Reconocimiento de Patrones</strong> en la <strong>Universidad Tecnológica de la Mixteca</strong>.<br><br>"
                "🔤 El modelo está entrenado para funcionar con opiniones escritas en <strong>inglés</strong>."
            )
            st.session_state.chat_history.append({
                "user": user_input,
                "bot": info_msg
            })
            st.rerun()
        else:
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

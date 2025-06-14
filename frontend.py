import streamlit as st

def render_interface(model, predict_fn):
    st.markdown("<h1 style='text-align: center;'>🔍 Analizador de Sentimientos</h1>", unsafe_allow_html=True)

    # Inicializar historial
    if "history" not in st.session_state:
        st.session_state.history = []

    # Entrada de texto
    user_input = st.text_area("Escribe un mensaje:")

    # Botón para analizar
    if st.button("Analizar"):
        if not user_input.strip():
            st.warning("Por favor escribe algo.")
        else:
            # Predicción usando la función pasada
            prediction = predict_fn(model, user_input)
            sentiment = "Positivo" if prediction == 1 else "Negativo"

            # Mostrar resultado
            if prediction == 1:
                st.success("Última predicción: ✅ Sentimiento POSITIVO")
            else:
                st.error("Última predicción: ❌ Sentimiento NEGATIVO")

            # Guardar en historial
            st.session_state.history.append({
                "Comentario": user_input,
                "Predicción": sentiment
            })

    # Mostrar historial
    if st.session_state.history:
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.markdown("<h3 style='text-align: center;'>Historial de Análisis</h3>", unsafe_allow_html=True)
        with col2:
            st.write("")
            if st.button("Limpiar Tabla"):
                st.session_state.history = []
                st.rerun()

        st.dataframe(st.session_state.history, use_container_width=True)

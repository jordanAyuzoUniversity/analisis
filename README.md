# Analizador de Sentimientos con Streamlit

Este proyecto es una interfaz web desarrollada con Streamlit para analizar el sentimiento de un comentario de texto. El modelo de aprendizaje automático predice si el sentimiento es **positivo** o **negativo**, y se almacena un historial de los análisis realizados durante la sesión.

## 🗂 Estructura del Proyecto

```
sentiment_app/
├── app.py                  # Archivo principal para ejecutar la 
├── frontend.py             # Interfaz de usuario con Streamlit
├── backend.py              # Carga y uso del modelo de predicción
├── sentiment_stacking_model.pkl  # Modelo previamente entrenado
```

## 📌 Requisitos

- **Python 3.8 o superior**
- Navegador web moderno(Testeado en Brave)

## 📦 Instalación

1. Clona este repositorio o descarga los archivos:

```bash
git clone https://github.com/JordanAyuzo/analizador-sentimientos.git
cd analizador-sentimientos
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv env
# En sistemas Unix/macOS:
source env/bin/activate
# En Windows:
env\Scripts\activate
```

3. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Si no tienes el archivo `requirements.txt`, puedes instalar manualmente:

```bash
pip install streamlit joblib scikit-learn xgboost
```

## ▶️ Ejecutar la aplicación

Desde la carpeta principal del proyecto, ejecuta:

```bash
streamlit run app.py
```

Esto abrirá la interfaz en tu navegador por defecto:

```
http://localhost:8501
```

## 🧠 Modelo de Predicción

El archivo `sentiment_stacking_model.pkl` es un modelo previamente entrenado que se carga automáticamente al iniciar la aplicación. Puedes reemplazarlo por otro modelo compatible si deseas experimentar con diferentes enfoques.

## 🛠 Modificación

- **Frontend**: Personaliza la interfaz editando `frontend.py`.
- **Backend**: Mejora o cambia el modelo en `backend.py`.

---

Hecho con ❤️ por [Jordan Ayuzo](https://github.com/JordanAyuzo)
import streamlit as st
import joblib
import numpy as np
import os

# Título y descripción
st.title("Predicción de Precio de Venta de Casas")
st.write("""
Esta aplicación carga un modelo de regresión entrenado sobre datos sintéticos
y predice el precio de venta de una casa según:
- Superficie en pies cuadrados (`sqft`)
- Número de habitaciones (`rooms`)
- Antigüedad de la vivienda en años (`age`)
- Distancia al centro de la ciudad en km (`dist`)
""")

# 1. Localizar la carpeta donde está este script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Ruta al modelo guardado en la misma carpeta
MODEL_PATH = os.path.join(CURRENT_DIR, "best_model_regresion.pkl")

# 3. Función para cargar y cachear el modelo como recurso
@st.cache_resource
def load_model(path):
    if not os.path.exists(path):
        st.error(f"❌ No se encontró el modelo en:\n`{path}`\nAsegúrate de haber subido `best_model.pkl`.")
        return None
    return joblib.load(path)

model = load_model(MODEL_PATH)
if model is None:
    st.stop()

# 4. Panel lateral: parámetros de entrada
st.sidebar.header("Parámetros de Entrada")
sqft  = st.sidebar.slider("Superficie (sqft)",      min_value=100,  max_value=5000,  value=1500, step=50)
rooms = st.sidebar.slider("Habitaciones",           min_value=1,    max_value=10,    value=3,    step=1)
age   = st.sidebar.slider("Antigüedad (años)",      min_value=0,    max_value=150,   value=20,   step=1)
dist  = st.sidebar.slider("Distancia al centro (km)", min_value=0.0,  max_value=100.0, value=10.0, step=0.5)

# 5. Preparar input y predecir
X_new      = np.array([[sqft, rooms, age, dist]])
pred_price = model.predict(X_new)[0]

# 6. Mostrar resultado
st.subheader("🔍 Resultado de la Predicción")
st.write(f"💰 **Precio estimado:** USD {pred_price:,.2f}")

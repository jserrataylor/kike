# ML & Streamlit Deployment

Este README proporciona instrucciones detalladas para:

1. Estructurar el repositorio.
2. Subir el proyecto a GitHub.
3. Preparar los archivos de modelo y requerimientos.
4. Configurar y desplegar las aplicaciones en Streamlit Cloud.

---
```
## 1. **Estructura del repositorio**

Organiza tu proyecto de la siguiente forma:

## App de Clasificación
app.py                        # Streamlit app para clasificación
best_model.pkl                # Modelo de clasificación entrenado
requirements.txt              # Dependencias

# App de Regresión
app-regresion.py              # Streamlit app para regresión
best_model_regresion.pkl      # Modelo de regresión entrenado
requirements.txt              # Dependencias (igual a la aplicación anterior
README.md                     # Este archivo
```

* **app.py**: Script principal para la aplicación de clasificación.
* **app-regresion.py**: Script principal para la aplicación de regresión.
* **best_model.pkl**: Coloca aquí el archivo de tu modelo serializado (joblib/pickle).
* **requirements.txt**: Lista de dependencias Python.

---

## 2. Crear el archivo `requirements.txt`

Crea un archivo `requirements.txt` con al menos las siguientes líneas:

```txt
streamlit
scikit-learn
numpy
joblib
```

Si usas versiones específicas, especifícalas así:

```txt
streamlit==1.26.0
scikit-learn==1.2.2
numpy==1.24.2
joblib==1.2.0
```

---

## 3. Inicializar el repositorio Git y subir a GitHub

1. **Crear repo en GitHub**
   * Entra a `https://github.com/` y crea un nuevo repositorio, por ejemplo `ml-streamlit`.
2. **Crear, Añadir, Copiar y/o confirmar los archivos de la aplicación con extensión .py(aplicacion), .txt(dependencias), .pkl(modelos) dentro del directorio**
   * Crear archivos de las aplicaciones (`app.py` y `app-regresion.py`)
   * Crear archivo de las dependencias (`requirements.txt`)
   * Subir los archivos de los modelos (`best_model.pkl` y `best_model_regresion.pkl`)

## 4. Preparar modelos y código

* Asegúrate de que el repositorio contenga:

  * El script `app.py` y/o `app-regresion.py`.
  * El archivos de los modelos entrenados `best_model.pkl` y `best_model_regresion.pkl` con el modelo serializado.
  * El archivo `requirements.txt`.

## 5. Crear cuenta y aplicaciones en Streamlit Cloud

1. **Registrarte en Streamlit Cloud**

   * Ve a `https://streamlit.io/` y regístrate con tu cuenta de GitHub.

2. **Conectar tu repositorio**

   * En tu dashboard, haz clic en **"New app"**.
   * Selecciona tu repositorio `ml-streamlit` y elige el branch `main`.

3. **Configurar despliegue de la app de clasificación**

   * En **App path**, ingresa `app.py` en el caso de clasificación y `app-regresion.py` en el caso de regresión.
   * En **Requirements file**, el sistema buscará automaticamente el archivo `requirements.txt` de manera automática.
   * Haz clic en **Deploy**.

4. **Configurar despliegue de la app de regresión**

   * Repite el proceso anterior, pero con:

     * **App path**: `regression/app-regresion.py`
     * **Requirements file path**: `regression/requirements.txt`

5. **App URL (optional)**

   * Usar el nombre sugerido o crear uno nombre para la aplicación, y oprimir `Deploy`. Una vez , obtendrás las URLs públicas donde podrás interactuar con cada app, pero eso se hace de manera indiviual para cada aplicación.

* Streamlit Cloud redeplegará automáticamente las apps.

---


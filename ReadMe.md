# ML & Streamlit Deployment

Este README proporciona instrucciones detalladas para:

1. Estructurar el repositorio local.
2. Subir el proyecto a GitHub.
3. Preparar los archivos de modelo y requerimientos.
4. Configurar y desplegar las aplicaciones en Streamlit Cloud.

---

## 1. Estructura del repositorio

Organiza tu proyecto de la siguiente forma:

```
ml-streamlit-project/
├── classification/                   # App de clasificación
│   ├── app.py                        # Streamlit app para clasificación
│   ├── best_model.pkl                # Modelo de clasificación entrenado
│   └── requirements.txt              # Dependencias
├── regression/                       # App de regresión
│   ├── app-regresion.py              # Streamlit app para regresión
│   ├── best_model.pkl                # Modelo de regresión entrenado
│   └── requirements.txt              # Dependencias
└── README.md                         # Este archivo
```

* **classification/app.py**: Script principal para la aplicación de clasificación.
* **regression/app-regresion.py**: Script principal para la aplicación de regresión.
* **best\_model.pkl**: Coloca aquí el archivo de tu modelo serializado (joblib/pickle).
* **requirements.txt**: Lista de dependencias Python.

---

## 2. Crear el archivo `requirements.txt`

Dentro de cada directorio (`classification/` y `regression/`), crea un archivo `requirements.txt` con al menos las siguientes líneas:

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

   * Entra a `https://github.com/` y crea un nuevo repositorio, por ejemplo `ml-streamlit-project`.
2. **Clonar localmente**

   ```bash
   git clone https://github.com/TU_USUARIO/ml-streamlit-project.git
   cd ml-streamlit-project
   ```
3. **Copiar archivos**

   * Copia tus carpetas `classification/`, `regression/` y `README.md` dentro de la carpeta clonada.
4. **Añadir y confirmar**

   ```bash
   git add .
   git commit -m "Iniciar proyecto ML con apps de Streamlit"
   ```
5. **Enviar a remoto**

   ```bash
   git push origin main
   ```

---

## 4. Preparar modelos y código

* Asegúrate de que cada subcarpeta (`classification/`, `regression/`) contenga:

  * El script `app.py` o `app-regresion.py`.
  * El archivo `best_model.pkl` con el modelo serializado.
  * El archivo `requirements.txt`.

* Verifica localmente que cada app se ejecuta correctamente:

  ```bash
  cd classification
  pip install -r requirements.txt
  streamlit run app.py
  ```

  ```bash
  cd regression
  pip install -r requirements.txt
  streamlit run app-regresion.py
  ```

---

## 5. Crear cuenta y aplicaciones en Streamlit Cloud

1. **Registrarte en Streamlit Cloud**

   * Ve a `https://streamlit.io/cloud` y regístrate con tu cuenta de GitHub.
2. **Conectar tu repositorio**

   * En tu dashboard, haz clic en **"New app"**.
   * Selecciona tu repositorio `ml-streamlit-project` y elige el branch `main`.
3. **Configurar despliegue de la app de clasificación**

   * En **App path**, ingresa `classification/app.py`.
   * En **Requirements file path**, ingresa `classification/requirements.txt`.
   * Haz clic en **Deploy**.
4. **Configurar despliegue de la app de regresión**

   * Repite el proceso anterior, pero con:

     * **App path**: `regression/app-regresion.py`
     * **Requirements file path**: `regression/requirements.txt`
5. **Verificar URLs**

   * Una vez desplegadas, obtendrás dos URLs públicas donde podrás interactuar con cada app.

---

## 6. Actualizaciones y CI/CD opcional

* Cada vez que hagas cambios en tu código o modelo, simplemente haz push a `main`:

  ```bash
  git add .
  git commit -m "Actualizar modelo o UI"
  git push origin main
  ```
* Streamlit Cloud redeplegará automáticamente las apps.

---

¡Con esto tendrás tus aplicaciones de ML deployadas y operativas en Streamlit!

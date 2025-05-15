# Predicción de Diabetes - Flask App

## 🎯 Objetivo

Aplicar un modelo de Machine Learning para predecir la progresión de la diabetes a partir del índice de masa corporal (BMI), y presentar los resultados en una aplicación web construida con Flask.

## 📊 Descripción del Dataset

Se utilizó el dataset de diabetes incluido en `sklearn.datasets`. Contiene medidas clínicas de pacientes y una variable objetivo que representa la progresión de la enfermedad.

- Fuente: `sklearn.datasets.load_diabetes()`
- Variables independientes: índice de masa corporal (`bmi`)
- Variable dependiente: progresión de la diabetes (`target`)

## 🧠 Modelo Aplicado

Se aplicó un modelo de **Regresión Lineal** simple. Esta técnica es adecuada para predecir una variable continua a partir de otra. En este caso, se predice el valor objetivo en función del BMI del paciente.

## 🖥️ Aplicación Web (Flask)

La aplicación permite al usuario ingresar un valor de BMI, realizar la predicción y visualizar el resultado junto con una gráfica generada con Matplotlib.

### Características:

- Interfaz con HTML, CSS y Jinja2, ademas de usar Animate.css
- Predicción interactiva con entrada de usuario
- Gráfica embebida del modelo y predicción
- Estilo visual personalizado

## 🛠️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Migatte-Yk/AppFlaskWorkshop.git
   cd AppFlaskWorkshop

2. Crea y activa un entorno virtual:

python -m venv venv
venv\Scripts\activate  # En Windows

3. Instala las dependencias:

pip install -r requirements.txt

4. Ejecuta la app:

python app.py

📸 Capturas de pantalla
![Captura de pantalla (6)](https://github.com/user-attachments/assets/df2aaf59-967a-4382-ba56-c285455e0cb3)
![Captura de pantalla (5)](https://github.com/user-attachments/assets/2726f161-9633-40b8-a60d-a4ec0a3f4dbb)
![Captura de pantalla (4)](https://github.com/user-attachments/assets/45b1bb5a-0339-40ff-b730-7009abb24c29)
![Captura de pantalla (3)](https://github.com/user-attachments/assets/6192a5a3-8c2e-41b7-a585-0ad9e98dccc1)



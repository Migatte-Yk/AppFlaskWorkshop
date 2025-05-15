from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Cargar modelo
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    bmi_input = ""
    explanation = ""
    image = None  # Para controlar si mostramos la imagen

    if request.method == "POST":
        # Verificar si es un submit del formulario o el botón de reset
        if 'bmi' in request.form:
            try:
                bmi_input = float(request.form["bmi"])
                prediction = model.predict(np.array([[bmi_input]]))[0]
                
                # Añadir explicación según el valor de BMI
                if bmi_input < 18.5:
                    explanation = "Bajo peso: Puede indicar desnutrición u otros problemas de salud."
                elif 18.5 <= bmi_input < 25:
                    explanation = "Peso normal: Buen indicador de salud general."
                elif 25 <= bmi_input < 30:
                    explanation = "Sobrepeso: Aumenta el riesgo de desarrollar diabetes tipo 2."
                else:
                    explanation = "Obesidad: Riesgo significativamente mayor de diabetes y otras enfermedades."
                    
            except ValueError:
                prediction = "Entrada inválida"
                explanation = "Por favor ingrese un valor numérico válido para el BMI."
        
        # Si es el botón de reset
        elif 'reset' in request.form:
            return redirect(url_for('index'))

    return render_template("index.html", 
                         prediction=prediction, 
                         bmi_input=bmi_input,
                         explanation=explanation,
                         image=None)

@app.route("/plot", methods=["GET", "POST"])
def plot():
    if request.method == "POST":
        # Si se envía el formulario desde la página del gráfico
        return redirect(url_for('index'))
    
    df = pd.read_csv("data/dataset.csv")

    # Graficar datos + línea de regresión
    plt.figure(figsize=(10, 6))
    plt.scatter(df["bmi"], df["target"], color="blue", label="Datos reales")
    plt.plot(df["bmi"], model.predict(df[["bmi"]]), color="red", label="Regresión")
    plt.xlabel("BMI (Índice de Masa Corporal)")
    plt.ylabel("Progresión de la enfermedad")
    plt.legend()
    plt.title("Modelo de Regresión para Diabetes")
    plt.grid(True)

    # Guardar imagen
    img_path = "static/plot.png"
    if os.path.exists(img_path):
        os.remove(img_path)
    plt.savefig(img_path)
    plt.close()
    
    return render_template("index.html", 
                         prediction=None, 
                         bmi_input="", 
                         explanation="",
                         image="plot.png")

@app.route("/reset")
def reset():
    # Eliminar la imagen si existe
    img_path = "static/plot.png"
    if os.path.exists(img_path):
        os.remove(img_path)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
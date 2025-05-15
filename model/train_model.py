import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

# Cargar dataset
data = load_diabetes()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Elegimos una sola variable para simplificar (por ejemplo, BMI)
X = X[["bmi"]]

# Entrenar modelo
model = LinearRegression()
model.fit(X, y)

# Guardar modelo entrenado
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Guardar dataset para usarlo en visualizaciones
df = X.copy()
df["target"] = y
df.to_csv("data/dataset.csv", index=False)

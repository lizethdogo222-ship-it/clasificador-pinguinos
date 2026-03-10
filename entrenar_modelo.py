import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

print("Entrenando modelo...")

# cargar dataset limpio
df = pd.read_csv("penguins_limpio.csv")

# convertir números a nombres de especies
mapa_especies = {1: "Adelie", 2: "Chinstrap", 3: "Gentoo"}
df['species'] = df['species'].map(mapa_especies)

# variables predictoras (4 medidas)
features = [
    'bill_length_mm',
    'bill_depth_mm',
    'flipper_length_mm',
    'body_mass_g'
]

X = df[features]
y = df['species']

# crear y entrenar modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X, y)

# guardar modelo
with open("modelo.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo guardado como modelo.pkl")
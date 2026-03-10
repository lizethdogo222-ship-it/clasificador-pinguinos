import pandas as pd
import pickle
from sistema_experto import clasificador_humano

# cargar modelo entrenado
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

print("Modelo cargado")

# leer datos de prueba
datos = pd.read_csv(
    "pinguinos_input.txt",
    header=None,
    names=[
        'id',
        'bill_length_mm',
        'bill_depth_mm',
        'flipper_length_mm',
        'body_mass_g'
    ]
)

print("\nResultados de predicción")
print("--------------------------------")

for _, row in datos.iterrows():

    id_p = int(row['id'])
    bill_length = row['bill_length_mm']
    bill_depth = row['bill_depth_mm']
    flipper = row['flipper_length_mm']
    masa = row['body_mass_g']

    # predicción sistema experto
    pred_humano = clasificador_humano(bill_length, bill_depth, flipper, masa)

    # predicción modelo ML
    entrada = pd.DataFrame(
        [[bill_length, bill_depth, flipper, masa]],
        columns=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    )
    pred_ml = modelo.predict(entrada)[0]

    print(f"\nPingüino {id_p}")
    print(f"  Sistema experto : {pred_humano}")
    print(f"  Árbol de decisión: {pred_ml}")

    if pred_humano == pred_ml:
        print("   Coinciden")
    else:
        print("   No coinciden")
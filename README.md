# Clasificador de Pingüinos 🐧

Proyecto de modelado predictivo que compara dos enfoques para clasificar especies de pingüinos:
**Sistema Experto** (programación tradicional) vs **Árbol de Decisión** (Machine Learning).

---

## ¿Qué hace este proyecto?

Dado un conjunto de medidas físicas de un pingüino, el programa predice a qué especie pertenece usando dos métodos distintos y compara sus resultados.

### Especies que clasifica
- **Adelie** — pico corto, aleta corta
- **Chinstrap** — pico largo y profundo
- **Gentoo** — aleta larga, pico delgado, más pesado

---

## Diferencia entre los dos enfoques

| | Sistema Experto | Árbol de Decisión (ML) |
|---|---|---|
| ¿Quién define las reglas? | El programador | La máquina aprende de los datos |
| Conocimiento requerido | Experto en el dominio | Solo datos de entrenamiento |
| Patrones complejos | Difícil de capturar | Los descubre automáticamente |
| Objetividad | Subjetiva | Objetiva y reproducible |

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `entrenar_modelo.py` | Entrena el árbol de decisión con el dataset y guarda el modelo |
| `modelo.pkl` | Modelo entrenado guardado (generado por entrenar_modelo.py) |
| `main.py` | Carga el modelo y compara ambas predicciones |
| `sistema_experto.py` | Reglas manuales para clasificar pingüinos |
| `penguins_limpio.csv` | Dataset de entrenamiento con 333 pingüinos |
| `pinguinos_input.txt` | Pingüinos de prueba para clasificar |

---

## Cómo correrlo

**Paso 1 — Entrenar el modelo** (solo necesario la primera vez o si cambias el dataset):
```
python entrenar_modelo.py
```

**Paso 2 — Correr el clasificador:**
```
python main.py
```

---

## Formato del archivo de entrada

El archivo `pinguinos_input.txt` contiene un pingüino por línea con 5 valores separados por coma:

```
id, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g
```

| Campo | Descripción |
|---|---|
| `id` | Número identificador del pingüino |
| `bill_length_mm` | Largo del pico en milímetros |
| `bill_depth_mm` | Profundidad del pico en milímetros |
| `flipper_length_mm` | Largo de la aleta en milímetros |
| `body_mass_g` | Masa corporal en gramos |

### Ejemplo:
```
1,39.1,18.7,181,3750
2,46.5,17.9,192,3500
3,46.1,13.2,211,4500
```

---

## Ejemplo de salida

```
Modelo cargado

Resultados de predicción
--------------------------------

Pingüino 1
  Sistema experto : Adelie
  Árbol de decisión: Adelie
  ✔ Coinciden

Pingüino 2
  Sistema experto : Chinstrap
  Árbol de decisión: Gentoo
  ✘ No coinciden
```

---

## Reglas del sistema experto

```python
if flipper_length > 205 and bill_depth <= 17:
    → Gentoo

elif bill_length > 45 and bill_depth > 17:
    → Chinstrap

else:
    → Adelie
```

---

## Dataset

Se utilizó el dataset **Palmer Penguins** con 333 registros limpios.
Variables usadas para entrenar: `bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`.

---

## Tecnologías

- Python 3
- scikit-learn (DecisionTreeClassifier)
- pandas

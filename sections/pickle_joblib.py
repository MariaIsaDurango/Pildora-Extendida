import streamlit as st
import pandas as pd


def show_pickle_joblib():

    st.title("🥊 Pickle vs Joblib")

    st.markdown("""
Después de comprender qué es la serialización, surge una pregunta muy importante:

> **¿Qué herramienta debo utilizar para guardar un modelo?**

Las dos bibliotecas más utilizadas son:

- 🐍 Pickle
- ⚡ Joblib

Veamos sus diferencias.
""")

    st.divider()

    # ===========================================================
    # COMPARACIÓN
    # ===========================================================

    st.header("📊 Comparación General")

    col1, col2 = st.columns(2)

    with col1:

        st.success("## 🐍 Pickle")

        st.write("""
✔ Biblioteca estándar de Python

✔ No requiere instalación

✔ Muy sencilla

✔ Compatible con cualquier objeto

✔ Ideal para proyectos pequeños
""")

    with col2:

        st.info("## ⚡ Joblib")

        st.write("""
✔ Optimizada para Machine Learning

✔ Más rápida

✔ Excelente con NumPy

✔ Archivos grandes

✔ Permite compresión
""")

    st.divider()

    # ===========================================================
    # TABLA
    # ===========================================================

    st.header("📋 Tabla Comparativa")

    tabla = pd.DataFrame({

        "Característica":[

            "Instalación",

            "Velocidad",

            "Matrices grandes",

            "Compresión",

            "Uso"

        ],

        "Pickle":[

            "No",

            "Media",

            "Buena",

            "No",

            "General"

        ],

        "Joblib":[

            "Sí",

            "Alta",

            "Excelente",

            "Sí",

            "Machine Learning"

        ]

    })

    st.dataframe(tabla, use_container_width=True)

    st.divider()

    # ===========================================================
    # CÓDIGO PICKLE
    # ===========================================================

    st.header("🐍 Guardar con Pickle")

    st.code(
"""
import pickle

with open("modelo.pkl","wb") as archivo:
    pickle.dump(modelo,archivo)
""",
language="python"
)

    st.code(
"""
with open("modelo.pkl","rb") as archivo:
    modelo = pickle.load(archivo)
""",
language="python"
)

    st.divider()

    # ===========================================================
    # CÓDIGO JOBLIB
    # ===========================================================

    st.header("⚡ Guardar con Joblib")

    st.code(
"""
from joblib import dump

dump(modelo,"modelo.joblib")
""",
language="python"
)

    st.code(
"""
from joblib import load

modelo = load("modelo.joblib")
""",
language="python"
)

    st.divider()

    # ===========================================================
    # CUÁNDO USAR
    # ===========================================================

    st.header("🎯 ¿Cuándo usar cada uno?")

    opcion = st.selectbox(

        "Selecciona un escenario",

        [

            "Proyecto pequeño",

            "Modelo con NumPy",

            "Modelo de Scikit-Learn",

            "Modelo muy grande"

        ]

    )

    if opcion == "Proyecto pequeño":

        st.success("🐍 Pickle es una excelente opción.")

    elif opcion == "Modelo con NumPy":

        st.success("⚡ Joblib es más eficiente.")

    elif opcion == "Modelo de Scikit-Learn":

        st.success("⚡ Joblib es la recomendación oficial en muchos casos.")

    else:

        st.success("⚡ Joblib permite trabajar mejor con archivos grandes.")

    st.divider()

    # ===========================================================
    # ERRORES
    # ===========================================================

    st.header("❌ Errores comunes")

    errores = [

        "Guardar el modelo sin entrenarlo.",

        "Olvidar guardar el preprocesamiento.",

        "Cambiar la versión de Python.",

        "Mover el archivo .pkl.",

        "Intentar cargar un archivo inexistente.",

        "Abrir archivos Pickle de origen desconocido."

    ]

    for e in errores:

        st.warning(e)

    st.divider()

    # ===========================================================
    # BUENAS PRÁCTICAS
    # ===========================================================

    st.header("✅ Buenas prácticas")

    buenas = [

        "Guardar el modelo y el preprocesamiento.",

        "Versionar los modelos.",

        "Documentar la versión de Scikit-Learn.",

        "Usar Joblib para modelos grandes.",

        "No cargar archivos desconocidos.",

        "Realizar pruebas antes de producción."

    ]

    for b in buenas:

        st.success(b)

    st.divider()

    # ===========================================================
    # CASO REAL
    # ===========================================================

    st.header("🏦 Caso de estudio")

    st.info("""
Un banco entrenó un modelo para detectar fraude.

Tiempo de entrenamiento:

⏱ 6 horas

Cada cliente solicita una predicción en menos de 1 segundo.

¿Entrenar nuevamente el modelo para cada cliente?

❌ Imposible.

La solución fue:

✔ Entrenar una sola vez.

✔ Guardar con Joblib.

✔ Cargar el modelo cuando inicia el servidor.

✔ Realizar miles de predicciones por minuto.
""")

    st.divider()

    # ===========================================================
    # DECISIÓN
    # ===========================================================

    st.header("🎮 ¿Qué elegirías?")

    decision = st.radio(

        "Si desarrollas un modelo de Scikit-Learn con muchos datos, utilizarías:",

        [

            "Pickle",

            "Joblib"

        ]

    )

    if decision == "Joblib":

        st.success("🎉 Correcto.")

    else:

        st.warning("Funciona, pero Joblib suele ser una mejor opción.")

    st.divider()

    # ===========================================================
    # RESUMEN
    # ===========================================================

    st.header("📝 Resumen")

    st.markdown("""

| Pickle | Joblib |
|---------|---------|
| Biblioteca estándar | Requiere instalación |
| Fácil de usar | Optimizada para ML |
| Compatible con cualquier objeto | Mejor con NumPy |
| Sin compresión | Compresión integrada |
| Uso general | Uso recomendado en modelos grandes |

""")

    st.success("""
🎉 Ya conoces las diferencias entre Pickle y Joblib.

Ahora estás listo para realizar el laboratorio práctico.
""")
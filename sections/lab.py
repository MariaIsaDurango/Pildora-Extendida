import streamlit as st
import pickle
import os

from joblib import dump, load

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def show_lab():

    # ==========================================
    # SESSION STATE
    # ==========================================

    if "modelo" not in st.session_state:
        st.session_state.modelo = None

    if "accuracy" not in st.session_state:
        st.session_state.accuracy = None

    if "modelo_entrenado" not in st.session_state:
        st.session_state.modelo_entrenado = False

    if "pickle_guardado" not in st.session_state:
        st.session_state.pickle_guardado = False

    if "joblib_guardado" not in st.session_state:
        st.session_state.joblib_guardado = False

    if "modelo_recuperado" not in st.session_state:
        st.session_state.modelo_recuperado = False

    # ==========================================
    # TITULO
    # ==========================================

    st.title("🧪 Laboratorio Interactivo")

    st.markdown("""
En este laboratorio realizaremos el ciclo completo de un modelo de Machine Learning.

1️⃣ Cargar datos

2️⃣ Entrenar

3️⃣ Guardar

4️⃣ Recuperar

5️⃣ Predecir
""")

    st.divider()

    # ==========================================
    # PASO 1
    # ==========================================

    st.header("📦 Paso 1 - Cargar Dataset")

    iris = load_iris()

    X = iris.data
    y = iris.target

    st.success("Dataset Iris cargado correctamente.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Filas", X.shape[0])

    with col2:
        st.metric("Variables", X.shape[1])

    if st.checkbox("Ver primeras filas"):

        import pandas as pd

        df = pd.DataFrame(
            X,
            columns=iris.feature_names
        )

        df["Clase"] = y

        st.dataframe(df.head())

    st.divider()

    # ==========================================
    # PASO 2
    # ==========================================

    st.header("🤖 Paso 2 - Entrenar Modelo")

    if st.button(
        "🚀 Entrenar Modelo",
        use_container_width=True
    ):

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.30,
            random_state=42
        )

        modelo = DecisionTreeClassifier()

        modelo.fit(X_train, y_train)

        pred = modelo.predict(X_test)

        acc = accuracy_score(y_test, pred)

        st.session_state.modelo = modelo
        st.session_state.accuracy = acc
        st.session_state.modelo_entrenado = True

        st.success("✅ Modelo entrenado correctamente")

    if st.session_state.modelo_entrenado:

        st.metric(
            "Accuracy",
            f"{st.session_state.accuracy:.2%}"
        )

        st.progress(st.session_state.accuracy)

    st.divider()

        # ==========================================
    # PASO 3 - GUARDAR PICKLE
    # ==========================================

    st.header("💾 Paso 3 - Guardar con Pickle")

    if st.button(
        "Guardar modelo (.pkl)",
        disabled=not st.session_state.modelo_entrenado,
        use_container_width=True
    ):

        os.makedirs("models", exist_ok=True)

        with open("models/modelo.pkl", "wb") as archivo:
            pickle.dump(st.session_state.modelo, archivo)

        st.session_state.pickle_guardado = True

        st.success("✅ Modelo guardado como models/modelo.pkl")

    if st.session_state.pickle_guardado:
        st.info("📄 Archivo creado: modelo.pkl")

    st.divider()

    # ==========================================
    # PASO 4 - GUARDAR JOBLIB
    # ==========================================

    st.header("⚡ Paso 4 - Guardar con Joblib")

    if st.button(
        "Guardar modelo (.joblib)",
        disabled=not st.session_state.modelo_entrenado,
        use_container_width=True
    ):

        os.makedirs("models", exist_ok=True)

        dump(
            st.session_state.modelo,
            "models/modelo.joblib"
        )

        st.session_state.joblib_guardado = True

        st.success("✅ Modelo guardado como models/modelo.joblib")

    if st.session_state.joblib_guardado:
        st.info("📄 Archivo creado: modelo.joblib")

    st.divider()

    # ==========================================
    # PASO 5 - ELIMINAR MODELO
    # ==========================================

    st.header("🗑 Paso 5 - Eliminar modelo de memoria")

    if st.button(
        "Eliminar modelo",
        disabled=not st.session_state.modelo_entrenado,
        use_container_width=True
    ):

        st.session_state.modelo = None
        st.session_state.modelo_entrenado = False

        st.warning("⚠️ El modelo fue eliminado de la memoria RAM.")

    st.divider()

    # ==========================================
    # PASO 6 - RECUPERAR MODELO
    # ==========================================

    st.header("📂 Paso 6 - Recuperar modelo")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Cargar Pickle",
            use_container_width=True
        ):

            if os.path.exists("models/modelo.pkl"):

                with open("models/modelo.pkl", "rb") as archivo:
                    st.session_state.modelo = pickle.load(archivo)

                st.session_state.modelo_recuperado = True

                st.success("✅ Modelo recuperado desde Pickle")

            else:

                st.error("No existe modelo.pkl")

    with col2:

        if st.button(
            "Cargar Joblib",
            use_container_width=True
        ):

            if os.path.exists("models/modelo.joblib"):

                st.session_state.modelo = load(
                    "models/modelo.joblib"
                )

                st.session_state.modelo_recuperado = True

                st.success("✅ Modelo recuperado desde Joblib")

            else:

                st.error("No existe modelo.joblib")

    if st.session_state.modelo_recuperado:
        st.success("🎉 El modelo está nuevamente listo para usarse.")

    st.divider()

        # ==========================================
    # PASO 7 - PREDICCIÓN
    # ==========================================

    st.header("🔮 Paso 7 - Realizar una Predicción")

    st.markdown("""
Ingresa las características de una flor para que el modelo prediga su especie.
""")

    col1, col2 = st.columns(2)

    with col1:

        sepal_length = st.slider(
            "Sepal Length (cm)",
            4.0,
            8.0,
            5.1
        )

        sepal_width = st.slider(
            "Sepal Width (cm)",
            2.0,
            5.0,
            3.5
        )

    with col2:

        petal_length = st.slider(
            "Petal Length (cm)",
            1.0,
            7.0,
            1.4
        )

        petal_width = st.slider(
            "Petal Width (cm)",
            0.1,
            3.0,
            0.2
        )

    if st.button(
        "🌸 Realizar Predicción",
        disabled=st.session_state.modelo is None,
        use_container_width=True
    ):

        muestra = [[

            sepal_length,
            sepal_width,
            petal_length,
            petal_width

        ]]

        pred = st.session_state.modelo.predict(muestra)

        clases = iris.target_names

        especie = clases[pred[0]]

        st.success(f"🌼 Especie predicha: **{especie.title()}**")

        # Mostrar probabilidades si el modelo las soporta
        if hasattr(st.session_state.modelo, "predict_proba"):

            probabilidades = st.session_state.modelo.predict_proba(muestra)[0]

            st.subheader("📊 Probabilidades")

            for nombre, prob in zip(clases, probabilidades):

                st.write(f"**{nombre.title()}**")

                st.progress(float(prob))

                st.caption(f"{prob:.2%}")

    st.divider()

    # ==========================================
    # PROGRESO DEL LABORATORIO
    # ==========================================

    st.header("🏆 Progreso del Laboratorio")

    progreso = 0

    if st.session_state.modelo_entrenado:
        progreso += 20

    if st.session_state.pickle_guardado:
        progreso += 20

    if st.session_state.joblib_guardado:
        progreso += 20

    if st.session_state.modelo_recuperado:
        progreso += 20

    if st.session_state.modelo is not None:
        progreso += 20

    st.progress(progreso / 100)

    st.metric(
        "Progreso",
        f"{progreso}%"
    )

    if progreso == 100:

        st.balloons()

        st.success("""
# 🎉 ¡Laboratorio Completado!

Has realizado correctamente todo el ciclo de vida de un modelo de Machine Learning.

✅ Dataset cargado

✅ Modelo entrenado

✅ Accuracy calculado

✅ Modelo serializado con Pickle

✅ Modelo serializado con Joblib

✅ Modelo recuperado

✅ Predicción realizada

¡Excelente trabajo!
""")

    st.divider()

    # ==========================================
    # RESUMEN
    # ==========================================

    with st.expander("📚 ¿Qué aprendimos?"):

        st.markdown("""

### Hoy aprendiste a:

- Entrenar un modelo.
- Calcular Accuracy.
- Guardarlo con Pickle.
- Guardarlo con Joblib.
- Recuperarlo desde disco.
- Realizar predicciones sin volver a entrenar.

### Idea clave

Entrenamos **una sola vez**.

Luego guardamos el modelo y lo reutilizamos todas las veces que sean necesarias.

Ese es el objetivo de la **serialización**.
""")
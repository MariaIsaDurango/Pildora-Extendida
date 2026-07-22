import streamlit as st
import time


def show_serialization():

    st.title("📦 Serialización de Modelos")

    st.markdown("""
La serialización consiste en **guardar un objeto en un archivo**
para poder recuperarlo posteriormente sin volver a crearlo.

En Machine Learning, ese objeto suele ser un **modelo entrenado**.
""")

    st.divider()

        # ==========================================
    # EL PROBLEMA
    # ==========================================

    st.header("🤔 El problema")

    st.error("""
Imagina que entrenaste un modelo durante **4 horas**.

Al día siguiente cierras Python...

¿Qué ocurre con el modelo?
""")

    respuesta = st.radio(
        "Selecciona una respuesta",
        (
            "Se pierde",
            "Permanece en la memoria",
            "Python lo guarda automáticamente",
        ),
        index=None,
        key="problem_question"
    )

    if st.button(
        "Comprobar respuesta",
        key="check_problem_question",
        use_container_width=True
    ):

        if respuesta is None:

            st.warning("Selecciona una opción antes de comprobarla. 👆")

        elif respuesta == "Se pierde":

            st.success("""
🎉 ¡Correcto!

Los modelos viven únicamente en la memoria RAM.

Cuando finaliza el programa de Python, toda esa información se pierde si no la hemos guardado mediante serialización.
""")

        else:

            st.error("""
❌ Incorrecto.

Python **no guarda automáticamente** los modelos y tampoco permanecen en memoria después de cerrar el programa.

Por eso utilizamos **Pickle** o **Joblib** para almacenarlos en un archivo.
""")

    if st.button(
        "Reintentar",
        key="reset_problem_question",
        use_container_width=True
    ):

        if "problem_question" in st.session_state:
            del st.session_state["problem_question"]

        st.rerun()

    st.divider()

    # =====================================================
    # MEMORIA
    # =====================================================

    st.header("🧠 ¿Qué ocurre en la memoria?")

    st.code("""

        Entrenar modelo

               │

               ▼

        Modelo en RAM

               │

      Cerrar Python

               │

               ▼

          ❌ Se pierde

    """)

    st.warning("""
Los objetos viven únicamente en la memoria RAM.

Cuando termina el programa, desaparecen.
""")

    st.divider()

    # =====================================================
    # SOLUCIÓN
    # =====================================================

    st.header("💡 La solución")

    st.success("""
En lugar de volver a entrenar el modelo...

lo guardamos en un archivo.

Ese proceso recibe el nombre de

**SERIALIZACIÓN**
""")

    st.code("""

        Modelo Entrenado

               │

               ▼

      Serialización

               │

               ▼

        modelo.pkl

               │

               ▼

      Cargar mañana

    """)

    st.divider()

    # =====================================================
    # ANALOGÍAS
    # =====================================================

    st.header("🎮 Analogías")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info("""
### 🎮 Videojuego

Guardas una partida.

La recuperas mañana.
""")

    with c2:

        st.success("""
### 🍰 Receta

Escribes una receta.

La utilizas cuando quieras.
""")

    with c3:

        st.warning("""
### 📒 Apuntes

Guardas tus apuntes.

No vuelves a escribirlos.
""")

    st.divider()

    # =====================================================
    # SIMULACIÓN
    # =====================================================

    st.header("▶ Simulación")

    if st.button("Entrenar modelo"):

        barra = st.progress(0)

        texto = st.empty()

        pasos = [

            "📂 Leyendo datos...",

            "🧹 Limpiando datos...",

            "🤖 Entrenando modelo...",

            "📈 Calculando métricas..."

        ]

        for i in range(4):

            texto.info(pasos[i])

            barra.progress((i + 1) * 25)

            time.sleep(1)

        texto.success("🎉 Modelo entrenado.")

    st.divider()

    if st.button("Cerrar Python"):

        st.error("""
💥 El modelo desapareció de la memoria.

Hay que volver a entrenarlo.
""")

    st.divider()

    if st.button("Guardar Modelo"):

        barra = st.progress(0)

        mensaje = st.empty()

        for i in range(100):

            barra.progress(i + 1)

            time.sleep(0.01)

        mensaje.success("""
Modelo guardado correctamente.

Archivo creado:

📄 modelo.pkl
""")

    st.divider()

    # =====================================================
    # BENEFICIOS
    # =====================================================

    st.header("🚀 Beneficios de serializar")

    col1, col2 = st.columns(2)

    with col1:

        st.success("""
✔ Ahorras tiempo

✔ No vuelves a entrenar

✔ Compartes modelos

✔ Implementas producción
""")

    with col2:

        st.info("""
✔ Recuperación inmediata

✔ Fácil despliegue

✔ Menor costo computacional

✔ Reutilización
""")

    st.divider()

    # =====================================================
    # ANTES VS DESPUÉS
    # =====================================================

    st.header("📊 Antes y Después")

    c1, c2 = st.columns(2)

    with c1:

        st.error("""
## ❌ Sin serialización

Entrenar

Cerrar Python

Entrenar nuevamente

Cerrar Python

Entrenar nuevamente
""")

    with c2:

        st.success("""
## ✅ Con serialización

Entrenar

Guardar

Cerrar Python

Cargar

Predecir
""")

    st.divider()

    # =====================================================
    # RESUMEN
    # =====================================================

    st.header("📋 Resumen")

    st.table({

        "Concepto":[

            "Modelo",

            "RAM",

            "Serialización",

            "Archivo",

            "Recuperación"

        ],

        "Descripción":[

            "Objeto entrenado",

            "Memoria temporal",

            "Guardar objeto",

            ".pkl o .joblib",

            "Volver a utilizar"

        ]

    })

    st.divider()

    # =====================================================
    # QUIZ
    # =====================================================

        # ==========================================
    # MINI QUIZ
    # ==========================================

    st.header("🎯 Mini Quiz")

    opcion = st.radio(
        "¿Cuál es el objetivo principal de la serialización?",
        (
            "Mejorar la precisión",
            "Guardar el modelo para reutilizarlo",
            "Entrenar más rápido",
        ),
        index=None,
        key="quiz_serialization"
    )

    if st.button(
        "Comprobar respuesta",
        key="check_quiz_serialization",
        use_container_width=True
    ):

        if opcion is None:

            st.warning("Selecciona una opción antes de comprobarla. 👆")

        elif opcion == "Guardar el modelo para reutilizarlo":

            st.success(
                "🎉 ¡Excelente! La serialización permite guardar el modelo para reutilizarlo sin volver a entrenarlo."
            )

        else:

            st.error(
                "❌ No es correcto. La serialización no mejora la precisión ni acelera el entrenamiento; su objetivo es guardar el modelo para reutilizarlo."
            )

    if st.button(
        "Reintentar",
        key="reset_quiz_serialization",
        use_container_width=True
    ):

        if "quiz_serialization" in st.session_state:
            del st.session_state["quiz_serialization"]

        st.rerun()

    st.divider()

    st.success("""
🎉 ¡Muy bien!

Ahora ya sabes por qué existe la serialización.

En la siguiente sección aprenderemos dos herramientas que realizan este proceso:

🐍 Pickle

⚡ Joblib
""")
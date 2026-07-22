import streamlit as st
import time


def show_model_lifecycle():

    st.title("🔄 Ciclo de Vida de un Modelo de Machine Learning")

    st.markdown("""
    Un modelo de Machine Learning **no termina cuando se entrena**.
    Al contrario, ese es solo el comienzo.

    En esta sección recorreremos cada una de las etapas hasta que el
    modelo es utilizado por un usuario en producción.
    """)

    st.divider()

    # ===========================================================
    # Analogía
    # ===========================================================

    st.header("🎮 Analogía")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### 🎮 Videojuego

1️⃣ Empiezas una partida

2️⃣ Juegas varias horas

3️⃣ Guardas la partida

4️⃣ Cierras el juego

5️⃣ Continúas mañana
""")

    with col2:

        st.success("""
### 🤖 Machine Learning

1️⃣ Obtienes datos

2️⃣ Entrenas el modelo

3️⃣ Guardas el modelo

4️⃣ Cierras Python

5️⃣ Lo cargas nuevamente
""")

    st.divider()

    # ===========================================================
    # Flujo
    # ===========================================================

    st.header("🛣 Flujo completo")

    st.code("""

        Datos
          │
          ▼
   Preparación
          │
          ▼
 Entrenamiento
          │
          ▼
   Evaluación
          │
          ▼
 Serialización
          │
          ▼
   Producción
          │
          ▼
   Predicción

""")

    st.divider()

    # ===========================================================
    # Simulador
    # ===========================================================

    st.header("🎮 Simulador del ciclo de vida")

    etapa = st.selectbox(
        "Selecciona una etapa",
        [
            "📂 Datos",
            "🧹 Preparación",
            "🤖 Entrenamiento",
            "📈 Evaluación",
            "💾 Serialización",
            "☁ Producción",
            "🔮 Predicción"
        ]
    )

    if etapa == "📂 Datos":

        st.success("Los datos son el punto de partida.")

        st.image(
            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=900"
        )

        st.write("""
Ejemplo:

- Ventas

- Clientes

- Imágenes

- Audio

- Texto
""")

    elif etapa == "🧹 Preparación":

        st.info("""
Los datos rara vez llegan limpios.

Normalmente debemos:

- eliminar valores nulos

- eliminar duplicados

- transformar variables

- normalizar datos
""")

    elif etapa == "🤖 Entrenamiento":

        st.warning("""
Aquí el algoritmo aprende patrones.

Ejemplos:

✔ Regresión

✔ Árboles

✔ Random Forest

✔ Redes Neuronales
""")

    elif etapa == "📈 Evaluación":

        st.success("""
Ahora comprobamos si el modelo aprendió correctamente.

Métricas comunes:

Accuracy

Precision

Recall

F1 Score

RMSE
""")

    elif etapa == "💾 Serialización":

        st.success("""
¡Aquí aparece Pickle y Joblib!

Guardamos el modelo para utilizarlo más adelante.

No queremos volver a entrenarlo.
""")

    elif etapa == "☁ Producción":

        st.info("""
El modelo ahora vive dentro de una aplicación.

Por ejemplo:

Netflix

Amazon

Spotify

Banco

Hospital
""")

    elif etapa == "🔮 Predicción":

        st.success("""
El usuario envía nuevos datos.

El modelo responde inmediatamente.

No vuelve a entrenarse.
""")

    st.divider()

    # ===========================================================
    # Animación
    # ===========================================================

    st.header("▶ Simulación")

    if st.button("Iniciar simulación"):

        barra = st.progress(0)

        estado = st.empty()

        pasos = [

            "📂 Cargando datos...",

            "🧹 Limpiando datos...",

            "🤖 Entrenando modelo...",

            "📈 Evaluando...",

            "💾 Guardando modelo...",

            "☁ Desplegando en producción...",

            "🔮 Realizando predicciones..."
        ]

        for i in range(7):

            estado.info(pasos[i])

            barra.progress((i + 1) * 14)

            time.sleep(1)

        estado.success("🎉 Modelo listo para producción.")

    st.divider()

    # ===========================================================
    # Tabla
    # ===========================================================

    st.header("📋 Resumen")

    st.table({

        "Etapa":[

            "Datos",

            "Preparación",

            "Entrenamiento",

            "Evaluación",

            "Serialización",

            "Producción",

            "Predicción"

        ],

        "Objetivo":[

            "Recolectar información",

            "Limpiar datos",

            "Aprender patrones",

            "Medir rendimiento",

            "Guardar modelo",

            "Publicarlo",

            "Responder usuarios"

        ]

    })

    st.divider()

    # ===========================================================
    # Pregunta
    # ===========================================================

 
    # ... código anterior ...

    st.header("🧠 Reflexiona")

    respuesta = st.radio(
        "¿En qué etapa aparece Pickle o Joblib?",
        (
            "Entrenamiento",
            "Evaluación",
            "Serialización",
            "Predicción",
        ),
        index=None,
        key="serialization_question"
    )

    if st.button("Comprobar respuesta", key="check_serialization"):

        if respuesta is None:

            st.warning("Selecciona una opción antes de comprobarla. 👆")

        elif respuesta == "Serialización":

            st.success(
                "🎉 ¡Correcto! Pickle y Joblib aparecen en la etapa de serialización del modelo."
            )

        else:

            st.error(
                "❌ No es correcto. Recuerda que después del entrenamiento guardamos el modelo mediante la serialización."
            )

    if st.button(
        "Reintentar",
        key="reset_serialization",
        use_container_width=True
    ):

        if "serialization_question" in st.session_state:
            del st.session_state["serialization_question"]

        st.rerun()

    st.divider()

    st.success("""
    ✅ Ya conoces todo el ciclo de vida.

    Ahora podemos pasar a la siguiente sección.
    """)
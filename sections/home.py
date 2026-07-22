import streamlit as st
import plotly.graph_objects as go


def show_home():

    # ======================================================
    # HERO
    # ======================================================

    st.markdown("""
    <div class="hero">
        <div class="big">
            🤖 Machine Learning Model Lifecycle Lab
        </div>
        <br>
        <div class="sub">
            Aprende el ciclo de vida de un modelo de Machine Learning y la serialización
            utilizando <b>Pickle</b> y <b>Joblib</b> mediante ejemplos prácticos.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([2, 1])

    with c1:
        if st.button("🚀 Comenzar la clase"):
            st.success("Selecciona **Ciclo de Vida** en el menú lateral.")

    with c2:
        if st.button("📚 Ver objetivos"):
            st.info("Desplázate hacia abajo para conocer el contenido .")

    st.divider()

    # ======================================================
    # MÉTRICAS
    # ======================================================

    st.subheader("📊 Información de la Pildora")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("⏱ Duración", "60 min")
    c2.metric("🎓 Nivel", "Principiante")
    c3.metric("🧪 Laboratorios", "2")
    c4.metric("🎯 Quiz", "10 preguntas")

    st.divider()

    # ======================================================
    # OBJETIVOS
    # ======================================================

    st.subheader("🎯 Objetivos de aprendizaje")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
<div class="card">

### 🔄 Ciclo de Vida

Comprenderás cómo un modelo pasa desde los datos hasta la producción.

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="card">

### 📦 Serialización

Entenderás por qué guardamos un modelo entrenado.

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="card">

### 🐍 Pickle

Aprenderás a guardar modelos utilizando Pickle.

</div>
""", unsafe_allow_html=True)

    with col2:

        st.markdown("""
<div class="card">

### ⚡ Joblib

Aprenderás cuándo utilizar Joblib y por qué es más eficiente.

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="card">

### 🧪 Laboratorio

Entrenarás un modelo y lo guardarás en disco.

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="card">

### 🎮 Quiz

Comprobarás tus conocimientos mediante preguntas.

</div>
""", unsafe_allow_html=True)

    st.divider()

    # ======================================================
    # RUTA DEL CURSO
    # ======================================================

    st.subheader("🛣 Ruta de aprendizaje")

    st.progress(0)

    st.code("""
          Datos
             │
             ▼
     Entrenamiento
             │
             ▼
        Modelo ML
             │
             ▼
   Pickle / Joblib
             │
             ▼
       Producción
             │
             ▼
      Predicciones
    """)

    st.divider()

    # ======================================================
    # DASHBOARD
    # ======================================================

    st.subheader("📊 Distribución del tiempo")

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[
                "Ciclo de Vida",
                "Serialización",
                "Pickle",
                "Joblib",
                "Laboratorio",
                "Quiz"
            ],
            y=[10, 10, 8, 8, 15, 9],
            text=[
                "10",
                "10",
                "8",
                "8",
                "15",
                "9"
            ],
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Tiempo estimado por tema",
        template="plotly_dark",
        height=450,
        xaxis_title="Tema",
        yaxis_title="Minutos"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ======================================================
    # EXPANDER
    # ======================================================

    with st.expander("📚 ¿Qué aprenderás durante la clase?"):

        st.markdown("""
### Al finalizar podrás:

✅ Explicar el ciclo de vida de un modelo.

✅ Comprender qué es la serialización.

✅ Diferenciar Pickle y Joblib.

✅ Guardar un modelo entrenado.

✅ Recuperar un modelo.

✅ Realizar predicciones sin volver a entrenarlo.
""")

    st.divider()

    # ======================================================
    # ANALOGÍA
    # ======================================================

    st.subheader("🎮 Analogía")

    c1, c2 = st.columns(2)

    with c1:

        st.info("🎮 Guardar una partida de un videojuego")

        st.write("""
1. Juegas durante horas.

2. Guardas la partida.

3. Apagas el computador.

4. Al día siguiente continúas exactamente donde estabas.
""")

    with c2:

        st.success("🤖 Modelo de Machine Learning")

        st.write("""
1. Entrenas el modelo.

2. Lo guardas con Pickle o Joblib.

3. Cierras Python.

4. Al día siguiente realizas predicciones sin volver a entrenarlo.
""")

    st.divider()

    # ======================================================
    # DATOS CURIOSOS
    # ======================================================

    st.subheader("💡 ¿Sabías que...?")

    a, b, c = st.columns(3)

    with a:
        st.info("""
🧠 **Entrenar un modelo** puede tardar horas.

**Cargarlo** tarda solo segundos.
""")

    with b:
        st.info("""
🚀 Empresas como Netflix, Google y Amazon utilizan modelos serializados.
""")

    with c:
        st.info("""
💾 Los modelos entrenados normalmente se almacenan en archivos **.pkl** o **.joblib**.
""")

    st.divider()

    # ======================================================
    # MINI QUIZ
    # ======================================================

    st.subheader("🎮 Mini Quiz")

    respuesta = st.radio(
        "¿Por qué guardamos un modelo entrenado?",
        (
            "Para no volver a entrenarlo",
            "Para mejorar automáticamente su precisión",
            "Para ocupar menos memoria RAM"
        )
    )

    if st.button("Comprobar respuesta", key="check_home_question"):
        if respuesta is None:
            st.warning("Elige una opción antes de comprobarla. 👆")
        elif respuesta == "Para no volver a entrenarlo":
            st.success("🎉 Correcto. Esa es la razón principal.")
        else:
            st.error("Aún no. La idea es poder reutilizar el modelo sin entrenarlo de nuevo.")
    st.button(
        "Reintentar",
        key="reset_home_question",
        on_click=lambda: st.session_state.pop("home_question", None),
    )

    st.info("🚀 Comienza en **Ciclo de vida** y termina aplicando lo aprendido en **Reto Colab**.")

    # ======================================================
    # CHECKLIST
    # ======================================================

    st.subheader("✅ Lo que lograrás hoy")

    col1, col2 = st.columns(2)

    with col1:
        st.checkbox("Comprender el ciclo de vida")
        st.checkbox("Entender la serialización")
        st.checkbox("Aprender Pickle")

    with col2:
        st.checkbox("Aprender Joblib")
        st.checkbox("Guardar modelos")
        st.checkbox("Recuperar modelos")

    st.divider()

    # ======================================================
    # BOTÓN FINAL
    # ======================================================

    if st.button("🚀 ¡Estoy listo para comenzar!"):

        st.balloons()

        st.success("""
Excelente.

Ahora selecciona **🔄 Ciclo de Vida** desde el menú lateral y comenzaremos la clase.
""")
import plotly.graph_objects as go
import streamlit as st


def show_home():
    st.markdown(
        """
        <div class="hero">
            <div class="big">🤖 Ciclo de Vida de Modelos ML</div>
            <br>
            <div class="sub">
                Aprende cómo un modelo pasa de los datos a las predicciones y cómo conservarlo con <b>Pickle</b> y <b>Joblib</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("📊 Información de la clase")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("⏱️ Duración", "45 min")
    c2.metric("🎓 Nivel", "Principiante")
    c3.metric("📚 Temas", "4")
    c4.metric("🎯 Quiz", "10 preguntas")

    st.divider()
    st.subheader("✨ Lo que aprenderás")
    col1, col2 = st.columns(2)
    cards = [
        ("🔄 Ciclo de vida", "Comprenderás cómo un modelo pasa desde los datos hasta producción."),
        ("📦 Serialización", "Entenderás por qué guardamos un modelo entrenado."),
        ("🐍 Pickle", "Conocerás una herramienta estándar para guardar objetos de Python."),
        ("⚡ Joblib", "Sabrás cuándo es conveniente para modelos y arreglos grandes."),
        ("🎯 Quiz", "Comprobarás tus conocimientos sin respuestas preseleccionadas."),
        ("🏆 Reto Colab", "Resolverás un reto guiado con pistas progresivas."),
    ]
    for index, (title, body) in enumerate(cards):
        with (col1 if index % 2 == 0 else col2):
            st.markdown(
                f'<div class="card"><h3>{title}</h3><p>{body}</p></div>',
                unsafe_allow_html=True,
            )

    st.divider()
    st.subheader("🗺️ Ruta de aprendizaje")
    st.code(
        """
Datos → Preparación → Entrenamiento → Evaluación
                 ↓
       Serialización (Pickle / Joblib)
                 ↓
          Producción → Predicciones
        """
    )

    fig = go.Figure(
        go.Bar(
            x=["Ciclo de vida", "Serialización", "Pickle vs Joblib", "Quiz", "Reto Colab"],
            y=[8, 8, 8, 7, 14],
            text=["8", "8", "8", "7", "14"],
            textposition="outside",
            marker_color=["#38bdf8", "#22c55e", "#a78bfa", "#f59e0b", "#f472b6"],
        )
    )
    fig.update_layout(
        title="Tiempo estimado por tema (minutos)",
        template="plotly_dark",
        height=380,
        xaxis_title="Tema",
        yaxis_title="Minutos",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("🧠 Pregunta de inicio")
    respuesta = st.radio(
        "¿Por qué guardamos un modelo entrenado?",
        [
            "Para no volver a entrenarlo",
            "Para mejorar automáticamente su precisión",
            "Para ocupar menos memoria RAM",
        ],
        index=None,
        key="home_question",
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

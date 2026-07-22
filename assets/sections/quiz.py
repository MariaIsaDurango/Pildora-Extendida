import streamlit as st


def _reset_quiz():
    for i in range(10):
        st.session_state.pop(f"quiz_response_{i}", None)


def show_quiz():

    st.title("🎯 Quiz Final")
    st.subheader("Demuestra cuánto aprendiste")

    st.markdown("""
Responde las siguientes preguntas.

Al finalizar obtendrás tu puntaje y una retroalimentación.
""")

    st.divider()

    preguntas = [

        {
            "pregunta":"1. ¿Qué es el ciclo de vida de un modelo de Machine Learning?",
            "opciones":[
                "El recorrido desde los datos hasta la producción",
                "Solo el entrenamiento",
                "Solo la predicción",
                "Solo la evaluación"
            ],
            "correcta":0,
            "explicacion":"El ciclo de vida comprende todas las etapas del modelo."
        },

        {
            "pregunta":"2. ¿Por qué no entrenamos un modelo cada vez que hacemos una predicción?",
            "opciones":[
                "Porque consume tiempo y recursos",
                "Porque Python no lo permite",
                "Porque cambia el algoritmo",
                "Porque pierde precisión"
            ],
            "correcta":0,
            "explicacion":"Entrenar puede tardar minutos u horas."
        },

        {
            "pregunta":"3. ¿Qué es la serialización?",
            "opciones":[
                "Guardar un objeto en un archivo",
                "Entrenar un modelo",
                "Evaluar un modelo",
                "Limpiar datos"
            ],
            "correcta":0,
            "explicacion":"Serializar significa guardar un objeto para reutilizarlo."
        },

        {
            "pregunta":"4. ¿Qué biblioteca pertenece a Python por defecto?",
            "opciones":[
                "Pickle",
                "Joblib",
                "TensorFlow",
                "PyTorch"
            ],
            "correcta":0,
            "explicacion":"Pickle viene incluido con Python."
        },

        {
            "pregunta":"5. ¿Qué extensión utiliza normalmente Pickle?",
            "opciones":[
                ".pkl",
                ".pickle",
                ".model",
                ".txt"
            ],
            "correcta":0,
            "explicacion":"La extensión más utilizada es .pkl"
        },

        {
            "pregunta":"6. ¿Qué biblioteca suele recomendarse para modelos grandes de Scikit-Learn?",
            "opciones":[
                "Joblib",
                "Pickle",
                "OpenCV",
                "Matplotlib"
            ],
            "correcta":0,
            "explicacion":"Joblib está optimizada para objetos grandes y matrices NumPy."
        },

        {
            "pregunta":"7. ¿Qué función guarda un modelo utilizando Pickle?",
            "opciones":[
                "pickle.dump()",
                "pickle.load()",
                "pickle.save()",
                "pickle.write()"
            ],
            "correcta":0,
            "explicacion":"dump() guarda el objeto."
        },

        {
            "pregunta":"8. ¿Qué función recupera un modelo con Pickle?",
            "opciones":[
                "pickle.load()",
                "pickle.dump()",
                "pickle.open()",
                "pickle.read()"
            ],
            "correcta":0,
            "explicacion":"load() reconstruye el objeto."
        },

        {
            "pregunta":"9. ¿Dónde vive un modelo antes de guardarlo?",
            "opciones":[
                "En la memoria RAM",
                "En Internet",
                "En la GPU permanentemente",
                "En el disco duro"
            ],
            "correcta":0,
            "explicacion":"Mientras el programa está ejecutándose vive en memoria."
        },

        {
            "pregunta":"10. ¿Cuál es una buena práctica?",
            "opciones":[
                "Guardar también el preprocesamiento",
                "Eliminar el modelo",
                "No documentar versiones",
                "Cargar archivos desconocidos"
            ],
            "correcta":0,
            "explicacion":"Siempre debemos guardar también el preprocesamiento."
        }

    ]

    respuestas = []

    contestadas = 0
    progreso = st.progress(0)

    for i, pregunta in enumerate(preguntas):

        st.markdown(f"### {pregunta['pregunta']}")

        respuesta = st.radio(
            "",
            pregunta["opciones"],
            index=None,
            key=f"quiz_response_{i}",
        )

        respuestas.append(respuesta)
        if respuesta is not None:
            contestadas += 1

        st.divider()

    progreso.progress(contestadas / len(preguntas))
    st.caption(f"Respuestas completadas: {contestadas}/{len(preguntas)}")

    if st.button(
        "✅ Calificar Quiz",
        use_container_width=True,
        disabled=contestadas != len(preguntas),
        help="Responde todas las preguntas para habilitar la calificación.",
    ):

        puntaje = 0

        st.header("Resultados")

        for i, pregunta in enumerate(preguntas):

            correcta = pregunta["opciones"][pregunta["correcta"]]

            if respuestas[i] == correcta:

                puntaje += 1
                st.success(f"Pregunta {i+1}: Correcta")

            else:

                st.error(f"Pregunta {i+1}: Incorrecta")

            st.info(pregunta["explicacion"])

        porcentaje = puntaje * 10

        st.divider()

        st.metric(
            "Puntaje",
            f"{puntaje}/10"
        )

        st.progress(puntaje / 10)

        if porcentaje >= 90:

            st.balloons()

            st.success("""
🏆 Excelente.

Dominas el tema perfectamente.
""")

        elif porcentaje >= 70:

            st.success("""
👏 Muy buen trabajo.

Solo necesitas reforzar algunos conceptos.
""")

        elif porcentaje >= 50:

            st.warning("""
🙂 Buen intento.

Te recomiendo repasar las secciones anteriores.
""")

        else:

            st.error("""
📚 Revisa nuevamente las secciones anteriores y vuelve a intentarlo.
""")

    st.divider()

    st.button("🔄 Reiniciar quiz", use_container_width=True, on_click=_reset_quiz)

    st.info("""
💡 Consejo:

No memorices el código.

Comprende el problema que resuelve la serialización.
""")

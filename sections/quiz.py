import streamlit as st


def show_quiz():

    st.title("🎯 Quiz Final")
    st.subheader("🧠 Pon a prueba lo que aprendiste, no solo lo que memorizaste")

    st.markdown("""
Estas preguntas no son de memoria — son **situaciones reales** que vas a
enfrentar en un proyecto de Machine Learning. Piensa antes de responder,
no busques la palabra clave, razona el escenario. 🎯

Al finalizar obtendrás tu puntaje y una explicación de cada respuesta.
""")

    st.divider()

    preguntas = [

        {
            "pregunta": "1️⃣ Entrenaste un `RandomForestClassifier` con 300 árboles sobre 200,000 filas. ¿Cómo deberías guardarlo y por qué?",
            "opciones": [
                "Con Pickle, porque es más simple de usar",
                "Con Joblib, porque está optimizado para los arrays grandes de NumPy que contiene el modelo",
                "No se guarda, se reentrena cada vez que se necesita predecir",
                "Como archivo de texto plano (.txt)"
            ],
            "correcta": 1,
            "explicacion": "🧩 Un RandomForest con muchos árboles almacena internamente grandes arrays de NumPy. Joblib está diseñado justo para ese caso: es más rápido y permite comprimir mejor el archivo final."
        },

        {
            "pregunta": "2️⃣ Un compañero guardó el modelo, pero olvidó guardar el `StandardScaler` que usó antes de entrenar. ¿Qué es lo más probable que ocurra cuando alguien cargue el modelo y prediga con datos sin escalar?",
            "opciones": [
                "Nada, el modelo escala los datos automáticamente",
                "El modelo puede dar predicciones incorrectas o fallar, porque espera datos ya escalados",
                "Python detecta el error y reentrena el modelo solo",
                "El archivo del modelo se corrompe"
            ],
            "correcta": 1,
            "explicacion": "⚠️ Este es el error más común en producción: si el modelo se entrenó con datos escalados y luego predice con datos sin escalar, los resultados pueden ser inconsistentes o abiertamente erróneos. Por eso se recomienda guardar el pipeline completo, no solo el modelo."
        },

        {
            "pregunta": "3️⃣ Un servidor en producción recibe 10,000 solicitudes de predicción por minuto. ¿Por qué sería una mala idea reentrenar el modelo en cada solicitud?",
            "opciones": [
                "Porque el modelo perdería precisión con cada reentrenamiento",
                "Porque entrenar toma mucho más tiempo que predecir, y el servidor no podría responder a tiempo",
                "Porque Python no permite entrenar más de una vez",
                "Porque los datos cambian solos con cada solicitud"
            ],
            "correcta": 1,
            "explicacion": "⏱ Entrenar puede tardar minutos, horas o incluso días, mientras que cargar un modelo ya serializado y predecir toma milisegundos. Por eso el modelo se entrena una sola vez y se reutiliza."
        },

        {
            "pregunta": "4️⃣ Tienes un archivo `modelo_v1.pkl` entrenado con scikit-learn 1.2, y tu servidor de producción tiene instalada la versión 1.6. ¿Qué riesgo corres al cargarlo?",
            "opciones": [
                "Ninguno, todas las versiones de scikit-learn son 100% compatibles entre sí",
                "Puede haber incompatibilidad: el archivo podría no cargar, o cargar con comportamientos distintos",
                "El archivo se actualiza automáticamente a la nueva versión",
                "El archivo deja de existir al detectar la diferencia de versión"
            ],
            "correcta": 1,
            "explicacion": "🧬 La incompatibilidad de versiones es uno de los errores más comunes en serialización. Por eso es buena práctica documentar la versión exacta de las librerías usadas al entrenar el modelo."
        },

        {
            "pregunta": "5️⃣ Recibes por correo un archivo `modelo.pkl` de un remitente que no conoces. ¿Cuál es la buena práctica?",
            "opciones": [
                "Cargarlo de inmediato para probar qué contiene",
                "No cargarlo sin verificar la fuente: un archivo .pkl puede ejecutar código arbitrario al deserializarse",
                "Convertirlo primero a .joblib para que sea seguro",
                "Abrirlo directamente con doble clic en el explorador de archivos"
            ],
            "correcta": 1,
            "explicacion": "🔒 Pickle puede ejecutar código al momento de cargar (deserializar) un archivo. Nunca se debe cargar un .pkl de una fuente no confiable, sin importar qué tan inofensivo parezca."
        },

        {
            "pregunta": "6️⃣ Tienes dos objetos que guardar: (A) un diccionario simple `{'lr': 0.01, 'epochs': 10}` y (B) un modelo de scikit-learn con miles de coeficientes. ¿Qué combinación tiene más sentido?",
            "opciones": [
                "A con Joblib y B con Pickle",
                "A con Pickle y B con Joblib",
                "Ambos únicamente con Pickle, sin excepción",
                "Ambos únicamente con Joblib, sin excepción"
            ],
            "correcta": 1,
            "explicacion": "⚖️ El diccionario simple no tiene arrays pesados, así que Pickle es suficiente. El modelo con muchos coeficientes sí se beneficia de la optimización de Joblib para arrays de NumPy."
        },

        {
            "pregunta": "7️⃣ Un ingeniero guarda solo el modelo entrenado, sin el pipeline de preprocesamiento, porque \"ya lo tiene anotado en un documento aparte\". ¿Qué problema práctico anticipas?",
            "opciones": [
                "Ninguno, mientras el documento exista no hay riesgo",
                "Riesgo de inconsistencia: alguien puede olvidar aplicar el preprocesamiento exacto, o aplicarlo mal, al usar el modelo",
                "El modelo mejora su rendimiento al no cargar el preprocesamiento",
                "El archivo del modelo ocupará más espacio en disco"
            ],
            "correcta": 1,
            "explicacion": "📄 Un documento aparte depende de que alguien lo lea y lo siga al pie de la letra, cada vez. Guardar el pipeline completo dentro del mismo archivo serializado elimina ese riesgo por completo."
        },

        {
            "pregunta": "8️⃣ Dentro del ciclo de vida de un modelo, ¿en qué momento ocurre exactamente la serialización?",
            "opciones": [
                "Antes de entrenar el modelo",
                "Entre la evaluación del modelo y su despliegue en producción",
                "Después de que el usuario recibe la predicción",
                "Durante la recolección de datos"
            ],
            "correcta": 1,
            "explicacion": "🔗 La serialización es el puente entre 'el modelo ya fue evaluado y funciona bien' y 'el modelo está listo para usarse en producción sin volver a entrenarlo'."
        },

        {
            "pregunta": "9️⃣ Tu archivo `modelo.joblib` pesa 900 MB y necesitas reducir su tamaño en disco. ¿Qué deberías usar?",
            "opciones": [
                "El parámetro `compress` de `joblib.dump()`",
                "Guardarlo como archivo de texto en vez de binario",
                "Eliminar la mitad de los árboles del modelo manualmente",
                "Cambiarlo a formato .pkl, que siempre pesa menos"
            ],
            "correcta": 0,
            "explicacion": "📦 Joblib incluye compresión integrada y fácil de activar con el parámetro `compress` (por ejemplo `joblib.dump(modelo, 'modelo.joblib', compress=3)`), ideal para modelos grandes."
        },

        {
            "pregunta": "🔟 ¿Cuál de estas situaciones NO es un buen caso para usar Pickle como primera opción?",
            "opciones": [
                "Guardar una lista simple de nombres de columnas",
                "Guardar un modelo RandomForest entrenado sobre un dataset grande",
                "Guardar un diccionario de configuración del proyecto",
                "Guardar un objeto propio simple, sin arrays pesados"
            ],
            "correcta": 1,
            "explicacion": "🌲 Un RandomForest grande contiene muchos arrays de NumPy internamente. Aunque Pickle técnicamente puede guardarlo, Joblib es la opción recomendada por ser más eficiente en ese caso."
        }

    ]

    respuestas = []

    progreso = st.progress(0)

    for i, pregunta in enumerate(preguntas):

        progreso.progress((i + 1) / len(preguntas))

        st.markdown(f"### {pregunta['pregunta']}")

        respuesta = st.radio(
            "Selecciona una opción",
            pregunta["opciones"],
            key=i,
            index=None,
            label_visibility="collapsed"
        )

        respuestas.append(respuesta)

        st.divider()

    if st.button("✅ Calificar Quiz", use_container_width=True):

        if any(r is None for r in respuestas):

            st.warning("⚠️ Todavía tienes preguntas sin responder. Contesta todas antes de calificar.")

        else:

            puntaje = 0

            st.header("📊 Resultados")

            for i, pregunta in enumerate(preguntas):

                correcta = pregunta["opciones"][pregunta["correcta"]]

                if respuestas[i] == correcta:

                    puntaje += 1
                    st.success(f"✅ Pregunta {i+1}: Correcta")

                else:

                    st.error(f"❌ Pregunta {i+1}: Incorrecta — la respuesta era: *{correcta}*")

                st.info(pregunta["explicacion"])

            porcentaje = puntaje * 10

            st.divider()

            st.metric(
                "🏁 Puntaje",
                f"{puntaje}/10"
            )

            st.progress(puntaje / 10)

            if porcentaje >= 90:

                st.balloons()

                st.success("""
🏆 **Excelente.**

Dominas el tema perfectamente: entiendes no solo qué hace cada herramienta,
sino cuándo y por qué usarla.
""")

            elif porcentaje >= 70:

                st.success("""
👏 **Muy buen trabajo.**

Solo necesitas reforzar algunos escenarios prácticos.
""")

            elif porcentaje >= 50:

                st.warning("""
🙂 **Buen intento.**

Te recomiendo repetir el laboratorio y volver a leer los casos de la
sección Pickle vs Joblib.
""")

            else:

                st.error("""
📚 Revisa nuevamente las secciones anteriores, presta atención a los
escenarios (no solo a las definiciones), y vuelve a intentarlo.
""")

    st.divider()

    st.info("""
💡 **Consejo:** no memorices el código.

Comprende el problema que resuelve la serialización, y la herramienta
correcta se vuelve una decisión lógica, no un dato que hay que recordar.
""")

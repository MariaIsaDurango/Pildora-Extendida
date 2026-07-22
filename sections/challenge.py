import streamlit as st


def show_challenge():

    st.title("🏆 Reto práctico en Google Colab")

    st.markdown("""
Después de haber visto la teoría y el laboratorio interactivo aquí en Streamlit,
ahora te toca practicar en Google Colab con tus propias manos.
""")

    st.divider()

    st.header("📌 ¿Qué vas a hacer?")

    st.markdown("""
1️⃣ Entrenar un modelo de clasificación con el dataset **Iris**.

2️⃣ Guardarlo con **Joblib**.

3️⃣ Reiniciar la sesión de Colab (simulando "apagar el servidor").

4️⃣ Cargarlo de nuevo y hacer una predicción, **sin volver a entrenar**.

5️⃣ Reto bonus: descubrir qué pasa si olvidas guardar el preprocesamiento.
""")

    st.divider()

    st.header("🔗 Abre el notebook")

    st.link_button(
        "Abrir el reto en Google Colab",
        "https://colab.research.google.com/drive/1eHu4UXGNZmfRIIBICO5h86Fyu6S5IMXK?hl=es#scrollTo=VsqQVaYu2w8V",
        use_container_width=True
    )

    st.info("""
Reemplaza el link de arriba por el link real de tu notebook
(reto_serializacion_modelos.ipynb) una vez que lo hayas subido a
Google Drive o a GitHub.
""")

    st.divider()

    st.header("✅ Criterios de éxito")

    st.markdown("""
Sabrás que resolviste el reto correctamente si:

- El modelo se guardó como un archivo `.joblib` en Colab.
- Después de reiniciar la sesión, pudiste cargarlo sin ejecutar de nuevo el entrenamiento.
- La predicción con el dato nuevo se realizó sin errores.
- Completaste el reto bonus y entiendes por qué falla sin el preprocesamiento.
""")

    st.divider()

    st.success("""
🎉 Al completar este reto, habrás recorrido el ciclo de vida completo de un
modelo de Machine Learning: desde los datos hasta una predicción en producción,
sin depender de reentrenar nada.
""")

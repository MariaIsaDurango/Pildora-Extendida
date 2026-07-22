from pathlib import Path

import streamlit as st


NOTEBOOK_PATH = Path(__file__).resolve().parent.parent / "reto_serializacion_modelos.ipynb"


def show_challenge():
    st.title("🏆 Reto Colab: serializa y recupera un modelo")
    st.write(
        "🎯 Completa un flujo de Machine Learning con Iris: entrenamiento, evaluación, "
        "guardado y recuperación del modelo."
    )

    st.subheader("Qué encontrarás en el Colab")
    st.markdown(
        """
        1. 📦 Carga y división del dataset Iris.
        2. 🤖 Entrenamiento y evaluación de un árbol de decisión.
        3. 💾 Serialización con **Pickle** y **Joblib**.
        4. ♻️ Recuperación del modelo y una predicción final.
        5. 💡 Pistas progresivas y preguntas de reflexión.
        """
    )

    if not NOTEBOOK_PATH.exists():
        st.error("No se encontró el archivo del reto. Vuelve a descargar el proyecto completo.")
        return

    notebook = NOTEBOOK_PATH.read_bytes()
    st.download_button(
        "⬇️ Descargar reto guiado para Google Colab (.ipynb)",
        data=notebook,
        file_name="reto_serializacion_modelos.ipynb",
        mime="application/x-ipynb+json",
        type="primary",
        use_container_width=True,
    )
    st.info("🚀 Después de descargarlo, abre Google Colab, selecciona **Subir** y carga el archivo .ipynb.")

    with st.expander("Criterios de entrega"):
        st.markdown(
            "- Ejecuta todas las celdas sin errores.\n"
            "- Incluye la exactitud obtenida.\n"
            "- Demuestra una predicción con el modelo recuperado.\n"
            "- Responde las preguntas finales en el cuaderno."
        )

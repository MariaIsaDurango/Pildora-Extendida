import streamlit as st
from streamlit_option_menu import option_menu

from sections.home import show_home
from sections.model_lifecycle import show_model_lifecycle
from sections.serialization import show_serialization
from sections.pickle_joblib import show_pickle_joblib
from sections.lab import show_lab
from sections.quiz import show_quiz
from sections.challenge import show_challenge

# ------------------------
# Configuración
# ------------------------

st.set_page_config(
    page_title="ML Lifecycle Lab",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------
# CSS
# ------------------------

with open("assets/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# ------------------------
# Sidebar
# ------------------------

with st.sidebar:

    st.markdown(
        """
        # 🤖 ML Lifecycle

        ### Pildora Interactivo
        """

    )

    selected = option_menu(
        menu_title="Menú",
        options=[
            "Inicio",
            "Ciclo de Vida",
            "Serialización",
            "Pickle vs Joblib",
            "Laboratorio",
            "Quiz",
            "Reto Colab"
        ],
        icons=[
            "house",
            "diagram-3",
            "archive",
            "boxes",
            "cpu",
            "patch-question",
            "trophy"
        ],
        default_index=0
    )

# ------------------------
# Contenido
# ------------------------

if selected == "Inicio":
    show_home()

elif selected == "Ciclo de Vida":
    show_model_lifecycle()

elif selected == "Serialización":
    show_serialization()

elif selected == "Pickle vs Joblib":
    show_pickle_joblib()

elif selected == "Laboratorio":
    show_lab()

elif selected == "Quiz":
    show_quiz()

elif selected == "Reto Colab":
    show_challenge()
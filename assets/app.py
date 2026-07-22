from pathlib import Path

import streamlit as st

from sections.challenge import show_challenge
from sections.home import show_home
from sections.model_lifecycle import show_model_lifecycle
from sections.pickle_joblib import show_pickle_joblib
from sections.quiz import show_quiz
from sections.serialization import show_serialization


BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Ciclo de Vida ML",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

css_path = BASE_DIR / "assets" / "style.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

pages = {
    "Inicio": show_home,
    "Ciclo de vida": show_model_lifecycle,
    "Serialización": show_serialization,
    "Pickle vs Joblib": show_pickle_joblib,
    "Quiz": show_quiz,
    "Reto Colab": show_challenge,
}

with st.sidebar:
    st.title("🤖 ML Lifecycle")
    st.caption("Pildora interactiva")
    selected = st.radio("Menú", list(pages), label_visibility="collapsed")
    st.divider()
    st.caption("Entrena, serializa y reutiliza modelos de clasificación.")

pages[selected]()

import streamlit as st
from utils import *

st.set_page_config(page_title="Primes Visualizer", page_icon=":1234:", layout="wide", initial_sidebar_state="collapsed", menu_items={"About": "Primes Visualizer v1, 2026"})

st.image("https://docs.sympy.org/latest/_images/sympy.svg", width=200)
st.title(":snake: Primes Visualizer App :abacus:", text_alignment="left")


st.write_stream(stream_page_guide_text("home"))

st.page_link("pages/1 Sieve.py", label="**Prime Sieve**", icon="🧮")
st.page_link("pages/2 Prime Endings.py", label="**Prime Endings**", icon="🧱")
st.page_link("pages/Charts.py", label="**Prime Endings Charts**", icon="📊")

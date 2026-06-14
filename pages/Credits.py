import streamlit as st
from utils import *

st.set_page_config(page_title="Primes Visualizer - Credits", page_icon=":1234:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Primes Visualizer v1, 2026"})

st.title(":snake: Library Credits :clap:", text_alignment="left")

st.write_stream(stream_credit_text("Altair"))
st.write_stream(stream_credit_text("Numpy"))
st.write_stream(stream_credit_text("Pandas"))
st.write_stream(stream_credit_text("Sympy"))





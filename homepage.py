import streamlit as st

st.set_page_config(page_title="Primator", page_icon=":1234:", layout="wide", initial_sidebar_state="collapsed", menu_items={"About": "Amawzing Primator App v 1.1.2, 2026 copyright"})

st.image("https://docs.sympy.org/latest/_images/sympy.svg", width=200)
st.title(":snake: Amazing Primes App :abacus:", text_alignment="left")

tables = st.Page(
    "pages/tables.py", title="Prime Tables", icon=":material/dashboard:", default=True
)
stats = st.Page("pages/stats.py", title="Prime Stats", icon=":material/bug_report:")
charts = st.Page(
    "pages/charts.py", title="Prime Charts", icon=":material/notification_important:"
)


st.page_link("pages/tables.py", label="**Prime Tables**", icon="🧮")
st.page_link("pages/stats.py", label="**Prime Stats**", icon="📈")
st.page_link("pages/charts.py", label="**Prime Charts**", icon="📊")

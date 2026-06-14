import streamlit as st

st.set_page_config(page_title="Primes Visualizer", page_icon=":1234:", layout="wide", initial_sidebar_state="collapsed", menu_items={"About": "Primes Visualizer v1, 2026"})

st.image("https://docs.sympy.org/latest/_images/sympy.svg", width=200)
st.title(":snake: Amazing Primes App :abacus:", text_alignment="left")

# sieves = st.Page(
#     "1 Sieve.py", title="Prime Sieves", icon=":abacus:", default=True
# )

# primes = st.Page(
#     "2 Primes.py", title="Prime Tables", icon=":bricks:"
# )

# charts = st.Page(
#     "Charts.py", title="Prime Charts", icon=":bar_chart:"
# )



st.page_link("pages/1 Sieve.py", label="**Prime Sieves**", icon="🧮")
st.page_link("pages/2 Primes.py", label="**Prime Tables**", icon="🧱")
st.page_link("pages/Charts.py", label="**Prime Charts**", icon="📊")

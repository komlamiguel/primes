import streamlit as st

st.set_page_config(page_title="Primator", page_icon=":1234:", layout="wide", initial_sidebar_state="collapsed", menu_items={"About": "Amawzing Primator App v 1.1.2, 2026 copyright"})

st.image("https://docs.sympy.org/latest/_images/sympy.svg", width=200)
st.title(":snake: Amazing Primes App :abacus:", text_alignment="left")

# sieves = st.Page(
#     "tables_sieve.py", title="Sieves Tables", icon=":material/dashboard:", default=True
# )

# primes = st.Page(
#     "tables_primes.py", title="Prime Tables", icon=":material/dashboard:"
# )

# charts = st.Page(
#     "charts.py", title="Prime Charts", icon=":material/notification_important:"
# )

# pg = st.navigation([sieves, primes, charts])

# pg.run()


# st.page_link("pages/1 Sieve.py", label="**Prime Tables**", icon="🧮")
# st.page_link("pages/2 Primes.py", label="**Prime Stats**", icon="📈")
# st.page_link("pages/charts.py", label="**Prime Charts**", icon="📊")

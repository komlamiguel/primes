# Adjust the legend using     color=alt.Color('Origin:N').legend(orient="left")


import altair as alt
import streamlit as st
import numpy as np
import pandas as pd
from sympy import isprime, primerange
from primes import *
import re
from numpy.random import default_rng as rng


st.set_page_config(page_title="Primator", page_icon=":1234:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Amawzing Primator App v 1.1.2, 2026 copyright"})

st.title("Prime Charts :bar_chart:")

number_of_primes = st.sidebar.slider('# Primes', min_value=100, max_value=10000, step=200, value=500)


df = get_primes_df_for_chart_new(number_of_primes)
df1 = df[:125]
df2 = df[125:250]
df3 = df[250:]

# st.scatter_chart(df_small, x=None, y="Prime", size=100, color="Desinence")


chart0 = (
    alt.Chart(df, title=f"1st to 500th Prime")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Desinence",
            color=alt.Color('Desinence:Q').legend(None),
            tooltip=["#", "Prime", "Desinence"]).properties(
                width=800,
                height=600
            )
)



chart1 = (
    alt.Chart(df1, title=f"1st to 125th Prime")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Desinence",
            color="Desinence",
            tooltip=["#", "Prime", "Desinence"]).properties(
                width=800,
                height=600
            )
)



chart2 = (
    alt.Chart(df2, title=f"125th to 250th Prime")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Desinence",
            color="Desinence",
            tooltip=["#", "Prime", "Desinence"]).properties(
                width=800,
                height=600
            )
)

chart3 = (
    alt.Chart(df3, title=f"250th to 500th Prime")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Desinence",
            color="Desinence",
            tooltip=["#", "Prime", "Desinence"]).properties(
                width=800,
                height=600
            )
)

st.altair_chart(chart0)
st.altair_chart(chart1)
st.altair_chart(chart2)
st.altair_chart(chart3)

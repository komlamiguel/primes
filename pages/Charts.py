# Adjust the legend using     color=alt.Color('Origin:N').legend(orient="left")


import altair as alt
import streamlit as st
import numpy as np
import pandas as pd
from sympy import isprime, primerange
from primes import *
import re
from utils import *



st.set_page_config(page_title="Primator", page_icon=":1234:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Amawzing Primator App v 1.1.2, 2026 copyright"})

st.header("Prime Charts :bar_chart:")

st.markdown(PAGE_GUIDES["charts"])

st.divider()


number_of_primes = st.sidebar.slider('# Primes', min_value=100, max_value=1000, step=50, value=200)


df = get_primes_below_n_df_for_chart(number_of_primes)
# df1 = df[:125]
# df2 = df[125:250]
# df3 = df[250:375]
# df4 = df[375:]

alpha = number_of_primes // 4

df1 = df[:alpha]
df2 = df[alpha:2*alpha]
df3 = df[2*alpha:3*alpha]
df4 = df[3*alpha:]


# st.scatter_chart(df_small, x=None, y="Prime", size=100, color="Ends in")


chart0 = (
    alt.Chart(df, title=f"Primes below {number_of_primes}")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Ends in",
            color=alt.Color('Ends in:Q').legend(None),
            tooltip=["Prime", "Ends in"]).properties(
                width=800,
                height=600
            )
)



chart1 = (
    alt.Chart(df1, title=f"Primes between 2 and {alpha}")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Ends in",
            color=alt.Color('Ends in:Q').legend(None),
            tooltip=["Prime", "Ends in"]).properties(
                width=800,
                height=600
            )
)



chart2 = (
    alt.Chart(df2, title=f"Primes between {alpha} and {2*alpha}")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Ends in",
            color=alt.Color('Ends in:Q').legend(None),
            tooltip=["Prime", "Ends in"]).properties(
                width=800,
                height=600
            )
)

chart3 = (
    alt.Chart(df3, title=f"Primes between {2*alpha} and {3*alpha}")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Ends in",
            color=alt.Color('Ends in:Q').legend(None),
            tooltip=["Prime", "Ends in"]).properties(
                width=800,
                height=600
            )
)

chart4 = (
    alt.Chart(df4, title=f"Primes between {3*alpha} and {number_of_primes}")
    .mark_circle()
    .encode(alt.X('#:Q').scale(zero=False),
            y="Prime",
            size="Ends in",
            color=alt.Color('Ends in:Q').legend(None),
            tooltip=["Prime", "Ends in"]).properties(
                width=800,
                height=600
            )
)



st.altair_chart(chart0)
st.altair_chart(chart1)
st.altair_chart(chart2)
st.altair_chart(chart3)
st.altair_chart(chart4)


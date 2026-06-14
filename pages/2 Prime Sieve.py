# See how to help the user use the app with helper instructions or little video at the start/homepage

# Max affichable, recommender max pour iphone, ipad vs laptop, ici sur pc max 25 colonnes
# How to hide dataframe column header row


# Table has border setting to hide border, dataframe hasnt
import streamlit as st
import numpy as np
import pandas as pd
from sympy import isprime, primerange
from primes import *
from utils import *

st.set_page_config(page_title="Primes Visualizer - Prime Sieve", page_icon=":1234:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Primes Visualizer v1, 2026"})

st.header("Prime Sieve 🧱")

st.write(PAGE_GUIDES["sieve"] + "*")
st.caption(f"A prime sieve or prime number sieve is a fast type of algorithm for finding primes. There are many prime sieves.")


st.divider()


hide_numbers_text = st.sidebar.toggle("Hide numbers", help="Toggle on or off numbers display")

columns = st.sidebar.number_input('# Columns ', min_value=1, max_value=25, step=10, value=20, help="Max Colums is 20 to fit well on screen", label_visibility="visible")

rows = st.sidebar.number_input('# Rows ', min_value=1, max_value=500, step=10, value=50)

primes_background_colour = st.sidebar.color_picker("Primes Highlight Colour", "#A51C30")

primes_text_colour = st.sidebar.color_picker("Primes Text Colour", "#FFF")

df = get_df_for_sieve(rows, columns, option="naturals")


if not hide_numbers_text:

    df_styled = df.style.map(style_prime_in_sieve, props="background-color: " + primes_background_colour + ";").map(style_prime_in_sieve, props="color: " + primes_text_colour + ";")

else:
    df_styled = df.style.map(style_not_prime_in_sieve, props="background-color: white;").map(style_not_prime_in_sieve, props="color: white;").map(style_prime_in_sieve, props="background-color: " + primes_background_colour + ";").map(style_prime_in_sieve, props="color: " + primes_background_colour + ";")

st.table(df_styled, border=True, width="stretch", height="content", hide_index=True, hide_header=True)



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

st.set_page_config(page_title="Primator", page_icon=":1234:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Amawzing Primator App v 1.1.2, 2026 copyright"})

st.header("Primes Sieves :abacus:")

st.write_stream(stream_page_guide_text("sieve"))

st.divider()


hide_numbers_text = st.sidebar.toggle("Hide numbers", help="Toggle on or off numbers display")

columns = st.sidebar.number_input('# Columns ', min_value=1, max_value=25, step=10, value=20, help="Max Colums is 20 to fit well on screen", label_visibility="visible")

rows = st.sidebar.number_input('# Rows ', min_value=1, max_value=500, step=10, value=50)

# Text in sidebar should show size of the Sieve being built 

primes_background_colour = st.sidebar.color_picker("Primes Highlight Colour", "#CD853F")
primes_text_colour = st.sidebar.color_picker("Primes Text Colour", "#FFF")

width_style = st.sidebar.radio("Table Width Style", ("stretch", "content"))  

df = get_df_for_sieve(rows, columns, option="naturals")


if not hide_numbers_text:

    df_styled = df.style.map(style_prime_in_sieve, props="background-color: " + primes_background_colour + ";").map(style_prime_in_sieve, props="color: " + primes_text_colour + ";")

else:
    df_styled = df.style.map(style_not_prime_in_sieve, props="background-color: white;").map(style_not_prime_in_sieve, props="color: white;").map(style_prime_in_sieve, props="background-color: " + primes_background_colour + ";").map(style_prime_in_sieve, props="color: " + primes_background_colour + ";")

st.table(df_styled, border=True, width=width_style, height="content", hide_index=True, hide_header=True)



# Max affichable, recommender max pour iphone, ipad vs laptop, ici sur pc max 25 colonnes
# How to hide dataframe column header row


# Table has border setting to hide border, dataframe hasnt
import streamlit as st
import numpy as np
import pandas as pd
from sympy import isprime, sieve, prime
from primes import *

st.set_page_config(page_title="Primator", page_icon=":1234:", layout="wide", initial_sidebar_state="collapsed", menu_items={"About": "Amawzing Primator App v 1.1.2, 2026 copyright"})

st.title("Prime Tables :abacus:")

rows = st.sidebar.number_input('# Rows ', min_value=10, max_value=200, step=10, value=50)
columns = st.sidebar.number_input('# Columns ', min_value=10, max_value=25, step=10, value=20)
primes_background_colour = st.sidebar.color_picker("Primes Highlight Colour", "#CD853F")

primes_text_colour = st.sidebar.color_picker("Primes Text Colour")

int_array = np.arange(1, rows*columns + 1)
int_array = int_array.reshape(rows, columns)

df = pd.DataFrame(int_array)

df_styled = df.style.map(style_prime, props="background-color: " + primes_background_colour + ";").map(style_prime, props="color: " + primes_text_colour + ";")

# df_styled = df.style.hide(axis="columns")
# df_styled

# st.dataframe(df, hide_index=True, width="content", height="content", column_config={"_index": None})

# st.dataframe(df_styled, hide_index=True, width="content", height="content")

st.table(df_styled, hide_index=True, width="content", height="content", hide_header=True)

list_of_primes = [prime(i) for i in range(1, 101)]


df = get_df_of_primes(500)

# To allow regex replacement of numbers to nothing
df_string = df.applymap(lambda x: str(x))



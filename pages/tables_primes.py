# Max affichable, recommender max pour iphone, ipad vs laptop, ici sur pc max 25 colonnes
# How to hide dataframe column header row


# Table has border setting to hide border, dataframe hasnt
import streamlit as st
import numpy as np
import pandas as pd
from sympy import isprime, primerange
from primes import *
import re

NUMBER_REGEX = re.compile(r"[0-9]+")

ENDING_IN_STYLE_FUNCTIONS = {
    1: [style_prime_ending_1, style_prime_not_ending_1],
    3: [style_prime_ending_3, style_prime_not_ending_3],
    7: [style_prime_ending_7, style_prime_not_ending_7],
    9: [style_prime_ending_9, style_prime_not_ending_9]
}

st.set_page_config(page_title="Primator", page_icon=":1234:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Amawzing Primator App v 1.1.2, 2026 copyright"})

st.title("Primes Ending in 1, 3, 7 or 9 :abacus:")

option = st.sidebar.radio("Highlight Primes ending in...", (1, 3, 7, 9))

hide_numbers_text = st.sidebar.toggle("Hide numbers", help="Toggle on or off prime numbers display")  

number_of_primes = st.sidebar.slider('# Primes', min_value=500, max_value=10000, step=500, value=500)

primes_background_colour = st.sidebar.color_picker("Primes Highlight Colour", "#3F90CD")
primes_text_colour = st.sidebar.color_picker("Primes Text Colour", "#FFF")

width_style = st.sidebar.radio("Table Width Style", ("stretch", "content"))  

df = get_df_of_primes(number_of_primes, 20)

# df_styled = df.style.map(style_prime_ending_1, props="background-color: " + primes_background_colour + ";").map(style_prime_ending_1, props="color: " + primes_text_colour + ";")

# df_styled = df.style.map(style_prime_ending_1, props="background-color: " + primes_background_colour + ";").map(style_prime_ending_1, props="color: " + primes_background_colour + ";")

if not hide_numbers_text:
    
    df_styled = df.style.map(ENDING_IN_STYLE_FUNCTIONS[option][1], props="background-color: white;").map(ENDING_IN_STYLE_FUNCTIONS[option][0], props="background-color: " + primes_background_colour + ";").map(ENDING_IN_STYLE_FUNCTIONS[option][0], props="color: " + primes_text_colour + ";")

else:
    
    df_styled = df.style.map(ENDING_IN_STYLE_FUNCTIONS[option][1], props="background-color: white;").map(ENDING_IN_STYLE_FUNCTIONS[option][1], props="color: white;").map(ENDING_IN_STYLE_FUNCTIONS[option][0], props="background-color: " + primes_background_colour + ";").map(ENDING_IN_STYLE_FUNCTIONS[option][0], props="color: " + primes_background_colour + ";")


st.table(df_styled, border=True, width=width_style, height="content", hide_index=True, hide_header=True)






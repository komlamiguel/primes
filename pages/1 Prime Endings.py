# Max affichable, recommender max pour iphone, ipad vs laptop, ici sur pc max 25 colonnes
# How to hide dataframe column header row


# Table has border setting to hide border, dataframe hasnt
import streamlit as st
import numpy as np
import pandas as pd
from sympy import isprime, primerange
from primes import *
import re
from utils import *

NUMBER_REGEX = re.compile(r"[0-9]+")


st.set_page_config(page_title="Primes Visualizer - Primes Endings", page_icon=":1234:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Primes Visualizer v1, 2026"})

st.header("Primes Ending in 1, 3, 7 or 9 🧮")

st.write(PAGE_GUIDES["primes"] + "*")
st.caption(f"Visualising side by side endings can help validate **Dr. Kannan Soundararajan**, Stanford University mathematician, *prime conspiracy* discovery.")


st.divider()

number_of_primes = st.sidebar.slider('# Primes', min_value=100, max_value=10000, step=200, value=500)


hide_numbers_text = st.sidebar.toggle("Hide numbers", help="Toggle on or off prime numbers display")  

option = st.sidebar.radio("Highlight Primes ending in...", ("All", 1, 3, 7, 9))

all_option_legend_container = st.sidebar.container()

other_option_container = st.sidebar.container()

df = get_df_of_primes(number_of_primes, 20)

if option != "All":

    with other_option_container:

        endings_compare_for_option = ENDINGS - set([option])
        option_compare = st.sidebar.radio(f"Highlight Primes ending in {option} and ...", sorted(endings_compare_for_option))

        primes_option_background_colour = st.sidebar.color_picker(f"Primes Ending in {option} Colour", ALL_ENDINGS_COLOURS[option])
        primes_option_compare_background_colour = st.sidebar.color_picker(f"Primes Ending in {option_compare} Colour", ALL_ENDINGS_COLOURS[option_compare])

    df_styled = get_primes_styled_df(df, option, option_compare, hide_numbers_text)
        
else:

    with all_option_legend_container:
        
        st.markdown(f"You've chosen to highlight primes ending in 1, 3, 7 or 9")
        st.color_picker("Ending in 1", value=ALL_ENDINGS_COLOURS[1], disabled=True)
        st.color_picker("Ending in 3", value=ALL_ENDINGS_COLOURS[3], disabled=True)
        st.color_picker("Ending in 7", value=ALL_ENDINGS_COLOURS[7], disabled=True)
        st.color_picker("Ending in 9", value=ALL_ENDINGS_COLOURS[9], disabled=True)

    df_styled = get_primes_styled_df(df, "All", "", hide_numbers_text)

st.table(df_styled, border=True, width="stretch", height="content", hide_index=True, hide_header=True)



# show_summary_stats = st.sidebar.toggle("Show Distribution Stats", help="Toggle on or off display of summary stats", value=True)  










    
    
    

    






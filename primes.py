# Il Sagit de trouver la decomposition en deux facteurs, donc rectangulaire d'un nombre donne
# Donc il vaudra mieux pour le moment separer les tables de premiers only sur une autre page

# Tester a petite echelle, corriger fonctions pour permettre un affichage rectangularire quelconque est ce qu'il vaut mieux utiliser number input plutot que slider

# Choix entre LaTex ou Markdown Style selector

# Idee utilisation du stream pour streamer une sequence de premiers qui defilent a l'ecran peut etre

# Update st version so that markdown allows coloured text as blue[cool] below

import streamlit as st
from sympy import isprime, primerange, prime
import time
import numpy as np
import pandas as pd



NUMBER_STRINGS = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100"


# Next see how to colour numbers inside it
def print_latex_table_of_numbers(columns, rows):
    
    for i in range(1, columns * rows, columns):
        cols = st.columns(columns)
        for j in range(columns):
            if isprime(i + j):
                cols[j].latex(f"\\bf {i + j}")
            else:
                cols[j].latex(f"{i + j}")

def print_markdown_table_of_numbers(colour, columns, rows):
    
    for i in range(1, columns * rows, columns):
        cols = st.columns(columns)
        for j in range(columns):
            if isprime(i + j):
                # columns[j].markdown(f"### :{colour}-background[{i + j}]")
                cols[j].markdown(f" :green-background[{i + j}]")
            else:
                cols[j].markdown(f" {i + j}")


def test(columns, rows):
    
    for i in range(1, columns * rows, columns):
        cols = st.columns(columns)
        for j in range(columns):
            if isprime(i + j):
                cols[j].latex("\colorbox{aqua}" + "{" + f"{i + j}" + "}")
            else:
                cols[j].latex("\\textcolor{#228B22}" + "{" + f"{i + j}" + "}")






def get_df_for_sieve(rows, columns, option="naturals"):

    n = rows * columns

    if option == "naturals":
    
        int_array = np.arange(1, n + 1)
        int_array = int_array.reshape(rows, columns)

        df = pd.DataFrame(int_array)


    else:
        
        primes = list(primerange(prime(n + 1)))
        primes_array = np.array(primes)
        primes_array = primes_array.reshape(rows, columns)

        df = pd.DataFrame(primes_array)

    return df


def get_df_of_primes(n, columns=20):

    rows = n // columns

    
    primes = list(primerange(prime(n + 1)))
    primes_array = np.array(primes)
    primes_array = primes_array.reshape(rows, columns)
    
    df = pd.DataFrame(primes_array)

    return df

        
def get_list_of_primes(n):
    return [prime(i) for i in range(1, n + 1)]


# Style functions
def style_prime_in_sieve(x, props=""):
    return props if isprime(x) else None


def style_prime_ending_1(x, props=""):
    return props if x % 10 == 1 else None

def style_prime_not_ending_1(x, props=""):
    return props if x % 10 != 1 else None

def style_prime_ending_3(x, props=""):
    return props if x % 10 == 3 else None

def style_prime_not_ending_3(x, props=""):
    return props if x % 10 != 3 else None


def style_prime_ending_5(x, props=""):
    return props if x % 10 == 5 else None

def style_prime_not_ending_5(x, props=""):
    return props if x % 10 != 5 else None


def style_prime_ending_7(x, props=""):
    return props if x % 10 == 7 else None

def style_prime_not_ending_7(x, props=""):
    return props if x % 10 != 7 else None


def style_prime_ending_9(x, props=""):
    return props if x % 10 == 9 else None

def style_prime_not_ending_9(x, props=""):
    return props if x % 10 != 9 else None



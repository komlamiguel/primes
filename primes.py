# Comments

import streamlit as st
from sympy import isprime, primerange, prime
import time
import numpy as np
import pandas as pd

ENDINGS = set([1, 3, 7, 9])


ALL_ENDINGS_COLOURS = {
    
    1: "#3FCDB6",
    2: "#FFFF",
    3: "#3F90CD",
    5: "#FFFF",
    7: "#6761D3",
    9: "#D1687B",

}

# Style functions
def style_prime_in_sieve(x, props=""):
    return props if isprime(x) else None

def style_not_prime_in_sieve(x, props=""):
    return props if not isprime(x) else None

def style_prime_ending_1(x, props=""):
    return props if x % 10 == 1 else None

def style_prime_ending_2(x, props=""):
    return props if x % 10 == 2 else None

def style_prime_not_ending_2(x, props=""):
    return props if x % 10 != 2 else None

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


ENDING_IN_STYLE_FUNCTIONS = {
    
    1: [style_prime_ending_1, style_prime_not_ending_1],
    2: [style_prime_ending_2, style_prime_not_ending_2],
    3: [style_prime_ending_3, style_prime_not_ending_3],
    5: [style_prime_ending_5, style_prime_not_ending_5],
    7: [style_prime_ending_7, style_prime_not_ending_7],
    9: [style_prime_ending_9, style_prime_not_ending_9]
}



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

def stats_of_primes_endings(n):
    
    primes = list(primerange(prime(n + 1)))
    primes_ending_1 = [prime for prime in primes if prime % 10 == 1]
    primes_ending_3 = [prime for prime in primes if prime % 10 == 3]
    primes_ending_7 = [prime for prime in primes if prime % 10 == 7]
    primes_ending_9 = [prime for prime in primes if prime % 10 == 9]

    n1 = len(primes_ending_1)
    n3 = len(primes_ending_3)
    n7 = len(primes_ending_7)
    n9 = len(primes_ending_9)
    
    
    ending_1_ratio = n1 / n
    ending_3_ratio = n3 / n
    ending_7_ratio = n7 / n
    ending_9_ratio = n9 / n


    return {
        1: {"count": n1, "ratio": ending_1_ratio},
        3: {"count": n3, "ratio": ending_3_ratio},
        7: {"count": n7, "ratio": ending_7_ratio},
        9: {"count": n9, "ratio": ending_9_ratio}

}

def get_list_of_primes(n):
    return [prime(i) for i in range(1, n + 1)]

def get_primes_df_for_chart(n):

    primes = list(primerange(prime(n + 1)))

    data = {"#": list(range(1, n + 1)),
            "Prime": [prime for prime in primes], 
            "Ends in": [prime % 10  for prime in primes]
    }

    df = pd.DataFrame(data)

    return df


def get_primes_below_n_df_for_chart(n):

    data = {"#": list(range(1, n + 1)),
            "Prime": [prime_or_none(i) for i in range(1, n + 1)], 
            "Ends in": [i % 10  for i in range(1, n + 1)]
    }

    df = pd.DataFrame(data)

    return df


def get_primes_df_for_heatmap_chart(n):

    primes = list(primerange(prime(n + 1)))

    data = {"#": list(range(1, n + 1)),
            "Prime": [prime_or_none(i) for i in range(1, n + 1)], 
            "Ends in": [prime % 10  for prime in primes],
            "Digits Sum": [get_digits_sum(prime) for prime in primes]
    }

    df = pd.DataFrame(data)

    return df


def get_digits_sum(n):
    n_string = str(n)
    n_digits = [int(n_string[i]) for i in range(len(n_string))]
    sum_n_digits = sum(n_digits)

    return sum_n_digits

def prime_or_none(n):
    return n if isprime(n) else None





def get_primes_styled_df(df, option, option_compare, hide_numbers_text):

    if option == "All":
        if not hide_numbers_text:
            df_styled = df.style.map(style_prime_ending_1, props="background-color: " + ALL_ENDINGS_COLOURS[1] + ";").map(style_prime_ending_2, props="background-color: " + ALL_ENDINGS_COLOURS[2] + ";").map(style_prime_ending_3, props="background-color: " + ALL_ENDINGS_COLOURS[3] + ";").map(style_prime_ending_5, props="background-color: " + ALL_ENDINGS_COLOURS[5] + ";").map(style_prime_ending_7, props="background-color: " + ALL_ENDINGS_COLOURS[7] + ";").map(style_prime_ending_9, props="background-color: " + ALL_ENDINGS_COLOURS[9] + ";")

        else:
            df_styled = df.style.map(style_prime_ending_1, props="background-color: " + ALL_ENDINGS_COLOURS[1] + ";" + "color: " + ALL_ENDINGS_COLOURS[1] + ";").map(style_prime_ending_2, props="background-color: " + ALL_ENDINGS_COLOURS[2] + ";" + "color: " + ALL_ENDINGS_COLOURS[2] + ";").map(style_prime_ending_3, props="background-color: " + ALL_ENDINGS_COLOURS[3] + ";" + "color: " + ALL_ENDINGS_COLOURS[3] + ";").map(style_prime_ending_5, props="background-color: " + ALL_ENDINGS_COLOURS[5] + ";" + "color: " + ALL_ENDINGS_COLOURS[5] + ";").map(style_prime_ending_7, props="background-color: " + ALL_ENDINGS_COLOURS[7] + ";" + "color: " + ALL_ENDINGS_COLOURS[7] + ";").map(style_prime_ending_9, props="background-color: " + ALL_ENDINGS_COLOURS[9] + ";" + "color: " + ALL_ENDINGS_COLOURS[9] + ";")
                        

    else:

        if not hide_numbers_text:
            df_styled = df.style.map(ENDING_IN_STYLE_FUNCTIONS[option][0], props="background-color: " + ALL_ENDINGS_COLOURS[option] + ";").map(ENDING_IN_STYLE_FUNCTIONS[option_compare][0], props="background-color: " + ALL_ENDINGS_COLOURS[option_compare] + ";")

        else:

            not_selected_endings = list(ENDINGS - set([option]) - set([option_compare]))
            not_selected_ending1 = not_selected_endings[0]
            not_selected_ending2 = not_selected_endings[1]
            
            df_styled = df.style.map(ENDING_IN_STYLE_FUNCTIONS[option][0], props="background-color: " + ALL_ENDINGS_COLOURS[option] + ";" + "color: " + ALL_ENDINGS_COLOURS[option] + ";").map(ENDING_IN_STYLE_FUNCTIONS[option_compare][0], props="background-color: " + ALL_ENDINGS_COLOURS[option_compare] + ";" + "color: " + ALL_ENDINGS_COLOURS[option_compare] + ";").map(ENDING_IN_STYLE_FUNCTIONS[not_selected_ending1][0], props="background-color: white;color: white").map(ENDING_IN_STYLE_FUNCTIONS[not_selected_ending2][0], props="background-color: white;color: white").map(ENDING_IN_STYLE_FUNCTIONS[2][0], props="background-color: white;color: white").map(ENDING_IN_STYLE_FUNCTIONS[5][0], props="background-color: white;color: white")
        


    return df_styled
        
        
        
    
    
        

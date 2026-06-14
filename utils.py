import streamlit as st
import time


CREDITS = {


"Altair": {"text": """Vega-Altair is a declarative statistical visualization library for Python, based on Vega and Vega-Lite. It offers a powerful and concise grammar that enables you to quickly build a wide range of statistical visualizations.""", "img": "https://altair-viz.github.io/_static/altair-logo-light.png", "url": "https://altair-viz.github.io/"},

"Numpy": {"text": "NumPy (pronounced /ˈnʌmpaɪ/ NUM-py) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.", "img": "https://numpy.org/doc/_static/numpylogo.svg", "url": "https://numpy.org/doc/"} ,

"Pandas": {"text": """Pandas (styled as pandas) is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series""", "img": "https://img.wikiwand.com/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1280px-Pandas_logo.svg.png", "url": "https://pandas.pydata.org/docs/"},

"Streamlit": {"text": "", "img": "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", "url": "https://docs.streamlit.io/"},

"Sympy": {"text": "SymPy is an open-source Python library for symbolic computation. It provides computer algebra capabilities either as a standalone application, as a library to other applications, or live on the web as SymPy Live or SymPy Gamma.SymPy is simple to install and to inspect because it is written entirely in Python with few dependencies. This ease of access combined with a simple and extensible codebase in a well-known language make SymPy a computer algebra system with a relatively low barrier to entry", "img": "https://docs.sympy.org/latest/_images/sympy.svg", "url": "https://docs.sympy.org/latest/index.html"}


}



PAGE_GUIDES = {
    
    "home": "Explore primes through their endings relationships, generate a sieve or colour plot your primes to find new prime patterns!",
    
    "primes": """Explore new Prime patterns/relationships with primes endings (1, 3, 7 or 9). Colour all endings or compare 2 endings side by side to corroborate a recent number theory discovery...""",

    "sieve": """Customise your Prime Sieve by choosing the size of the sieve, picking up your primes highlight color. Explore & Discover new Prime patterns/relationships along the way. Test the nifty 'Hide numbers' feature that hides the numbers text and just shows primes as coloured boxes!""",

    "charts": """Last but not least, you can visualise prime ending distribution by playing around with scatter coloured plots! """

}



def stream_page_guide_text(page):
    for word in PAGE_GUIDES[page].split(" "):
        yield word + " "
        time.sleep(0.02)


def stream_credit_text(library):
    st.image(CREDITS[library]["img"], width=200)
    
    for word in CREDITS[library]["text"].split(" "):
        yield word + " "
        time.sleep(0.02)

    st.write(CREDITS[library]["url"])

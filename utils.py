import streamlit as st
import time

PAGE_GUIDES = {
    "sieve": """Customise your Prime Sieve by choosing the size of the sieve, picking up your primes highlight color. Explore & Discover new Prime patterns/relationships along the way. Test the nifty 'Hide numbers' feature that hides the numbers text and just shows primes as coloured boxes!""",
    "primes": """Play around with a table of the first n Primes. Choose the total primes count, pick up your primes highlight & text color. Explore & Discover new Prime patterns/relationships with primes endings (1, 3, 7 or 9). Test the nifty 'Hide numbers' feature that hides the numbers text and just shows primes as coloured boxes""",
    "charts": """Last but not least you can visualise the first 500 Primes plotted using Altair's Python Data Visualization library scatter plots! """

}



def stream_page_guide_text(page):
    for word in PAGE_GUIDES[page].split(" "):
        yield word + " "
        time.sleep(0.02)

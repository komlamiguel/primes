# Limiter selection entiers a un max raisonable pour le mode latex, jusqu'a 5000 entiers max?


from primes import *

st.title("Prime Tables")


option = st.sidebar.radio('Display Mode', ("LaTeX", "Markdown"))
rows = st.sidebar.number_input('# Rows ', min_value=10, max_value=100, step=10)
columns = st.sidebar.number_input('# Columns ', min_value=10, max_value=100, step=10)


if option.lower() == "latex":
    print_latex_table_of_numbers(columns, rows)
    # test(columns, rows)

else:
    print_markdown_table_of_numbers("orange", columns, rows)

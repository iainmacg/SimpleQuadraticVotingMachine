import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Quadratic Voting Machine",
    page_icon=":panda_face:",
    layout="wide",
    initial_sidebar_state="auto",
)

st.header("Streamlit Quadratic Voting Machine")
st.title("A simple quadratic voting machine with OECD Better Life Index categories")
st.write("You get 100 points, but the more you vote for one thing the less that vote is worth (the number gets values).")

budget=100.0
categories = ["Housing", "Income", "Jobs", "Community", "Education", "Environment", "Civic Engagement", "Health", "Life Satisfaction", "Safety", "Work-Life Balance"]
#col1_cat = categories[:len(categories)//2]
#col2_cat = categories[len(categories)//2:]
n = 3
cats = [categories[i * n:(i + 1) * n] for i in range((len(categories) + n - 1) // n )]
values = []
col1, col2, col3 = st.beta_columns([1, 1, 1])
for cat in cats[0]:
    value = col1.slider(cat, min_value=0.0, max_value=budget**0.5, step=0.1)
    col1.write(f"{cat}: {round(value**2, 2)}")
    values.append(value)
for cat in cats[1]:
    value = col2.slider(cat, min_value=0.0, max_value=budget**0.5, step=0.1)
    col2.write(f"{cat}: {round(value**2, 2)}")
    values.append(value)
for cat in cats[2]:
    value = col3.slider(cat, min_value=0.0, max_value=budget**0.5, step=0.1)
    col3.write(f"{cat}: {round(value**2, 2)}")
    values.append(value)
if len(cats[3]) == 1:
    value = col1.slider(cats[3][0], min_value=0.0, max_value=budget**0.5, step=0.1)
    col1.write(f"{cats[3][0]}: {round(value**2, 2)}")
    values.append(value)
elif len(cats[3]) == 2:
    value = col1.slider(cats[3][0], min_value=0.0, max_value=budget**0.5, step=0.1)
    col1.write(f"{cats[3][0]}: {round(value**2, 2)}")
    values.append(value)
    value = col2.slider(cats[3][1], min_value=0.0, max_value=budget**0.5, step=0.1)
    col2.write(f"{cats[3][1]}: {round(value**2, 2)}")
    values.append(value)
squared = [value ** 2 for value in values]
sq_sum = sum(squared)
rem_budget = budget-sq_sum
if rem_budget < 0:
    st.warning(f"You have exceeded the budget by {round(rem_budget, 2)} points!")
st.subheader(f"Budget remaining: {round(rem_budget, 2)}")
d = {"Values": values, "Squared": squared, "Squared Sum": sq_sum}
results_df = pd.DataFrame(data=d, index=categories)
st.dataframe(results_df)

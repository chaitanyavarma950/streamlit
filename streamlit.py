import streamlit as st
import pandas as pd

st.title("📊 Simple Streamlit App")
st.write("This is a web app written entirely in Python!")

# Input widgets
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", 0, 100, 25)

# Logic in Python
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")

# Display a table
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Sales": [120, 230, 310]
})
st.bar_chart(data.set_index("Month"))

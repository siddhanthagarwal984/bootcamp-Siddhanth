import streamlit as st
import pandas as pd

st.title("Interactive Data Table")

# Sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

# Display the dataframe interactively
st.dataframe(df)
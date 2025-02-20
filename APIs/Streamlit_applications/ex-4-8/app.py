import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

st.title("Interactive Scatter Plot with Plotly")

# Generate random data
np.random.seed(42)
df = pd.DataFrame({
    "X": np.random.rand(100),
    "Y": np.random.rand(100),
    "Category": np.random.choice(["A", "B", "C"], 100)
})

# Create a scatter plot
fig = px.scatter(df, x="X", y="Y", color="Category", title="Random Scatter Plot")

# Display the plot
st.plotly_chart(fig)
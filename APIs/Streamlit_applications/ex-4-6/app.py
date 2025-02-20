import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Matplotlib Graph in Streamlit")

# Generate random data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure
fig, ax = plt.subplots()
ax.plot(x, y, label="Sine Wave")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

import streamlit as st

st.title("Interactive Slider Example")

# Slider widget
value = st.slider("Select a number", min_value=0, max_value=100, value=50)

# Display selected value
st.write(f"You selected: {value}")
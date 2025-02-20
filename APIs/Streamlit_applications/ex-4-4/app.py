import streamlit as st

st.title("Basic Authentication in Streamlit")

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

# User input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Authentication check
if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("Login successful!")
        st.write("Welcome to the protected content!")
    else:
        st.error("Invalid username or password.")
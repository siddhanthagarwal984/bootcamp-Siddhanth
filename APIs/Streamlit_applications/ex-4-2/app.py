import streamlit as st

st.set_page_config(page_title="Multipage App")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/home.py", label="Home")
st.sidebar.page_link("pages/about.py", label="About")

st.write("Welcome to the Multipage Streamlit App! Use the sidebar to navigate.")
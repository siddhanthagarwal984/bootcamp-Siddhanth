import streamlit as st

st.title("Counter App with Session State")

# Initialize session state
if "count" not in st.session_state:
    st.session_state.count = 0

# Button to increment the counter
if st.button("Increment Counter"):
    st.session_state.count += 1

st.write(f"Counter Value: {st.session_state.count}")

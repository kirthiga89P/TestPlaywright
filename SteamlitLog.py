import streamlit as st

# Title for the app
st.title("Login Page")

# Input fields for username and password
username = st.text_input("Username"),
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    # Check if username and password match predefined values new
    if username == "admin" and password == "password123":
        st.success("Login successful")
    else:
        st.error("Login unsuccessful")

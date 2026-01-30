
import streamlit as st


st.set_page_config(page_title="Owl AI", page_icon="🦉", layout="centered")


st.title("🦉 Owl AI Web Application")
st.write("Welcome to Owl AI! This is a simple interactive web app.")


menu = st.sidebar.selectbox("Navigation", ["Home", "User Input", "About"])


if menu == "Home":
    st.header("Home")
    st.success("This application demonstrates a simple AI-based interface.")


elif menu == "User Input":
    st.header("User Input Form")

    name = st.text_input("Enter your name")
    interest = st.selectbox("Select your interest", ["AI", "Python", "Web Development", "Data Science"])

    if st.button("Submit"):
        st.write(f"Hello **{name}** 👋")
        st.write(f"You are interested in **{interest}** 🚀")

elif menu == "About":
    st.header("About Owl AI")
    st.info("Owl AI is a learning-focused platform for AI and Python development.")

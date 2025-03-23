import streamlit as st

def home_page():
    st.title("🏠 Home Page")
    st.write("Welcome to my AI-powered website!")
    
    # Display images
    st.image("welcome img.png", caption="Artificial Intelligence wil be part of our future.It's inevitable!")
    st.image("AI.webp", caption="AI for All", use_container_width=True)
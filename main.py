import streamlit as st
from About import about_page  # Ensure `about.py` exists with `about_page()`
from Home import home_page  # Ensure `home.py` exists with `home_page()`
from Contact import contact_page  # Ensure `contact.py` exists with `contact_page()`

# Set default page in session state
if "page" not in st.session_state:
    st.session_state.page = None  # No page until name is entered

st.title("🚀 Future AI Website!")  
st.write("Welcome to my Future web app.")  

# Text input for name
name = st.text_input("Enter your name to continue:")

# When the user enters a name, store it and show the home page
if name:
    st.session_state.page = "Home"
    st.success(f"Hello, {name}! 🎉 Redirecting to the website...")

# Show the website only if the name is entered
if st.session_state.page:
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Contact"], index=0)
    st.session_state.page = page

    # Display the selected page
    if st.session_state.page == "Home":
        home_page()  # Calls `home_page()` from home.py
    elif st.session_state.page == "About":
        about_page()  # Calls `about_page()` from about.py
    elif st.session_state.page == "Contact":
        contact_page()  # Calls `contact_page()` from contact.py


# Footer with styling
footer = """
<style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 16px;
        border-top: 1px solid #ccc;
    }
</style>

<div class="footer">
    Developed with ❤️ by <a href="https://www.linkedin.com/in/sabreena-zahid-ali-1343a8198/" target="_blank">Sabreena Daniyal</a>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
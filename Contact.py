import streamlit as st

def contact_page():
    st.title("📞 Contact Page")
    st.write("Feel free to reach out!")
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        st.success(f"Thank you, {name}! We will get back to you soon.")

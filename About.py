import streamlit as st

def about_page():
    st.header("🤖 About Artificial Intelligence")
    
    st.write("""
    Artificial Intelligence (AI) is transforming the way we interact with technology and the world around us. 
    AI enables machines to learn, reason, and make decisions, mimicking human intelligence.
    """)

    st.image("ai-robot.png", caption="The Future of AI", use_container_width=True)

    st.subheader("🌍 Impact of AI")
    st.write("""
    AI is revolutionizing industries such as healthcare, finance, education, and transportation. 
    From self-driving cars to intelligent virtual assistants, AI is reshaping our daily lives.
    """)

    st.subheader("⚡ AI Applications")
    st.write("""
    - **Machine Learning**: Enables computers to learn patterns from data.
    - **Natural Language Processing (NLP)**: Powers chatbots and language translation.
    - **Computer Vision**: Helps in facial recognition and object detection.
    - **Automation**: Reduces repetitive tasks in industries.
    """)

    st.info("💡 Did you know? AI can generate realistic human-like images and text using deep learning models!")

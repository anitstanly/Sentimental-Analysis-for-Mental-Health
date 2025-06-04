import streamlit as st
st.markdown(
    """
    <style>
    /* Set background image */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb'); /* Replace with your image URL */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* Optional: Make text easier to read on image */
    h1, h2, h3, h4, h5, h6, p, div {
        color: #ffffff;
        text-shadow: 1px 1px 2px #000000;
    }

    /* Optional: make chat input and boxes more visible */
    .block-container {
        background-color: rgba(.2, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Main page content
st.markdown("# Happy Helper 🌞")
st.markdown(
    """
    <div style='
        color: #E6F0FF;
        font-family: "Trebuchet MS", sans-serif;
        font-size: 20px;
        font-weight: bold;
        background-color: rgba(255, 255, 255, 0);
        padding: 12px 18px;
        '>
        🌼 Your anytime anywhere mental wellness companion.
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("""


This app is designed to support your mental well-being through three helpful tools.  
Use the navigation sidebar to explore the following features:

### 🌿 Emotion Detector
Understand your emotional state by simply typing how you feel.  
The system will analyze your input and give you insight into your current emotions.

### 🤖 Supportive Chatbot
Talk freely with a kind, empathetic AI companion.  
Your companion is always here to listen and support you without judgment.

### 🧘 Mental Health Toolkit
Access instant relief tools like music, calming reads, relaxing games, journaling, and trusted mental health resources.  
A perfect place to recharge and find positive energy.

---

Take a deep breath, and let's begin your journey to emotional clarity and calm. 🌿
""")
#st.sidebar.markdown("# Happy Helper 🎈")

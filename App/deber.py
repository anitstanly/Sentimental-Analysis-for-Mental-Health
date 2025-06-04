import streamlit as st
from transformers import pipeline
from transformers import AutoModelForSequenceClassification, AutoTokenizer
st.markdown(
    """
    <style>
    /* Set background image */
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e'); /* Replace with your image URL */
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
# Path to your saved DeBERTa model
model_path = "./model"  # or replace with Hugging Face model name if not local

# Load DeBERTa model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load your trained model
sentiment_pipeline = pipeline("text-classification", model="model", tokenizer="model")

# Label mapping
label_map = {
    "LABEL_0": "Anxiety",
    "LABEL_1": "Bipolar Disorder",
    "LABEL_2": "Depression",
    "LABEL_3": "Normal",
    "LABEL_4": "Personality Disorder",
    "LABEL_5": "Stress",
    "LABEL_6": "Suicidal"
}

# Empathetic response for each label
response_map = {
    "LABEL_0": "You might be experiencing **Anxiety**. It's natural to feel a bit overwhelmed at times. Our mental health toolkit contains resources designed to help you unwind and find a sense of calm. And remember, if you're looking to share how you're feeling, the chatbot is always here to lend an empathetic ear.🍃",
    "LABEL_1": "Your emotions may indicate signs of Bipolar Disorder. If you're noticing significant mood swings, please remember that you're not alone. However, note that this model does not provide clinical diagnoses—it only offers insights based on your input. For personalized guidance, consider reaching out to a professional, and check our resource section for additional support options.💙",
    "LABEL_2": "Your words suggest signs of depression. Please remember that this model does not provide professional diagnoses. If you'd like to discuss your feelings further, feel free to use our chatbot for more in-depth support.🌼",
    "LABEL_3": "You seem to be in a Normal state of mind. That's wonderful to hear—keep nurturing this balance and peace.☀️",
    "LABEL_4": "Your words may indicate some signs of a Personality Disorder. Please note that this tool does not provide a diagnosis. If you're concerned about these signals, consider checking our resource section to find professional help for a thorough consultation.🌸",
    "LABEL_5": "You might be experiencing some Stress—and that's completely valid. Consider checking our toolkit for calming music and engaging games to help you relax.🌸",
    "LABEL_6": "It sounds like you're experiencing Suicidal Thoughts. Please know: you are not alone. If you’re in Germany and feel unsafe or need immediate help, please call 📞 0800-1110111. Alternatively, consider reaching out to someone you trust or speaking with a mental health professional. Your life matters, and there are people who care deeply about you.❤️"
}

# Streamlit UI
#st.set_page_config(page_title="Emotional Insight", page_icon="🧠")
st.title("Emotion Detector 🌿")

st.markdown("""
I’m here to listen and understand how you're feeling.

**💫 Go ahead, express yourself.**
""")

# User input
text = st.text_area("💬 Describe how you feel:")

# Processing input
if text:
    result = sentiment_pipeline(text)
    label = result[0]['label']
    condition = label_map.get(label, "Unknown")
    message = response_map.get(label, "I'm here to support you.")

    st.subheader(f"🧠 Emotional State Detected: {condition}")
    st.info(message)


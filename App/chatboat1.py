import streamlit as st
from llama_index.llms.groq import Groq
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.base.llms.types import ChatMessage, MessageRole
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
# --- Initialize the LLM ---
llm = Groq(
    model="llama3-70b-8192",
    max_new_tokens=512,
    temperature=0.01,
    top_p=0.95,
    repetition_penalty=1.03,
    api_key="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",  # Replace with your actual Groq API key
)

# --- System prompts ---
prompts = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content="You are a kind and helpful companion talking to a human.",
    ),
    ChatMessage(
        role=MessageRole.SYSTEM,
        content="Keep your answers short and succinct.",
    ),
]

# --- Initialize chatbot ---
@st.cache_resource
def init_chat():
    return SimpleChatEngine.from_defaults(llm=llm, prefix_messages=prompts)

chat_engine = init_chat()

# --- Streamlit UI ---
st.title("Supportive Chatbot 🤖")
st.write("Your companion is always here to listen and support you without judgment.")

st.markdown(
    "Your space to open up. Chat freely and let your mind breathe. 🧘‍♀️🌿"
)

# --- Initialize session state ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Chat input ---
user_input = st.chat_input("Say something...")

if user_input:
    # Append user input
    st.session_state.chat_history.append(("You", user_input))

    # Get response
    response = chat_engine.chat(user_input)

    # Append chatbot response
    st.session_state.chat_history.append(("Companion", response.response))

# --- Display chat ---
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)

from rag_pipeline import answer_query, retrieve_docs, llm_model
import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="AI Lawyer", page_icon="⚖️", layout="centered")

# Custom CSS for styling
st.markdown("""
   <style>
    .main {
        background-color: #34495e;
        padding: 2rem;
    }
    .block-container {
        border-radius: 12px;
        padding: 2rem;
    }
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #2e86de;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    .stFileUploader>div {
        border: 2px dashed #bbb;
        padding: 1rem;
        border-radius: 10px;
        background-color: #ecf0f1;
    }

    /* Fix for file name color */
    .stFileUploader div[data-testid="stFileUploaderFileName"] {
        color: #2c3e50 !important; /* Set a dark color for the file name */
    }
</style>


""", unsafe_allow_html=True)

# Title and description
st.markdown("<div class='title'>⚖️ AI Lawyer Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload a legal PDF and ask anything — get intelligent legal insights instantly!</div>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("📄 Upload your legal PDF document:", type="pdf")

# Prompt input
user_query = st.text_area("🧠 Enter your prompt:", height=150, placeholder="Type your legal question here...")

# Ask button
ask_question = st.button("Ask AI Lawyer")

# Chat logic
if ask_question:
    if uploaded_file:
        st.chat_message("user").write(user_query)

        # RAG Pipeline
        retrieved_docs = retrieve_docs(user_query)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)

        st.chat_message("AI Lawyer").write(response)
    else:
        st.error("🚫 Please upload a valid PDF file before asking your question.")

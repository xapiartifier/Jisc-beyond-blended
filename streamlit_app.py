import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Beyond Blended Agent", layout="wide")

st.title("🎓 Jisc Beyond Blended Agent")

# Load a non-API Hugging Face model (e.g., sentiment-analysis)
@st.cache_resource
def load_model():
  return pipeline("text-generation", model="gpt2")
  
generator = load_model()

prompt = st.text_area("Enter your query or prompt:", height=200)

if st.button("Generate Response"):
  if prompt:
        with st.spinner("Generating..."):
            result = generator(prompt, max_length=150, do_sample=True)
            st.success(result[0]['generated_text'])
    else:
        st.warning("Please enter a prompt.")

import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Beyond Blended Agent", layout="wide")

st.title("🎓 Jisc Beyond Blended Agent")

# Load a non-API Hugging Face model with caching
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

prompt = st.text_area("Enter your query or prompt:", height=200)

if st.button("Generate Response"):
    if prompt:
        with st.spinner("Generating..."):
            result = generator(prompt, max_length=150, do_sample=True)
            st.success(result[0]['generated_text'])
    else:
        st.warning("Please enter a prompt.")
from langchain.document_loaders import PyPDFLoader, UnstructuredPowerPointLoader
import glob

# Load PDF and PPTX files
pdf_files = glob.glob("docs/**/*.pdf", recursive=True)
pptx_files = glob.glob("docs/**/*.pptx", recursive=True)

documents = []
for pdf_path in pdf_files:
    loader = PyPDFLoader(pdf_path)
    documents.extend(loader.load())

for pptx_path in pptx_files:
    loader = UnstructuredPowerPointLoader(pptx_path)
    documents.extend(loader.load())


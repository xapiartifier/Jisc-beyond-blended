import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_agent():
  # Use CPU-only configuration to avoid GPU-related errors
  embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
    )
    db = FAISS.load_local("vectorstore", embeddings)
    return db

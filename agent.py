from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_agent():
    # Load the FAISS vector store using HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vectorstore", embeddings)
    return db

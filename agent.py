from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_agent():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
    db = FAISS.load_local("vectorstore", embeddings)
    return db

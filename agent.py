from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_agent():
    db = FAISS.load_local("vectorstore", OpenAIEmbeddings())
    retriever = db.as_retriever()
    llm = ChatOpenAI(temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

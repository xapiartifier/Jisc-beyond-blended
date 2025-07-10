from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

loader = TextLoader("docs/sample_beyond_blended.txt")
docs = loader.load()

db = FAISS.from_documents(docs, OpenAIEmbeddings())
db.save_local("vectorstore")

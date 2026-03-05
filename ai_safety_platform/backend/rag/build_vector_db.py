import json
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

def load_dataset():
	with open("law_dataset.json") as f:
		data = json.load(f)
	docs = [Document(page_content=item["content"]) for item in data]
	return docs

def build_db():
	docs = load_dataset()
	embeddings = HuggingFaceEmbeddings()
	db = FAISS.from_documents(docs, embeddings)
	db.save_local("law_vector_db")
	return db
# Simple Vector Store for Regulation RAG

class VectorStore:
    def __init__(self, documents):
        self.documents = documents

    def similarity_search(self, query, k=3):
        # Dummy similarity: return first k docs
        return self.documents[:k]

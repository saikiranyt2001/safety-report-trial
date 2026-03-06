# RAG Engine for Regulation Retrieval

from .regulation_loader import RegulationLoader
from .vector_store import VectorStore

regulation_loader = RegulationLoader('backend/rag/regulations.json')
vector_db = VectorStore(regulation_loader.get_all())

def retrieve_regulation(hazard):
    results = vector_db.similarity_search(hazard, k=3)
    return [r['content'] for r in results]

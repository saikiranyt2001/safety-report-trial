# rag_engine.py
# RAG engine logic

def search_laws(hazard):

    laws = {
        "working at heights": "Fall protection and safety harness required above 2 meters.",
        "confined space": "Gas monitoring and rescue plan required."
    }

    return laws.get(hazard.lower(), "General workplace safety rules apply.")
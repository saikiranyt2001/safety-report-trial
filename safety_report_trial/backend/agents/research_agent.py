# research_agent.py
# Research agent logic (RAG-based law search)

from safety_report_trial.backend.rag.rag_engine import search_laws

def research_agent(hazard: str):
    if not hazard:
        return ["No hazard provided"]
    try:
        laws = search_laws(hazard)
        if not laws:
            return ["No safety regulations found"]
        return laws
    except Exception as e:
        return [f"Law search failed: {str(e)}"]
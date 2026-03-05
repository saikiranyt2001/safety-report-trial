# research_agent.py
# Research agent logic

from ai_safety_platform.backend.rag.rag_engine import search_laws

def research_agent(hazard):
    laws = search_laws(hazard)
    return laws
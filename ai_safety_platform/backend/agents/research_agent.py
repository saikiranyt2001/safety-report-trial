# research_agent.py
# Research agent logic

from rag.rag_engine import search_laws

def research_agent(hazard):

    laws = search_laws(hazard)

    return laws
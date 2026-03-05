# report_service.py
# Report service logic

from agents.research_agent import research_agent
from agents.draft_agent import draft_document
from agents.compliance_agent import compliance_check

def generate_report(industry, hazard):

    laws = research_agent(hazard)

    draft = draft_document(industry, hazard, laws)

    final = compliance_check(draft)

    return final
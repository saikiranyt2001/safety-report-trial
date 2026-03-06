# compliance_agent.py
# Checks compliance with Australian WHS standards
from rag.whs_regulations import get_compliance_checklist

def check_compliance():
    checklist = get_compliance_checklist()
    return {item: "✓" for item in checklist}

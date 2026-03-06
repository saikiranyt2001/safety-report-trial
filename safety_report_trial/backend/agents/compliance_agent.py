# Add missing get_compliance_reference function
def get_compliance_reference(hazard):
    return {
        "standard": "ISO 45001",
        "reference": "General Workplace Safety",
        "hazard": hazard
    }
# compliance_agent.py
# Compliance agent logic

def compliance_check(report):
    checklist = [
        "hazard",
        "control",
        "ppe",
        "emergency"
    ]
    warnings = []
    for item in checklist:
        if item not in report.lower():
            warnings.append(item)
    if warnings:
        report += "\n\nCompliance Warning:\n"
        for w in warnings:
            report += f"Missing: {w}\n"
    return report
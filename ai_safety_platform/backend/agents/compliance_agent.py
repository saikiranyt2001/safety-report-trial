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
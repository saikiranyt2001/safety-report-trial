# compliance_agent.py
# AI + Rule-based Compliance Agent

import os
from openai import OpenAI

# Initialize OpenAI client safely
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ISO reference lookup
def get_compliance_reference(hazard):
    return {
        "standard": "ISO 45001",
        "reference": "General Workplace Safety",
        "hazard": hazard
    }


# AI reasoning for compliance
def ai_compliance_check(report_text):
    if not report_text:
        return "No report provided for AI compliance analysis."
    prompt = f"""
You are a workplace safety compliance auditor.

Evaluate whether the following safety report complies with ISO 45001
workplace safety standards.

Safety Report:
{report_text}

Check for:
1. Hazard identification
2. Risk control measures
3. PPE requirements
4. Emergency procedures

Return:
- A short compliance summary
- Any missing safety elements
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert workplace safety compliance auditor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI compliance analysis failed: {str(e)}"


# Rule-based compliance check
def compliance_check(report, hazard):
    if not report:
        report = ""
    checklist = [
        "hazard",
        "control",
        "ppe",
        "emergency"
    ]
    missing = []
    for item in checklist:
        if item not in report.lower():
            missing.append(item)
    reference = get_compliance_reference(hazard)
    ai_review = ai_compliance_check(report)
    return {
        "compliant": len(missing) == 0,
        "missing_items": missing,
        "reference": reference,
        "ai_review": ai_review
    }
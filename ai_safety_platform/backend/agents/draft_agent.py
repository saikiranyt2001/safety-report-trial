# draft_agent.py
# Draft agent logic

from openai import OpenAI

client = OpenAI()

def draft_document(industry, hazard, laws):
    prompt = f"""
    Create a workplace safety report.

    Industry: {industry}
    Hazard: {hazard}

    Safety rules:
    {laws}

    Include:
    hazards
    risk controls
    PPE
    emergency procedures
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
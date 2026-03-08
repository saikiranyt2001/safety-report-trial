# draft_agent.py
# Draft agent logic

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def draft_document(industry, hazard, laws):
    prompt = f"""
Create a workplace safety report.

Industry: {industry}
Hazard: {hazard}

Safety regulations:
{laws}

The report must include:

1. Hazard identification
2. Risk controls
3. Required PPE
4. Emergency procedures

Write the report clearly and professionally.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a workplace safety report generator."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Draft generation failed: {str(e)}"
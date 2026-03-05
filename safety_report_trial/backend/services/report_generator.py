# report_generator.py
# Real AI report generation using OpenAI (or RAG)

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_report(industry, hazard, location, crew):
    prompt = f"""
Generate a detailed workplace safety report for the following:
Industry: {industry}
Hazard: {hazard}
Location: {location}
Crew Size: {crew}
Include recommended safety measures, compliance notes, and risk assessment.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600
    )
    return response.choices[0].message.content.strip()

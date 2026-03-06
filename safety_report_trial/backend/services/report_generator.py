# report_generator.py
# Real AI report generation using OpenAI (or RAG)

import os
import openai
from dotenv import load_dotenv
from safety_report_trial.backend.risk.hazard_library import get_hazards
from safety_report_trial.backend.risk.risk_matrix import calculate_risk

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ai_report(industry, location, crew, hazard=None, likelihood="Possible", consequence="Major"):
    hazards = get_hazards(industry)
    selected_hazard = hazard if hazard else (hazards[0] if hazards else "Unknown")
    risk_level = calculate_risk(likelihood, consequence)
    prompt = f"""
Australian WHS Safety Report
Industry: {industry}
Location: {location}
Crew Size: {crew}
Hazards Identified: {', '.join(hazards)}
Selected Hazard: {selected_hazard}
Risk Assessment:
  Likelihood: {likelihood}
  Consequence: {consequence}
  Risk Level: {risk_level}
Include:
  - Recommended control measures (hierarchy of controls)
  - PPE requirements
  - Incident history
  - Compliance with WHS Act
  - Recommendations
  - Review date
"""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800
    )
    return response.choices[0].message.content.strip()

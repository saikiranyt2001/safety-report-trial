# recommendation_agent.py
# Recommendation Agent for Safety Suggestions

RECOMMENDATIONS = {
    "working at height": [
        "Use fall protection systems",
        "Install guardrails",
        "Ensure workers wear safety harnesses"
    ],
    "falling objects": [
        "Use overhead protection",
        "Wear hard hats",
        "Secure loose materials"
    ],
    "electrical hazard": [
        "Use insulated tools",
        "De-energize circuits before maintenance",
        "Wear electrical PPE"
    ],
    "forklift collision": [
        "Separate pedestrian walkways",
        "Install warning alarms",
        "Train forklift operators"
    ],
    "manual lifting injury": [
        "Provide lifting training",
        "Use mechanical lifting aids",
        "Limit load weight"
    ],
    "machine entanglement": [
        "Install machine guards",
        "Follow lockout-tagout procedures",
        "Provide operator training"
    ],
    "chemical exposure": [
        "Use chemical-resistant PPE",
        "Ensure proper ventilation",
        "Provide safety data sheets"
    ]
}

def generate_recommendations(hazards):
    recommendations = []
    for hazard in hazards:
        hazard = hazard.lower()
        if hazard in RECOMMENDATIONS:
            recommendations.extend(RECOMMENDATIONS[hazard])
        else:
            recommendations.append(f"Implement safety procedures for {hazard}")
    return recommendations

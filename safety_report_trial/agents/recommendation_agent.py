# recommendation_agent.py
# Generates recommendations based on hierarchy of controls

HIERARCHY_OF_CONTROLS = [
    "Elimination",
    "Substitution",
    "Engineering Controls",
    "Administrative Controls",
    "PPE"
]

def recommend_controls(hazard, controls):
    recs = {}
    for level in HIERARCHY_OF_CONTROLS:
        recs[level] = controls.get(level, None)
    return recs

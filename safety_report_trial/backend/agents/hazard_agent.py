# hazard_agent.py
# Hazard identification agent

HAZARDS = {
    "construction": [
        "working at height",
        "falling objects",
        "electrical hazard"
    ],
    "warehouse": [
        "forklift collision",
        "manual lifting injury"
    ],
    "manufacturing": [
        "machine entanglement",
        "chemical exposure"
    ]
}

def identify_hazards(site_type: str):
    if not site_type:
        return []
    site_type = site_type.lower().strip()
    hazards = HAZARDS.get(site_type)
    if hazards:
        return hazards
    # fallback if site type unknown
    return ["general workplace hazard"]

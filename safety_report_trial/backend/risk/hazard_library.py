# hazard_library.py
# Australian Industry Hazard Library

HAZARDS = {
    "construction": [
        "working at height",
        "falling objects",
        "scaffold collapse",
        "electrical hazard"
    ],
    "manufacturing": [
        "machine entanglement",
        "chemical exposure",
        "noise hazard"
    ],
    "mining": [
        "gas exposure",
        "vehicle collision",
        "explosion risk"
    ]
}

def get_hazards(industry):
    return HAZARDS.get(industry.lower(), [])

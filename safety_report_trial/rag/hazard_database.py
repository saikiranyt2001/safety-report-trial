# hazard_database.py
# Australian Industry Hazard Library

HAZARD_LIBRARY = {
    "construction": [
        "working at height",
        "falling objects",
        "scaffold collapse",
        "electric shock"
    ],
    "manufacturing": [
        "machine entanglement",
        "chemical exposure",
        "noise hazard",
        "heat stress"
    ],
    "mining": [
        "explosion risk",
        "gas exposure",
        "vehicle collision"
    ]
}

def get_hazards(industry):
    return HAZARD_LIBRARY.get(industry.lower(), [])

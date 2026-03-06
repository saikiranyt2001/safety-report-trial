# Hazard Agent for Hazard Identification

try:
    from ..risk.hazard_library import HAZARDS
except ImportError:
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
    site_type = site_type.lower()
    return HAZARDS.get(site_type, [])

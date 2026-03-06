# Hazard Agent for Hazard Identification

try:
    from ..risk.hazard_library import HAZARDS
except ImportError:
    HAZARDS = {}

def identify_hazards(site_type: str):
    site_type = site_type.lower()
    return HAZARDS.get(site_type, [])

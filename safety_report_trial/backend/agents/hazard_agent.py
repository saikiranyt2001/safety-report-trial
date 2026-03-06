# Hazard Agent for Hazard Identification
from ..risk.hazard_library import HAZARDS

def identify_hazards(site_type):
    return HAZARDS.get(site_type, [])

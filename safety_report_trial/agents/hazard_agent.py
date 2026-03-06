# hazard_agent.py
# Identifies hazards based on site type and data
from rag.hazard_database import get_hazards

def identify_hazards(site_type, site_data):
    hazards = get_hazards(site_type)
    detected = hazards.copy()
    if "unsafe_conditions" in site_data:
        detected.extend(site_data["unsafe_conditions"])
    return list(set(detected))

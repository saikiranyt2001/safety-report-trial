# Hierarchy of Controls for Australian WHS

CONTROLS = {
    "working at height": {
        "elimination": ["avoid work at height where possible"],
        "substitution": ["use extendable tools from ground"],
        "engineering": ["install guard rails"],
        "administrative": ["worker training"],
        "ppe": ["safety harness"]
    },
    "electrical hazard": {
        "elimination": ["de-energize circuits before work"],
        "substitution": ["use battery tools"],
        "engineering": ["insulated tools"],
        "administrative": ["electric safety training"],
        "ppe": ["lockout tagout"]
    }
}

def recommend_controls(hazard: str):
    hazard = hazard.lower()
    return CONTROLS.get(hazard, {"general": ["follow general safety procedures"]})

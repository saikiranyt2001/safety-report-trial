# Hierarchy of Controls for Australian WHS
CONTROLS = {
    "working at height": {
        "engineering": ["install guard rails"],
        "administrative": ["worker training"],
        "ppe": ["safety harness"]
    },
    "electrical hazard": {
        "engineering": ["insulated tools"],
        "administrative": ["electric safety training"],
        "ppe": ["lockout tagout"]
    }
}

def recommend_controls(hazard):
    return CONTROLS.get(hazard, {"general": ["general safety procedure"]})

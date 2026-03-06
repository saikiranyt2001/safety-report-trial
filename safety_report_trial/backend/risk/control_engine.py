# Hierarchy of Controls Generator for Australian WHS

CONTROLS = {
    "working at height": [
        "Elimination: Remove unsafe conditions",
        "Substitution: Use safer equipment",
        "Engineering Controls: Install guard rails",
        "Administrative Controls: Provide worker training",
        "PPE: Use safety harness"
    ],
    "electrical hazard": [
        "Elimination: De-energize circuits",
        "Substitution: Use insulated tools",
        "Engineering Controls: Install circuit breakers",
        "Administrative Controls: Electric safety training",
        "PPE: Wear rubber gloves"
    ]
}

def get_controls(hazard):
    return CONTROLS.get(hazard, ["General safety procedure"])

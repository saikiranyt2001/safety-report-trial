# Recommendation Agent

RECOMMENDATIONS = {
    "working at height": [
        "install guard rails",
        "use safety harness",
        "provide fall protection training"
    ],
    "electrical hazard": [
        "de-energize circuits before work",
        "use insulated tools",
        "apply lockout tagout procedures"
    ],
    "machine entanglement": [
        "install machine guards",
        "provide operator training",
        "use protective gloves"
    ]
}

def generate_recommendations(hazards):
    results = {}
    for h in hazards:
        results[h] = RECOMMENDATIONS.get(
            h,
            ["follow standard safety procedures"]
        )
    return results

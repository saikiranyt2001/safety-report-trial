# Recommendation Agent for Safety Suggestions

def generate_recommendations(hazards):
    recs = []
    for hazard in hazards:
        recs.append(f"Review procedures for {hazard}")
    return recs

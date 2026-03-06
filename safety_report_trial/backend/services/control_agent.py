# Control Agent for Hierarchy of Controls

try:
    from ..risk.control_recommender import recommend_controls
except ImportError:
    def recommend_controls(hazard):
        return f"General safety controls recommended for {hazard}"

def get_control_recommendations(hazard: str) -> str:
    return recommend_controls(hazard)

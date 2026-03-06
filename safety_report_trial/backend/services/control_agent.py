# Control Agent for Hierarchy of Controls
from backend.risk.control_recommender import recommend_controls

def get_control_recommendations(hazard):
    return recommend_controls(hazard)

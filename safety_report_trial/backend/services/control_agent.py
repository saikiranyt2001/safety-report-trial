# Control Agent for Hierarchy of Controls
from ..risk.control_recommender import recommend_controls

def get_control_recommendations(hazard):
    return recommend_controls(hazard)

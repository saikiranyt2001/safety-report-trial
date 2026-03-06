# swp_agent.py
# Generates Safe Work Procedures (SWP) for tasks

def generate_swp(task, hazards, controls, ppe):
    return {
        "Task": task,
        "Hazards": hazards,
        "Controls": controls,
        "PPE": ppe
    }

# swp_agent.py
# Generates Safe Work Procedures (SWP) for tasks

def generate_swp(task, hazards, controls, ppe, risk):
    return {
        "task": task,
        "hazards": hazards,
        "controls": controls,
        "ppe": ppe,
        "risk": risk,
        "procedure_steps": [
            "Inspect work area",
            "Identify hazards before starting",
            "Apply control measures",
            "Wear required PPE",
            "Perform task safely",
            "Report incidents or unsafe conditions"
        ]
    }

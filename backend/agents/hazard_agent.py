def identify_hazards(site_type):
    hazards = {
        "construction": [
            "Fall from height",
            "Scaffold collapse",
            "Electrical exposure"
        ],
        "factory": [
            "Machine entanglement",
            "Chemical exposure"
        ]
    }
    return hazards.get(site_type.lower(), [])

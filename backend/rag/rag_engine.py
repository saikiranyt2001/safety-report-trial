class RAGEngine:
    def __init__(self):
        # Normally this would load vector DB
        self.regulations = [
            "Workers must wear helmets in construction zones.",
            "Chemical plants must maintain proper ventilation.",
            "Electrical equipment must be grounded."
        ]

    def generate_report(self, user_request: str):
        """
        Generate a simple safety report using regulations
        """
        report = f"Safety Report\n\nRequest: {user_request}\n\nRelevant Regulations:\n"

        for r in self.regulations:
            report += f"- {r}\n"

        report += "\nRecommendations:\nFollow all listed safety regulations."

        return report

def retrieve_regulation(query: str):
    """
    Dummy regulation retrieval for now.
    Later this can connect to vector database / embeddings.
    """

    regulations = {
        "ppe": "Workers must wear helmets, gloves, and safety shoes.",
        "fire": "Fire extinguishers must be accessible within 15 meters.",
        "electrical": "Electrical panels must be properly insulated.",
        "working_at_height": "Workers above 2 meters must use fall protection."
    }

    for key in regulations:
        if key in query.lower():
            return regulations[key]

    return "Follow general workplace safety regulations."

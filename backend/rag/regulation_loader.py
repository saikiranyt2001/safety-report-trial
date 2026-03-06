# Regulation Loader for RAG System

import json

class RegulationLoader:
    def __init__(self, regulation_path):
        self.regulation_path = regulation_path
        self.regulations = self.load_regulations()

    def load_regulations(self):
        with open(self.regulation_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_all(self):
        return self.regulations

# validation_agent.py
"""
AI Report Quality Validator
Checks for missing hazards, invalid regulation references, and incomplete controls.
"""

import re

class ValidationAgent:
    def __init__(self, hazard_list=None, regulation_list=None):
        self.hazard_list = hazard_list or []
        self.regulation_list = regulation_list or []

    def validate_report(self, report_text):
        issues = []
        text = report_text.lower()

        if not report_text.strip():
            return ["Report text is empty."]

        # Section checks
        if "hazards:" not in text:
            issues.append("Hazards section missing.")
        if "controls:" not in text:
            issues.append("Controls section missing.")
        if "regulations:" not in text:
            issues.append("Regulations section missing.")
        if "recommendations:" not in text:
            issues.append("Recommendations section missing.")

        if len(report_text.strip()) < 100:
            issues.append("Report too short.")

        # Original checks
        if self.hazard_list:
            missing = [
                hazard for hazard in self.hazard_list
                if hazard.lower() not in text
            ]
            if missing:
                issues.append(f"Missing hazards: {', '.join(missing)}")
        if self.regulation_list:
            invalid_refs = []
            matches = re.findall(r'Regulation\s*([A-Za-z0-9\-]+)', report_text)
            for match in matches:
                if match not in self.regulation_list:
                    invalid_refs.append(match)
            if invalid_refs:
                issues.append(f"Invalid regulation references: {', '.join(invalid_refs)}")
        if "controls:" in text:
            parts = text.split("controls:")
            controls_section = parts[1] if len(parts) > 1 else ""
            if len(controls_section.strip()) < 20:
                issues.append("Controls section appears incomplete.")
        return issues

# Example usage:
# agent = ValidationAgent(hazard_list=["fall", "electrical"], regulation_list=["WHS-123", "WHS-456"])
# issues = agent.validate_report(report_text)

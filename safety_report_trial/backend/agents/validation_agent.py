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
        # Check for missing hazards
        if self.hazard_list:
            missing = [hazard for hazard in self.hazard_list if hazard.lower() not in report_text.lower()]
            if missing:
                issues.append(f"Missing hazards: {', '.join(missing)}")
        # Check for invalid regulation references
        if self.regulation_list:
            invalid_refs = []
            for match in re.findall(r'Regulation\s*([A-Za-z0-9\-]+)', report_text):
                if match not in self.regulation_list:
                    invalid_refs.append(match)
            if invalid_refs:
                issues.append(f"Invalid regulation references: {', '.join(invalid_refs)}")
        # Check for incomplete controls
        if 'controls:' in report_text.lower():
            controls_section = report_text.lower().split('controls:')[1]
            if len(controls_section.strip()) < 20:
                issues.append("Controls section appears incomplete.")
        else:
            issues.append("Controls section missing.")
        return issues

# Example usage:
# agent = ValidationAgent(hazard_list=["fall", "electrical"], regulation_list=["WHS-123", "WHS-456"])
# issues = agent.validate_report(report_text)

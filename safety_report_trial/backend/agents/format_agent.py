# format_agent.py
# Report formatting agent

from ..template.template_engine import fill_template

def format_report(data):
    if not data:
        return "No report data available."
    try:
        formatted = fill_template(data)
        return formatted
    except Exception as e:
        return f"Report formatting failed: {str(e)}"
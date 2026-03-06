from backend.workflow.safety_pipeline import run_safety_workflow
from backend.utils.logger import logger

def generate_report(data):
    try:
        logger.info("Running safety workflow")
        result = run_safety_workflow(data)
        return result
    except Exception as e:
        logger.error(f"Report generation failed: {e}")
        return {
            "status": "error",
            "message": "Report generation failed"
        }

from backend.database.models.audit_log import AuditLog
from backend.database.database import SessionLocal
import datetime

def log_audit_action(user, action, project_id=None):
    db = SessionLocal()
    audit = AuditLog(
        user=user,
        action=action,
        timestamp=datetime.datetime.utcnow(),
        project_id=project_id
    )
    db.add(audit)
    db.commit()
    db.close()

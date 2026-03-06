def get_monthly_usage(month=None):
    db: Session = SessionLocal()
    if not month:
        month = datetime.datetime.now().strftime('%Y-%m')
    usage_records = db.query(Usage).filter_by(month=month).all()
    result = []
    for usage in usage_records:
        result.append({
            "user_id": usage.user_id,
            "tokens": usage.tokens,
            "reports": usage.reports,
            "cost": usage.cost
        })
    return result
# usage_tracker.py
# Track AI token usage, reports generated, and monthly cost


import datetime
from sqlalchemy.orm import Session
from backend.database.database import SessionLocal
from backend.database.models import Usage

def track_usage(user_id, tokens, report_id=None, cost=None):
    month = datetime.datetime.now().strftime('%Y-%m')
    db: Session = SessionLocal()
    usage = db.query(Usage).filter_by(user_id=user_id, month=month).first()
    if usage:
        usage.tokens += tokens
        usage.reports += 1
        if cost:
            usage.cost += cost
        usage.report_id = report_id
    else:
        usage = Usage(
            user_id=user_id,
            month=month,
            tokens=tokens,
            reports=1,
            cost=cost if cost else 0,
            report_id=report_id,
            created_at=datetime.datetime.utcnow()
        )
        db.add(usage)
    db.commit()
    db.refresh(usage)
    print(f"Tracked usage: user_id={user_id}, month={month}, tokens={usage.tokens}, reports={usage.reports}, cost={usage.cost}")

# Example usage:
# track_usage(user_id=123, tokens=500, report_id=42, cost=0.10)

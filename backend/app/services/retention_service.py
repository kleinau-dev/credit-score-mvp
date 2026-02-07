from datetime import datetime, timedelta
from app.models.credit_score import CreditScore

RETENTION_DAYS = 365

def cleanup_old_scores(db):
    limit_date = datetime.utcnow() - timedelta(days=RETENTION_DAYS)
    db.query(CreditScore).filter(
        CreditScore.created_at < limit_date
    ).delete()
    db.commit()
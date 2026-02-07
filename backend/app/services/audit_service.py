from app.models.audit_log import Auditlog

def log_action(db, user_id: int, action: str):
    log = Auditlog(
        user_id=user_id,
        action=action
    )
    db.add(log)
    db.commit()
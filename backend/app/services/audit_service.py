from sqlalchemy.orm import Session
from app.models.audit_log import AuditLog
from app.utils.audit_actions import AuditAction
from app.utils.audit_entities import AuditEntity
from datetime import datetime

def log_action(
    db,
    user_id: int,
    action: AuditAction,
    entity: AuditEntity,
    entity_id: int | None = None
):
    log = AuditLog(
        user_id=user_id,
        action=action.value,
        entity=entity.value,
        entity_id=entity_id
    )

    db.add(log)
    db.commit()

def get_user_audit_logs(
    db: Session,
    user_id: int,
    limit: int = 50,
    offset: int = 0
):
    return (
        db.query(AuditLog)
        .filter(AuditLog.user_id == user_id)
        .order_by(AuditLog.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )

def get_all_audit_logs(
    db: Session,
    limit: int = 100,
    offset: int = 0
):
    return (
        db.query(AuditLog)
        .order_by(AuditLog.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )

def filter_audit_logs(
    db: Session,
    user_id: int | None = None,
    action: str | None = None,
    entity: str | None = None,
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    limit: int = 100,
    offset: int = 0
):
    query = db.query(AuditLog)

    if user_id is not None:
        query = query.filter(AuditLog.user_id == user_id)

    if action is not None:
        query = query.filter(AuditLog.action == action)

    if entity is not None:
        query = query.filter(AuditLog.entity == entity)

    if start_date is not None:
        query = query.filter(AuditLog.created_at >= start_date)

    if end_date is not None:
        query = query.filter(AuditLog.created_at <= end_date)

    return (
        query
        .order_by(AuditLog.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
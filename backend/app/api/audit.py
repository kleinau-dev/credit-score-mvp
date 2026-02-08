from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.audit import AuditLogResponse
from app.services.audit_service import (
    get_user_audit_logs,
    get_all_audit_logs,
    filter_audit_logs
)
from app.security.auth import get_current_user
from datetime import datetime

router = APIRouter(prefix="/admin/audit", tags=["Admin - Audit"])

@router.get(
    "/user/{user_id}",
    response_model=list[AuditLogResponse]
)
def audit_logs_by_user(
    user_id: int,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_user_audit_logs(db, user_id, limit, offset)

@router.get(
    "/",
    response_model=list[AuditLogResponse]
)
def audit_logs_all(
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    
    return get_all_audit_logs(db, limit, offset)

@router.get(
    "/search",
    response_model=list[AuditLogResponse]
)
def search_audit_logs(
    user_id: int | None = None,
    action: str | None = None,
    entity: str | None = None,
    start_date: datetime | None = Query(None),
    end_date: datetime | None = Query(None),
    limit: int = 100,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return filter_audit_logs(
        db=db,
        user_id=user_id,
        action=action,
        entity=entity,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        offset=offset
    )

@router.get("/export")
def export_audit_logs(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logs = get_all_audit_logs(db, limit=1000)

    return [
        {
            "id": log.id,
            "user_id": log.user_id,
            "action": log.action,
            "entity": log.entity,
            "entity_id": log.entity_id,
            "created_at": log.created_at.isoformat()
        }
        for log in logs
    ]

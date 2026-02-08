from app.models.financial_data import FinancialData
from app.services.audit_service import log_action
from app.utils.audit_actions import AuditAction
from app.utils.audit_entities import AuditEntity

def create_financial_data(db, user_id: int, data):
    financial = FinancialData(
        user_id=user_id,
        income=data.income,
        debt=data.debt,
        history=data.history,
        consistency=data.consistency
    )

    db.add(financial)
    db.commit()
    db.refresh(financial)

    log_action(
        db=db,
        user_id=user_id,
        action=AuditAction.FINANCIAL_DATA_CREATED,
        entity=AuditEntity.FINANCIAL_DATA,
        entity_id=financial.id
    )

    return financial 
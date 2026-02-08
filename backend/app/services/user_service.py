from app.models.user import User
from app.models.financial_data import FinancialData
from app.models.credit_score import CreditScore
from app.services.audit_service import log_action
from app.utils.audit_actions import AuditAction
from app.utils.audit_entities import AuditEntity

def delete_user_data(db, user_id: int):
    db.query(CreditScore).filter(CreditScore.user_id == user_id).delete()
    db.query(FinancialData).filter(FinancialData.user_id == user_id).delete()
    db.query(User).filter(User.id == user_id).delete()

    db.commit()

    log_action(
        db=db,
        user_id=user_id,
        action=AuditAction.USER_DATA_DELETED,
        entity=AuditEntity.USER,
        entity_id=user_id
    )
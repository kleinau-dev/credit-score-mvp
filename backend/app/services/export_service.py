from app.models.user import User
from app.models.financial_data import FinancialData
from app.models.credit_score import CreditScore
from app.services.audit_service import log_action
from app.utils.audit_actions import AuditAction
from app.utils.audit_entities import AuditEntity

def export_user_data(db, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    financial = db.query(FinancialData).filter(FinancialData.user_id == user_id).all()
    scores = db.query(CreditScore).filter(CreditScore.user_id == user_id).all()

    log_action(
        db=db,
        user_id=user_id,
        action=AuditAction.USER_DATA_EXPORTED,
        entity=AuditEntity.USER,
        entity_id=user_id
    )

    return {
        "user": {
            "id": user.id,
            "email": user.email
        },
        "financial_data": [
            {
                "income": f.income,
                "debt": f.debt,
                "history": f.history,
                "consistency": f.consistency
            } for f in financial
        ],
        "scores": [
            {
                "score": s.score,
                "created_at": s.created_at
            } for s in scores
        ]
    }

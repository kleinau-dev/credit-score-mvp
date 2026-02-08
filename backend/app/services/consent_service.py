from datetime import datetime
from app.models.user_consent import UserConsent
from app.services.audit_service import log_action
from app.utils.audit_actions import AuditAction
from app.utils.audit_entities import AuditEntity

CURRENT_CONSENT_VERSION = "1.0"

def give_consent(db, user_id: int):
    consent = UserConsent(
        user_id=user_id,
        accepted=True,
        accepted_at=datetime.utcnow(),
        version=CURRENT_CONSENT_VERSION
    )
    db.commit()
    db.commit()

    log_action(
        db=db,
        user_id=user_id,
        action=AuditAction.CONSENT_GIVEN,
        entity=AuditEntity.USER_CONSENT
    )

    return consent

def has_consent(db, user_id: int) -> bool:
    return (
        db.query(UserConsent)
        ,filter(
            UserConsent.user_id == user_id,
            UserConsent.accepted == True,
            UserConsent.version == CURRENT_CONSENT_VERSION
        )
        .first()
        is not None
    )
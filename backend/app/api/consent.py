from fastapi import APIRouter, Depends
from app.security.auth import get_current_user
from app.db.session import SessionLocal
from app.services.consent_service import give_consent
from app.services.audit_service import log_action

router = APIRouter(
    prefix="/consent",
    tags=["Consent"]
)

@router.post("/accepted")
def accepted_consent(user=Depends(get_current_user)):
    db = SessionLocal()
    give_consent(db, int(user["sub"]))
    log_action(
    db,
    user_id=int(user["sub"]),
    action="consent_given",
    entity="user_consent",
    entity_id=int(user["sub"])
)
    return {"message": "Consentimento registrado com sucesso"}
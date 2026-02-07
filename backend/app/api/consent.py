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
    log_action(db, int(user["sub"]), "consent_given")
    return {"message": "Consentimento registrado com sucesso"}
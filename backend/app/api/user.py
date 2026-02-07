from fastapi import APIRouter, Depends
from app.security.auth import get_current_user
from app.db.session import SessionLocal
from app.services.user_service import delete_user_data
from app.services.export_service import export_user_data
from app.services.audit_service import log_action

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.delete("/data")
def delete_data(user=Depends(get_current_user)):
    db = SessionLocal()
    delete_user_data(db, int(user["sub"]))
    log_action(db, int(user["sub"]), "data_exported")
    return {"message": "Todos os dados do usuário foram removidos"}

@router.get("/export")
def export_data(user=Depends(get_current_user)):
    db = SessionLocal()
    log_action(db, int(user["sub"]), "user_data_deleted")
    return export_user_data(db, int(user["sub"]))
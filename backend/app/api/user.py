from fastapi import APIRouter, Depends
from app.security.auth import get_current_user
from app.db.session import SessionLocal
from app.services.user_service import delete_user_data

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.delete("/data")
def delete_data(user=Depends(get_current_user)):
    db = SessionLocal()
    delete_user_data(db, int(user["sub"]))
    return {"message": "Todos os dados do usuário foram removidos"}
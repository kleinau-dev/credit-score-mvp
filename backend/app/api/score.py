from fastapi import APIRouter, Depends, HTTPException
from app.security.auth import get_current_user
from app.db.session import SessionLocal
from app.models.financial_data import FinancialData
from app.services.score_service import generate_score, get_score_history
from app.schemas.score import ScoreHistoryOut
from typing import List 

router = APIRouter(
    prefix="/score",
    tags=["Score"]
)

@router.post("/")
def calculate(user=Depends(get_current_user)):
    db = SessionLocal()
    

    financial_data = (
        db.query(FinancialData)
        .filter(FinancialData.user_id == int(user["sub"]))
        .order_by(FinancialData.id.desc())
        .first()
    )

    if not financial_data:
        raise HTTPException(
            status_code=400,
            detail="Nenhum dado financeiro encontrado para o usuário"
        )

    return generate_score(db, int(user["sub"]), financial_data)

@router.get("/history", response_model=List[ScoreHistoryOut])
def history(user=Depends(get_current_user)):
    db = SessionLocal()
    return get_score_history(db, int(user["sub"]))
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.security.auth import get_current_user
from app.db.session import get_db
from app.db.session import SessionLocal
from app.models.financial_data import FinancialData
from app.services.score_service import generate_score, get_score_history
from app.schemas.score import ScoreHistoryOut
from typing import List 
from app.services.score_explanation import explain_score
from app.models.score_rule import ScoreRule
from app.models.credit_score import CreditScore

router = APIRouter(
    prefix="/score",
    tags=["Score"]
)

@router.post("/")
def calculate(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    financial_data = (
        db.query(FinancialData)
        .filter(FinancialData.user_id == int(user["sub"]))
        .first()  
    )

    rules = db.query(ScoreRule).filter(ScoreRule.enabled == True).all()
    
    score = generate_score(db, int(user["sub"]), financial_data)
    explanation = explain_score(financial_data, rules)

    return {
        "score": score.score,
        "explanation": explanation
    }

@router.get("/history")
def history(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_score_history(db, int(user["sub"]))

@router.get("/history")
def score_history(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    scores = (
        db.query(CreditScore)
        .filter(CreditScore.user_id == int(user["sub"]))
        .order_by(CreditScore.created_at.desc())
        .all()
    )

    return scores
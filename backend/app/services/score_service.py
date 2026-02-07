from app.services.score_engine import calculate_score
from app.models.credit_score import CreditScore

def generate_score(db, user_id: int, financial_data):
    score_value = calculate_score(financial_data)

    score = CreditScore(
        user_id=user_id,
        score=score_value
    )

    db.add(score)
    db.commit()
    db.refresh(score)

    return {"score": score_value}

def get_score_history(db, user_id: int):
    return (
        db.query(CreditScore)
        .filter(CreditScore.user_id == user_id)
        .order_by(CreditScore.created_at.desc())
        .all()
    )
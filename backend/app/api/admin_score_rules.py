from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.score_rule import ScoreRule
from app.security.auth import get_current_user

router = APIRouter(
    prefix="/admin/score",
    tags=["Admin - Score"]
)

@router.put("/rules/{rule_id}")
def update_rule(
    rule_id: int,
    weight: float,
    enabled: bool,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    rule = (
        db.query(ScoreRule)
        .filter(ScoreRule.id == rule_id)
        .first()
    )

    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    rule.weight = weight
    rule.enabled = enabled

    db.commit()
    db.refresh(rule)

    return rule

from app.models.score_rule import ScoreRule
from app.services.score_engine import calculate_score
from app.models.credit_score import CreditScore
from app.services.score_snapshot import build_rules_snapshot
from app.services.audit_service import log_action
from app.utils.audit_actions import AuditAction
from app.utils.audit_entities import AuditEntity

ENGINE_VERSION = "1.0"

def generate_score(db, user_id: int, financial_data):
    rules = (
        db.query(ScoreRule)
        .filter(ScoreRule.enabled == True)
        .all()
    )

    score_value = calculate_score(financial_data, rules)
    snapshot = build_rules_snapshot(rules)

    score = CreditScore(
        user_id=user_id,
        score=score_value,
        rules_snapshot=snapshot,
        engine_version=ENGINE_VERSION
    )

    db.add(score)
    db.commit()
    db.refresh(score)

    log_action(
        db=db,
        user_id=user_id,
        action=AuditAction.SCORE_GENERATED,
        entity=AuditEntity.CREDIT_SCORE,
        entity_id=score.id
    )

    return score

def get_score_history(db, user_id: int):
    return (
        db.query(CreditScore)
        .filter(CreditScore.user_id == user_id)
        .order_by(CreditScore.created_at.desc())
        .all()
    )
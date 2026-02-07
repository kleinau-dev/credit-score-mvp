from app.db.session import SessionLocal
from app.models.score_rule import ScoreRule

db = SessionLocal()

rules = [
    ScoreRule(name="Income", field="income", weight=0.3),
    ScoreRule(name="Debt", field="debt", weight=0.4),
    ScoreRule(name="Age", field="age", weight=0.2),
    ScoreRule(name="Payment History", field="payment_history", weight=0.1)
]

db.add_all(rules)
db.commit()
db.close()
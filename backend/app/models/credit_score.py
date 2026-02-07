from sqlalchemy import Column, Integer, ForeignKey, DateTime, JSON, String
from datetime import datetime
from app.db.base import Base

class CreditScore(Base):
    __tablename__ = "credit_scores"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer, nullable=False)

    rules_snapshot = Column(JSON, nullable=False)
    engine_version = Column(String, default="1.0")
    
    created_at = Column(DateTime, default=datetime.utcnow)

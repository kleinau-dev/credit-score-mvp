from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from app.db.base import Base

class CreditScore(Base):
    __tablename__ = "credit_scores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

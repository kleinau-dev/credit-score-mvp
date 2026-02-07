from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.base import Base

class ScoreRule(Base):
    __tablename__ = "score_rules"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    field = Column(String, nullable=False)   
    weight = Column(Float, nullable=False)
    enabled = Column(Boolean, default=True)

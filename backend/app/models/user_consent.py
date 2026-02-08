from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey, String
from datetime import datetime
from app.db.base import Base

class UserConsent(Base):
    __tablename__ = "user_consents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    accepted = Column(Boolean, default=False)
    accepted_at = Column(DateTime)
    version = Column(String) 
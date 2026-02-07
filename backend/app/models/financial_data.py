from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db.base import Base

class FinancialData(Base):
    __tablename__ = "financial_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    income = Column(Float)
    debt = Column(Float)
    history = Column(Integer)
    consistency = Column(Integer)

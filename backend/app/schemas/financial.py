from pydantic import BaseModel

class FinancialDataCreate(BaseModel):
    income: float
    debt: float
    history: int
    consistency: int

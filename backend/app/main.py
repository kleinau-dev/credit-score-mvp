from fastapi import FastAPI
from app.api.routes import router
from app.db.base import Base
from app.db.engine import engine
from app.models.user import User
from app.models.financial_data import FinancialData
from app.models.credit_score import CreditScore
from app.models.user_consent import UserConsent
from app.db import imports

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Credit Score API"
)

app.include_router(router)

@app.get(
    "/health",
    tags=["System"],
    summary="Health check",
    description="Endpoint used for monitoring and uptime checks"
)
def health():
    return {"status": "ok"}

from fastapi import APIRouter, Depends
from app.schemas.financial import FinancialDataCreate
from app.security.auth import get_current_user
from app.db.session import SessionLocal
from app.services.financial_service import create_financial_data

router = APIRouter(
    prefix="/financial-data",
    tags=["Financial"]
)

@router.post("/")
def create_data(
    data: FinancialDataCreate,
    user=Depends(get_current_user)
):
    db = SessionLocal()

    return create_financial_data(
        db=db,
        user_id=int(user["sub"]),
        data=data
    )

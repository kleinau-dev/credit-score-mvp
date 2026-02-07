from app.models.user import User
from app.models.financial_data import FinancialData
from app.models.credit_score import CreditScore

def delete_user_data(db, user_id: int):
    db.query(CreditScore).filter(CreditScore.user_id == user_id).delete()
    db.query(FinancialData).filter(FinancialData.user_id == user_id).delete()
    db.query(User).filter(User.id == user_id).delete()

    db.commit()
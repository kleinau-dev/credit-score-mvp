from app.models.financial_data import FinancialData

def create_financial_data(db, user_id: int, data):
    financial = FinancialData(
        user_id=user_id,
        income=data.income,
        debt=data.debt,
        history=data.history,
        consistency=data.consistency
    )

    db.add(financial)
    db.commit()
    db.refresh(financial)

    return financial 
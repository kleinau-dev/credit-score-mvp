from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.security.dependencies import get_current_user
from app.db.session import get_db
from sqlalchemy.orm import Session

def require_admin(
        current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).get(int(current_user["sub"]))

    if not user or user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )

    return user
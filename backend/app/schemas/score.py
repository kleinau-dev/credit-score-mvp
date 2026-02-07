from pydantic import BaseModel
from datetime import datetime

class ScoreHistoryOut(BaseModel):
    score: int 
    created_at: datetime

    class Config:
        from_attributes = True 
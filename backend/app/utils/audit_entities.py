from enum import Enum

class AuditEntity(str, Enum):
    USER = "user"
    USER_CONSENT = "user_consent"
    FINANCIAL_DATA = "financial_data"
    CREDIT_SCORE = "credit_score"
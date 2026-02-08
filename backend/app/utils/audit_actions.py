from enum import Enum

class AuditAction(str, Enum):
    CONSENT_GIVEN = "consent_given"

    FINANCIAL_DATA_CREATED = "financial_data_created"

    SCORE_GENERATED = "score_generated"

    USER_DATA_EXPORTED = "user_data_exported"
    USER_DATA_DELETED = "user_data_deleted"
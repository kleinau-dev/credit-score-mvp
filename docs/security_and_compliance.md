# Security and Compliance

## Authentication
- JWT-based authentication
- Stateless access tokens
- Secure password hashing

## Authorization
- Endpoint-level protection using FastAPI dependencies
- Role-aware authorization support

## Consent Management
- Explicit user consent required
- Versioned consent control
- Consent verification before sensitive operations

## Audit Logging
- All critical actions are recorded:
  - Consent acceptance
  - Data export
  - Data deletion
  - Score calculation
- Logs include user, action, entity, and timestamp

## Compliance
The system is aligned with LGPD/GDPR principles:
- Explicit consent
- Right to access (export)
- Right to erasure (delete)
- Data minimization
- Accountability through audit logs
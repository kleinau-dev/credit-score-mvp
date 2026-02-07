# API Reference

The API is fully documented using Swagger.

Available endpoints include:

Authentication:
- POST /auth/register
- POST /auth/login

Financial Data:
- POST /financial-data/

Score:
- POST /score/
- GET /score/history

User Data:
- GET /user/export
- DELETE /user/data

Consent:
- POST /consent/

All protected endpoints require a valid Bearer token.

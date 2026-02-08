# API Reference – Credit Score API

The API is fully documented via Swagger (OpenAPI).

Base URL (development):
http://localhost:8000

## Authentication
- POST /auth/register
- POST /auth/login

## Financial Data
- POST /financial-data

## Credit Score
- POST /score
- GET /score/history

## User Data
- GET /user/export
- DELETE /user/data

## Consent
- POST /consent/accepted

## Health
- GET /

All protected endpoints require a valid JWT token via Authorization header.
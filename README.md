# Credit Score MVP – Backend

This repository contains the backend implementation of a Credit Score MVP.

## Overview
The system provides a secure and auditable API that allows users to:
- Register and authenticate
- Submit financial data
- Calculate and track credit scores
- Manage consent
- Export and delete personal data

The backend is designed with security, compliance, and scalability in mind.

## Tech Stack
- Python 
- FastAPI
- SQLAlchemy
- Alembic
- SQLite (development)
- JWT Authentication

## Main Features
- Authentication and authorization
- Credit score calculation engine
- Score history
- Explicit consent management
- Audit logging
- Data export and deletion

## API Documentation
Interactive API documentation is available via Swagger:
http://localhost:8000/docs

## Running the Project (Development)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Project Status

✅ Backend completed
🚧 Frontend pending
📦 Ready for frontend integration and client validation

Notes

This project was developed following clean architecture principles and is suitable as a foundation for production environments with minimal adjustments (database and infrastructure).
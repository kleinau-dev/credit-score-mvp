# Technical Overview – Credit Score MVP

This project is a backend MVP for a Credit Score system, designed with a clean architecture, security best practices, and data compliance in mind.

The system exposes a RESTful API built with FastAPI and follows a layered architecture separating API, services, models, and security concerns.

## Main Technologies
- Python 
- FastAPI
- SQLAlchemy ORM
- Alembic (database migrations)
- SQLite (development database)
- JWT (JSON Web Tokens) for authentication

## Core Features
- User authentication and authorization
- Financial data ingestion
- Credit score calculation engine
- Score history tracking
- Explicit user consent management
- Full audit logging of sensitive actions
- User data export and deletion (LGPD/GDPR-aligned)

## Design Principles
- Separation of concerns
- Stateless authentication
- Explicit consent handling
- Auditability of critical actions
- Versioned business rules

This backend is production-ready in terms of structure and security and is intended to be consumed by a frontend application.

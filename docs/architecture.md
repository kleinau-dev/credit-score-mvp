# System Architecture

The backend follows a layered architecture:

- API Layer: Handles HTTP requests and responses (FastAPI)
- Service Layer: Business rules and domain logic
- Data Layer: Database models and persistence
- Security Layer: Authentication, authorization and consent enforcement

This separation ensures maintainability, testability and scalability.

All endpoints are exposed as REST APIs and documented using OpenAPI (Swagger).

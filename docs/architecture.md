# System Architecture

The system follows a layered architecture to ensure maintainability, scalability, and clarity.

## Layers

### API Layer
- Handles HTTP requests and responses
- Validates input and authentication
- Delegates business logic to services

### Service Layer
- Contains all business logic
- Coordinates database operations
- Responsible for audit logging and validations

### Model Layer
- SQLAlchemy ORM models
- Database schema definitions
- Relationships and constraints

### Security Layer
- JWT token generation and validation
- Authentication dependencies
- Role-based and permission-based access

### Database
- SQLite for development
- Managed via Alembic migrations

## Flow Example
Client → API → Service → Model → Database  
Security dependencies are enforced before business logic execution.
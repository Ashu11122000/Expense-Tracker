# Import settings → global configuration object loaded from .env
from app.core.config import settings

# Import ExpenseService → contains business logic
from app.services.expense_service import ExpenseService


# Dependency function to provide settings
def get_settings():
    
    """
    Dependency to provide application settings.

    This allows injecting settings into routes or services
    without directly importing them everywhere.
    """

    # Return the already created settings instance
    # This ensures a single source of truth across the app
    return settings


# Dependency function to provide ExpenseService instance
def get_expense_service():
    
    """
    Dependency to provide ExpenseService instance.

    Instead of creating service manually inside routes,
    we inject it using FastAPI Depends().
    """

    # Create and return a new instance of ExpenseService
    # FastAPI will call this function automatically when needed
    return ExpenseService()
# Import APIRouter → used to group multiple route modules together
from fastapi import APIRouter

# Import expense routes module
# This contains all endpoints related to expenses (GET, POST, etc.)
from app.api.v1.endpoints import expenses


# Create a main API router
# This acts as a central router to combine all endpoint modules
api_router = APIRouter()


# Include expense routes into main router
api_router.include_router(
    
    # Pass the router defined inside expenses.py
    expenses.router,
    
    # Prefix → all routes inside expenses will start with /expenses
    # Example:
    # "/" → "/expenses/"
    # "/create" → "/expenses/create"
    prefix="/expenses",
    
    # Tags → used for grouping in Swagger UI (/docs)
    # All these endpoints will appear under "Expenses" section
    tags=["Expenses"]
)
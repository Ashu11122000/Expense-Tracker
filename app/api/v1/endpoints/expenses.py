# Import APIRouter → used to create route groups (modular APIs)
from fastapi import APIRouter

# Import ExpenseCreate schema → used for request validation
from app.schemas.expense import ExpenseCreate

# Import service layer → contains business logic
from app.services.expense_service import ExpenseService


# Create router instance
# This router will hold all expense-related endpoints
router = APIRouter()


# Initialize service
# This connects API layer to business logic layer
service = ExpenseService()


# GET endpoint → fetch all expenses
@router.get("/")
def get_expenses():
    
    """
    GET all expenses
    """

    # Call service layer method
    # Returns list of expenses
    return service.get_expenses()


# POST endpoint → create a new expense
@router.post("/")
def create_expense(expense: ExpenseCreate):
    
    """
    POST a new expense
    """

    # FastAPI automatically:
    # 1. Parses request body
    # 2. Validates using ExpenseCreate schema
    # 3. Converts to Python object
    
    # Call service method to create expense
    return service.create_expense(expense)
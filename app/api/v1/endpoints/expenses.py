# Import APIRouter → used to create route groups (modular APIs)
from fastapi import APIRouter, Depends, Query

# Import ExpenseCreate schema → used for request validation
from app.schemas.expense import ExpenseCreate

# Import service layer → contains business logic
from app.services.expense_service import ExpenseService

# Import dependency function -> used for dependency injection
from app.api.deps import get_expense_service


# Create router instance
# This router will hold all expense-related endpoints
router = APIRouter()


# Initialize service
# This connects API layer to business logic layer
service = ExpenseService()


# GET endpoint → fetch all expenses
@router.get("/")
def get_expenses(
    
    # Query parameters (optional)
    # Filter by category
    category: str = Query(None),
    
    # Filter by date    
    date: str = Query(None),   
    
    # Filter by minimum amount 
    min_amount: float = Query(None),
    
    # Dependency Injection -> FastAPI will automatically provide service instance    
    service: ExpenseService = Depends(get_expense_service),
):
    
    """
    GET all expenses
    """
    
    # If any filter parameter is provided -> apply filtering
    if category or date or min_amount:
        return service.filter_expenses(category, date, min_amount)

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


# PUT endpoint -> Update an existing expense
@ router.put("/{expense_id}")
def update_expense(
    
    # expense id (path parameter)
    expense_id: int,
    
    # Validated (Request body)
    expense: ExpenseCreate,
    
    # Inject service instance
    service: ExpenseService = Depends(get_expense_service),
): 
    
    # Call service layer update logic
    return service.update_expense(expense_id, expense)

# DELETE endpoint -> delete an expense
@router.delete("/{expense_id}")
def delete_expense(
    
    # path parameter (expense id)
    expense_id: int,
    
    # Inject Service
    service: ExpenseService = Depends(get_expense_service)
):
    
    # Call service layer delete logic
    return service.delete_expense(expense_id)

# GET endpoint -> get summary (analytics)
@router.get("/summary")
def get_summary(
    
    # Inject service
    service: ExpenseService = Depends(get_expense_service),
):
    
    # Returns analytics data (total, category-wise, monthly)
    return service.get_summary()
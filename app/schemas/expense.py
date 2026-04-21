# Import BaseModel -> Used to create data validation schemas
# Import Field -> used to add extra validation rules and metadata
from pydantic import BaseModel, Field

# Import date type -> used to store only date (YYYY-MM-DD)
from datetime import date

# Schema used when creating a new expense (input from user)
class ExpenseCreate(BaseModel):
    """
    Schema for creating a new expense
    """
    
    # Title of expense (e.g., "Groceries", "Rent")
    # ... means this field is required
    # example is used for documentation (like Swagger UI)
    title: str = Field(..., example = "Groceries")
    
    # Amount of expense 
    amount: float = Field(..., gt = 0, example = 250.5)
    
    # Category of expense (e.g., Food, Travel, Bills)
    category: str = Field(..., example = "Food")
    
    # Date of Expense (YYYY-MM-DD format)
    # Pydantic automatically converts string -> data object
    date: date

# Schema used when returning expense data (API response/output)
class ExpenseResponse(BaseModel):
    """
    Schema for returning expense data
    """
    
    # Unique ID of expense (usually generated internally)
    id: int
    
    # Title of expense
    title: str
    
    # Amount (always float in response for consistency)
    amount: float
    
    # Category of expense
    category: str
    
    # Date of expense
    date: date
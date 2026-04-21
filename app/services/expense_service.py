# Import ExpenseRepository → used to interact with CSV/data layer
from app.repositories.expense_repo import ExpenseRepository

# Service layer -> contains business logic
# Acts as a bridge between API layer and repository layer
class ExpenseService:
    """
    Service layer contains business logic
    """
    
    # Constructor -> initialize repository
    def __init__(self):
        
        # Create repository instance
        # This allows service to access data operations
        self.repo = ExpenseRepository()
        
    # Method to fetch all expenses
    def get_expenses(self):
        """
        Get all expenses
        """
        
        # Directly call  repository method
        # Currently no additionally business logic applied
        return self.repo.get_all_expenses()
    
    # Method to create a new expense
    def create_expense(self, expense):
        """
        Create a new expense
        """
        
        # Call repository method to store expense
        # Repository returns newly created expense ID
        expense_id = self.repo.create_expense(expense)
        
        # Returns a structured response
        # This is useful for API responses
        return {
            "message": "Expense Created Successfully",    # Success message
            "id": expense_id,    # Newly created expense ID
        }
    
    
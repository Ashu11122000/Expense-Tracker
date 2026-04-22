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
    
    # Service method for updating expense
    def update_expense(self, expense_id, expense):
        
        # Call Repository method to update the expense in data storage (CSV/DB)
        updated = self.repo.update_expense(expense_id, expense)
        
        # If update failed (expense not found)
        if not updated:
            
            # Return error response (typically used in API layer)
            return {"error": "Expense not found"}
        
        # If update successful -> return success message with ID
        return {"message": "Expense updated", "id": expense_id}
    
    # Service method for deleting expense
    def delete_expense(self, expense_id):
        
        # Call repository method to delete expense
        deleted = self.repo.delete_expense(expense_id)
        
        # If deletion failed (expense not found)
        if not deleted:
            
            # Return error response (typically used in API layer)
            return{"error": "Expense not found"}
        
        # If deletion successful -> return success message with ID
        return {"message": "Expense deleted"}
    
    # Service method for filtering expenses
    def filter_expenses(self, category = None, date = None, min_amount = None):
        
        # Directly delegate filtering logic to repository layer
        # Repository handles actual filtering of data
        return self.repo.filter_expenses(category, date, min_amount)
    
    # Service method for getting summary of all expenses
    def get_summary(self):
        
        # Delegate summary/analytics calculation to repository
        # Returns total spending, category-wise and monthly summaries
        return self.repo.get_summary()
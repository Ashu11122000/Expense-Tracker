# Import CSVHandler -> handles low-level CSV operations (read/write) 
from app.utils.csv_handler import CSVHandler

# Import settings -> contains configuration like file path from .env
from app.core.config import settings

# Repository layer -> responsible for interacting with data source (CSV her)
class ExpenseRepository:
    """
    Repository layer handles data storage and retrieval
    """
    
    # Constructor -> runs when object is created
    def __init__(self):
        
        # Initialize CSV handler with file path from settings
        # This connects repository to the CSV file
        self.csv = CSVHandler(settings.csv_file_path)
        
    # Method to fetch all expenses
    def get_all_expenses(self):
        """
        Fetch all expenses from CSV
        """
        
        # Call CSV handler's read method and return all records
        return self.csv.read_all()
    
    # Method to create (add) a new expense
    def create_expense(self, expense):
        """
        Add a new expense to CSV
        """
        
        # Step 1: Read existing data from CSV
        data = self.csv.read_all()
        
        # Step 2: Generate new ID
        # If data exists -> take last record's ID and increment
        if data:
            
            # data[-1] -> last row
            # ["id"] -> get id value (string from CSV)
            # int() -> converts string to integer
            last_id = int(data[-1]["id"])
            new_id = last_id + 1
        else:
            
            # If no data -> first record -> ID = 1
            new_id = 1
            
        # Step 3: Prepare row data in list format
        # Order must match CSV headers
        row = [
            new_id,     # Unique ID
            expense.title,    # Title from schema
            expense.amount,    # Amount
            expense.category,    # Category
            expense.date,    # Date
        ]
        
        # Step 4: Append new row to CSV file
        self.csv.append_row(row)
        
        # Step 5: Return new ID (useful for response)
        return new_id
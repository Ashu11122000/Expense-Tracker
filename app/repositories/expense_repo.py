# Import CSVHandler -> handles low-level CSV operations (read/write) 
from app.utils.csv_handler import CSVHandler

# Import settings -> contains configuration like file path from .env
from app.core.config import settings

# Import datetime for date parsing and formatting
from datetime import datetime

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
    
    # Method to update expenses 
    def update_expense(self, expense_id: int, updated_expense):
        
        # Read all existing data from csv
        data = self.csv.read_all()
        
        # This will store updated rows
        updated_data = []
        
        # Flag to check if the expense was found
        found = False
        
        # Loop through each row in CSV data
        for row in data:
            
            # Check if current row matched the given expense_id
            if int(row["id"]) == expense_id:
                
                # Replace old data with updated data
                updated_data.append([
                    expense_id,    # Keep same id
                    updated_expense.title,    # New title
                    updated_expense.amount,    # New amount
                    updated_expense. category,    # New category
                    updated_expense.date,    # New date
                ])
                
                # Mark as found
                found = True
                
            else:
                
                # Keep existing row unchanged
                updated_data.append([
                    row["id"],
                    row["title"],
                    row["amount"],
                    row["category"],
                    row["date"],
                ])
                
        # If no matching expense found -> return None
        if not found: 
            return None
        
        # Rewrite entire CSV with updated data
        self.csv.write_all(updated_data)
        
        # Return updated expense id
        return expense_id
    
    # Method for delete expense
    def delete_expense(self, expense_id: int):
        
        # Reads all data from CSV
        data = self.csv.read_all()
        
        # Stores filtered data (excluding deleted one)
        new_data = []
        
        # Flag to check if expense exists
        found = False
        
        # Loop through all rows
        for row in data:
            
            # If ID matches -> skip this row (delete it)
            if int(row["id"]) == expense_id:
                found = True
                continue    # Skip adding this row
            
            # Keep all other rows
            new_data.append([
                row["id"],
                row["title"],
                row["amount"],
                row["category"],
                row["date"]
            ])
            
        # If no expense found -> return False
        if  not found:
            return False
        
        # Rewrite CSV without deleted row
        self.csv.write_all(new_data)
        
        # Return success
        return True
    
    # Method for filtering expenses
    def filter_expenses(self, category = None, date = None, min_amount = None):
        
        # Read all data
        data = self.csv.read_all()
        
        # Store filtered results
        result = []
        
        # Loop through each row
        for row in data:
            
            # Filter by category (if provided)
            if category and row["category"] != category:
                
                # skip non-matching
                continue
            
            # Filter by date (if provided)
            if date and row["date"] != date:
                continue
            
            # Filter by minimum amount (if provided)
            if min_amount and float(row["amount"]) < float(min_amount):
                continue
            
            # If all conditions pass -> include row
            result.append(row)
            
        # Return filtered data    
        return result
    
    # Method to get summary of all expenses 
    def get_summary(self):
        
        # Read all data
        data = self.csv.read_all()
        
        # Total spending accumulator
        total = 0
        
        # Dictionary to store category-wise totals
        category_summary = {}
        
        # Dictionary to store monthly totals
        monthly_summary = {}
        
        # Loop through each row
        for row in data:
            
            # Convert amount to float
            amount = float(row["amount"])
            
            # Add to total spending
            total += amount
            
            # Extract category
            category = row["category"]
            
            # Add amount to category total
            # .get(category, 0) -> default 0 if key not exists
            category_summary[category] = category_summary.get(category, 0) + amount
            
            # Convert string date to datetime object
            date_obj = datetime.strptime(row["date"], "%Y-%m-%d")
            
            # Extract month in "YYYY-MM" format
            month = date_obj.strftime("%Y-%m")
            
            # Add amount to monthly salary
            monthly_summary[month] = monthly_summary.get(month, 0) + amount
            
        return {
            
            # Overall total
            "total_spending": total,
            
            # Category-wise breakdown
            "category_summary": category_summary,
            
            # Month-wise breakdown
            "monthly_summary": monthly_summary
        }
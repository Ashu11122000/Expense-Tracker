# Import CSV module
# This module helps us to read from and write to CSV files easily
import csv

# Import os module
# Used for interacting with the operating system (like checking if a file exists)
import os

# Create a class to handle all CSV-related operations
class CSVHandler:
    """
    This class handles all CSV file operations:
    - Create file if not exists
    - Reads data
    - Write data
    """
    
    # Constructor method (runs automatically when object is created)
    def __init__(self, file_path: str):
        
        # Stores the file path provided by user
        # self is a reference to the specific instance of a class
        self.file_path = file_path
        
        # Ensures that the CSV file exists
        # If not, it will be created with headers
        self._ensure_file_exists()  # ✅ FIXED: added underscore
        
    # Private method (indicated by underscore)
    # This is used internally inside the class only
    def _ensure_file_exists(self):
        """
        Creates CSV file with headers if it does not exist
        """
        
        # Check if the file exists at given path or not
        if not os.path.exists(self.file_path):
            
            # Open the file in write mode ("w")
            # newline = "" prevents extra blank lines in CSV (important in Windows)
            with open(self.file_path, mode = "w", newline = "") as file:
                
                # Create a CSV writer object
                writer = csv.writer(file)
                
                # Write header row (column names)
                writer.writerow(["id", "title", "amount", "category", "date"])
                
    # Method to read all data from CSV file
    def read_all(self):
        """
        Read all rows from CSV file
        """
        
        # Open file in read mode ("r")
        with open(self.file_path, mode = "r") as file:
            
            # DictReader reads each row as a dictionary
            # Example: {"id": "1", "title": "Food", ....}
            reader = csv.DictReader(file)
            
            # Convert all rows into a list and return
            return list(reader)
        
    # Method to append (add) a new row into CSV
    def append_row(self, row: list):
        """
        Add a new row to CSV file
        """
        
        # Open file in append mode ("a"), adds data at the end
        with open(self.file_path, mode = "a", newline = "") as file:
            
            # Create CSV writer object
            writer = csv.writer(file)
            
            # Write the new row into a file
            # Example: row = [1, "Food", 200, "Expense", "2026-04-21"]
            writer.writerow(row)
    
    def write_all(self, data: list):
        """
        Rewrite entire CSV file with new data
        """
        # Open the file in write mode ("w")
        # - This will overwrite the existing file content completely
        # - newline = "" prevents extra blank lines in CSV (important for Windows)
        with open(self.file_path, mode = "w", newline="") as file:
            
            # Create a CSV writer object
            # - This object is responsible for writing rows into the CSV file
            writer = csv.writer(file)
            
            # Write the header row (column names)
            # - This ensures the CSV file always a consistent structure
            writer.writerow(["id", "title", "amount", "category", "date"])
            
            # Loop through each row in the provided data list
            # - Each 'row' is expected to be a list like:
            # [id, title, amount, category, date]
            for row in data:
                
                # Write each row into the CSV file
                # - Each row in written as a new line in the file
                writer.writerow(row)
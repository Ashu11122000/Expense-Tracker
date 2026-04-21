# Import OS module → used for file operations (delete file after test)
import os

# Import tempfile → used to create temporary files for testing
import tempfile

# Import pytest → testing framework
import pytest


# Import TestClient → allows testing FastAPI endpoints like real HTTP calls
from fastapi.testclient import TestClient


# Import your FastAPI app
from app.main import app

# Import settings → to override CSV file path during tests
from app.core.config import settings


# Create TestClient instance
# This simulates API requests (GET, POST, etc.)
client = TestClient(app)


# Create a fixture → reusable setup for tests
@pytest.fixture(scope="function")
def temp_csv_file():
    
    """
    Create a temporary CSV file for testing.
    This prevents modifying real data.
    """

    # Create a temporary file
    # mode="w+" → read & write
    # delete=False → we will delete manually later
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_file:
        
        # Write CSV header (VERY IMPORTANT for DictReader)
        temp_file.write("id,title,amount,category,date\n")
        
        # Ensure data is written to disk
        temp_file.flush()


        # Store original CSV path
        original_path = settings.csv_file_path
        
        # Override CSV path with temp file
        settings.csv_file_path = temp_file.name


        # Yield → provide this file to test functions
        yield temp_file.name


        # Cleanup after test finishes
        # Restore original path
        settings.csv_file_path = original_path
        
        # Delete temporary file
        os.remove(temp_file.name)


# Test: GET when no expenses exist
def test_get_expenses_empty(temp_csv_file):
    
    """
    Test GET when no expenses exist
    """

    # Send GET request
    response = client.get("/api/v1/expenses/")

    # Assert status code is 200 (success)
    assert response.status_code == 200

    # Assert response is empty list
    assert response.json() == []


# Test: Create a new expense
def test_create_expense(temp_csv_file):
    
    """
    Test creating a new expense
    """

    # Prepare request payload
    payload = {
        "title": "Groceries",
        "amount": 250.5,
        "category": "Food",
        "date": "2025-01-01"
    }

    # Send POST request
    response = client.post("/api/v1/expenses/", json=payload)

    # Assert success
    assert response.status_code == 200

    # Parse response JSON
    data = response.json()

    # Validate response content
    assert data["message"] == "Expense created successfully"
    assert data["id"] == 1


# Test: GET after creating expense
def test_get_expenses_after_create(temp_csv_file):
    
    """
    Test GET after adding an expense
    """

    payload = {
        "title": "Lunch",
        "amount": 100,
        "category": "Food",
        "date": "2025-01-02"
    }

    # First create expense
    client.post("/api/v1/expenses/", json=payload)

    # Then fetch expenses
    response = client.get("/api/v1/expenses/")

    # Check status
    assert response.status_code == 200

    # Parse response
    data = response.json()

    # Validate data
    assert len(data) == 1
    assert data[0]["title"] == "Lunch"


# Test: Invalid amount (negative)
def test_create_expense_invalid_amount(temp_csv_file):
    
    """
    Test validation: amount must be > 0
    """

    payload = {
        "title": "Invalid Expense",
        "amount": -50,  # Invalid value
        "category": "Misc",
        "date": "2025-01-01"
    }

    # Send POST request
    response = client.post("/api/v1/expenses/", json=payload)

    # Expect validation error (422 Unprocessable Entity)
    assert response.status_code == 422


# Test: Missing required fields
def test_create_expense_missing_field(temp_csv_file):
    
    """
    Test validation: missing required field
    """

    payload = {
        "title": "Incomplete Expense",
        "amount": 100
        # Missing category and date
    }

    # Send POST request
    response = client.post("/api/v1/expenses/", json=payload)

    # Expect validation error
    assert response.status_code == 422
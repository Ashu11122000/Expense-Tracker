# Import BaseSettings from Pydantic
# BaseSettings is a special class used to read environment variables
# and automatically map them to Python variables
from pydantic_settings import BaseSettings

# Create a Settings class that inherits from BaseSettings
# This class will automatically read values from environment variables
class Settings(BaseSettings):
    """
    This class loads environment variables from .env file
    and makes them accessible throughout the project.
    """
    
    # Defines a variable 'app_name' of type string
    # Pydantic will look for an environment variable named APP_NAME
    # Assign its value to this variable
    app_name: str
    
    # Defines a variable 'debug' of type boolean
    # It will read DEBUG = True/False from the .env file
    # and automatically convert it into a Python boolean
    debug: bool
    
    # Defines a variable 'csv_file_path' of type string
    # It will read CSV_FILE_PATH from the .env file
    csv_file_path: str
    
    # Inner Config class used to customize behavior of BaseSettings
    class Config:
        
        # Tells Pydantic to load environment variables from a file named ".env"
        env_file = ".env"
    
# Creates an instance of Settings class
# When this line runs:
# 1. It reads the .env file
# 2. Fetches all required variables
# 3. Validates their types (str, bool, etc.)
# 4. Stores them in "settings" object
settings = Settings()
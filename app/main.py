# Import FastAPI → main framework to build APIs
from fastapi import FastAPI

# Import CORS middleware → allows frontend (React, etc.) to call backend
from fastapi.middleware.cors import CORSMiddleware

# Import api_router → contains all grouped routes (expenses, etc.)
from app.api.v1.api import api_router

# Import settings → loads values from .env (app name, debug, etc.)
from app.core.config import settings


# Create FastAPI app instance
# This is the main entry point of your backend
app = FastAPI(
    
    # Title of your API (visible in Swagger UI)
    title=settings.app_name,
    
    # Debug mode (True → shows detailed errors, False → production safe)
    debug=settings.debug
)


# Add CORS (Cross-Origin Resource Sharing) middleware
# This allows frontend apps (running on different ports/domains)
# to communicate with your backend
app.add_middleware(
    
    CORSMiddleware,
    
    # Allow all origins
    allow_origins=["*"],
    
    # Allow cookies/auth headers
    allow_credentials=True,
    
    # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_methods=["*"],
    
    # Allow all headers
    allow_headers=["*"],
)


# Include all API routes
# prefix="/api/v1" → adds versioning to your API
app.include_router(
    api_router,
    prefix="/api/v1"
)
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')  # No default value
    ADMIN_API_KEY = os.getenv('ADMIN_API_KEY')    # No default value

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')  
    ADMIN_API_KEY = os.getenv('ADMIN_API_KEY')    
    HOST=os.getenv('HOST')
    DATABASE=os.getenv('DATABASE')
    USER=os.getenv('USER')
    PASSWORD=os.getenv('PASSWORD')

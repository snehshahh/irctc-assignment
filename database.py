import psycopg2
from config import Config
def get_db_connection():
    conn = psycopg2.connect(
            host=Config.HOST,
            database=Config.DATABASE,
            user=Config.USER,
            password=Config.PASSWORD)
    return conn

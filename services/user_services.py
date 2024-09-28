import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from database import get_db_connection
from models import User
import psycopg2

class AuthService:
    @staticmethod
    def register_user(user: User):
        if not user.username or not user.password:
            raise ValueError('Missing username or password')
        
        hashed_password = generate_password_hash(user.password)

        conn = get_db_connection()
        cur = conn.cursor()

        try:
            cur.execute("""
                INSERT INTO users (username, password, email, role) 
                VALUES (%s, %s, %s, %s) RETURNING user_id
            """, (user.username, hashed_password, user.email, user.role))
    
            new_user_id = cur.fetchone()[0]

            if user.role.lower() == 'admin':
                admin_key = str(uuid.uuid4()) 
                cur.execute("""
                    INSERT INTO admin_keys (admin_key, user_id) 
                    VALUES (%s, %s)
                """, (admin_key, new_user_id))

            conn.commit()
            return {'message': 'User registered successfully.Please Login To Continue'}

        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            raise ValueError('Username or email already exists')

        finally:
            cur.close()
            conn.close()

    @staticmethod
    def login(user: User):
        if not user.username or not user.password:
            raise ValueError('Username and password are required')

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT user_id, username, password, role FROM users WHERE username = %s", (user.username,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()

        if not user_data:
            raise ValueError('Invalid username or password')

        stored_password = user_data[2]
        if not check_password_hash(stored_password, user.password):
            raise ValueError('Invalid username or password')

        user_role = user_data[3]
        if user_role.lower() != 'admin' and user.role.lower() == 'admin':
            raise ValueError('Unauthorized access. You must be an admin to login. Try a different role')

        access_token = create_access_token(identity={'user_id': user_data[0], 'username': user_data[1], 'role': user_role})
        return {'access_token': access_token}

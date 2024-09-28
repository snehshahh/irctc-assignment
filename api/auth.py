from flask import Blueprint, request, jsonify
from services.user_services import AuthService
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/user/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = User(
        username=data.get('username'),
        password=data.get('password'),
        email=data.get('email'),
        role=data.get('role', 'User')
    )
    try:
        result = AuthService.register_user(user)
        return jsonify(result), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/user/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User(
        username=data.get('username'),
        password=data.get('password'),
        email=data.get('password'),
        role=data.get('role')
    )
    try:
        result = AuthService.login(user)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Train
from config import Config
from functools import wraps
from services.train_services import TrainService

trains_bp = Blueprint('trains', __name__)

def require_admin_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = request.get_json()
        api_key = data.get('api_key')

        #Also Possible via headers
        #api_key = request.headers.get('X-API-Key')

        if api_key != Config.ADMIN_API_KEY:
            return jsonify({'error': 'Unauthorized: Invalid Admin API key'}), 403
        
        return f(*args, **kwargs)
    
    return decorated_function

@trains_bp.route('/trains/add_train', methods=['POST'])
@require_admin_key  
@jwt_required()
def add_new_train():
    current_user = get_jwt_identity()
    user_role = current_user['role']

    if user_role != 'Admin':
        return jsonify({'error': 'Unauthorized access. Admins only.'}), 403

    data = request.get_json()
    train_name = data.get('train_name')
    source_station = data.get('source_station')
    destination_station = data.get('destination_station')
    total_seats = data.get('total_seats')

    if not train_name or not source_station or not destination_station or total_seats is None:
        return jsonify({'error': 'All fields are required'}), 400
    train = Train(
        train_name=train_name,
        source_station=source_station,
        destination_station=destination_station,
        total_seats=total_seats
    )

    try:
        TrainService.add_train(train)
        return jsonify({'message': 'Train added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@trains_bp.route('/trains/get_available_trains', methods=['GET'])
@jwt_required()
def get_available_trains():
    from_station = request.args.get('FromStation')
    to_station = request.args.get('ToStation')
    
    if not from_station or not to_station:
        return jsonify({'error': 'All fields are required'}), 400
    
    try:
        trains_available = TrainService.get_avaliable_trains(from_station, to_station)
        
        return jsonify([train.to_dict() for train in trains_available]), 200 
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
    

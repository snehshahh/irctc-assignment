from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.booking_services import BookingService
from models import BookingDetailsResponse

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/bookings/book_ticket', methods=['POST'])
@jwt_required()
def book_ticket_endpoint():
    data = request.get_json()
    train_id = data.get('train_id')
    no_of_seats = data.get('no_of_seats_required')

    if not train_id:
        return jsonify({'error': 'Train No is required'}), 400

    user_info = get_jwt_identity()
    result = BookingService.book_ticket(user_info, train_id, no_of_seats)

    if isinstance(result, dict):
        return jsonify(result), result.get('status_code', 500)

    return jsonify({
        'message': 'Seats booked successfully',
        'booking_id': result.booking_id,
        'seat_numbers': result.seat_numbers
    }), 200

@bookings_bp.route('/bookings/booking_details', methods=['GET'])
@jwt_required()
def booking_details():
    booking_id = request.args.get('BookingId')

    if not booking_id:
        return jsonify({'error': 'All fields are required'}), 400
    
    try:
        booking_details = BookingService.get_booking_details(booking_id)
        
        return jsonify([detail.to_dict() for detail in booking_details]), 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500



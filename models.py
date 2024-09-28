from database import get_db_connection

class User:
    def __init__(self, username, password,email,role):
        self.username = username
        self.password = password
        self.email = email
        self.role = role

class Train:
    def __init__(self, train_name, source_station,destination_station,total_seats):
        self.train_name = train_name
        self.source_station = source_station
        self.destination_station = destination_station
        self.total_seats = total_seats

class AvailableTrains:
    def __init__(self,train_id,train_name,no_of_seats_avaliable):
        self.train_id=train_id
        self.train_name=train_name
        self.no_of_seats_avaliable=no_of_seats_avaliable

    def to_dict(self):
        return {
            'train_id': self.train_id,
            'train_name': self.train_name,
            'no_of_seats_avaliable': self.no_of_seats_avaliable
        }
    
class BookingResponse:
     def __init__(self,message,booking_id,seat_numbers):
        self.message=message
        self.booking_id=booking_id
        self.seat_numbers=seat_numbers

class BookingDetailsResponse:
    def __init__(self,train_name,seat_number,status):
        self.train_name=train_name
        self.seat_number=seat_number
        self.status=status

    def to_dict(self):
        return {
            'train_name': self.train_name,
            'seat_number': self.seat_number,
            'status':self.status
        }
        


import threading
from database import get_db_connection
from models import BookingResponse
from models import BookingDetailsResponse
import uuid

class BookingService:
    booking_lock = threading.Lock()

    @staticmethod
    def book_ticket(user_info, train_id, no_of_seats_required):
        with BookingService.booking_lock:
            conn = get_db_connection()
            cur = conn.cursor()

            try:
                cur.execute("SELECT available_seats FROM trains WHERE train_id = %s FOR UPDATE", (train_id,))
                train = cur.fetchone()

                if not train:
                    return {'message': 'Train not found'}, 404

                available_seats = train[0]

                if available_seats <= 0:
                    return {'message': 'No available seats'}, 400
                
                if available_seats < no_of_seats_required:
                    return {'message': 'Required number of seats not available. Try a lesser number of seats.'}, 400

          
                booking_id = str(uuid.uuid4())

                seat_numbers = []
                for _ in range(no_of_seats_required):
                    seat_number = BookingService.get_next_available_seat(train_id, cur)
                    if seat_number is None:
                        return {'message': 'No available seats'}, 400
                    seat_numbers.append(seat_number)

       
                    cur.execute("""
                        INSERT INTO bookings (booking_id, user_id, train_id, seat_number, status) 
                        VALUES (%s, %s, %s, %s, 'booked')
                    """, (booking_id, user_info['user_id'], train_id, seat_number))

                new_available_seats = available_seats - no_of_seats_required
                cur.execute("UPDATE trains SET available_seats = %s WHERE train_id = %s", (new_available_seats, train_id))

                conn.commit()

                return BookingResponse(
                    message='Seats booked successfully',
                    booking_id=booking_id,
                    seat_numbers=seat_numbers 
                )

            except Exception as e:
                conn.rollback()
                return {'message': str(e)}, 500

            finally:
                cur.close()
                conn.close()

    @staticmethod
    def get_next_available_seat(train_id, cursor):
        cursor.execute("SELECT seat_number FROM bookings WHERE train_id = %s", (train_id,))
        booked_seats = {row[0] for row in cursor.fetchall()}

        total_seats = 100
        for seat_number in range(1, total_seats + 1):
            if seat_number not in booked_seats:
                return seat_number  

        return None

    @staticmethod
    def get_booking_details(booking_id):
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            booking_details=[]
            cur.execute("""
                SELECT  T.train_name,B.seat_number,B.status
                FROM public.bookings B 
                inner join trains T on B.train_id=T.train_id
                inner join users U  on B.user_id=U.user_id
                Where B.booking_id=%s
                ORDER BY booking_id ASC, seat_number ASC 
                """, (booking_id,))
            list=cur.fetchall()
            for i in range(0,len(list)):
                obj= BookingDetailsResponse(
                    train_name=list[i][0],
                    seat_number=list[i][1],
                    status=list[i][2]
                )
                obj.to_dict()
                booking_details.append(obj)
            return booking_details
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()
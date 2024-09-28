from models import Train,AvailableTrains
from database import get_db_connection

class TrainService:
    @staticmethod
    def add_train(train: Train):
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO trains (train_name, source_station, destination_station, total_seats, available_seats, created_at)
                VALUES (%s, %s, %s, %s, %s, NOW())
                """, (train.train_name, train.source_station, train.destination_station, train.total_seats, train.total_seats))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()
    
    @staticmethod
    def get_avaliable_trains(from_station,to_station):
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            available_trains=[]
            cur.execute("""
                select train_id,train_name,available_seats from trains
                where source_station= %s and destination_station= %s and available_seats>0 
                """, (from_station,to_station))
            list=cur.fetchall()
            for i in range(0,len(list)):
                obj= AvailableTrains(
                    train_id=list[i][0],
                    train_name=list[i][1],
                    no_of_seats_avaliable=list[i][2]
                )
                obj.to_dict()
                available_trains.append(obj)
            return available_trains
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close()
            conn.close()
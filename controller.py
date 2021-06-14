from model import Reservation
from app import db

def get_reservations():
    return Reservation.query.all()

def get_reservation(reservation_id):
    return Reservation.query.filter_by(ReservationID = reservation_id).first()

def create_reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate, ReservationName,ReservationLastName):
    reservation = Reservation(Passenger_ID=Passenger_ID, DepartureCity=DepartureCity, ArrivalCity=ArrivalCity,DepartureDate=DepartureDate,ReturnDate=ReturnDate,ReservationName=ReservationName,ReservationLastName=ReservationLastName)
    db.session.add(reservation)
    db.session.commit()

def update_post(reservation_id, Passenger_ID, DepartureCity, ArrivalCity,DepartureDate , ReturnDate, ReservationName,ReservationLastName):
    reserve= get_reservation(reservation_id)
    reserve.Passenger_ID= Passenger_ID
    reserve.DepartureCity=DepartureCity
    reserve.ArrivalCity=ArrivalCity
    reserve.DepartureDate=DepartureDate
    reserve.ReturnDate=ReturnDate
    reserve.ReservationName=ReservationName
    reserve.ReservationLastName=ReservationLastName
    db.session.commit()

def delete_post(reservation_id):
    reserve = get_reservation(reservation_id)
    db.session.delete(reserve)
    db.session.commit()
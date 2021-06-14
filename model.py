from app import db

db.create_all()

Passenger_to_Plane = db.Table('Passenger_to_Plane',
    db.Column('Plane_ID', db.Integer, db.ForeignKey('Plane.PlaneID'), primary_key=True),
    db.Column('Passenger_ID', db.Integer, db.ForeignKey('Passenger.PassengerID'), primary_key=True)
)


class Passenger(db.Model):
    __tablename__ = "Passenger"

    PassengerID = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.TEXT, nullable = False)
    Street = db.Column(db.VARCHAR, nullable = False)
    City = db.Column(db.TEXT, nullable = False)
    State = db.Column(db.TEXT, nullable = False)
    ZipCode =db.Column(db.Integer, nullable = False)
    Reservations = db.relationship("Reservation")

    def __repr__(self):
        return '<Passenger %r>' % self.Name


class Reservation(db.Model):
    __tablename__ = "Reservation"

    ReservationID = db.Column(db.Integer, primary_key = True)
    DepartureCity = db.Column(db.TEXT, nullable = False)
    ArrivalCity = db.Column(db.TEXT, nullable = False)
    DepartureDate = db.Column(db.String, nullable = False)
    ReturnDate = db.Column(db.String, nullable = False)
    ReservationName = db.Column(db.TEXT, nullable=False)
    ReservationLastName = db.Column(db.TEXT, nullable=False)
    Passenger_ID = db.Column(db.Integer, db.ForeignKey('Passenger.PassengerID'))

    def __repr__(self):
        return '<Reservation %r>' % self.ReservationName

class Plane(db.Model):
    __tablename__ = "Plane"

    PlaneID = db.Column(db.Integer, primary_key = True)
    PlaneSeats = db.Column(db.Integer, nullable = False)
    Passenger_to_Plane = db.relationship('Passenger', secondary=Passenger_to_Plane, lazy='subquery',
                           backref=db.backref('planes', lazy=True))



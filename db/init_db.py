import sqlite3

connection = sqlite3.connect('databas.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

#Passenger Data insertion
cur.execute("INSERT INTO Passenger(Name, Street, City, State, ZipCode) VALUES(?, ?, ?, ?, ?)", ('John','Nulla St.','Mankapo','Mississippi','96522'))
cur.execute("INSERT INTO Passenger(Name, Street, City, State, ZipCode) VALUES(?, ?, ?, ?, ?)", ('Iris','Ulllamcorper St.','Roseville','NH','11523'))
cur.execute("INSERT INTO Passenger(Name, Street, City, State, ZipCode) VALUES(?, ?, ?, ?, ?)", ('Theodore','Sit Rd.','Azusa','New York','39531'))
cur.execute("INSERT INTO Passenger(Name, Street, City, State, ZipCode) VALUES(?, ?, ?, ?, ?)", ('Kyla','Sodales Av.','Tamuning','PA','10855'))
cur.execute("INSERT INTO Passenger(Name, Street, City, State, ZipCode) VALUES(?, ?, ?, ?, ?)", ('Forrest','Integer Rd.','Corona','New Mexico','08219'))

#Reservation Data Insertion
cur.execute("INSERT INTO Reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate,  ReservationName, ReservationLastName) VALUES(?, ?, ?, ?, ?, ?, ?)",
            ('1','CTU','PEK', '6/7/2021','6/14/2021','John','Smith'))
cur.execute("INSERT INTO Reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate,  ReservationName, ReservationLastName) VALUES(?, ?, ?, ?, ?, ?, ?)",
            ('2', 'SHA','PEK', '7/20/2021','7/31/2021','Ashley','Tisdale'))
cur.execute("INSERT INTO Reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate,  ReservationName, ReservationLastName) VALUES(?, ?, ?, ?, ?, ?, ?)",
            ('3', 'PEK','CTU', '7/20/2021','','Bruno','Mars'))
cur.execute("INSERT INTO Reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate,  ReservationName, ReservationLastName) VALUES(?, ?, ?, ?, ?, ?, ?)",
            ('3', 'PEK','SHA', '8/20/2021','','Bruno','Mars'))
cur.execute("INSERT INTO Reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate,  ReservationName, ReservationLastName) VALUES(?, ?, ?, ?, ?, ?, ?)",
            ('4', 'PEK','SHA', '6/31/2021','7/31/2021','Dua','Lipa'))
cur.execute("INSERT INTO Reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate,  ReservationName, ReservationLastName) VALUES(?, ?, ?, ?, ?, ?, ?)",
            ('5', 'XIY','PEK', '10/01/2021','10/08/2021','Maria','Sanchez'))

#Plane Data Insertion
cur.execute("INSERT INTO Plane(PlaneSeats) VALUES(?)", ('300',))
cur.execute("INSERT INTO Plane(PlaneSeats) VALUES(?)", ('1000',))
cur.execute("INSERT INTO Plane(PlaneSeats) VALUES(?)", ('700',))
cur.execute("INSERT INTO Plane(PlaneSeats) VALUES(?)", ('100',))
cur.execute("INSERT INTO Plane(PlaneSeats) VALUES(?)", ('500',))


#Aircraft Data insertion
cur.execute("INSERT INTO Passenger_to_Plane(Plane_ID, Passenger_ID) VALUES(?, ?)", ('1','1'))
cur.execute("INSERT INTO Passenger_to_Plane(Plane_ID, Passenger_ID) VALUES(?, ?)", ('1','2'))
cur.execute("INSERT INTO Passenger_to_Plane(Plane_ID, Passenger_ID) VALUES(?, ?)", ('2','3'))
cur.execute("INSERT INTO Passenger_to_Plane(Plane_ID, Passenger_ID) VALUES(?, ?)", ('1','3'))
cur.execute("INSERT INTO Passenger_to_Plane(Plane_ID, Passenger_ID) VALUES(?, ?)", ('4','4'))

connection.commit()
connection.close()
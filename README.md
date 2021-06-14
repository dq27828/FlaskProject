# FlaskProject
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. 

# Installation
```bash
pip install -r requirements.txt
```
or
You just type the requirement libraries such as 

flask==2.0.1

flask_sqlalchemy

and you download them automatically.

# Usage
```python
import from flask import Flask, render_template, request, url_for, flash, redirect

return render_template('index.html') #returns the index template
return render_template('reserved.html', Reservation=Reservation) #returns the reserved template

```
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/databas.db'
db = SQLAlchemy(app) 
```

# Parts of the code
```python
return Reservation.query.all() #this method finds all the reservations and with the help of a route
@app.route('/reserved')
Reservation = controller.get_reservations() #gets the reservations and displays them
```
```python
return Reservation.query.filter_by(ReservationID = reservation_id).first() #this method finds the reservation based on the id and with the help of a route
def get_reservation(reservation_id):
    return Reservation.query.filter_by(ReservationID = reservation_id).first() #gets the reservations and displays them
```
```python
reservation = Reservation(..attributes..)
    db.session.add(reservation) #this method finds the reservation based on the id and with the help of a route
def get_reservation(reservation_id):
    return Reservation.query.filter_by(ReservationID = reservation_id).first() #gets the reservations and displays them
```
```python
return Reservation.query.filter_by(ReservationID = reservation_id).first() #this method adds a reservation
@app.route('/create', methods=('GET', 'POST'))
def create():
    controller.create_reservation(..attributes..)
    return redirect(url_for('index')) #this method adds the reservation with the help of attributes and redirects the index page
```
```python
def edit(ReservationID):
    Reservation = controller.get_reservation(ReservationID) #with the help of the previous method it takes the reservation based on the id
controller.update_post(..attributes..)
            return redirect(url_for('index')) #updates the reservation with the help of the update_post method and redirects the index page
def update_post(..attributes..):
```
```python
def delete_post(reservation_id): #this method takes the reservation id and deletes it
    reserve = get_reservation(reservation_id)
    db.session.delete(reserve) 
    
@app.route('/<int:ReservationID>/delete', methods=('POST',)) #the route
def delete(ReservationID):
    controller.delete_post(ReservationID)
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

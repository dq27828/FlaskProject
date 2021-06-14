import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect, Response
from werkzeug.exceptions import abort
from flask_sqlalchemy import SQLAlchemy
import controller

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/databas.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reserved')
def reserved():
    Reservation = controller.get_reservations()
    return render_template('reserved.html', Reservation=Reservation)

@app.route('/<int:reserve_id>')
def reserve(reserve_id):
    reservation = controller.get_reservation(reserve_id)
    return render_template('reservation.html', Reservation=reservation)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        Passenger_ID = request.form['Passenger_ID']
        DepartureCity = request.form['DepartureCity']
        ArrivalCity = request.form['ArrivalCity']
        DepartureDate = request.form['DepartureDate']
        ReturnDate = request.form['ReturnDate']
        ReservationName = request.form['ReservationName']
        ReservationLastName = request.form['ReservationLastName']

        if not Passenger_ID:
            flash('Passenger ID is required!')
        else:
            controller.create_reservation(Passenger_ID, DepartureCity, ArrivalCity, DepartureDate, ReturnDate, ReservationName,ReservationLastName)
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:ReservationID>/edit', methods=('GET', 'POST'))
def edit(ReservationID):
    Reservation = controller.get_reservation(ReservationID)

    if request.method == 'POST':
        Passenger_ID = request.form['Passenger_ID']
        DepartureCity = request.form['DepartureCity']
        ArrivalCity = request.form['ArrivalCity']
        DepartureDate = request.form['DepartureDate']
        ReturnDate = request.form['ReturnDate']
        ReservationName = request.form['ReservationName']
        ReservationLastName = request.form['ReservationLastName']
        if not Passenger_ID:
            flash('Passenger ID is required!')
        else:
            controller.update_post(ReservationID, Passenger_ID, DepartureCity, ArrivalCity,DepartureDate , ReturnDate, ReservationName,ReservationLastName)
            return redirect(url_for('index'))

    return render_template('edit.html', Reservation=Reservation)

@app.route('/<int:ReservationID>/delete', methods=('POST',))
def delete(ReservationID):
    controller.delete_post(ReservationID)
    flash('"{}" was successfully deleted!'.format(ReservationID))
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run()

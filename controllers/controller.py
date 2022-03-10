from flask import render_template, request
from app import app
from models.event_list import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['post'])
def add_event():
    event_date = request.form['date']
    event_name = request.form["name of event"]
    event_guest_no = request.form["number of guests"]
    event_room_location = request.form["room location"]
    event_description = request.form['description']
    event_recurring_status = request.form['recurring']
    event_recurring_period = request.form['recurring period']
    new_event = Event(event_date, event_name, event_guest_no, event_room_location, event_description, event_recurring_status, event_recurring_period)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)

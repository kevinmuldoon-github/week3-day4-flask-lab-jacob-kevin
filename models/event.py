class Event():

    def __init__(self,date, name_of_event, no_of_guests, room_location, description, recurring, recurring_period):
        self.date = date
        self.name_of_event = name_of_event
        self.no_of_guests = no_of_guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring
        self.recurring_period = recurring_period
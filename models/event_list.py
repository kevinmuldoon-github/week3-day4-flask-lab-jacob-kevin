from models.event import *



event1 = Event ("25 December 2021" , "Santa's Birthday" , 5000 , "North Pole" , "The party of the yea." , True, "Two Weeks")
event2 = Event ("1 January 2022" , "Hogmany" , 700 , "Edinburgh Castle" , "Tickets are not cheap" , False, "")
event3 = Event ("1 June 2022" , "Summertime" , 5000 , "Everywhere" , "Time for a swim" , True, "Yearly")
event4 = Event ("Saturday" , "No work!" , 5 , "New York" , "Put your feet up" , False, "")


events =[event1, event2, event3, event4]

def add_new_event (event):
    events.append(event)


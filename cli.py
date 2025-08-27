from models.models import Event, Attendee
from database import session
from datetime import datetime
def main_menu():
    while True:
        print("\n--- Event % Attendee Manager")
        print("1. Manage Events")
        print("2. Manage Attendees")
        print("3. Exit")

        choice = input("Choose an option:").strip()

        if choice == "1":
            manage_events()
        elif choice =="2":
            manage_attendees()
        elif choice =="3":
            print("Exiting...Ishiia, Enda Uza uji!")
            break
        else:
            print("Invalid choice bro! Acha ufala")

def manage_events():
    while True:
        print("\n--- Events Menu---")
        print("1. Create Event")
        print("2. View all Events")
        print("3.Delete Event")
        print("4. Back to Main Menu")
        
        choice = input("Choose an option mzee: ").strip()

        if choice == "1":
            create_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            break
        else:
            print("Invalid Choice. Try again ama chujaa!!")
def create_event():
    print("\n--- Create new Event---")
    title = input("Enter event title: ")
    venue= input("Enter venue: ")
    budget = int(input("Enter budget: "))

    date_str = input("Enter event date (YYYY-MM-DD): ")
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD Na uache ushamba!!")
        return
    
    time_str = input("Enter event time (HH:MM, optional): ")
    time_obj = None
    if time_str.strip():
        try:
            time_obj = datetime.strptime(time_str, "%H:%M")
        except ValueError:
            print("Invalid time format! Use HH:MM,Kwani haulearn!")
            return
    
    event = Event.create(title = title, venue=venue,budget=budget,
                         date=date_obj,time=time_obj)
    print(f"The {event.title} created successfully!")

def view_events():
        print("/n--- All Events---")
        events = Event.get_all()
        if not events:
            print("Labda utengeneze event yako...Msm")
            return
        for e in events:
            print(e)
def delete_event():
        id_ = input("Enter Event ID to delete: ")
        if Event.delete(int(id_)):
            print("Event deleted")
        else:
            print("Event not found")

def manage_attendees():
    while True:
        print("\n---Attendees Menu---")
        print("1. Create Attendee")
        print("2. View All Attendees")
        print("3. Delete Attendee")
        print("4. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_attendee()
        elif choice == "2":
            view_attendees()
        elif choice == "3":
            delete_attendee()
        elif choice == "4":
            break
        else:
            print("Invalid choice.Try again")
def create_attendee():
    print("\n--- Create New Attendee---")
    name = input("Enter Name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number:")

    events = Event.get_all()
    if not events:
        print("No events available.Tengeneza yako bana")
        return
    print("Select Event ID to assign attendee to:")
    for e in events:
        print(f"{e.id}. {e.title}")
    try:
        event_id = int(input("Enter event id:"))
    except ValueError:
        print("Invalid ID")
        return
    
    attendee = Attendee.create(name=name, email=email, phone_number=phone,
                               event_id=event_id)
    print(f"Attendee {attendee.name} created successfully")

def view_attendees():
        print("\n---All Attendees---")
        attendees = session.query(Attendee).all()
        if not attendees:
            print("No attendees found")
            return
        for a in attendees:
            print(a)
def delete_attendee():
        id_ = input("Enter Attendee ID to delete:")
        if Attendee.delete(int(id_)):
            print("Attendee deleted")
        else:
            print("Attendee not found")

if __name__ == "__main__":
    main_menu()
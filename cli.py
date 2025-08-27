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
            print("Exiting...Ishiia!")
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

    date_str = datetime.strptime(date_str,"%Y-%m-%d")
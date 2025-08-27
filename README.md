# Event Attendee Manager

A simple **Command-Line Interface (CLI) application** built with **Python** and **SQLAlchemy ORM** for managing events and their attendees.  

## Features
- **Events**
  - Create an event with title, venue, budget, date, and optional time
  - View all events
  - Delete an event
- **Attendees**
  - Create an attendee and assign them to an event
  - View all attendees
  - Delete an attendee
- **Menus**
  - Simple CLI menus to navigate between managing events and attendees
  - Input validation and helpful prompts

---

## Tech Stack
- Python 3.12+
- SQLAlchemy (ORM)
- SQLite (default database)

---

## Installation & Setup

1. **Clone the repository**
   ```bash

   git clone https://github.com/your-username/Event-Attendee-Manager.git

   cd Event-Attendee-Manager
2. Set Up a virtual environment 
    -pipenv install
    -pipenv shell

3. Initialize the database
    -python models/models.py
    
4. Run the application
    -python cli.py
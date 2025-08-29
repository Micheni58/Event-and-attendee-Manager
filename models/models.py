from sqlalchemy import String, Integer, ForeignKey, Column, DateTime, create_engine
from sqlalchemy.orm import relationship, validates
from database import base, session


class Event(base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    time = Column(DateTime, nullable=True)
    venue = Column(String, nullable=False)
    # budget is optional for now
    budget = Column(Integer, nullable=False)

    attendees = relationship("Attendee", back_populates="event", cascade="all, delete-orphan")
    tickets = relationship("Ticket", back_populates="event", cascade="all, delete-orphan")

    @validates("title", "venue")
    def validate_non_empty(self, key, value):
        if not value or not value.strip():
            raise ValueError(f"{key.capitalize()} is required.")
        return value.strip()

    @validates("budget")
    def validate_budget(self, key, value):
        if value is None:
            return None
        if not isinstance(value, int) or value < 0:
            raise ValueError("Budget must be a non-negative integer or leave it blank.")
        return value

    # ORM helpers
    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id_):
        return session.get(cls, id_)

    @classmethod
    def delete(cls, id_):
        obj = cls.find_by_id(id_)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True

    def __repr__(self):
        return f"Event #{self.id} {self.title} on {self.date} at {self.venue}"


class Attendee(base):
    __tablename__ = "attendees"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    event = relationship("Event", back_populates="attendees")

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Name is required!")
        return value.strip()

    @validates("email")
    def validate_email(self, key, value):
        if not value or "@" not in value:
            raise ValueError("Provide a valid email address")
        return value.strip()

    @validates("phone_number")
    def validate_phoneNo(self, key, value):
        if value:
            digits = "".join(ch for ch in value if ch.isdigit())
            if len(digits) < 7:
                raise ValueError("Phone number is too short")
        return value

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj

    @classmethod
    def find_by_id(cls, id_):
        return session.get(cls, id_)

    @classmethod
    def delete(cls, id_):
        obj = cls.find_by_id(id_)
        if obj:
            session.delete(obj)
            session.commit()
            return True

    def __repr__(self):
        return f"Attendee #{self.id} {self.name} ({self.email})"


class Ticket(base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    seat_number = Column(String, nullable=True)

    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    attendee_id = Column(Integer, ForeignKey("attendees.id"), nullable=True)

    event = relationship("Event", back_populates="tickets")
    attendee = relationship("Attendee")

    @validates("price")
    def validate_price(self, key, value):
        if value is None or not isinstance(value, int) or value < 0:
            raise ValueError("Price must be a non-negative integer.")
        return value

    def __repr__(self):
        return f"Ticket #{self.id} for Event {self.event_id} - Price: {self.price}"

    # FIXED: mark as classmethod
    @classmethod
    def create(cls, price, event_id):
        ticket = cls(price=price, event_id=event_id)
        session.add(ticket)
        session.commit()
        return ticket

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def delete(cls, id_):
        ticket = session.get(cls, id_)
        if ticket:
            session.delete(ticket)
            session.commit()
            return True
        return False


if __name__ == "__main__":
    from database import base, engine
    base.metadata.create_all(engine)

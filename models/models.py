from sqlalchemy import String,Integer,ForeignKey,Column,DateTime,create_engine
from sqlalchemy.orm import relationship,validates
from database import base,session

class Event(base):
    __tablename__ = "events"
    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    date = Column(DateTime , nullable= False)
    time = Column(DateTime, nullable=True)
    venue = Column(String,nullable=False)
    # budget is optional for now
    budget = Column(Integer, nullable=False)
    attendees = relationship("Attendee", back_populates="event",cascade="all, delete-orphan")
    
    @validates("title","venue")
    def validate_non_empty(self,key,value):
        if not value or not value.strip():
            raise ValueError(f"{key.capitalize} is required.")
        return value.strip()
    @validates("budget")
    def validate_budget(self,key,value):
        if value is None:
            return None
        if not isinstance(value,int) or value < 0:
            raise ValueError("Budget must be a non-negative integer or leave it blank.")
        return value
    
    # Below are the orm helpers
    @classmethod
    def create(cls,**kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    @classmethod
    def find_by_id(cls,id_):
        return session.get(cls, id_)
    @classmethod
    def delete(cls,id_):
        obj = cls.find_by_id(id_)
        if not obj:
            return False
        session.delete()
        session.commit()
        return True
    def __repr__(self):
        return f"<E"
    
class Attendee(base):
    __tablename__ = "Attendees"
    id = Column(Integer, primary_key = True)
    name = Column(String,nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)


if __name__ == "__main__":
    engine = create_engine("sqlite:///events.db")
    base.metadata.create_all(engine)
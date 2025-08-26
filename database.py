from sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy import create_engine
base = declarative_base()
engine = create_engine("sqlite:///events.db")
Session = sessionmaker(bind=engine)
session = Session()
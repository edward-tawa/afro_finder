from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import inspect

db_url = "mysql://root:password@localhost:3306/scholarship"

engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Scholarship(Base):
    __tablename__ = 'scholarships'
    id = Column(Integer, primary_key=True)
    name = Column(String(90))
    location = Column(String(80))
    about = Column(LONGTEXT)
    grantt = Column(String(80))
    deadline = Column(String(80))

Base.metadata.create_all(engine)

session.commit()
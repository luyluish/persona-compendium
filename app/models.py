from sqlalchemy import Column, Integer, String, Text, ARRAY
from .database import Base

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    arcana = Column(String)
    level = Column(Integer)
    description = Column(Text)
    image = Column(Text)
    strength = Column(Integer)
    magic = Column(Integer)
    endurance = Column(Integer)
    agility = Column(Integer)
    luck = Column(Integer)
    weak = Column(ARRAY(String))
    resists = Column(ARRAY(String))
    reflects = Column(ARRAY(String))
    absorbs = Column(ARRAY(String))
    nullifies = Column(ARRAY(String))
    dlc = Column(Integer)
    query = Column(String)
from sqlalchemy.orm import Session
from . import models, schemas

# Gets all personas from database
def get_personas(db: Session, skip: int = 0):
    return db.query(models.Persona).order_by(models.Persona.id).offset(skip).all()

# Gets one persona from database
def get_persona(db: Session, query: str):
    return db.query(models.Persona).filter(models.Persona.query == query).first()

def get_root(db: Session, skip: int = 0):
    return db.query(models.Persona.query).order_by(models.Persona.query).all()
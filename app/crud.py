from sqlalchemy.orm import Session
from . import models, schemas
from .utils import convert_name

# Gets all personas from database
def get_personas(db: Session, skip: int = 0):
    return db.query(models.Persona).order_by(models.Persona.id).offset(skip).all()

# Gets one persona from database
def get_persona(db: Session, query: str):
    return db.query(models.Persona).filter(models.Persona.query == query).first()
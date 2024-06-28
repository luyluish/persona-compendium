from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .utils import convert_name

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Persona Compendium",
    description="API for getting information about all the personas from Persona 3 Reload",
    version="v1",
    docs_url="/docs"
)

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Read all personas
@app.get("/personas/", response_model=list[schemas.Persona])
async def read_personas(skip: int = 0, db: Session = Depends(get_db)):
    personas = crud.get_personas(db, skip=skip)
    return personas

# Read specific persona
@app.get("/personas/{persona_name}", response_model=schemas.Persona)
async def read_persona(persona_name: str, db: Session = Depends(get_db)):
    persona = crud.get_persona(db, persona_name)
    if persona is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return persona
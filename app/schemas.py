from pydantic import BaseModel, Field
from typing import List

class Persona(BaseModel):
    id: int
    name: str = Field(..., exmaple="Orpheus")
    arcana: str = Field(..., exmaple="Fool")
    level: int = Field(..., exmaple=1)
    description: str = Field(..., exmaple="Some brief description about the persona.")
    image: str = Field(..., example="https://example.com/image.png")
    strength: int = Field(..., example=10)
    magic: int = Field(..., example=20)
    endurance: int = Field(..., example=15)
    agility: int = Field(..., example=30)
    luck: int = Field(..., example=25)
    weak: List[str] = Field(..., example=["Electric", "Dark"])
    resists: List[str] = Field(..., example=["Fire"])
    reflects: List[str] = Field(..., example=["Light"])
    absorbs: List[str] = Field(..., example=["Ice", "Strike"])
    nullifies: List[str] = Field(..., example=["Pierce"])
    dlc: int = Field(..., example=0)
    query: str = Field(..., example="orpheus")

    class Config:
        orm_mode = True
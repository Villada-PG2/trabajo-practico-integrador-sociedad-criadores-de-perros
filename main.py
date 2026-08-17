from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date
from typing import Optional

class Pais(BaseModel):
    nombre: str = Field(..., description="Nombre del pais")


class Ciudad(BaseModel):
    nombre: str = Field(..., description="Nombre de la ciudad")
    pais: Pais = Field(..., description="Pais al que pertenece la ciudad")


class Raza(BaseModel):
    nombre: str = Field(..., description="Nombre de la raza")
    descripcion: str = Field(..., description="Descripcion de la raza")
    paisOrigen: str = Field(..., description="Pais de origen de la raza")



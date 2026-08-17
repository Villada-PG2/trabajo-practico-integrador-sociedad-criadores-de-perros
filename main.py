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


class Persona(BaseModel):
    nombre: str = Field(..., description="Nombre de la persona")
    apellido: str = Field(..., description="Apellido de la persona")
    dni: str = Field(..., description="DNI de la persona")
    telefono: str = Field(..., description="Telefono de contacto")
    email: str = Field(..., description="Email de contacto")


class HistorialResponsable(BaseModel):
    fechaInicio: date = Field(..., description="Fecha de inicio del vinculo")
    fechaFin: Optional[date] = Field(default=None, description="Fecha de fin del vinculo, si ya finalizo")
    persona: Persona = Field(..., description="Persona responsable en este periodo")


class TipoObservacion(BaseModel):
    nombre: str = Field(..., description="Nombre del tipo de observacion")
    descripcion: str = Field(..., description="Descripcion del tipo de observacion")


class ObservacionSanitaria(BaseModel):
    fecha: date = Field(..., description="Fecha de la observacion")
    descripcion: str = Field(..., description="Descripcion de la observacion")
    implicaRestriccion: bool = Field(..., description="Si impide participar en concursos")
    tipo: TipoObservacion = Field(..., description="Tipo de observacion")
    realizador: Persona = Field(..., description="Persona que realizo la observacion")


class Perro(BaseModel):
    nombre: str = Field(..., description="Nombre del perro")
    fechaNacimiento: date = Field(..., description="Fecha de nacimiento")
    sexo: str = Field(..., description="Sexo del perro")
    raza: Raza = Field(..., description="Raza del perro")
    camadaOrigen: Optional["Camada"] = Field(default=None, description="Camada en la que nacio")
    listaHistorialResponsables: list[HistorialResponsable] = Field(..., description="Historial de responsables (1..*)")
    listaObservacionesSanitarias: list[ObservacionSanitaria] = Field(..., description="Historial sanitario (0..*)")


class PaternidadProbable(BaseModel):
    probabilidad: float = Field(..., description="Probabilidad de paternidad en porcentaje (0-100)")
    padreCandidato: Perro = Field(..., description="Perro candidato a padre")


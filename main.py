from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import date
from typing import Optional

PAISES = []
CIUDADES = []
RAZAS = []
PERSONAS = []
PERROS = []
TIPOS_CONCURSO = []
TIPOS_RECONOCIMIENTO = []
TIPOS_OBSERVACION = []
CONCURSOS = []
PARTICIPACIONES = []

class Pais(BaseModel):
    nombre: str = Field(..., description="Nombre del pais")


class Ciudad(BaseModel):
    nombre: str = Field(..., description="Nombre de la ciudad")
    pais: Pais = Field(..., description="Pais al que pertenece la ciudad")

    def getPais(self) -> Pais:
        return self.pais


class Raza(BaseModel):
    nombre: str = Field(..., description="Nombre de la raza")
    descripcion: str = Field(..., description="Descripcion de la raza")
    paisOrigen: str = Field(..., description="Pais de origen de la raza")

    def esDeRaza(self, nombre: str) -> bool:
        return self.nombre == nombre


class Persona(BaseModel):
    nombre: str = Field(..., description="Nombre de la persona")
    apellido: str = Field(..., description="Apellido de la persona")
    dni: str = Field(..., description="DNI de la persona")
    telefono: str = Field(..., description="Telefono de contacto")
    email: str = Field(..., description="Email de contacto")

    def getPerrosActualesACargo(self) -> list:
        perrosACargo = []
        for perro in PERROS:
            responsable = perro.getResponsableActual()
            if responsable is not None and responsable is self:
                perrosACargo.append(perro)
        return perrosACargo

class HistorialResponsable(BaseModel):
    fechaInicio: date = Field(..., description="Fecha de inicio del vinculo")
    fechaFin: Optional[date] = Field(default=None, description="Fecha de fin del vinculo, si ya finalizo")
    persona: Persona = Field(..., description="Persona responsable en este periodo")

    def esVigente(self) -> bool:
        return self.fechaFin is None

    def cerrarVinculacion(self, fechaFin: date):
        self.fechaFin = fechaFin


class TipoObservacion(BaseModel):
    nombre: str = Field(..., description="Nombre del tipo de observacion")
    descripcion: str = Field(..., description="Descripcion del tipo de observacion")


class ObservacionSanitaria(BaseModel):
    fecha: date = Field(..., description="Fecha de la observacion")
    descripcion: str = Field(..., description="Descripcion de la observacion")
    implicaRestriccion: bool = Field(..., description="Si impide participar en concursos")
    tipo: TipoObservacion = Field(..., description="Tipo de observacion")
    realizador: Persona = Field(..., description="Persona que realizo la observacion")

    def restriccionParticipacion(self) -> bool:
        return self.implicaRestriccion

    def estaVigente(self) -> bool:
        return self.implicaRestriccion

class Perro(BaseModel):
    nombre: str = Field(..., description="Nombre del perro")
    fechaNacimiento: date = Field(..., description="Fecha de nacimiento")
    sexo: str = Field(..., description="Sexo del perro")
    raza: Raza = Field(..., description="Raza del perro")
    camadaOrigen: Optional["Camada"] = Field(default=None, description="Camada en la que nacio")
    listaHistorialResponsables: list[HistorialResponsable] = Field(default_factory=list, description="Historial de responsables (1..*)")
    listaObservacionesSanitarias: list[ObservacionSanitaria] = Field(default_factory=list, description="Historial sanitario (0..*)")

    @field_validator("listaHistorialResponsables")
    @classmethod
    def validarHistorialInicial(cls, value):
        if not value:
            raise ValueError("Un perro debe registrarse con al menos un responsable inicial.")
        return value

    def getResponsableActual(self) -> Optional[Persona]:
        for historial in self.listaHistorialResponsables:
            if historial.esVigente():
                return historial.persona
        return None

    def registrarCambioResponsable(self, persona: Persona, fechaInicio: date):
        for historial in self.listaHistorialResponsables:
            if historial.esVigente():
                historial.cerrarVinculacion(fechaInicio)
                break
        self.listaHistorialResponsables.append(HistorialResponsable(fechaInicio=fechaInicio, persona=persona))

    def registrarObservacionSanitaria(self, fecha: date, descripcion: str, tipo: TipoObservacion, realizador: Persona, implicaRestriccion: bool) -> ObservacionSanitaria:
        nuevaObservacion = ObservacionSanitaria(
            fecha=fecha,
            descripcion=descripcion,
            implicaRestriccion=implicaRestriccion,
            tipo=tipo,
            realizador=realizador,
        )
        self.listaObservacionesSanitarias.append(nuevaObservacion)
        return nuevaObservacion

    def tieneRestriccionVigente(self) -> bool:
        for obs in self.listaObservacionesSanitarias:
            if obs.estaVigente():
                return True
        return False

    def getParticipaciones(self) -> list["Participacion"]:
            lista_resultado = []
            for participacion in PARTICIPACIONES:
                if participacion.perro is self:
                    lista_resultado.append(participacion)
                    
            return lista_resultado

class PaternidadProbable(BaseModel):
    probabilidad: float = Field(..., description="Probabilidad de paternidad en porcentaje (0-100)")
    padreCandidato: Perro = Field(..., description="Perro candidato a padre")

    @field_validator("probabilidad")
    @classmethod
    def validarProbabilidad(cls, value: float):
        if value < 0 or value > 100:
            raise ValueError("La probabilidad debe estar entre 0 y 100.")
        return value

    def getProbabilidad(self) -> float:
        return self.probabilidad

    def getPadreCandidato(self) -> Perro:
        return self.padreCandidato

    
class Camada(BaseModel):
    fechaNacimiento: date = Field(..., description="Fecha de nacimiento de la camada")
    cantidadCachorros: int = Field(..., description="Cantidad de cachorros de la camada")
    madre: Perro = Field(..., description="Perro madre de la camada")
    listaPaternidades: list[PaternidadProbable] = Field(..., description="Padres probables con su probabilidad (0..*)")

    @model_validator(mode="after")
    def validarSumaProbabilidades(self):
        suma = sum(paternidad.probabilidad for paternidad in self.listaPaternidades)
        if suma > 100:
            raise ValueError("La suma de probabilidades de paternidad no puede superar el 100%.")
        return self

    def getMadre(self) -> Perro:
        return self.madre

    def getCachorros(self) -> list[Perro]:
        return [perro for perro in PERROS if perro.camadaOrigen is self]

    def getPadresProbables(self) -> list[PaternidadProbable]:
        return self.listaPaternidades


Perro.model_rebuild()

class TipoConcurso(BaseModel):
    nombre: str = Field(..., description="Nombre del tipo de concurso")
    descripcion: str = Field(..., description="Descripcion del tipo de concurso")


class TipoReconocimiento(BaseModel):
    nombre: str = Field(..., description="Nombre del reconocimiento")
    descripcion: str = Field(..., description="Descripcion del reconocimiento")
    nivel: int = Field(..., description="Nivel/jerarquia del reconocimiento")

    def tieneNivel(self) -> bool:
        return self.nivel > 0

    def esAusenciaDeCalificacion(self) -> bool:
        return self.nivel == 0

class Participacion(BaseModel):
    fecha: date = Field(..., description="Fecha de la participacion")
    perro: Perro = Field(..., description="Perro participante")
    reconocimiento: TipoReconocimiento = Field(..., description="Reconocimiento obtenido")

    def tieneCalificacion(self) -> bool:
        return not self.reconocimiento.esAusenciaDeCalificacion()

    def getReconocimiento(self) -> TipoReconocimiento:
        return self.reconocimiento


class Concurso(BaseModel):
    nombre: str = Field(..., description="Nombre del concurso")
    fecha: date = Field(..., description="Fecha de realizacion")
    frecuencia: str = Field(..., description="Frecuencia del concurso")
    tipoConcurso: TipoConcurso = Field(..., description="Tipo de concurso")
    ciudad: Ciudad = Field(..., description="Ciudad donde se realiza")
    listaParticipaciones: list[Participacion] = Field(..., description="Participaciones registradas (0..*)")

    def registrarParticipacion(self, perro: Perro, reconocimiento: TipoReconocimiento, fecha: Optional[date] = None) -> Participacion:
        nuevaParticipacion = Participacion(
            fecha=fecha if fecha is not None else self.fecha,
            perro=perro,
            reconocimiento=reconocimiento,)
        self.listaParticipaciones.append(nuevaParticipacion)
        PARTICIPACIONES.append(nuevaParticipacion)
        return nuevaParticipacion

    def getParticipantes(self) -> list[Perro]:
        return [participacion.perro for participacion in self.listaParticipaciones]

    @classmethod
    def filtrarPorCiudad(cls, ciudad: Ciudad) -> list["Concurso"]:
        return [concurso for concurso in CONCURSOS if concurso.ciudad is ciudad]

    @classmethod
    def filtrarPorPais(cls, pais: Pais) -> list["Concurso"]:
        return [concurso for concurso in CONCURSOS if concurso.ciudad.pais is pais]


if __name__ == "__main__":

    argentina = Pais(nombre="Argentina")
    PAISES.append(argentina)
    cordoba = Ciudad(nombre="Cordoba", pais=argentina)
    CIUDADES.append(cordoba)
    labrador = Raza(nombre="Labrador Retriever", descripcion="Raza de caza y compania", paisOrigen="Canada")
    RAZAS.append(labrador)
    ana = Persona(nombre="Ana", apellido="Gomez", dni="30111222", telefono="3511234567", email="ana@gmail.com")
    luis = Persona(nombre="Luis", apellido="Perez", dni="28999888", telefono="3517654321", email="luis@gmail.com")
    PERSONAS.extend([ana, luis])
    madre = Perro(
        nombre="Luna", fechaNacimiento=date(2020, 3, 10), sexo="Hembra", raza=labrador,
        listaHistorialResponsables=[HistorialResponsable(fechaInicio=date(2020, 5, 1), persona=ana)],
    )
    padre = Perro(
        nombre="Rocky", fechaNacimiento=date(2019, 6, 20), sexo="Macho", raza=labrador,
        listaHistorialResponsables=[HistorialResponsable(fechaInicio=date(2019, 8, 1), persona=luis)],
    )
    PERROS.extend([madre, padre])
    camada1 = Camada(
        fechaNacimiento=date(2023, 1, 15),
        cantidadCachorros=1,
        madre=madre,
        listaPaternidades=[PaternidadProbable(probabilidad=80, padreCandidato=padre)],
    )
    cachorro = Perro(
        nombre="Toby", fechaNacimiento=date(2023, 1, 15), sexo="Macho", raza=labrador,
        camadaOrigen=camada1,
        listaHistorialResponsables=[HistorialResponsable(fechaInicio=date(2023, 3, 1), persona=ana)],
    )
    PERROS.append(cachorro)

    print(f"Cachorros de la camada: {[p.nombre for p in camada1.getCachorros()]}")
    print(f"Padres probables: {[(pp.padreCandidato.nombre, pp.probabilidad) for pp in camada1.getPadresProbables()]}")
    print(f"Responsable actual de Toby: {cachorro.getResponsableActual().nombre}")
    cachorro.registrarCambioResponsable(luis, date(2024, 1, 10))
    print(f"Nuevo responsable actual de Toby: {cachorro.getResponsableActual().nombre}")
    print(f"Perros a cargo de Luis: {[p.nombre for p in luis.getPerrosActualesACargo()]}")
    displasia = TipoObservacion(nombre="Control clinico", descripcion="Chequeo general")
    TIPOS_OBSERVACION.append(displasia)
    cachorro.registrarObservacionSanitaria(
        fecha=date(2024, 2, 1), descripcion="Displasia de cadera leve",
        tipo=displasia, realizador=ana, implicaRestriccion=True,
    )
    print(f"Toby tiene restriccion vigente: {cachorro.tieneRestriccionVigente()}")

    expo = TipoConcurso(nombre="Exposicion", descripcion="Exposicion de raza")
    TIPOS_CONCURSO.append(expo)
    mejorDeRaza = TipoReconocimiento(nombre="Mejor de Raza", descripcion="Primer puesto por raza", nivel=1)
    sinCalificar = TipoReconocimiento(nombre="Sin calificar", descripcion="No obtuvo puntaje", nivel=0)
    TIPOS_RECONOCIMIENTO.extend([mejorDeRaza, sinCalificar])

    concurso1 = Concurso(
        nombre="Expo Cordoba 2026", fecha=date(2026, 9, 5), frecuencia="Anual",
        tipoConcurso=expo, ciudad=cordoba,
    )
    CONCURSOS.append(concurso1)

    concurso1.registrarParticipacion(perro=madre, reconocimiento=mejorDeRaza)
    concurso1.registrarParticipacion(perro=padre, reconocimiento=sinCalificar)

    print(f"Participantes del concurso: {[p.nombre for p in concurso1.getParticipantes()]}")
    print(f"Participaciones de Luna: {[p.reconocimiento.nombre for p in madre.getParticipaciones()]}")
    print(f"Concursos en Cordoba: {[c.nombre for c in Concurso.filtrarPorCiudad(cordoba)]}")
    print(f"Concursos en Argentina: {[c.nombre for c in Concurso.filtrarPorPais(argentina)]}")

    try:
        PaternidadProbable(probabilidad=150, padreCandidato=padre)
    except ValueError as error:
        print(f"Error esperado (probabilidad invalida): {error}")

    try:
        Camada(
            fechaNacimiento=date(2024, 1, 1), cantidadCachorros=2, madre=madre,
            listaPaternidades=[
                PaternidadProbable(probabilidad=70, padreCandidato=padre),
                PaternidadProbable(probabilidad=50, padreCandidato=padre),
            ],
        )
    except ValueError as error:
        print(f"Error esperado (suma de probabilidades > 100%): {error}")

    try:
        Perro(nombre="SinResponsable", fechaNacimiento=date(2024, 1, 1), sexo="Macho", raza=labrador)
    except ValueError as error:
        print(f"Error esperado (perro sin responsable inicial): {error}")

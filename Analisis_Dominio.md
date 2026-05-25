# Análisis de Requerimientos — Sociedad Criadores de Perros

---
# Entradas y Salidas

## Entradas

1. Datos del perro: Nombre, fecha de nacimiento, sexo, raza.
2. Datos de raza: Nombre, descripción, país de origen.
3. Datos de cruce reproductivo: Hembra involucrada, machos candidatos, fecha del cruce.
4. Registro de camada: Fecha de nacimiento, cantidad de cachorros, madre, padres probables con probabilidades.
5. Datos del responsable: Nombre, apellido, DNI, teléfono, email.
6. Asignación de responsable: Perro, persona, fecha de inicio.
7. Datos de concurso: Nombre, fecha de realización, ciudad, tipo de concurso.
8. Datos de ciudad: Nombre de ciudad, nombre de país.
9. Participación en concurso: Perro, concurso, reconocimiento obtenido.
10. Registro sanitario: Fecha, descripción, tipo de observación, perro, persona que la realiza, si implica restricción.

## Salidas

1. Ficha del perro: Información completa del perro.
2. Árbol genealógico: Madre y padres probables con sus respectivas probabilidades de paternidad.
3. Historial de responsables: Lista de responsables que estuvieron a cargo de un mismo perro en distintas fechas.
4. Responsable actual: Persona que esta actualmente a cargo del perro.
5. Historial de participaciones: Registro de las competencias de las que el perro formó parte.
6. Resultados de concurso: Lista con el desempeño de cada perro en las distintas competencias.
7. Historial sanitario: Registro de las observaciones medicas hechas sobre un perro, ordenadas cronológicamente.
8. Perros con restricción sanitaria: Lista de perros con observaciones que impiden su participación en eventos.
9. Listado de concursos: Concursos filtrados por ciudad, país o fecha.
10. Perros a cargo por persona: Listado de perros actuales o históricos bajo responsabilidad de una persona.

---

# Frontera

## ¿Que incluye el sistema?

1. Gestión de perros de raza y su información individual.
2. Registro de cruces reproductivos y camadas con paternidad probabilística.
3. Gestión de responsables y su historial de vinculación con cada perro.
4. Registro y consulta de concursos caninos y sus participantes.
5. Registro de observaciones sanitarias y su impacto en la participación en eventos.

## ¿Que se excluye del sistema?

1. Gestión financiera (venta, compra o valuación de cachorros).
2. Gestión clínica veterinaria completa (diagnósticos, tratamientos, etc).
3. Gestión de contratos de acuerdos entre criadores.
4. Comunicación externa (notificaciones, correos, publicaciones en redes).
5. Inscripción automática a concursos.

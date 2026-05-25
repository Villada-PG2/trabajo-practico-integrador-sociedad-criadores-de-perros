# **Análisis de Requerimientos — Sociedad Criadores de Perros**

---
# **Entradas y Salidas**

## _**Entradas**_

1. **Datos del perro:** Nombre, fecha de nacimiento, sexo, raza.
2. **Datos de raza:** Nombre, descripción, país de origen.
3. **Datos de cruce reproductivo:** Hembra involucrada, machos candidatos, fecha del cruce.
4. **Registro de camada:** Fecha de nacimiento, cantidad de cachorros, madre, padres probables con probabilidades.
5. **Datos del responsable:** Nombre, apellido, DNI, teléfono, email.
6. **Asignación de responsable:** Perro, persona, fecha de inicio.
7. **Datos de concurso:** Nombre, fecha de realización, ciudad, tipo de concurso.
8. **Datos de ciudad:** Nombre de ciudad, nombre de país.
9. **Participación en concurso:** Perro, concurso, reconocimiento obtenido.
10. **Registro sanitario:** Fecha, descripción, tipo de observación, perro, persona que la realiza, si implica restricción.

## _**Salidas**_

1. **Ficha del perro:** Información completa del perro.
2. **Árbol genealógico:** Madre y padres probables con sus respectivas probabilidades de paternidad.
3. **Historial de responsables:** Lista de responsables que estuvieron a cargo de un mismo perro en distintas fechas.
4. **Responsable actual:** Persona que esta actualmente a cargo del perro.
5. **Historial de participaciones:** Registro de las competencias de las que el perro formó parte.
6. **Resultados de concurso:** Lista con el desempeño de cada perro en las distintas competencias.
7. **Historial sanitario:** Registro de las observaciones medicas hechas sobre un perro, ordenadas cronológicamente.
8. **Perros con restricción sanitaria:** Lista de perros con observaciones que impiden su participación en eventos.
9. **Listado de concursos:** Concursos filtrados por ciudad, país o fecha.
10. **Perros a cargo por persona:** Listado de perros actuales o históricos bajo responsabilidad de una persona.

---

# **Frontera y Alcances**

## _**Frontera**_

### **¿Que incluye el sistema?**

1. **Gestión de perros de raza y su información individual.**
2. **Registro de cruces reproductivos y camadas con paternidad probabilística.**
3. **Gestión de responsables y su historial de vinculación con cada perro.**
4. **Registro y consulta de concursos caninos y sus participantes.**
5. **Registro de observaciones sanitarias y su impacto en la participación en eventos.**

### **¿Que se excluye del sistema?**

1. **Gestión financiera** (venta, compra o valuación de cachorros).
2. **Gestión clínica veterinaria completa** (diagnósticos, tratamientos, etc).
3. **Gestión de contratos de acuerdos entre criadores.**
4. **Comunicación externa** (notificaciones, correos, publicaciones en redes).
5. **Inscripción automática a concursos.**

## _**Alcances**_

1. **Gestionar el padrón canino** registrar, consultar y actualizar la información de cada perro, incluyendo su raza, datos personales y camada de origen.
2. **Gestionar la reproducción:** registrar cruces entre machos y hembras, y dar una expectativa sobre las camadas donde la paternidad puede ser incierta y distribuida entre varios perros con distintos porcentajes de serlo.
3. **Gestionar la responsabilidad sobre los cachorros:** mantener un historial completo de personas vinculadas a cada perro, identificando quién es el responsable actual.
4. **Gestionar concursos y participaciones:** registrar las competiciones realizadas en distintas ciudades y países, junto con los resultados obtenidos por cada perro (calificaciones o ausencia en ellas).
5. **Gestionar el historial sanitario:** registrar observaciones de salud de cualquier origen o contexto, indicando si implican restricciones para la participación en actividades o competiciones.

---

# **Requerimientos Funcionales y No Funcionales**

## _**Requerimientos Funcionales**_

1. **El sistema debe permitir registrar perros con sus datos básicos:** nombre, fecha de nacimiento, sexo y raza.
2. **El sistema debe permitir registrar las razas:** nombre, descripción y país de origen.
3. **El sistema debe permitir registrar camadas:** madre, fecha de nacimiento y la lista de cachorros.
4. **El sistema debe permitir asociar padres probables a una camada, con una probabilidad de paternidad expresada en porcentaje.**
5. **El sistema debe permitir consultar el árbol de origen de un perro** (madre y padres probables con sus probabilidades).
6. **El sistema debe permitir registrar personas responsables con sus datos de contacto.**
7. **El sistema debe permitir asignar un responsable a un perro indicando la fecha de inicio con opción a fecha de fin.**
8. **El sistema debe permitir consultar el historial de responsables de un perro ordenado cronológicamente.**
9. **El sistema debe identificar el responsable actual de un perro.** 
10. **El sistema debe permitir registrar concursos:** nombre, fecha, frecuencia, país, ciudad y tipo de competencia.
11. **El sistema debe permitir registrar ciudades asociadas a un país.**
12. **El sistema debe permitir registrar la participación de un perro en un concurso y el reconocimiento obtenido, incluyendo la posibilidad de ausencia de calificación.**
13. **El sistema debe permitir consultar el historial de participaciones de un perro en concursos.**
14. **El sistema debe permitir filtrar concursos por ciudad o por país.**
15. **El sistema debe permitir registrar observaciones sanitarias sobre un perro:** fecha, descripción, tipo de observación, persona que la realiza, y si implica restricción de participación.
16. **El sistema debe permitir consultar el historial sanitario de un perro.**
17. **El sistema debe poder identificar qué perros tienen restricciones sanitarias vigentes que les impidan participar en concursos.**
18. **El sistema debe permitir listar todos los perros actualmente a cargo de una persona.**


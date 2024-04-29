class Profesor():
    #si dentro de una clase tenemos un def, es un mètodo
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email
        #el self serìa el equivalente a un this

    def dame_tu_nombre(self):
        return self.__nombre__


class Alumno():
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def falta(self):
        self.__inasistencias__ += 1

    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__ = la_dieta
    
    def es_vegano(self):
        self.__dieta__ = "vegano"
    
    def mentoria(self, profesor):
        self.__mentor__ = profesor

    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "NO ESTA LIBRE"

profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@gmail.com")

alumno_juan = Alumno("Juanito")
alumno_maria = Alumno("Maria")

los_alumnos = [alumno_juan, alumno_maria]

print(profe_elio.dame_tu_nombre())
print(profe_gabi.dame_tu_nombre())

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_maria.elegir_dieta_especial("vegana")
print(alumno_maria.__dieta__)
alumno_juan.es_vegano()
print(alumno_juan.__dieta__)
alumno_juan.mentoria(profe_elio)

print(alumno_juan.__mentor__)
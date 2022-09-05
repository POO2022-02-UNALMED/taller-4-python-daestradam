

from classroom.asignatura import Asignatura
#from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12" #None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        if asignaturas is None: #self._asignaturas = asignaturas
            self._asignaturas = []
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs): #kwargs
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = [alumno] #self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista + [alumno] #self.listadoAlumnos = [alumno] 

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
    """"
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
    """
    #creacion del metodo __str__
    def __str__(self):
        return "Grupo de estudiantes: grupo predeterminado"


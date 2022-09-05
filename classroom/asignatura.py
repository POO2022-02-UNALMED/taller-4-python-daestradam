class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    #Creaciones de metodo set, get y __str__   
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre

    def __str__(self):
        return self._nombre + " " + self._salon



import os 
from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera, turno):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera
        self.turno = turno




  

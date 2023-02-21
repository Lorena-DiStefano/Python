import os

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
       return f"{self.nombre} {self.apellido} {self.edad}"

    def info_persona(self):
       return f"\
        Nombre:   {self.nombre}\n\
        Apellido: {self.apellido}\n\
        Edad:     {self.edad}\n\
        Carrera:  {self.carrera}\n\
        Turno:    {self.turno}\n"
        



import os

class Planta:
    def __init__(self, nombre: str, flores: bool, ambiente: str):
        self.nombre = nombre
        self.flores = flores
        self.ambiente = ambiente


class Tallo(Planta):
    def __init__(self, nombre: str, flores: bool, ambiente: str,tallo:str):
        super().__init__(nombre, flores, ambiente)
        self.tallo= tallo
    
    def __str__(self):
        return f"\
          Nombre: {self.nombre}\n\
          Flores: {self.flores}\n\
          Tallo:  {self.tallo}\n\
          Ambiente: {self.ambiente}\n"

os.system('cls')

malvon = Tallo('Malvón',True,'interior','fino')

print(malvon)
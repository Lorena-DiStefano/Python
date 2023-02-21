from bandas import Banda
from autores import Autor
import os

class Cancion(Banda,Autor):
   def __init__(self,nombre_cancion:str, nombre_banda: str, origen: str, surge: int, estilo: str,nombre_autor:str,nacionalidad:str,rol:str):
      Banda.__init__(self,nombre_banda,origen,surge)
      Autor.__init__(self,nombre_autor,nacionalidad,rol)
      self.nombre_cancion = nombre_cancion 
      self.estilo = estilo

   def __str__ (self):
      return f"\
      Canción =            {self.nombre_cancion}\n\
      Estilo musical =     {self.estilo}\n\
      Nombre de la banda = {self.nombre_banda}\n\
      País de Origen =     {self.origen}\n\
      Surge en =           {self.surge}\n\
      Autor del tema =     {self.nombre_autor}\n\
      Nacionalidad =       {self.nacionalidad}\n\
      Rol en la Banda =    {self.rol}\n"
   

if __name__ == '__main__':
  os.system('cls')
  rapsody = Cancion('Bohemian Rapsody','Queen','Inglaterra',1970,'Rock & Opera','Freddy Mercury','Tanzano','Vocalista')

  print(f'\n{rapsody}')






  
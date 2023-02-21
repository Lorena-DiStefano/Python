import random
import time
import os

class tv:
    def __init__(self, modelo, marca, cant_canales, pulgadas, precio):
        self.modelo = modelo
        self.marca = marca
        self.cant_canales = cant_canales
        self.pulgadas = pulgadas
        self.precio = precio
        self.encendido = False
        self.volumen = 50
        self.canal = random.randint(1,cant_canales)
       
        # ctrl + alt + flecha arriba/abajo : tipear palabra ejemplo self.

    def __str__(self):
        return f"\
          Modelo:   {self.modelo}\n\
          Marca:    {self.marca}\n\
          Canales:  {self.cant_canales}\n\
          Pulgadas: {self.pulgadas}\n\
          Precio:   {self.precio}\n"

    def encender(self):
        time.sleep(1)
        if self.encendido == False:
            self.encendido = True
            print(f"La TV está encendida")
            return self.encendido
        else:
            self.encendido = False
            print(f"La TV está apagada")
            return self.encendido

    def cambiar_canal(self,canal_elegido):
        print(f"Canal inicial: {self.canal}")        
        if canal_elegido <= self.cant_canales and canal_elegido >0:
            if self.canal == canal_elegido:
                return "No es necesario cambiar de canal"
            else:
                self.canal = canal_elegido
                return f"Canal actual: {self.canal}"
        else:
            return f"El canal elegido no existe"
            
 #canal_elegido es exclusivo de def cambiar_canal por eso no lleva self, a diferencia de canal, que es un atributo de la clase

    def subir_volumen(self):
        time.sleep(1)
        if self.volumen >= 49:
            return "El volumen está al máximo"
        else:
            self.volumen +=1
            return f"Volúmen: {self.volumen}"

    def bajar_volumen(self):
        time.sleep(1)
        if self.volumen <=1:
            return "El volumen está en mínimo"
        else:
            self.volumen -=1
            return f"Volúmen: {self.volumen}"


if __name__=="__main__":
    
  os.system('cls')

  philco = tv("RT24", "Philco", 50, 24, 35000)
  print(philco)

  print(philco.encender())
  print(philco.encender())

  print(philco.cambiar_canal(50))

  print(philco.bajar_volumen())
  print(philco.bajar_volumen())
  print(philco.bajar_volumen())
  print(philco.bajar_volumen())

# Nota if__name__ == "__main__" 
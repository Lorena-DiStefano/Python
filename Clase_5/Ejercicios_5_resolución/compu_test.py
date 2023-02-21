import time
import os

class Computadora:
    def __init__(self, marca, modelo, ram, ssd, pulgadas, precio):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.ssd = ssd
        self.pulgadas = pulgadas
        self.precio = precio
        self.encendido = False
        self.pagina_web = 'Google' 
        
    def __str__(self):
        return f"\
         Marca:    {self.marca}\n\
         Modelo:   {self.modelo}\n\
         Ram:      {self.ram}\n\
         Ssd:      {self.ssd}\n\
         Pulgadas: {self.pulgadas}\n\
         Precio:   {self.precio}\n"

    def encender(self):
        time.sleep(1)
        if self.encendido == False:
            self.encendido = True
            print(f"\nLa Notebook está encendida")
            return self.encendido
        else:
            self.encendido = False
            print(f"\nLa Notebook está apagada")
            return self.encendido
        
    def bateria (self,status_bateria):
        if status_bateria <=15:
            return f"\nBatería: {status_bateria}\nConectar al cargador\n"
        elif status_bateria >15 or status_bateria <25:
            return f"\nBatería: {status_bateria}\nAtencion! La batería está por agotarse\n"       
        else:
            return f"\nBatería:{status_bateria}\nCarga suficiente\n"
        
    def navegar (self,pag_web_elegida):
        print (f"Página Web inicial: {self.pagina_web}")
        if pag_web_elegida == self.pagina_web:
            return f"\nYa está en la página elegida:{pag_web_elegida}\n"
        else:
            self.pagina_web == pag_web_elegida
            return f"\nAhora está en la página elegida:{pag_web_elegida}\n"
        

if __name__ == "__main__":
  os.system('cls')

  lenovo = Computadora('Lenovo', '15 G2', '8gb', 256, 15, 409000)

  print(lenovo)

  print(lenovo.encender())
  print(lenovo.encender())

  print(lenovo.bateria(20))
  print(lenovo.navegar('Google'))
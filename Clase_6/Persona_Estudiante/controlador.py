from estudiante import Estudiante
import os

if __name__ == "__main__":
    os.system('cls')
    
    alumno_a= Estudiante('Andrea','Delgado',32,'Diseño gráfico','tarde')
    print(alumno_a.info_persona())
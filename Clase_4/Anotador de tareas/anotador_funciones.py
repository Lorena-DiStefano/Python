from datetime import datetime
lista_tareas = {}


def agregar_tarea(diccionario: dict):

    nombre = input("Ingrese el nombre de la tarea: ").upper()
    if nombre in diccionario:
        print(f"\nEste tarea ya existe, intente con otro nombre.")
    else:
        detalle = input("Ingresa descripción: ")
        status = input("Ingrese el status: ")
        duedate = input("Ingrese la fecha límite: ")

        diccionario[nombre] = {
            'detalle': detalle, 'Status': status, 'duedate': duedate}

        print(f"Tarea guardada.\n")


def eliminar_tarea(diccionario: dict):

    nombre = input(
        "Ingrese el nombre de la tarea que quiera eliminar: ").upper()
    if nombre in diccionario:
        diccionario.pop(nombre)
    else:
        print(f"\nEl nombre ingresado no está en la lista de productos")

    print(f"\nTarea {nombre} eliminada")


def editar_tarea(diccionario: dict):
    nombre = input("Ingrese el nombre de la tarea: ").upper()
    if nombre not in diccionario:
        print(f"\nEste tarea no existe, intente con otro nombre.")
    else:
        detalle = input("Ingresa descripción: ")
        status = input("Ingrese el status: ")
        duedate = input("Ingrese la fecha límite: ")

        diccionario[nombre] = {
            'detalle': detalle, 'Status': status, 'duedate': duedate}
    
    print("Tarea modificada\n")


def listar_tareas(diccionario: dict):
    for clave, valor in diccionario.items():
        print(f"\n{clave}:")
        for a, b in valor.items():
            print(f"\t{a}: {b}")


def buscar_tarea(diccionario:dict):
    nombre = input("Introduzca un nombre a buscar: ").upper()
    if nombre in diccionario:
        print(f"\n{nombre.upper()}:\n")

        tarea = diccionario[nombre]
        for x, y in tarea.items():
            print(f"{x}: {y}")
    else:
        print(f"\nTarea no encontrada, intente con otro nombre")
    print("\n")
   


def mostrar_diccionario(diccionario: dict):
    print("\n")
    for x, y in diccionario.items():
        print(f"{x}. {y}")


def comprobar_opcion(opcion):

    if opcion >= 1 and opcion <= 6:
        if opcion == 1:
            agregar_tarea(lista_tareas)
            return False
        elif opcion == 2:
            eliminar_tarea(lista_tareas)
            return False
        elif opcion == 3:
            editar_tarea(lista_tareas)
            return False
        elif opcion == 4:
           listar_tareas(lista_tareas)
           return False
        elif opcion == 5:
            buscar_tarea(lista_tareas)       
            return False
        elif opcion == 6:
            print(f"\nLa app se ha cerrado correctamente!!\n")
            return True

        return True

    else:
        print(f"\n Opción incorrecta, por favor elija una del 1 al 6\n")
        return False

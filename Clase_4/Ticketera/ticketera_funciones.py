lista_productos = {}


def agregar_producto(diccionario: dict):
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in diccionario:
        print("Este producto ya existe, intente con otro.")
    else:

        cantidad = input("Ingrese la cantidad: ")
        precio = input("Ingrese el precio: ")

        diccionario[nombre] = {'Cantidad': cantidad, 'Precio': precio}

        print("Producto guardado.\n")


def eliminar_producto(diccionario: dict):

    nombre = input("Ingrese el nombre del producto que quiera eliminar: ")
    if nombre in diccionario:
        diccionario.pop(nombre)
    else:
        print("El nombre ingresado no está en la lista de productos\n")

    print(f"Producto {nombre} eliminado")


def editar_producto(diccionario: dict):
    nombre = input("Ingrese el nombre del producto que desea modificar: ")
    if nombre in diccionario:
        cantidad = input("Ingrese cantidad: ")
        precio = input("Ingrese el precio: ")
    else:
        print("El producto no existe")  

    diccionario[nombre] = {'Cantidad': cantidad, 'Precio': precio}
    print("Producto guardado.\n")

def ver_productos(diccionario: dict):
    for clave, valor in diccionario.items():
        print(f"\n{clave}:")
        for a, b in valor.items():
            print(f"\t{a}: {b}")

def imprimir_ticket(diccionario:dict):
    pass    
    subtotal = 0

def sumar_todo(diccionario: dict):
    suma_total = 0
    suma_cantidad = 0
    for valor in diccionario.values():
        lista_2 = []
        for b in valor.values():
            lista_2.append(b)
        suma_total = suma_total + (int(lista_2[0]) * float(lista_2[1]))
        suma_cantidad = suma_cantidad + int(lista_2[0])
    print(f"Cantidad de productos: {suma_cantidad}\nTotal a abonado: {suma_total}")


def mostrar_diccionario(diccionario: dict):
    for x, y in diccionario.items():
        print(f"{x}. {y}")


def comprobar_opcion(opcion):

    if opcion >= 1 and opcion <= 6:
        if opcion == 1:
            agregar_producto(lista_productos)
            return False
        elif opcion == 2:
            eliminar_producto(lista_productos)
            return False
        elif opcion ==3:
            editar_producto(lista_productos)
            return False
        elif opcion == 4:
            ver_productos(lista_productos)
            return False
        elif opcion ==5:
          # imprimir_ticket(lista_productos)
            return False  
        elif opcion == 6:
            print("\n")
            sumar_todo(lista_productos)
            return True

        return True

    else:
        print("\n Opción incorrecta, por favor elija una del 1 al 6\n")
        return False

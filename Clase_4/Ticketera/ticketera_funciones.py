from datetime import datetime

lista_productos = {}

def agregar_producto(diccionario: dict):

    nombre = input("Ingrese el nombre del producto: ")
    if nombre in diccionario:
        print("Este producto ya existe, intente con otro.")
    else:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingresa el precio: "))
        sub_total = round((cantidad * precio),2)        

        diccionario[nombre] = {'Cantidad': cantidad,
                               'Precio': precio, 'Sub_total': sub_total}

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
       cantidad = int(input("Ingrese la cantidad: "))
       precio = float(input("Ingresa el precio: "))
    else:
        print("El producto no existe")

    diccionario[nombre] = {'Cantidad': cantidad, 'Precio': precio}
    print("Producto guardado.\n")

def ver_productos(diccionario: dict):
    for clave, valor in diccionario.items():
        print(f"\n{clave}:")
        for a, b in valor.items():
            print(f"\t{a}: {b}")
        

def sumar_todo(diccionario: dict):
    suma_total = 0
    suma_cantidad = 0
    fecha = datetime.strftime(datetime.now(), "%d-%m-%Y / %H.%M")
    for valor in diccionario.values():
        lista_2 = []
        for b in valor.values():
            lista_2.append(b)
        suma_total = suma_total + (int(lista_2[0]) * int(lista_2[1]))
        suma_cantidad = suma_cantidad + int(lista_2[0])
    print(
        f"\nCantidad de productos: {suma_cantidad}\nTotal a pagar: ${suma_total}\n{fecha}\n")


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
        elif opcion == 3:
            editar_producto(lista_productos)
            return False
        elif opcion == 4:
            ver_productos(lista_productos)
            return False
        elif opcion == 5:
            ver_productos(lista_productos)
            print('\n')
            sumar_todo(lista_productos)
            return False
        elif opcion == 6:
            print("\nMuchas gracias por su compra!\n")
            return True

        return True

    else:
        print("\n Opción incorrecta, por favor elija una del 1 al 6\n")
        return False

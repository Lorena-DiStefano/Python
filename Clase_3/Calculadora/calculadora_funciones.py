

def recorrer_diccionario(diccionario: dict):
    print("\n")
    for x, y in diccionario.items():
        print(f"{x}. {y}")
    print("\n")


def inputs():
    a = float(input("Ingrese un número: "))
    b = float(input("Ingrese el siguiente número: "))
    return (a, b)


def sumar(a, b):
    return a+b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero!!"
    else:
        return f"La división es: {a / b}"


def verificar_opcion(opcion: int):
    if opcion == 1:
        numeros = inputs()
        print(f"La suma es: {sumar(numeros[0], numeros[1])}")
        return True

    elif opcion == 2:
        numeros = inputs()
        resta = restar(numeros[0], numeros[1])
        print(f"La resta es: {resta}")
        return True

    elif opcion == 3:
        numeros = inputs()
        multi = multiplicar(numeros[0], numeros[1])
        print(f"La multiplicacion es: {multi}")
        return True

    elif opcion == 4:
        numeros = inputs()
        div = dividir(numeros[0], numeros[1])
        print(div)
        return True

    elif opcion == 5:
        print("Gracias por usar el programa...")
        return False

    else:
        print("No seleccionó una opción correcta.\nPor favor intente nuevamente")
        return True

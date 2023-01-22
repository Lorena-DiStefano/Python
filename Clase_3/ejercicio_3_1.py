""" CONSIDERAR USAR LO QUE VIMOS EN LA CLASE 3"""

# 1. Ingresar desde la consola 3 números y devolver por consola esa lista ordenada de mayor a menor y de menor a mayor

numbers = [68, 2, 14]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

# 2. Crear una función que sume los números ingresados en la lista anterior.

# Opción 2a


def sumar(a: int, b: int, c: int,):
    return a + b + c

resultado = sumar(numbers[0], numbers[1], numbers[2])

print(f"Resultado opción 2a : {resultado}")


# Opción 2b
suma = 0

for i in numbers:
    suma = suma + i
print(f"Resultado opción 2b : {suma}")


# 3. Crear una función que dado 2 números cualquiera devuelva todos los números comprendidos entre si (solamente los enteros)

variable = 5

while variable < 21:
    if (variable % 2 == 0):
        print(variable)
    variable += 1

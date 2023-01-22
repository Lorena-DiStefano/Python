""" CONDICIONALES """
# nombre = input("Ingresá tu nombre: ")
# edad = int(input("Que edad tenes: "))

# if edad > 18:
#     print(f"{nombre} es mayor de edad")
# elif edad == 18:
#     print(f"La edad de {nombre} es 18")
# else:
#     print(f"{nombre} no es mayor de edad")

# numero_1 = 18
# numero_2 = 200
# # print(not numero_1 > 100)
# # print(not numero_2 > 100)
# if not numero_1 > 100 and numero_2 > 100:
#     print("Los numeros son mayores a 100")
# else:
#     print("Los numeros no son mayores a 100")

""" CICLO FOR """

# lista = ["a", "b", "c", "d"]

# for elemento in lista:
#     print(elemento)

# diccionario = {
#     "nombre": "Luis",
#     "apellido": "Perez",
#     "Direccion": "Av. siempre viva 123"
# }

# print(diccionario.items())

#  for clave, valor in diccionario.items():
#      # print(clave,":" ,valor)
#      # print(clave + ": " + valor)
#       print(f"{clave}: {valor}")

""" CICLO WHILE """

# variable = 4
# print(variable < 10)

# while variable < 10:
#     print(variable)
#     print("Estoy en el ciclo while")
#     variable = variable + 1

#     variable += 1

""" FUNCIONES """

# def funcion_suma(a: int, b: int):
#     """
#     Funcion que devuelve la suma de 2 números
#     """
#     resultado = a + b
#     print(resultado)

# funcion_suma(2, 3)
# funcion_suma("hola ", "mundo")
# funcion_suma()

# print()

# def funcion_multiplicar(valor_1, valor_2):
#     return valor_1 * valor_2

# print(funcion_multiplicar(3, 5))

# variable = funcion_multiplicar(2 , 3)

# print(variable)

# def suma_de_enteros(a: int, b: int):

#     if type(a) == int and type(b) == int:
#         print("son enteros")
#     else:
#         print("No son enteros")

# suma_de_enteros(1, 2)
# suma_de_enteros("abc", 3.6)

# suma = lambda a, b : a + b

# print(suma(2, 3))

# print((lambda a, b : a * b)(5, 3))

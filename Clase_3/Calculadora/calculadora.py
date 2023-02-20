from calculadora_funciones import recorrer_diccionario,verificar_opcion 

# Calculadora que recibe 2 valores
menu = {1: "Sumar", 2: "Restar", 3: "Mulplicar", 4: "Dividir", 5: "Salir"}


loop = True

while loop:
    recorrer_diccionario(menu)
    opcion = int(input("Ingrese una opción: "))
    loop = verificar_opcion(opcion)

""" Usando el formulario creado en la primera clase """

# 1- Crear una lista con esos datos y mostrar por consola
datos = ['nombre', 'apellido', 'edad', 'anio_nacimiento']

print(datos)

# 2- Crear un diccionario poniendo como clave lo que representa cada valor

datos_dic = {'nombre': 'Lorena', 'apellido': 'Di Stefano',
             'edad': 54, 'anio_nacimiento': 1968}


# 3- Solicitar al usuario ingresar 3 datos por consola y luego insertarlos en un conjunto
# para mostrarlos por pantalla

conjunto_a = {'a'}

conjunto_a.add(input('Color favorito: '))
conjunto_a.add(input('Animal favorito: '))
conjunto_a.add(input("Personaje Favorito: "))

print(conjunto_a)

# PROFE!!!! te elevo algunas dudas:
# Si intento el mismo código pero con un "conjunto" vacío me tira error. Para que funcione tengo que agregar algún elemento o las comillas '' ¿Qué estoy haciendo mal? (si lo explicaste y se me escapó Perdón!!!)


""" DICCIONARIOS ANIDADOS """

# 4- Introducir en un diccionario 4 alumnos, cada uno tendrá 3 notas de las siguientes asignaturas
# Lengua - Matemática - Informática

alumno_1 = {
    'Lengua': 9,
    'Matemática': 7,
    'Informática': 7
}

alumno_2 = {
    'Lengua': 3,
    'Matemática': 4,
    'Informática': 5
}

alumno_3 = {
    'Lengua': 6,
    'Matemática': 7,
    'Informática': 8
}

alumno_4 = {
    'Lengua': 9,
    'Matemática': 8,
    'Informática': 5
}

alumnos = {
}

alumnos.update({'alumno_1': alumno_1})
alumnos.update({'alumno_2': alumno_3})
alumnos['alumno_3']= alumno_3
alumnos['alumno_4'] = alumno_4

print(alumnos)


# 5- Actualiza los datos de un alumno en particular y elimina uno del diccionario
# "alumnos" que precisamente no haya sido el que se actualizaron los datos

alumno_3.update({'Inglés':9})

alumnos.pop('alumno_4')
print(alumnos)

# 6- Agrega un alumno más por consola, solamente pidiendo que ingrese las notas de este quinto alumno

alumno_5={}

lengua = int(input('Nota obtenida en Lengua:'))
matematica= int(input('Nota obtenida en Matemática:'))
informatica=int(input('Nota obtenida en Informatica:'))

print(
    f'El alumno_5 obtuvo las siguientes calificaciones= \nLengua:{lengua}\nMatemática:{matematica}\nInformática:{informatica}')

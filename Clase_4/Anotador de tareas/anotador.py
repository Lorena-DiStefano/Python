import anotador_funciones as m_tareas

menu = {
    1: "Agregar tarea",
    2: "Eliminar tarea",
    3: "Editar tarea",
    4: "Listar tareas",
    5: "Buscar tarea",
    6: "Salir"
}

menu_variable = False

while not menu_variable:
    m_tareas.mostrar_diccionario(menu)

    valor = int(input("\nElija una opción: "))

    menu_variable = m_tareas.comprobar_opcion(valor)

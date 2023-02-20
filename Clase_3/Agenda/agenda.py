from modulo_funciones import validar_opcion,mostrar_dict

menu = {
    1: "Agregar contacto",
    2: "Eliminar contacto",
    3: "Editar contacto",
    4: "Listar contactos",
    5: "Buscar  contacto",
    6: "Salir",
}



validacion = True

while validacion:
    mostrar_dict(menu)
    opcion = int(input("\nElija una opción del menu: "))
    validacion = validar_opcion(opcion)
# ====================================================


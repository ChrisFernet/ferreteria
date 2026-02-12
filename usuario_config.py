def gestion_usuarios():
    usuarios = []
    while True:
        print("Gestión de usuarios")
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_usuario(usuarios)
        elif opcion == "2":
            mostrar_usuario(usuarios)
        elif opcion == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def agregar_usuario(usuarios):  
    id = input("Ingrese el ID del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el primer apellido del usuario: ")
    telefono = int(input("Ingrese el teléfono del usuario: "))
    direccion = input("Ingrese la dirección del usuario: ")
    tipo = input("Ingrese el tipo de usuario: ")
    
    usuario = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }
    
    usuario.append(usuarios)
    print("Usuario agregado exitosamente.")
 
def mostrar_usuario(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Categoría: {usuario['categoria']}, Cantidad: {usuario['cantidad']}, Estado: {usuario['estado']}, Valor Estimado: {usuario['valor_estimado']}")

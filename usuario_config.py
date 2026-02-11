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

from json_config import cargar_datos, guardar_datos

def gestion_usuarios(usuarios):
    usuarios = cargar_datos("usuarios.json")
    
    while True:
        print("\n" + "="*50)
        print("Gestión de usuarios")
        print("="*50)
        print("1. Agregar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_usuario(usuarios)
            guardar_datos(usuarios, "usuarios.json")
        elif opcion == "2":
            cargar_datos(usuarios)
            mostrar_usuario(usuarios)
        elif opcion == "3":
            buscar_usuario(usuarios)
        elif opcion == "4":
            actualizar_usuario(usuarios)
            guardar_datos(usuarios, "usuarios.json")
        elif opcion == "5":
            eliminar_usuario(usuarios)
            guardar_datos(usuarios, "usuarios.json")
        elif opcion == "6":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
    
    return usuarios

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
    
    usuarios.append(usuarios)
    print("Usuario agregado exitosamente.")

def mostrar_usuario(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    print("\n" + "="*100)
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Categoría: {usuario['categoria']}, Cantidad: {usuario['cantidad']}, Estado: {usuario['estado']}, Valor Estimado: {usuario['valor_estimado']}")
    print("="*100)

def buscar_usuario(usuarios):
    print("\nBuscar usuario por:")
    print("1. ID")
    print("2. Nombre")
    opcion = input("Seleccione opción: ")
    
    if opcion == "1":
        id_buscar = input("Ingrese el ID: ")
        for u in usuarios:
            if u["id"] == id_buscar:
                print("\n--- Usuario encontrado ---")
                print(f"ID: {u['id']}")
                print(f"Nombre: {u['nombre']} {u['apellido']}")
                print(f"Teléfono: {u['telefono']}")
                print(f"Dirección: {u['direccion']}")
                print(f"Tipo: {u['tipo']}")
                return
        print("Usuario no encontrado.")
    
    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre: ").lower()
        encontrados = [u for u in usuarios if nombre_buscar in u["nombre"].lower()]
        if encontrados:
            print(f"\n--- Se encontraron {len(encontrados)} usuario(s) ---")
            for u in encontrados:
                print(f"ID: {u['id']}, Nombre: {u['nombre']} {u['apellido']}, Tipo: {u['tipo']}")
        else:
            print("No se encontraron usuarios con ese nombre.")

def actualizar_usuario(usuarios):
    id_actualizar = input("Ingrese el ID del usuario a actualizar: ")
    
    for u in usuarios:
        if u["id"] == id_actualizar:
            print("\n--- Usuario encontrado ---")
            print(f"Nombre actual: {u['nombre']} {u['apellido']}")
            print("\n¿Qué desea actualizar?")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Teléfono")
            print("4. Dirección")
            print("5. Tipo de usuario")
            print("6. Todo")
            
            opcion = input("Seleccione opción: ")
            
            if opcion == "1":
                u["nombre"] = input("Nuevo nombre: ")
            elif opcion == "2":
                u["apellido"] = input("Nuevo apellido: ")
            elif opcion == "3":
                u["telefono"] = int(input("Nuevo teléfono: "))
            elif opcion == "4":
                u["direccion"] = input("Nueva dirección: ")
            elif opcion == "5":
                u["tipo"] = input("Nuevo tipo (residente/administrador): ")
            elif opcion == "6":
                u["nombre"] = input("Nuevo nombre: ")
                u["apellido"] = input("Nuevo apellido: ")
                u["telefono"] = int(input("Nuevo teléfono: "))
                u["direccion"] = input("Nueva dirección: ")
                u["tipo"] = input("Nuevo tipo: ")
            
            print("Usuario actualizado exitosamente.")
            return
    
    print("Usuario no encontrado.")

def eliminar_usuario(usuarios):
    id_eliminar = input("Ingrese el ID del usuario a eliminar: ")
    
    for i, u in enumerate(usuarios):
        if u["id"] == id_eliminar:
            print(f"\n¿Está seguro de eliminar a '{u['nombre']} {u['apellido']}'? (s/n): ", end="")
            confirmacion = input().lower()
            if confirmacion == "s":
                usuarios.pop(i)
                print("Usuario eliminado exitosamente.")
            else:
                print("Eliminación cancelada.")
            return
    
    print("Usuario no encontrado.")
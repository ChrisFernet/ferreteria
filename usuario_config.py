from json_config import cargar_datos, guardar_datos

def gestion_usuarios():
    """Menú principal de gestión de usuarios"""
    usuarios = cargar_datos("usuarios.json")
    
    while True:
        print("\n" + "="*50)
        print("GESTION DE USUARIOS")
        print("="*50)
        print("1. Agregar usuario")
        print("2. Mostrar todos los usuarios")
        print("3. Buscar un usuario")
        print("4. Volver al menu principal")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            agregar_usuario(usuarios)
            guardar_datos(usuarios, "usuarios.json")
            print("\nPresione ENTER para continuar...")
            input()
            
        elif opcion == "2":
            mostrar_usuarios(usuarios)
            print("\nPresione ENTER para continuar...")
            input()
            
        elif opcion == "3":
            buscar_usuario(usuarios)
            print("\nPresione ENTER para continuar...")
            input()
            
        elif opcion == "4":
            print("Volviendo al menu principal...")
            break
            
        else:
            print("Opcion no valida.")
            print("\nPresione ENTER para continuar...")
            input()


def agregar_usuario(usuarios):
    """Agrega un nuevo usuario a la lista"""
    print("\n--- AGREGAR NUEVO USUARIO ---")
    
    id = input("ID del usuario: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    direccion = input("Direccion: ")
    tipo = input("Tipo (residente/administrador): ")
    
    nuevo_usuario = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }
    
    usuarios.append(nuevo_usuario)
    print("\nUsuario agregado correctamente!")


def mostrar_usuarios(usuarios):
    """Muestra todos los usuarios"""
    if len(usuarios) == 0:
        print("\nNo hay usuarios registrados.")
        return
    
    print("\n" + "="*80)
    print("LISTA DE USUARIOS")
    print("="*80)
    
    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']} {usuario['apellido']}")
        print(f"Telefono: {usuario['telefono']}")
        print(f"Direccion: {usuario['direccion']}")
        print(f"Tipo: {usuario['tipo']}")
        print("-" * 80)
    
    print(f"Total: {len(usuarios)} usuarios")


def buscar_usuario(usuarios):
    """Busca un usuario por ID"""
    if len(usuarios) == 0:
        print("\nNo hay usuarios registrados.")
        return
    
    print("\n--- BUSCAR USUARIO ---")
    id_buscar = input("Ingrese el ID del usuario: ")
    
    usuario_encontrado = None
    
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado:
        print("\nUsuario encontrado:")
        print(f"ID: {usuario_encontrado['id']}")
        print(f"Nombre: {usuario_encontrado['nombre']} {usuario_encontrado['apellido']}")
        print(f"Telefono: {usuario_encontrado['telefono']}")
        print(f"Direccion: {usuario_encontrado['direccion']}")
        print(f"Tipo: {usuario_encontrado['tipo']}")
    else:
        print("\nUsuario no encontrado.")
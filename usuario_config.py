from json_config import cargar_datos, guardar_datos

# color

AZUL_OSCURO = '\033[34m'
AZUL_CLARO = '\033[94m'
CYAN = '\033[96m'
AZUL_BRILLANTE = '\033[1;34m'
BLANCO = '\033[97m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
RESET = '\033[0m'
NEGRITA = '\033[1m'

# funciones de apariencia

def limpiar_pantalla():
    """Simula limpiar la pantalla"""
    print("\n" * 50)

def linea(longitud=70, color=AZUL_CLARO):
    """Crea una línea simple"""
    print(f"{color}{'─' * longitud}{RESET}")

def titulo(texto):
    """Crea un título simple y centrado"""
    longitud = 70
    print(f"\n{AZUL_BRILLANTE}{NEGRITA}{texto.center(longitud)}{RESET}")
    linea(longitud, AZUL_OSCURO)

def pausa():
    """Pausa hasta que el usuario presione ENTER"""
    input(f"\n{AZUL_CLARO}Presione ENTER para continuar...{RESET}")

def gestion_usuarios():
    usuarios = cargar_datos("usuarios.json")
    
    while True:
        limpiar_pantalla()
        titulo("GESTION DE USUARIOS")
        print()
        
        print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Agregar usuario{RESET}")
        print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Mostrar todos los usuarios{RESET}")
        print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Buscar usuario{RESET}")
        print(f"{AZUL_CLARO}  4.{RESET} {BLANCO}Eliminar usuario{RESET}")
        print(f"{AZUL_CLARO}  5.{RESET} {BLANCO}Volver al menu principal{RESET}")
        
        print()
        linea()
        
        opcion = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion == "1":
            agregar_usuario(usuarios)
            guardar_datos(usuarios, "usuarios.json")
            pausa()
            
        elif opcion == "2":
            mostrar_usuarios(usuarios)
            pausa()
            
        elif opcion == "3":
            buscar_usuario(usuarios)
            pausa()
            
        elif opcion == "4":
            eliminar_usuario(usuarios)
            guardar_datos(usuarios, "usuarios.json")
            pausa()
            
        elif opcion == "5":
            print(f"\n{CYAN}Volviendo al menu principal...{RESET}")
            break
            
        else:
            print(f"\n{ROJO}Opcion no valida. Intente de nuevo.{RESET}")
            pausa()

def agregar_usuario(usuarios):
    limpiar_pantalla()
    titulo("AGREGAR NUEVO USUARIO")
    print()
    
    id = input(f"{CYAN}Id del usuario: {RESET}")
    nombre = input(f"{CYAN}Nombre: {RESET}")
    apellido = input(f"{CYAN}Apellido: {RESET}")
    telefono = (input(f"{CYAN}Teléfono: {RESET}"))
    direccion = input(f"{CYAN}Dirección: {RESET}")
    tipo = (input(f"{CYAN}Tipo de usuario(residente/administrador): ${RESET}"))
    
    nuevo_usuario = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }

    usuarios.append(nuevo_usuario)
    print(f"\n{VERDE}✓ Herramienta agregada exitosamente!{RESET}")

def mostrar_usuarios(usuarios):
    """Muestra todos los usuarios de forma dinámica"""
    limpiar_pantalla()
    titulo("REGISTRO DE USUARIOS")
    print()
    
    if len(usuarios) == 0:
        print(f"{AMARILLO}No hay usuarios registrados en el sistema.{RESET}")
        return
    
    # Mostrar resumen
    print(f"{CYAN}Total de usuarios: {NEGRITA}{len(usuarios)}{RESET}")
    print()
    linea(70, AZUL_CLARO)
    
    # Mostrar cada usuario con formato bonito
    numero = 1
    for usuario in usuarios:
        print()
        print(f"{AZUL_BRILLANTE}▶ Usuario #{numero}{RESET}")
        print(f"  {CYAN}ID:{RESET} {usuario['id']}")
        print(f"  {CYAN}Nombre:{RESET} {NEGRITA}{usuario['nombre']} {usuario['apellido']}{RESET}")
        print(f"  {CYAN}Telefono:{RESET} {usuario['telefono']}")
        print(f"  {CYAN}Direccion:{RESET} {usuario['direccion']}")
        
        # Color según el tipo de usuario
        if usuario['tipo'].lower() == 'administrador':
            color_tipo = VERDE
        else:
            color_tipo = AZUL_CLARO
        
        print(f"  {CYAN}Tipo:{RESET} {color_tipo}{usuario['tipo']}{RESET}")
        
        # Línea separadora entre usuarios (excepto el último)
        if numero < len(usuarios):
            print(f"{AZUL_CLARO}{'┄' * 70}{RESET}")
        
        numero = numero + 1
    
    print()
    linea(70, AZUL_CLARO)
    
    # Estadísticas adicionales
    print()
    print(f"{AZUL_BRILLANTE}ESTADISTICAS:{RESET}")
    
    # Contar usuarios por tipo
    administradores = 0
    residentes = 0
    
    for u in usuarios:
        if u['tipo'].lower() == 'administrador':
            administradores = administradores + 1
        else:
            residentes = residentes + 1
    
    print(f"  {VERDE}● Administradores:{RESET} {administradores}")
    print(f"  {AZUL_CLARO}● Residentes:{RESET} {residentes}")


def buscar_usuario(usuarios):
    
    # usuarios por id 
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

def eliminar_usuario(usuarios):

    limpiar_pantalla()
    titulo("ELIMINAR USUARIO")
    print()
    
    if len(usuarios) == 0:
        print(f"{AMARILLO}No hay usuarios registrados.{RESET}")
        return
    
    id_eliminar = input(f"{CYAN}Ingrese el ID del usuario a eliminar: {RESET}")
    
    for i, h in enumerate(usuarios):
        if h["id"] == id_eliminar:
            print()
            linea(70, AMARILLO)
            print(f"{AMARILLO}{NEGRITA}⚠ ADVERTENCIA{RESET}")
            linea(70, AMARILLO)
            print(f"\n{BLANCO}Esta a punto de eliminar el usuario:{RESET}")
            print(f"  {CYAN}Nombre:{RESET} {h['nombre']}")
            print(f"  {CYAN}Apellido:{RESET} {h['apellido']}")
            print()
            
            confirmacion = input(f"{ROJO}¿Esta seguro? (s/n): {RESET}").lower()
            
            if confirmacion == "s":
                usuarios.pop(i)
                print(f"\n{VERDE}✓ Usuario eliminado exitosamente.{RESET}")
            else:
                print(f"\n{CYAN}Eliminacion cancelada.{RESET}")
            return
    
    print(f"\n{ROJO}✗ Usuario no encontrado.{RESET}")

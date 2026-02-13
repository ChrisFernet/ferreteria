from herramientas_config import gestionar_herramientas
from usuario_config import gestion_usuarios
from prestamos_config import gestionar_prestamos
from reportes_config import consultas_y_reportes
from json_config import cargar_datos, guardar_datos
from estilos import *

# ========================================
# FUNCIONES DE MENÚ
# ========================================

def mensaje_bienvenida():
    limpiar_pantalla()
    print()
    linea(60, CYAN)
    print(f"{CYAN}{NEGRITA}{'SISTEMA DE GESTION DE HERRAMIENTAS'.center(60)}{RESET}")
    print(f"{AZUL_CLARO}{'Comunidad Vecinal'.center(60)}{RESET}")
    linea(60, CYAN)
    print()
    input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")


def login():
    """Valida el usuario y retorna sus datos"""
    limpiar_pantalla()
    titulo("INICIO DE SESION", 60)
    print()
    
    # Cargar usuarios
    usuarios = cargar_datos("usuarios.json")
    
    # Si no hay usuarios, mostrar error
    if len(usuarios) == 0:
        mensaje_error("No hay usuarios registrados en el sistema.")
        mensaje_advertencia("Por favor, contacte al administrador.")
        return None
    
    # Pedir ID
    id_usuario = input(f"{CYAN}Ingrese su ID de usuario: {RESET}")
    
    # Buscar el usuario
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            # Usuario encontrado
            print(f"\n{VERDE}Bienvenido, {usuario['nombre']} {usuario['apellido']}!{RESET}")
            print(f"{CYAN}Tipo de usuario: {usuario['tipo']}{RESET}")
            pausa()
            return usuario  # Retorna los datos del usuario
    
    # Si llegamos aquí, el usuario no existe
    mensaje_error("Usuario no encontrado.")
    pausa()
    return None


def main_menu():
    """Función del menú principal con validación de usuario"""
    mensaje_bienvenida()
    
    while True:
        # LLAMAR AL LOGIN
        usuario_actual = login()
        
        # Si el login falló, volver a intentar
        if usuario_actual is None:
            continuar = input(f"\n{CYAN}¿Desea intentar de nuevo? (s/n): {RESET}").lower()
            if continuar != "s":
                limpiar_pantalla()
                print()
                linea(60, CYAN)
                print(f"{CYAN}{NEGRITA}{'Gracias por usar el sistema'.center(60)}{RESET}")
                print(f"{AZUL_CLARO}{'Saliendo del programa...'.center(60)}{RESET}")
                linea(60, CYAN)
                print()
                break
            continue
        
        # VERIFICAR EL TIPO DE USUARIO
        if usuario_actual["tipo"].lower() == "administrador":
            # Es administrador → Ir a menú administrador
            menu_administrador()
        else:
            # Es usuario/residente → Ir a menú usuario
            menu_usuario_residente(usuario_actual)
        
        # Preguntar si quiere cerrar sesión
        cerrar = input(f"\n{CYAN}¿Desea cerrar sesion? (s/n): {RESET}").lower()
        if cerrar == "s":
            limpiar_pantalla()
            print()
            linea(60, CYAN)
            print(f"{CYAN}{NEGRITA}{'Sesion cerrada'.center(60)}{RESET}")
            print(f"{AZUL_CLARO}{'Hasta pronto!'.center(60)}{RESET}")
            linea(60, CYAN)
            print()
            break


def menu_administrador():
    while True:
        limpiar_pantalla()
        titulo("MENU ADMINISTRADOR", 60)
        print()
        
        print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Gestionar usuarios{RESET}")
        print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Gestionar herramientas{RESET}")
        print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Gestionar prestamos{RESET}")
        print(f"{AZUL_CLARO}  4.{RESET} {BLANCO}Consultas y reportes{RESET}")
        print(f"{AZUL_CLARO}  5.{RESET} {BLANCO}Volver al menu principal{RESET}")
        
        print()
        linea(60)
        
        opcion_admin = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion_admin == "1":
            gestion_usuarios()
            
        elif opcion_admin == "2":
            gestionar_herramientas()
            
        elif opcion_admin == "3":
            gestionar_prestamos()
            
        elif opcion_admin == "4":
            consultas_y_reportes()
            
        elif opcion_admin == "5":
            print(f"\n{CYAN}Volviendo al menu principal...{RESET}")
            break
            
        else:
            mensaje_error("Opcion no valida.")
            pausa()


def ver_herramientas_disponibles_usuario():
    """Muestra solo herramientas disponibles para usuarios"""
    limpiar_pantalla()
    titulo("HERRAMIENTAS DISPONIBLES", 60)
    print()
    
    herramientas = cargar_datos("herramientas.json")
    
    # Filtrar solo las disponibles
    disponibles = []
    for h in herramientas:
        if h.get('cantidad', 0) > 0 and h.get('estado', '').lower() == 'activa':
            disponibles.append(h)
    
    if len(disponibles) == 0:
        mensaje_advertencia("No hay herramientas disponibles en este momento.")
        return
    
    print(f"{CYAN}Total de herramientas disponibles: {NEGRITA}{len(disponibles)}{RESET}")
    print()
    linea(60, AZUL_CLARO)
    
    numero = 1
    for h in disponibles:
        print()
        print(f"{AZUL_BRILLANTE}▶ Herramienta #{numero}{RESET}")
        print(f"  {CYAN}ID:{RESET} {h['id']}")
        print(f"  {CYAN}Nombre:{RESET} {NEGRITA}{h['nombre']}{RESET}")
        print(f"  {CYAN}Categoria:{RESET} {h['categoria']}")
        print(f"  {CYAN}Cantidad disponible:{RESET} {VERDE}{h['cantidad']} unidades{RESET}")
        print(f"  {CYAN}Estado:{RESET} {VERDE}{h['estado']}{RESET}")
        
        if numero < len(disponibles):
            print(f"{AZUL_CLARO}{'┄' * 60}{RESET}")
        
        numero = numero + 1
    
    print()
    linea(60, AZUL_CLARO)


def buscar_herramienta_usuario():
    """Busca una herramienta disponible"""
    limpiar_pantalla()
    titulo("BUSCAR HERRAMIENTA", 60)
    print()
    
    herramientas = cargar_datos("herramientas.json")
    
    if len(herramientas) == 0:
        mensaje_advertencia("No hay herramientas registradas.")
        return
    
    id_buscar = input(f"{CYAN}Ingrese el ID de la herramienta: {RESET}")
    
    encontrada = None
    for h in herramientas:
        if h['id'] == id_buscar:
            encontrada = h
            break
    
    if encontrada:
        print()
        linea(60, VERDE)
        print(f"{VERDE}{NEGRITA}HERRAMIENTA ENCONTRADA{RESET}")
        linea(60, VERDE)
        print(f"\n  {CYAN}ID:{RESET} {encontrada['id']}")
        print(f"  {CYAN}Nombre:{RESET} {NEGRITA}{encontrada['nombre']}{RESET}")
        print(f"  {CYAN}Categoria:{RESET} {encontrada['categoria']}")
        print(f"  {CYAN}Cantidad disponible:{RESET} {encontrada['cantidad']} unidades")
        print(f"  {CYAN}Estado:{RESET} {encontrada['estado']}")
        
        # Verificar si está disponible
        if encontrada.get('cantidad', 0) > 0 and encontrada.get('estado', '').lower() == 'activa':
            print(f"\n  {VERDE}✓ Esta herramienta esta disponible para solicitar{RESET}")
        else:
            print(f"\n  {ROJO}✗ Esta herramienta NO esta disponible{RESET}")
    else:
        mensaje_error("Herramienta no encontrada.")


def solicitar_herramienta_usuario(usuario_actual):
    """Permite al usuario solicitar una herramienta"""
    limpiar_pantalla()
    titulo("SOLICITAR HERRAMIENTA", 60)
    print()
    
    print(f"{CYAN}Usuario: {NEGRITA}{usuario_actual['nombre']} {usuario_actual['apellido']}{RESET}")
    print()
    
    herramientas = cargar_datos("herramientas.json")
    solicitudes = cargar_datos("solicitudes.json")
    
    # Mostrar herramientas disponibles
    disponibles = []
    for h in herramientas:
        if h.get('cantidad', 0) > 0 and h.get('estado', '').lower() == 'activa':
            disponibles.append(h)
    
    if len(disponibles) == 0:
        mensaje_advertencia("No hay herramientas disponibles para solicitar.")
        return
    
    print(f"{CYAN}--- HERRAMIENTAS DISPONIBLES ---{RESET}")
    numero = 1
    for h in disponibles:
        print(f"{numero}. ID: {h['id']} - {h['nombre']} ({h['cantidad']} disponibles)")
        numero = numero + 1
    
    print()
    id_herramienta = input(f"{CYAN}Ingrese el ID de la herramienta: {RESET}")
    
    # Buscar herramienta
    herramienta = None
    for h in disponibles:
        if h['id'] == id_herramienta:
            herramienta = h
            break
    
    if herramienta is None:
        mensaje_error("Herramienta no encontrada o no disponible.")
        return
    
    # Pedir cantidad
    cantidad_str = input(f"{CYAN}Cantidad (max {herramienta['cantidad']}): {RESET}")
    
    try:
        cantidad = int(cantidad_str)
    except Exception:
        mensaje_error("Cantidad invalida.")
        return
    
    if cantidad <= 0 or cantidad > herramienta['cantidad']:
        mensaje_error("Cantidad invalida.")
        return
    
    # Pedir fecha
    fecha_devolucion = input(f"{CYAN}Fecha de devolucion (ej: 2026-03-01): {RESET}")
    
    # Crear solicitud
    nueva_solicitud = {
        "id": generar_id_solicitud(solicitudes),
        "id_usuario": usuario_actual['id'],
        "nombre_usuario": f"{usuario_actual['nombre']} {usuario_actual['apellido']}",
        "id_herramienta": herramienta['id'],
        "nombre_herramienta": herramienta['nombre'],
        "cantidad": cantidad,
        "fecha_devolucion": fecha_devolucion,
        "estado": "pendiente"
    }
    
    solicitudes.append(nueva_solicitud)
    guardar_datos(solicitudes, "solicitudes.json")
    
    print()
    linea(60, VERDE)
    print(f"{VERDE}{NEGRITA}✓ SOLICITUD CREADA EXITOSAMENTE{RESET}")
    linea(60, VERDE)
    print(f"\n  {CYAN}ID Solicitud:{RESET} {nueva_solicitud['id']}")
    print(f"  {CYAN}Herramienta:{RESET} {herramienta['nombre']}")
    print(f"  {CYAN}Cantidad:{RESET} {cantidad}")
    print(f"  {CYAN}Estado:{RESET} {AMARILLO}Pendiente de aprobacion{RESET}")
    print()
    print(f"{CYAN}Un administrador revisara tu solicitud.{RESET}")


def ver_mis_solicitudes_usuario(usuario_actual):
    """Muestra las solicitudes del usuario actual"""
    limpiar_pantalla()
    titulo("MIS SOLICITUDES", 60)
    print()
    
    print(f"{CYAN}Usuario: {NEGRITA}{usuario_actual['nombre']} {usuario_actual['apellido']}{RESET}")
    print()
    
    solicitudes = cargar_datos("solicitudes.json")
    
    # Filtrar solo las del usuario actual
    mis_solicitudes = []
    for s in solicitudes:
        if s.get('id_usuario') == usuario_actual['id']:
            mis_solicitudes.append(s)
    
    if len(mis_solicitudes) == 0:
        mensaje_advertencia("No tienes solicitudes registradas.")
        return
    
    print(f"{CYAN}Total de solicitudes: {NEGRITA}{len(mis_solicitudes)}{RESET}")
    print()
    linea(60, AZUL_CLARO)
    
    numero = 1
    for s in mis_solicitudes:
        print()
        print(f"{AZUL_BRILLANTE}▶ Solicitud #{numero}{RESET}")
        print(f"  {CYAN}ID:{RESET} {s['id']}")
        print(f"  {CYAN}Herramienta:{RESET} {s.get('nombre_herramienta', 'No especificada')}")
        print(f"  {CYAN}Cantidad:{RESET} {s.get('cantidad', 1)} unidades")
        print(f"  {CYAN}Fecha devolucion:{RESET} {s.get('fecha_devolucion', 'No especificada')}")
        
        # Color según estado
        estado = s.get('estado', 'pendiente')
        if estado == 'aprobada':
            color_estado = VERDE
        elif estado == 'pendiente':
            color_estado = AMARILLO
        else:
            color_estado = ROJO
        
        print(f"  {CYAN}Estado:{RESET} {color_estado}{estado}{RESET}")
        
        if numero < len(mis_solicitudes):
            print(f"{AZUL_CLARO}{'┄' * 60}{RESET}")
        
        numero = numero + 1
    
    print()
    linea(60, AZUL_CLARO)


def generar_id_solicitud(solicitudes):
    """Genera un ID único para la solicitud"""
    if len(solicitudes) == 0:
        return "S001"
    
    max_id = 0
    for s in solicitudes:
        try:
            num = int(s['id'][1:])
            if num > max_id:
                max_id = num
        except Exception:
            pass
    
    nuevo_num = max_id + 1
    
    if nuevo_num < 10:
        return f"S00{nuevo_num}"
    elif nuevo_num < 100:
        return f"S0{nuevo_num}"
    else:
        return f"S{nuevo_num}"


def menu_usuario_residente(usuario_actual):
    while True:
        limpiar_pantalla()
        titulo("MENU USUARIO", 60)
        print()
        print(f"{CYAN}Usuario actual: {NEGRITA}{usuario_actual['nombre']} {usuario_actual['apellido']}{RESET}")
        print()
        
        print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Ver herramientas disponibles{RESET}")
        print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Buscar herramienta{RESET}")
        print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Solicitar herramienta{RESET}")
        print(f"{AZUL_CLARO}  4.{RESET} {BLANCO}Mis solicitudes{RESET}")
        print(f"{AZUL_CLARO}  5.{RESET} {BLANCO}Cerrar sesion{RESET}")
        
        print()
        linea(60)
        
        opcion = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion == "1":
            ver_herramientas_disponibles_usuario()
            pausa()
            
        elif opcion == "2":
            buscar_herramienta_usuario()
            pausa()
            
        elif opcion == "3":
            solicitar_herramienta_usuario(usuario_actual)
            pausa()
            
        elif opcion == "4":
            ver_mis_solicitudes_usuario(usuario_actual)
            pausa()
            
        elif opcion == "5":
            print(f"\n{CYAN}Cerrando sesion...{RESET}")
            break
            
        else:
            mensaje_error("Opcion no valida.")
            pausa()


# Ejecutar
if __name__ == "__main__":
    main_menu()
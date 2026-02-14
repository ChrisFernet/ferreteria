from json_config import cargar_datos, guardar_datos
from estilos import *
from logs import *  

# GESTIÓN DE PRÉSTAMOS

def gestionar_prestamos():
    """Menú principal de gestión de préstamos para ADMINISTRADORES"""
    while True:
        limpiar_pantalla()
        titulo("GESTION DE PRESTAMOS - ADMINISTRADOR")
        print()
        
        print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Ver solicitudes pendientes{RESET}")
        print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Aprobar/Rechazar solicitud{RESET}")
        print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Devolver herramienta{RESET}")
        print(f"{AZUL_CLARO}  4.{RESET} {BLANCO}Ver prestamos activos{RESET}")
        print(f"{AZUL_CLARO}  5.{RESET} {BLANCO}Ver historial completo{RESET}")
        print(f"{AZUL_CLARO}  6.{RESET} {BLANCO}Volver al menu principal{RESET}")
        
        print()
        linea()
        
        opcion = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion == "1":
            ver_solicitudes_pendientes()
            pausa()
            
        elif opcion == "2":
            aprobar_rechazar_solicitud()
            pausa()
            
        elif opcion == "3":
            devolver_herramienta()
            pausa()
            
        elif opcion == "4":
            ver_prestamos_activos()
            pausa()
            
        elif opcion == "5":
            ver_historial_completo()
            pausa()
            
        elif opcion == "6":
            print(f"\n{CYAN}Volviendo al menu principal...{RESET}")
            break
            
        else:
            print(f"\n{ROJO}Opcion no valida. Intente de nuevo.{RESET}")
            pausa()

# ========================================
# FUNCIONES AUXILIARES
# ========================================

def generar_id_prestamo(prestamos):
    """Genera un ID único para el préstamo"""
    if len(prestamos) == 0:
        return "P001"
    
    max_id = 0
    for p in prestamos:
        try:
            numero_str = p['id'][1:]
            num = int(numero_str)
            if num > max_id:
                max_id = num
        except Exception:
            pass
    
    nuevo_num = max_id + 1
    
    if nuevo_num < 10:
        return f"P00{nuevo_num}"
    elif nuevo_num < 100:
        return f"P0{nuevo_num}"
    else:
        return f"P{nuevo_num}"

# ========================================
# FUNCIONES DE PRÉSTAMOS
# ========================================

def ver_solicitudes_pendientes():
    """Muestra todas las solicitudes pendientes de aprobación"""
    limpiar_pantalla()
    titulo("SOLICITUDES PENDIENTES")
    print()
    
    solicitudes = cargar_datos("solicitudes.json")
    
    # Filtrar solo pendientes
    pendientes = []
    for s in solicitudes:
        if s.get('estado') == 'pendiente':
            pendientes.append(s)
    
    if len(pendientes) == 0:
        print(f"{AMARILLO}No hay solicitudes pendientes.{RESET}")
        return
    
    print(f"{CYAN}Total de solicitudes pendientes: {NEGRITA}{len(pendientes)}{RESET}")
    print()
    linea(70, AZUL_CLARO)
    
    numero = 1
    for s in pendientes:
        print()
        print(f"{AZUL_BRILLANTE}▶ Solicitud #{numero}{RESET}")
        print(f"  {CYAN}ID:{RESET} {s['id']}")
        print(f"  {CYAN}Usuario:{RESET} {s.get('nombre_usuario', 'No especificado')}")
        print(f"  {CYAN}ID Usuario:{RESET} {s.get('id_usuario', 'No especificado')}")
        print(f"  {CYAN}Herramienta:{RESET} {s.get('nombre_herramienta', 'No especificada')}")
        print(f"  {CYAN}ID Herramienta:{RESET} {s.get('id_herramienta', 'No especificado')}")
        print(f"  {CYAN}Cantidad:{RESET} {s.get('cantidad', 1)} unidades")
        print(f"  {CYAN}Fecha devolucion:{RESET} {s.get('fecha_devolucion', 'No especificada')}")
        print(f"  {CYAN}Estado:{RESET} {AMARILLO}{s['estado']}{RESET}")
        
        if numero < len(pendientes):
            print(f"{AZUL_CLARO}{'┄' * 70}{RESET}")
        
        numero = numero + 1
    
    print()
    linea(70, AZUL_CLARO)


def aprobar_rechazar_solicitud():
    """Permite al administrador aprobar o rechazar una solicitud"""
    limpiar_pantalla()
    titulo("APROBAR/RECHAZAR SOLICITUD")
    print()
    
    solicitudes = cargar_datos("solicitudes.json")
    herramientas = cargar_datos("herramientas.json")
    prestamos = cargar_datos("prestamos.json")
    
    # Filtrar pendientes
    pendientes = []
    for s in solicitudes:
        if s.get('estado') == 'pendiente':
            pendientes.append(s)
    
    if len(pendientes) == 0:
        print(f"{AMARILLO}No hay solicitudes pendientes.{RESET}")
        return
    
    # Mostrar solicitudes pendientes
    print(f"{CYAN}--- SOLICITUDES PENDIENTES ---{RESET}")
    numero = 1
    for s in pendientes:
        print(f"{numero}. ID: {s['id']} - {s.get('nombre_usuario', 'Usuario')} - {s.get('nombre_herramienta', 'Herramienta')} ({s.get('cantidad', 1)} unidades)")
        numero = numero + 1
    
    print()
    id_solicitud = input(f"{CYAN}Ingrese el ID de la solicitud: {RESET}")
    
    # Buscar la solicitud
    solicitud_encontrada = None
    indice_solicitud = -1
    for i, s in enumerate(solicitudes):
        if s['id'] == id_solicitud and s.get('estado') == 'pendiente':
            solicitud_encontrada = s
            indice_solicitud = i
            break
    
    if solicitud_encontrada is None:
        print(f"\n{ROJO}Solicitud no encontrada o ya fue procesada.{RESET}")
        return
    
    # Mostrar detalles
    print()
    linea(70, CYAN)
    print(f"{CYAN}{NEGRITA}DETALLES DE LA SOLICITUD{RESET}")
    linea(70, CYAN)
    print(f"\n  {CYAN}ID Solicitud:{RESET} {solicitud_encontrada['id']}")
    print(f"  {CYAN}Usuario:{RESET} {solicitud_encontrada.get('nombre_usuario', 'No especificado')}")
    print(f"  {CYAN}ID Usuario:{RESET} {solicitud_encontrada.get('id_usuario', 'No especificado')}")
    print(f"  {CYAN}Herramienta:{RESET} {solicitud_encontrada.get('nombre_herramienta', 'No especificada')}")
    print(f"  {CYAN}ID Herramienta:{RESET} {solicitud_encontrada.get('id_herramienta', 'No especificado')}")
    print(f"  {CYAN}Cantidad:{RESET} {solicitud_encontrada.get('cantidad', 1)} unidades")
    print(f"  {CYAN}Fecha devolucion:{RESET} {solicitud_encontrada.get('fecha_devolucion', 'No especificada')}")
    
    # Verificar disponibilidad
    herramienta = None
    indice_herramienta = -1
    for i, h in enumerate(herramientas):
        if h['id'] == solicitud_encontrada.get('id_herramienta'):
            herramienta = h
            indice_herramienta = i
            break
    
    if herramienta is None:
        print(f"\n{ROJO}Error: Herramienta no encontrada en el inventario.{RESET}")
        return
    
    cantidad_solicitada = solicitud_encontrada.get('cantidad', 1)
    cantidad_disponible = herramienta.get('cantidad', 0)
    
    print()
    if cantidad_disponible >= cantidad_solicitada:
        print(f"  {VERDE}✓ Stock disponible: {cantidad_disponible} unidades{RESET}")
    else:
        print(f"  {ROJO}✗ Stock insuficiente: solo hay {cantidad_disponible} unidades{RESET}")
    
    # Preguntar acción
    print()
    linea(70, AZUL_CLARO)
    print()
    print(f"{AZUL_CLARO}1.{RESET} Aprobar solicitud")
    print(f"{AZUL_CLARO}2.{RESET} Rechazar solicitud")
    print(f"{AZUL_CLARO}3.{RESET} Cancelar")
    print()
    
    accion = input(f"{AZUL_BRILLANTE}Seleccione una accion: {RESET}")
    
    if accion == "1":
        # APROBAR
        if cantidad_disponible < cantidad_solicitada:
            # Registrar error en logs
            log_stock_insuficiente(
                solicitud_encontrada.get('nombre_herramienta'),
                cantidad_solicitada,
                cantidad_disponible,
                "ADMIN"
            )
            
            print(f"\n{ROJO}✗ No se puede aprobar: stock insuficiente.{RESET}")
            return
        
        # Crear el préstamo
        nuevo_prestamo = {
            "id": generar_id_prestamo(prestamos),
            "id_solicitud": solicitud_encontrada['id'],
            "id_usuario": solicitud_encontrada.get('id_usuario'),
            "nombre_usuario": solicitud_encontrada.get('nombre_usuario'),
            "id_herramienta": solicitud_encontrada.get('id_herramienta'),
            "nombre_herramienta": solicitud_encontrada.get('nombre_herramienta'),
            "cantidad": cantidad_solicitada,
            "fecha_devolucion": solicitud_encontrada.get('fecha_devolucion'),
            "estado": "activo",
            "observaciones": ""
        }
        
        # Reducir stock
        herramientas[indice_herramienta]['cantidad'] = herramientas[indice_herramienta]['cantidad'] - cantidad_solicitada
        
        # Cambiar estado de solicitud
        solicitudes[indice_solicitud]['estado'] = 'aprobada'
        
        # Guardar todo
        prestamos.append(nuevo_prestamo)
        
        # Registrar en logs
        log_solicitud_aprobada(
            solicitud_encontrada['id'],
            "ADMIN",
            solicitud_encontrada.get('nombre_usuario'),
            solicitud_encontrada.get('nombre_herramienta'),
            cantidad_solicitada
        )
        
        log_prestamo_creado(
            nuevo_prestamo['id'],
            solicitud_encontrada.get('id_usuario'),
            solicitud_encontrada.get('nombre_usuario'),
            solicitud_encontrada.get('nombre_herramienta'),
            cantidad_solicitada
        )
        
        guardar_datos(prestamos, "prestamos.json")
        guardar_datos(solicitudes, "solicitudes.json")
        guardar_datos(herramientas, "herramientas.json")
        
        print()
        linea(70, VERDE)
        print(f"{VERDE}{NEGRITA}✓ SOLICITUD APROBADA Y PRESTAMO CREADO{RESET}")
        linea(70, VERDE)
        print(f"\n  {CYAN}ID Prestamo:{RESET} {nuevo_prestamo['id']}")
        print(f"  {CYAN}Usuario:{RESET} {nuevo_prestamo['nombre_usuario']}")
        print(f"  {CYAN}Herramienta:{RESET} {nuevo_prestamo['nombre_herramienta']}")
        print(f"  {CYAN}Cantidad:{RESET} {cantidad_solicitada} unidades")
        print(f"  {CYAN}Stock restante:{RESET} {herramientas[indice_herramienta]['cantidad']} unidades")
        
    elif accion == "2":
        # RECHAZAR
        solicitudes[indice_solicitud]['estado'] = 'rechazada'
        
        # Registrar en logs
        log_solicitud_rechazada(
            solicitud_encontrada['id'],
            "ADMIN",
            solicitud_encontrada.get('nombre_usuario'),
            solicitud_encontrada.get('nombre_herramienta'),
            "Rechazado por administrador"
        )
        
        guardar_datos(solicitudes, "solicitudes.json")
        
        print()
        linea(70, ROJO)
        print(f"{ROJO}{NEGRITA}✗ SOLICITUD RECHAZADA{RESET}")
        linea(70, ROJO)
        print(f"\n{CYAN}La solicitud ha sido rechazada. El usuario sera notificado.{RESET}")
        
    else:
        print(f"\n{CYAN}Accion cancelada.{RESET}")


def devolver_herramienta():
    """Registra la devolución de una herramienta"""
    limpiar_pantalla()
    titulo("DEVOLVER HERRAMIENTA")
    print()
    
    prestamos = cargar_datos("prestamos.json")
    herramientas = cargar_datos("herramientas.json")
    
    # Filtrar préstamos activos
    activos = []
    for p in prestamos:
        if p.get('estado') == 'activo':
            activos.append(p)
    
    if len(activos) == 0:
        print(f"{AMARILLO}No hay prestamos activos.{RESET}")
        return
    
    # Mostrar préstamos activos
    print(f"{CYAN}--- PRESTAMOS ACTIVOS ---{RESET}")
    numero = 1
    for p in activos:
        nombre_usuario = p.get('nombre_usuario', 'Usuario desconocido')
        nombre_herramienta = p.get('nombre_herramienta', 'Herramienta desconocida')
        cantidad = p.get('cantidad', 1)
        
        print(f"{numero}. ID: {p['id']} - {nombre_usuario} - {nombre_herramienta} ({cantidad} unidades)")
        numero = numero + 1
    
    print()
    id_prestamo = input(f"{CYAN}Ingrese el ID del prestamo a devolver: {RESET}")
    
    # Buscar el préstamo
    prestamo_encontrado = None
    indice_prestamo = -1
    for i, p in enumerate(prestamos):
        if p['id'] == id_prestamo and p.get('estado') == 'activo':
            prestamo_encontrado = p
            indice_prestamo = i
            break
    
    if prestamo_encontrado is None:
        print(f"\n{ROJO}Prestamo no encontrado o ya fue devuelto.{RESET}")
        return
    
    # Mostrar detalles
    print()
    linea(70, CYAN)
    print(f"{CYAN}{NEGRITA}DETALLES DEL PRESTAMO{RESET}")
    linea(70, CYAN)
    print(f"\n  {CYAN}ID Prestamo:{RESET} {prestamo_encontrado['id']}")
    print(f"  {CYAN}Usuario:{RESET} {prestamo_encontrado.get('nombre_usuario', 'No especificado')}")
    print(f"  {CYAN}Herramienta:{RESET} {prestamo_encontrado.get('nombre_herramienta', 'No especificada')}")
    print(f"  {CYAN}Cantidad:{RESET} {prestamo_encontrado.get('cantidad', 1)} unidades")
    print(f"  {CYAN}Fecha devolucion:{RESET} {prestamo_encontrado.get('fecha_devolucion', 'No especificada')}")
    
    print()
    confirmacion = input(f"{AZUL_BRILLANTE}¿Confirmar devolucion? (s/n): {RESET}").lower()
    
    if confirmacion != 's':
        print(f"\n{CYAN}Devolucion cancelada.{RESET}")
        return
    
    # Buscar la herramienta y restaurar stock
    id_herramienta = prestamo_encontrado.get('id_herramienta')
    cantidad_devolver = prestamo_encontrado.get('cantidad', 1)
    
    herramienta_encontrada = False
    for i, h in enumerate(herramientas):
        if h['id'] == id_herramienta:
            herramientas[i]['cantidad'] = herramientas[i]['cantidad'] + cantidad_devolver
            herramienta_encontrada = True
            break
    
    if not herramienta_encontrada:
        print(f"\n{ROJO}Error: No se pudo encontrar la herramienta en el inventario.{RESET}")
        return
    
    # Cambiar estado del préstamo
    prestamos[indice_prestamo]['estado'] = 'devuelto'
    
    # Registrar en logs
    log_devolucion(
        prestamo_encontrado['id'],
        prestamo_encontrado.get('id_usuario'),
        prestamo_encontrado.get('nombre_usuario'),
        prestamo_encontrado.get('nombre_herramienta'),
        cantidad_devolver
    )
    
    # Guardar cambios
    guardar_datos(prestamos, "prestamos.json")
    guardar_datos(herramientas, "herramientas.json")
    
    print()
    linea(70, VERDE)
    print(f"{VERDE}{NEGRITA}✓ DEVOLUCION REGISTRADA EXITOSAMENTE{RESET}")
    linea(70, VERDE)
    print(f"\n  {CYAN}Herramienta devuelta:{RESET} {prestamo_encontrado.get('nombre_herramienta', 'No especificada')}")
    print(f"  {CYAN}Cantidad:{RESET} {cantidad_devolver} unidades")
    print(f"  {CYAN}Stock actualizado correctamente{RESET}")


def ver_prestamos_activos():
    """Muestra todos los préstamos activos"""
    limpiar_pantalla()
    titulo("PRESTAMOS ACTIVOS")
    print()
    
    prestamos = cargar_datos("prestamos.json")
    
    # Filtrar solo los activos
    activos = []
    for p in prestamos:
        if p.get("estado") == "activo":
            activos.append(p)
    
    if len(activos) == 0:
        print(f"{AMARILLO}No hay prestamos activos en este momento.{RESET}")
        return
    
    print(f"{CYAN}Total de prestamos activos: {NEGRITA}{len(activos)}{RESET}")
    print()
    linea(70, AZUL_CLARO)
    
    numero = 1
    for prestamo in activos:
        print()
        print(f"{AZUL_BRILLANTE}▶ Prestamo #{numero}{RESET}")
        print(f"  {CYAN}ID:{RESET} {prestamo['id']}")
        print(f"  {CYAN}Usuario:{RESET} {prestamo.get('nombre_usuario', 'No especificado')}")
        print(f"  {CYAN}Herramienta:{RESET} {prestamo.get('nombre_herramienta', 'No especificada')}")
        print(f"  {CYAN}Cantidad:{RESET} {prestamo.get('cantidad', 1)} unidades")
        print(f"  {CYAN}Fecha devolucion:{RESET} {prestamo.get('fecha_devolucion', 'No especificada')}")
        
        if prestamo.get('observaciones'):
            print(f"  {CYAN}Observaciones:{RESET} {prestamo['observaciones']}")
        
        print(f"  {CYAN}Estado:{RESET} {VERDE}{prestamo['estado']}{RESET}")
        
        if numero < len(activos):
            print(f"{AZUL_CLARO}{'┄' * 70}{RESET}")
        
        numero = numero + 1
    
    print()
    linea(70, AZUL_CLARO)


def ver_historial_completo():
    """Muestra el historial completo de préstamos y solicitudes"""
    limpiar_pantalla()
    titulo("HISTORIAL COMPLETO")
    print()
    
    prestamos = cargar_datos("prestamos.json")
    solicitudes = cargar_datos("solicitudes.json")
    
    print(f"{CYAN}Total de prestamos: {NEGRITA}{len(prestamos)}{RESET}")
    print(f"{CYAN}Total de solicitudes: {NEGRITA}{len(solicitudes)}{RESET}")
    print()
    
    # Mostrar préstamos
    if len(prestamos) > 0:
        linea(70, AZUL_CLARO)
        print(f"\n{AZUL_BRILLANTE}PRESTAMOS:{RESET}\n")
        
        numero = 1
        for p in prestamos:
            estado = p.get('estado', 'activo')
            if estado == 'activo':
                color_estado = VERDE
            else:
                color_estado = AZUL_CLARO
            
            print(f"{numero}. ID: {p['id']} - {p.get('nombre_usuario', 'Usuario')} - {p.get('nombre_herramienta', 'Herramienta')} - Estado: {color_estado}{estado}{RESET}")
            numero = numero + 1
    
    # Mostrar solicitudes
    if len(solicitudes) > 0:
        print()
        linea(70, AZUL_CLARO)
        print(f"\n{AZUL_BRILLANTE}SOLICITUDES:{RESET}\n")
        
        numero = 1
        for s in solicitudes:
            estado = s.get('estado', 'pendiente')
            if estado == 'aprobada':
                color = VERDE
            elif estado == 'pendiente':
                color = AMARILLO
            else:
                color = ROJO
            
            print(f"{numero}. ID: {s['id']} - {s.get('nombre_usuario', 'Usuario')} - {s.get('nombre_herramienta', 'Herramienta')} - Estado: {color}{estado}{RESET}")
            numero = numero + 1
    
    print()
    linea(70, AZUL_CLARO)
    
    # Estadísticas
    print()
    print(f"{AZUL_BRILLANTE}ESTADISTICAS:{RESET}")
    
    # Préstamos
    activos = 0
    devueltos = 0
    for p in prestamos:
        if p.get('estado') == 'activo':
            activos = activos + 1
        elif p.get('estado') == 'devuelto':
            devueltos = devueltos + 1
    
    # Solicitudes
    pendientes = 0
    aprobadas = 0
    rechazadas = 0
    for s in solicitudes:
        estado = s.get('estado', 'pendiente')
        if estado == 'pendiente':
            pendientes = pendientes + 1
        elif estado == 'aprobada':
            aprobadas = aprobadas + 1
        elif estado == 'rechazada':
            rechazadas = rechazadas + 1
    
    print(f"\n{CYAN}Prestamos:{RESET}")
    print(f"  {VERDE}● Activos:{RESET} {activos}")
    print(f"  {AZUL_CLARO}● Devueltos:{RESET} {devueltos}")
    
    print(f"\n{CYAN}Solicitudes:{RESET}")
    print(f"  {AMARILLO}● Pendientes:{RESET} {pendientes}")
    print(f"  {VERDE}● Aprobadas:{RESET} {aprobadas}")
    print(f"  {ROJO}● Rechazadas:{RESET} {rechazadas}")
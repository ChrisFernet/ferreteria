from json_config import cargar_datos
from estilos import *

# ========================================
# MENÚ PRINCIPAL DE REPORTES
# ========================================

def consultas_y_reportes():
    """Menú principal de consultas y reportes para administradores"""
    while True:
        limpiar_pantalla()
        titulo("CONSULTAS Y REPORTES")
        print()
        
        print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Herramientas con stock bajo{RESET}")
        print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Prestamos activos y vencidos{RESET}")
        print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Historial de prestamos de un usuario{RESET}")
        print(f"{AZUL_CLARO}  4.{RESET} {BLANCO}Herramientas mas solicitadas{RESET}")
        print(f"{AZUL_CLARO}  5.{RESET} {BLANCO}Usuarios que mas herramientas han solicitado{RESET}")
        print(f"{AZUL_CLARO}  6.{RESET} {BLANCO}Reporte general del sistema{RESET}")
        print(f"{AZUL_CLARO}  7.{RESET} {BLANCO}Volver al menu principal{RESET}")
        
        print()
        linea()
        
        opcion = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion == "1":
            herramientas_stock_bajo()
            pausa()
            
        elif opcion == "2":
            prestamos_activos_vencidos()
            pausa()
            
        elif opcion == "3":
            historial_usuario()
            pausa()
            
        elif opcion == "4":
            herramientas_mas_solicitadas()
            pausa()
            
        elif opcion == "5":
            usuarios_mas_activos()
            pausa()
            
        elif opcion == "6":
            reporte_general()
            pausa()
            
        elif opcion == "7":
            print(f"\n{CYAN}Volviendo al menu principal...{RESET}")
            break
            
        else:
            mensaje_error("Opcion no valida. Intente de nuevo.")
            pausa()


# ========================================
# 1. REPORTE: HERRAMIENTAS CON STOCK BAJO
# ========================================

def herramientas_stock_bajo():
    """Muestra herramientas con stock bajo (menos de 3 unidades)"""
    limpiar_pantalla()
    titulo("HERRAMIENTAS CON STOCK BAJO")
    print()
    
    # Cargar herramientas
    herramientas = cargar_datos("herramientas.json")
    
    # Preguntar cuál es el límite de stock bajo
    print(f"{CYAN}Stock bajo predeterminado: menos de 3 unidades{RESET}")
    limite = input(f"{CYAN}Ingrese limite personalizado (Enter para usar 3): {RESET}")
    
    # Si el usuario no ingresó nada, usar 3 como límite
    if limite == "":
        limite = 3
    else:
        limite = int(limite)
    
    # Buscar herramientas con stock bajo
    stock_bajo = []
    for herramienta in herramientas:
        cantidad = herramienta.get('cantidad', 0)
        if cantidad < limite:
            stock_bajo.append(herramienta)
    
    # Si no hay ninguna con stock bajo
    if len(stock_bajo) == 0:
        mensaje_exito(f"Todas las herramientas tienen stock suficiente (>= {limite} unidades).")
        return
    
    # Mostrar las herramientas con stock bajo
    print()
    linea(70, AMARILLO)
    print(f"{AMARILLO}{NEGRITA}⚠ SE ENCONTRARON {len(stock_bajo)} HERRAMIENTA(S) CON STOCK BAJO{RESET}")
    linea(70, AMARILLO)
    print()
    
    numero = 1
    for h in stock_bajo:
        cantidad = h.get('cantidad', 0)
        
        # Decidir el color según qué tan crítico es
        if cantidad == 0:
            color_stock = ROJO
            simbolo = "✗"
        elif cantidad < 2:
            color_stock = ROJO
            simbolo = "⚠"
        else:
            color_stock = AMARILLO
            simbolo = "⚠"
        
        print(f"{AZUL_BRILLANTE}▶ Herramienta #{numero}{RESET}")
        print(f"  {CYAN}ID:{RESET} {h['id']}")
        print(f"  {CYAN}Nombre:{RESET} {NEGRITA}{h['nombre']}{RESET}")
        print(f"  {CYAN}Categoria:{RESET} {h['categoria']}")
        print(f"  {CYAN}Stock:{RESET} {color_stock}{simbolo} {cantidad} unidades{RESET}")
        print(f"  {CYAN}Estado:{RESET} {h.get('estado', 'No especificado')}")
        
        if cantidad == 0:
            print(f"  {ROJO}CRÍTICO: Sin stock disponible{RESET}")
        
        if numero < len(stock_bajo):
            print(f"{AZUL_CLARO}{'┄' * 70}{RESET}")
            print()
        
        numero = numero + 1
    
    print()
    linea(70, AMARILLO)
    
    # Contar cuántas no tienen stock
    sin_stock = 0
    for h in stock_bajo:
        if h.get('cantidad', 0) == 0:
            sin_stock = sin_stock + 1
    
    # Mostrar resumen
    print()
    print(f"{AZUL_BRILLANTE}RESUMEN:{RESET}")
    print(f"  {ROJO}● Sin stock (0 unidades):{RESET} {sin_stock}")
    print(f"  {AMARILLO}● Stock bajo (< {limite} unidades):{RESET} {len(stock_bajo)}")


# ========================================
# 2. REPORTE: PRÉSTAMOS ACTIVOS Y VENCIDOS
# ========================================

def prestamos_activos_vencidos():
    """Muestra préstamos activos y detecta los vencidos"""
    limpiar_pantalla()
    titulo("PRESTAMOS ACTIVOS Y VENCIDOS")
    print()
    
    # Cargar préstamos
    prestamos = cargar_datos("prestamos.json")
    
    # Filtrar solo los activos
    activos = []
    for p in prestamos:
        if p.get('estado') == 'activo':
            activos.append(p)
    
    if len(activos) == 0:
        mensaje_info("No hay prestamos activos en este momento.")
        return
    
    # Pedir fecha actual para comparar
    fecha_hoy = input(f"{CYAN}Ingrese la fecha de hoy (YYYY-MM-DD, ej: 2026-02-15): {RESET}")
    
    # Si no ingresó nada, usar una fecha de ejemplo
    if fecha_hoy == "":
        fecha_hoy = "2026-02-15"
    
    # Separar préstamos vencidos y al día
    vencidos = []
    al_dia = []
    
    for p in activos:
        fecha_devolucion = p.get('fecha_devolucion', '')
        
        # Comparar fechas (formato: YYYY-MM-DD)
        # Si fecha_devolucion < fecha_hoy, está vencido
        if fecha_devolucion < fecha_hoy:
            vencidos.append(p)
        else:
            al_dia.append(p)
    
    # Mostrar préstamos VENCIDOS
    if len(vencidos) > 0:
        print()
        linea(70, ROJO)
        print(f"{ROJO}{NEGRITA}⚠ PRESTAMOS VENCIDOS: {len(vencidos)}{RESET}")
        linea(70, ROJO)
        print()
        
        numero = 1
        for p in vencidos:
            print(f"{ROJO}▶ Préstamo #{numero} - VENCIDO{RESET}")
            print(f"  {CYAN}ID:{RESET} {p['id']}")
            print(f"  {CYAN}Usuario:{RESET} {p.get('nombre_usuario', 'No especificado')}")
            print(f"  {CYAN}Herramienta:{RESET} {p.get('nombre_herramienta', 'No especificada')}")
            print(f"  {CYAN}Cantidad:{RESET} {p.get('cantidad', 1)} unidades")
            print(f"  {CYAN}Fecha devolucion:{RESET} {p.get('fecha_devolucion', 'No especificada')}")
            
            if numero < len(vencidos):
                print(f"{ROJO}{'┄' * 70}{RESET}")
                print()
            
            numero = numero + 1
    
    # Mostrar préstamos AL DÍA
    if len(al_dia) > 0:
        print()
        linea(70, VERDE)
        print(f"{VERDE}{NEGRITA}✓ PRESTAMOS AL DIA: {len(al_dia)}{RESET}")
        linea(70, VERDE)
        print()
        
        numero = 1
        for p in al_dia:
            print(f"{VERDE}▶ Préstamo #{numero}{RESET}")
            print(f"  {CYAN}ID:{RESET} {p['id']}")
            print(f"  {CYAN}Usuario:{RESET} {p.get('nombre_usuario', 'No especificado')}")
            print(f"  {CYAN}Herramienta:{RESET} {p.get('nombre_herramienta', 'No especificada')}")
            print(f"  {CYAN}Cantidad:{RESET} {p.get('cantidad', 1)} unidades")
            print(f"  {CYAN}Fecha devolucion:{RESET} {p.get('fecha_devolucion', 'No especificada')}")
            
            if numero < len(al_dia):
                print(f"{AZUL_CLARO}{'┄' * 70}{RESET}")
                print()
            
            numero = numero + 1
    
    # Mostrar resumen
    print()
    linea(70, AZUL_CLARO)
    print()
    print(f"{AZUL_BRILLANTE}RESUMEN:{RESET}")
    print(f"  {VERDE}● Prestamos al dia:{RESET} {len(al_dia)}")
    print(f"  {ROJO}● Prestamos vencidos:{RESET} {len(vencidos)}")
    print(f"  {CYAN}● Total activos:{RESET} {len(activos)}")


# ========================================
# 3. REPORTE: HISTORIAL DE UN USUARIO
# ========================================

def historial_usuario():
    """Muestra el historial completo de préstamos de un usuario específico"""
    limpiar_pantalla()
    titulo("HISTORIAL DE PRESTAMOS POR USUARIO")
    print()
    
    # Cargar datos
    usuarios = cargar_datos("usuarios.json")
    prestamos = cargar_datos("prestamos.json")
    solicitudes = cargar_datos("solicitudes.json")
    
    if len(usuarios) == 0:
        mensaje_advertencia("No hay usuarios registrados.")
        return
    
    # Mostrar lista de usuarios
    print(f"{CYAN}--- USUARIOS REGISTRADOS ---{RESET}")
    numero = 1
    for u in usuarios:
        print(f"{numero}. ID: {u['id']} - {u['nombre']} {u['apellido']}")
        numero = numero + 1
    
    print()
    id_usuario = input(f"{CYAN}Ingrese el ID del usuario: {RESET}")
    
    # Buscar el usuario
    usuario_encontrado = None
    for u in usuarios:
        if u['id'] == id_usuario:
            usuario_encontrado = u
            break
    
    if usuario_encontrado is None:
        mensaje_error("Usuario no encontrado.")
        return
    
    # Buscar préstamos del usuario
    prestamos_usuario = []
    for p in prestamos:
        if p.get('id_usuario') == id_usuario:
            prestamos_usuario.append(p)
    
    # Buscar solicitudes del usuario
    solicitudes_usuario = []
    for s in solicitudes:
        if s.get('id_usuario') == id_usuario:
            solicitudes_usuario.append(s)
    
    # Mostrar información del usuario
    print()
    linea(70, CYAN)
    print(f"{CYAN}{NEGRITA}HISTORIAL DE: {usuario_encontrado['nombre']} {usuario_encontrado['apellido']}{RESET}")
    linea(70, CYAN)
    print(f"\n  {CYAN}ID:{RESET} {usuario_encontrado['id']}")
    print(f"  {CYAN}Tipo:{RESET} {usuario_encontrado['tipo']}")
    print(f"  {CYAN}Total de prestamos:{RESET} {len(prestamos_usuario)}")
    print(f"  {CYAN}Total de solicitudes:{RESET} {len(solicitudes_usuario)}")
    
    # Mostrar préstamos
    if len(prestamos_usuario) > 0:
        print()
        linea(70, AZUL_CLARO)
        print(f"\n{AZUL_BRILLANTE}PRESTAMOS:{RESET}\n")
        
        numero = 1
        for p in prestamos_usuario:
            estado = p.get('estado', 'activo')
            
            # Color según el estado
            if estado == 'activo':
                color_estado = VERDE
            else:
                color_estado = AZUL_CLARO
            
            print(f"{numero}. {p.get('nombre_herramienta', 'Herramienta')} - "
                  f"Fecha dev: {p.get('fecha_devolucion', 'N/A')} - "
                  f"Estado: {color_estado}{estado}{RESET}")
            numero = numero + 1
    else:
        mensaje_advertencia("Este usuario no tiene prestamos registrados.")
    
    # Mostrar solicitudes
    if len(solicitudes_usuario) > 0:
        print()
        linea(70, AZUL_CLARO)
        print(f"\n{AZUL_BRILLANTE}SOLICITUDES:{RESET}\n")
        
        numero = 1
        for s in solicitudes_usuario:
            estado = s.get('estado', 'pendiente')
            
            # Color según el estado
            if estado == 'aprobada':
                color_estado = VERDE
            elif estado == 'pendiente':
                color_estado = AMARILLO
            else:
                color_estado = ROJO
            
            print(f"{numero}. {s.get('nombre_herramienta', 'Herramienta')} - "
                  f"Cantidad: {s.get('cantidad', 1)} - "
                  f"Estado: {color_estado}{estado}{RESET}")
            numero = numero + 1


# ========================================
# 4. REPORTE: HERRAMIENTAS MÁS SOLICITADAS
# ========================================

def herramientas_mas_solicitadas():
    """Muestra las herramientas más solicitadas por la comunidad"""
    limpiar_pantalla()
    titulo("HERRAMIENTAS MAS SOLICITADAS")
    print()
    
    # Cargar solicitudes
    solicitudes = cargar_datos("solicitudes.json")
    
    if len(solicitudes) == 0:
        mensaje_advertencia("No hay datos suficientes para generar el reporte.")
        return
    
    # Contar cuántas veces se solicitó cada herramienta
    # Usamos un diccionario: {id_herramienta: cantidad_de_veces}
    contador = {}
    nombres = {}  # Para guardar el nombre de cada herramienta
    
    for s in solicitudes:
        id_herramienta = s.get('id_herramienta', 'N/A')
        nombre_herramienta = s.get('nombre_herramienta', 'No especificada')
        
        # Si es la primera vez que vemos esta herramienta
        if id_herramienta not in contador:
            contador[id_herramienta] = 0
            nombres[id_herramienta] = nombre_herramienta
        
        # Incrementar el contador
        contador[id_herramienta] = contador[id_herramienta] + 1
    
    # Convertir el diccionario a una lista para poder ordenarla
    ranking = []
    for id_herr in contador:
        ranking.append({
            'id': id_herr,
            'nombre': nombres[id_herr],
            'solicitudes': contador[id_herr]
        })
    
    # Ordenar de mayor a menor
    # (Usamos una función lambda para decirle que ordene por 'solicitudes')
    ranking.sort(key=lambda x: x['solicitudes'], reverse=True)
    
    # Mostrar el TOP 10
    print(f"{CYAN}Total de herramientas diferentes solicitadas: {NEGRITA}{len(ranking)}{RESET}")
    print()
    linea(70, AZUL_CLARO)
    print()
    
    top = 10
    if len(ranking) < 10:
        top = len(ranking)
    
    print(f"{AZUL_BRILLANTE}TOP {top} HERRAMIENTAS MAS SOLICITADAS:{RESET}")
    print()
    
    for i in range(top):
        h = ranking[i]
        
        # Poner medallas para el top 3
        if i == 0:
            medalla = "🥇"
        elif i == 1:
            medalla = "🥈"
        elif i == 2:
            medalla = "🥉"
        else:
            medalla = f"{i + 1}."
        
        print(f"{medalla} {NEGRITA}{h['nombre']}{RESET}")
        print(f"   {CYAN}Numero de solicitudes:{RESET} {h['solicitudes']}")
        
        if i < top - 1:
            print()


# ========================================
# 5. REPORTE: USUARIOS MÁS ACTIVOS
# ========================================

def usuarios_mas_activos():
    """Muestra los usuarios que más herramientas han solicitado"""
    limpiar_pantalla()
    titulo("USUARIOS MAS ACTIVOS")
    print()
    
    # Cargar solicitudes
    solicitudes = cargar_datos("solicitudes.json")
    
    if len(solicitudes) == 0:
        mensaje_advertencia("No hay solicitudes registradas.")
        return
    
    # Contar cuántas solicitudes hizo cada usuario
    contador = {}
    nombres = {}
    
    for s in solicitudes:
        id_usuario = s.get('id_usuario', 'N/A')
        nombre_usuario = s.get('nombre_usuario', 'Usuario desconocido')
        
        # Si es la primera vez que vemos este usuario
        if id_usuario not in contador:
            contador[id_usuario] = 0
            nombres[id_usuario] = nombre_usuario
        
        # Incrementar el contador
        contador[id_usuario] = contador[id_usuario] + 1
    
    # Convertir a lista
    ranking = []
    for id_usr in contador:
        ranking.append({
            'id': id_usr,
            'nombre': nombres[id_usr],
            'total': contador[id_usr]
        })
    
    # Ordenar de mayor a menor
    ranking.sort(key=lambda x: x['total'], reverse=True)
    
    # Mostrar el TOP 10
    print(f"{CYAN}Total de usuarios que han solicitado: {NEGRITA}{len(ranking)}{RESET}")
    print()
    linea(70, AZUL_CLARO)
    print()
    
    top = 10
    if len(ranking) < 10:
        top = len(ranking)
    
    print(f"{AZUL_BRILLANTE}TOP {top} USUARIOS MAS ACTIVOS:{RESET}")
    print()
    
    for i in range(top):
        u = ranking[i]
        
        # Poner medallas para el top 3
        if i == 0:
            medalla = "🥇"
        elif i == 1:
            medalla = "🥈"
        elif i == 2:
            medalla = "🥉"
        else:
            medalla = f"{i + 1}."
        
        print(f"{medalla} {NEGRITA}{u['nombre']}{RESET} (ID: {u['id']})")
        print(f"   {CYAN}Total de solicitudes:{RESET} {u['total']}")
        
        if i < top - 1:
            print()


# ========================================
# 6. REPORTE GENERAL DEL SISTEMA
# ========================================

def reporte_general():
    """Genera un reporte general completo del sistema"""
    limpiar_pantalla()
    titulo("REPORTE GENERAL DEL SISTEMA")
    print()
    
    # Cargar todos los datos
    herramientas = cargar_datos("herramientas.json")
    usuarios = cargar_datos("usuarios.json")
    prestamos = cargar_datos("prestamos.json")
    solicitudes = cargar_datos("solicitudes.json")
    
    # ===== SECCIÓN 1: HERRAMIENTAS =====
    linea(70, CYAN)
    print(f"\n{CYAN}{NEGRITA}📦 INVENTARIO DE HERRAMIENTAS{RESET}\n")
    
    total_herramientas = len(herramientas)
    total_unidades = 0
    valor_total = 0
    
    # Sumar todas las cantidades y valores
    for h in herramientas:
        total_unidades = total_unidades + h.get('cantidad', 0)
        valor_total = valor_total + h.get('valor_estimado', 0)
    
    # Contar por estado
    activas = 0
    en_reparacion = 0
    fuera_servicio = 0
    
    for h in herramientas:
        estado = h.get('estado', '').lower()
        if estado == 'activa':
            activas = activas + 1
        elif 'reparacion' in estado:
            en_reparacion = en_reparacion + 1
        elif 'fuera' in estado:
            fuera_servicio = fuera_servicio + 1
    
    # Contar stock bajo
    stock_bajo = 0
    sin_stock = 0
    
    for h in herramientas:
        cantidad = h.get('cantidad', 0)
        if cantidad < 3:
            stock_bajo = stock_bajo + 1
        if cantidad == 0:
            sin_stock = sin_stock + 1
    
    # Mostrar datos de herramientas
    print(f"  {CYAN}Total de herramientas diferentes:{RESET} {total_herramientas}")
    print(f"  {CYAN}Total de unidades disponibles:{RESET} {total_unidades}")
    print(f"  {CYAN}Valor total del inventario:{RESET} ${valor_total:,.2f}")
    print()
    print(f"  {VERDE}● Activas:{RESET} {activas}")
    print(f"  {AMARILLO}● En reparacion:{RESET} {en_reparacion}")
    print(f"  {ROJO}● Fuera de servicio:{RESET} {fuera_servicio}")
    print()
    print(f"  {AMARILLO}⚠ Stock bajo (< 3):{RESET} {stock_bajo}")
    print(f"  {ROJO}⚠ Sin stock:{RESET} {sin_stock}")
    
    # ===== SECCIÓN 2: USUARIOS =====
    print()
    linea(70, CYAN)
    print(f"\n{CYAN}{NEGRITA}👥 USUARIOS{RESET}\n")
    
    total_usuarios = len(usuarios)
    administradores = 0
    residentes = 0
    
    for u in usuarios:
        tipo = u.get('tipo', '').lower()
        if tipo == 'administrador':
            administradores = administradores + 1
        else:
            residentes = residentes + 1
    
    print(f"  {CYAN}Total de usuarios:{RESET} {total_usuarios}")
    print(f"  {VERDE}● Administradores:{RESET} {administradores}")
    print(f"  {AZUL_CLARO}● Residentes:{RESET} {residentes}")
    
    # ===== SECCIÓN 3: PRÉSTAMOS =====
    print()
    linea(70, CYAN)
    print(f"\n{CYAN}{NEGRITA}📋 PRESTAMOS{RESET}\n")
    
    total_prestamos = len(prestamos)
    prestamos_activos = 0
    prestamos_devueltos = 0
    
    for p in prestamos:
        estado = p.get('estado')
        if estado == 'activo':
            prestamos_activos = prestamos_activos + 1
        elif estado == 'devuelto':
            prestamos_devueltos = prestamos_devueltos + 1
    
    print(f"  {CYAN}Total de prestamos:{RESET} {total_prestamos}")
    print(f"  {VERDE}● Activos:{RESET} {prestamos_activos}")
    print(f"  {AZUL_CLARO}● Devueltos:{RESET} {prestamos_devueltos}")
    
    # ===== SECCIÓN 4: SOLICITUDES =====
    print()
    linea(70, CYAN)
    print(f"\n{CYAN}{NEGRITA}📝 SOLICITUDES{RESET}\n")
    
    total_solicitudes = len(solicitudes)
    pendientes = 0
    aprobadas = 0
    rechazadas = 0
    
    for s in solicitudes:
        estado = s.get('estado')
        if estado == 'pendiente':
            pendientes = pendientes + 1
        elif estado == 'aprobada':
            aprobadas = aprobadas + 1
        elif estado == 'rechazada':
            rechazadas = rechazadas + 1
    
    print(f"  {CYAN}Total de solicitudes:{RESET} {total_solicitudes}")
    print(f"  {AMARILLO}● Pendientes:{RESET} {pendientes}")
    print(f"  {VERDE}● Aprobadas:{RESET} {aprobadas}")
    print(f"  {ROJO}● Rechazadas:{RESET} {rechazadas}")
    
    # ===== RESUMEN FINAL =====
    print()
    linea(70, VERDE)
    print(f"\n{VERDE}{NEGRITA}✓ ESTADO DEL SISTEMA{RESET}\n")
    
    # Mostrar alertas si hay
    if pendientes > 0:
        print(f"  {AMARILLO}⚠ Hay {pendientes} solicitud(es) pendiente(s) de revision{RESET}")
    
    if stock_bajo > 0:
        print(f"  {AMARILLO}⚠ Hay {stock_bajo} herramienta(s) con stock bajo{RESET}")
    
    if sin_stock > 0:
        print(f"  {ROJO}⚠ Hay {sin_stock} herramienta(s) sin stock{RESET}")
    
    if prestamos_activos > 0:
        print(f"  {CYAN}ℹ Hay {prestamos_activos} prestamo(s) activo(s){RESET}")
    
    # Si todo está bien
    if pendientes == 0 and stock_bajo == 0 and sin_stock == 0:
        print(f"  {VERDE}✓ El sistema está funcionando correctamente{RESET}")
    
    print()
    linea(70, VERDE)
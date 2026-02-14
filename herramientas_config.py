from json_config import cargar_datos, guardar_datos
from estilos import *
from logs import *  

def gestionar_herramientas():
    """Menú principal de gestión de herramientas"""
    herramientas = cargar_datos("herramientas.json")
    
    while True:
        limpiar_pantalla()
        titulo("GESTION DE HERRAMIENTAS")
        print()
        
        print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Agregar herramienta{RESET}")
        print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Mostrar todas las herramientas{RESET}")
        print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Buscar herramienta{RESET}")
        print(f"{AZUL_CLARO}  4.{RESET} {BLANCO}Actualizar herramienta{RESET}")
        print(f"{AZUL_CLARO}  5.{RESET} {BLANCO}Eliminar herramienta{RESET}")
        print(f"{AZUL_CLARO}  6.{RESET} {BLANCO}Volver al menu principal{RESET}")
        
        print()
        linea()
        
        opcion = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion == "1":
            agregar_herramienta(herramientas)
            guardar_datos(herramientas, "herramientas.json")
            pausa()
            
        elif opcion == "2":
            mostrar_herramientas(herramientas)
            pausa()
            
        elif opcion == "3":
            buscar_herramienta(herramientas)
            pausa()
            
        elif opcion == "4":
            actualizar_herramienta(herramientas)
            guardar_datos(herramientas, "herramientas.json")
            pausa()
            
        elif opcion == "5":
            eliminar_herramienta(herramientas)
            guardar_datos(herramientas, "herramientas.json")
            pausa()
            
        elif opcion == "6":
            print(f"\n{CYAN}Volviendo al menu principal...{RESET}")
            break
            
        else:
            mensaje_error("Opcion no valida. Intente de nuevo.")
            pausa()


# ========================================
# FUNCIONES DE GESTIÓN
# ========================================

def agregar_herramienta(herramientas):
    """Agrega una nueva herramienta"""
    limpiar_pantalla()
    titulo("AGREGAR NUEVA HERRAMIENTA")
    print()
    
    id = input(f"{CYAN}ID de la herramienta: {RESET}")
    nombre = input(f"{CYAN}Nombre: {RESET}")
    categoria = input(f"{CYAN}Categoria (construccion, jardineria, etc.): {RESET}")
    cantidad = int(input(f"{CYAN}Cantidad disponible: {RESET}"))
    estado = input(f"{CYAN}Estado (activa/en reparacion/fuera de servicio): {RESET}")
    valor_estimado = float(input(f"{CYAN}Valor estimado: ${RESET}"))
    
    herramienta = {
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "estado": estado,
        "valor_estimado": valor_estimado
    }
    
    herramientas.append(herramienta)
    log_agregar_herramienta(id, nombre, cantidad, "ADMIN")
    
    mensaje_exito("Herramienta agregada exitosamente!")


def mostrar_herramientas(herramientas):
    """Muestra todas las herramientas del inventario"""
    limpiar_pantalla()
    titulo("INVENTARIO DE HERRAMIENTAS")
    print()
    
    if len(herramientas) == 0:
        mensaje_advertencia("No hay herramientas registradas en el sistema.")
        return
        
    print(f"{CYAN}Total de herramientas: {NEGRITA}{len(herramientas)}{RESET}")
    print()
    linea(70, AZUL_CLARO)
    
    # Mostrar cada herramienta
    for i, h in enumerate(herramientas, 1):
        print()
        print(f"{AZUL_BRILLANTE}▶ Herramienta #{i}{RESET}")
        print(f"  {CYAN}ID:{RESET} {h['id']}")
        print(f"  {CYAN}Nombre:{RESET} {NEGRITA}{h['nombre']}{RESET}")
        print(f"  {CYAN}Categoria:{RESET} {h['categoria']}")
        print(f"  {CYAN}Cantidad:{RESET} {h['cantidad']} unidades")
        
        # Color dependiendo del estado
        if h['estado'].lower() == 'activa':
            color_estado = VERDE
        elif h['estado'].lower() == 'en reparacion':
            color_estado = AMARILLO
        else:
            color_estado = ROJO
        
        print(f"  {CYAN}Estado:{RESET} {color_estado}{h['estado']}{RESET}")
        print(f"  {CYAN}Valor estimado:{RESET} ${h['valor_estimado']:.2f}")
        
        # Línea separadora
        if i < len(herramientas):
            print(f"{AZUL_CLARO}{'┄' * 70}{RESET}")
    
    print()
    linea(70, AZUL_CLARO)
    
    # Estadísticas
    print()
    print(f"{AZUL_BRILLANTE}ESTADISTICAS:{RESET}")
    
    # Contar herramientas por estado
    activas = sum(1 for h in herramientas if h['estado'].lower() == 'activa')
    en_reparacion = sum(1 for h in herramientas if 'reparacion' in h['estado'].lower())
    fuera_servicio = sum(1 for h in herramientas if 'fuera' in h['estado'].lower())
    
    print(f"  {VERDE}● Activas:{RESET} {activas}")
    print(f"  {AMARILLO}● En reparacion:{RESET} {en_reparacion}")
    print(f"  {ROJO}● Fuera de servicio:{RESET} {fuera_servicio}")
    
    # Valor total del inventario
    valor_total = sum(h['valor_estimado'] for h in herramientas)
    print(f"\n  {CYAN}Valor total del inventario:{RESET} {NEGRITA}${valor_total:.2f}{RESET}")


def buscar_herramienta(herramientas):
    """Busca una herramienta por ID o nombre"""
    limpiar_pantalla()
    titulo("BUSCAR HERRAMIENTA")
    print()
    
    if len(herramientas) == 0:
        mensaje_advertencia("No hay herramientas registradas.")
        return
    
    print(f"{AZUL_CLARO}  1.{RESET} Buscar por ID")
    print(f"{AZUL_CLARO}  2.{RESET} Buscar por nombre")
    print()
    
    opcion = input(f"{AZUL_BRILLANTE}Seleccione opcion: {RESET}")
    
    if opcion == "1":
        id_buscar = input(f"\n{CYAN}Ingrese el ID: {RESET}")
        encontrada = False
        
        for h in herramientas:
            if h["id"] == id_buscar:
                print()
                linea(70, VERDE)
                print(f"{VERDE}{NEGRITA}HERRAMIENTA ENCONTRADA{RESET}")
                linea(70, VERDE)
                print(f"\n  {CYAN}ID:{RESET} {h['id']}")
                print(f"  {CYAN}Nombre:{RESET} {NEGRITA}{h['nombre']}{RESET}")
                print(f"  {CYAN}Categoria:{RESET} {h['categoria']}")
                print(f"  {CYAN}Cantidad:{RESET} {h['cantidad']} unidades")
                print(f"  {CYAN}Estado:{RESET} {h['estado']}")
                print(f"  {CYAN}Valor estimado:{RESET} ${h['valor_estimado']:.2f}")
                encontrada = True
                break
        
        if not encontrada:
            mensaje_error("Herramienta no encontrada.")
    
    elif opcion == "2":
        nombre_buscar = input(f"\n{CYAN}Ingrese el nombre: {RESET}").lower()
        encontradas = [h for h in herramientas if nombre_buscar in h["nombre"].lower()]
        
        if encontradas:
            print()
            linea(70, VERDE)
            print(f"{VERDE}{NEGRITA}SE ENCONTRARON {len(encontradas)} HERRAMIENTA(S){RESET}")
            linea(70, VERDE)
            
            for h in encontradas:
                print(f"\n  {CYAN}ID:{RESET} {h['id']} | {CYAN}Nombre:{RESET} {h['nombre']} | {CYAN}Cantidad:{RESET} {h['cantidad']}")
        else:
            mensaje_error("No se encontraron herramientas con ese nombre.")
    else:
        mensaje_error("Opcion no valida.")


def actualizar_herramienta(herramientas):
    """Actualiza los datos de una herramienta"""
    limpiar_pantalla()
    titulo("ACTUALIZAR HERRAMIENTA")
    print()
    
    if len(herramientas) == 0:
        mensaje_advertencia("No hay herramientas registradas.")
        return
    
    id_actualizar = input(f"{CYAN}Ingrese el ID de la herramienta a actualizar: {RESET}")
    
    for h in herramientas:
        if h["id"] == id_actualizar:
            print()
            linea(70, VERDE)
            print(f"{VERDE}Herramienta encontrada: {NEGRITA}{h['nombre']}{RESET}")
            linea(70, VERDE)
            print()
            
            print(f"{AZUL_CLARO}  1.{RESET} Nombre")
            print(f"{AZUL_CLARO}  2.{RESET} Categoria")
            print(f"{AZUL_CLARO}  3.{RESET} Cantidad")
            print(f"{AZUL_CLARO}  4.{RESET} Estado")
            print(f"{AZUL_CLARO}  5.{RESET} Valor estimado")
            print(f"{AZUL_CLARO}  6.{RESET} Actualizar todo")
            print()
            
            opcion = input(f"{AZUL_BRILLANTE}¿Que desea actualizar?: {RESET}")
            
            if opcion == "1":
                h["nombre"] = input(f"{CYAN}Nuevo nombre: {RESET}")
            elif opcion == "2":
                h["categoria"] = input(f"{CYAN}Nueva categoria: {RESET}")
            elif opcion == "3":
                valor_anterior = h["cantidad"]
                h["cantidad"] = int(input(f"{CYAN}Nueva cantidad: {RESET}"))
                log_actualizar_herramienta(h['id'], h['nombre'], 'cantidad', valor_anterior, h["cantidad"], "ADMIN")
            elif opcion == "4":
                h["estado"] = input(f"{CYAN}Nuevo estado: {RESET}")
            elif opcion == "5":
                h["valor_estimado"] = float(input(f"{CYAN}Nuevo valor estimado: ${RESET}"))
            elif opcion == "6":
                h["nombre"] = input(f"{CYAN}Nuevo nombre: {RESET}")
                h["categoria"] = input(f"{CYAN}Nueva categoria: {RESET}")
                h["cantidad"] = int(input(f"{CYAN}Nueva cantidad: {RESET}"))
                h["estado"] = input(f"{CYAN}Nuevo estado: {RESET}")
                h["valor_estimado"] = float(input(f"{CYAN}Nuevo valor estimado: ${RESET}"))
            else:
                mensaje_error("Opcion no valida.")
                return
            
            mensaje_exito("Herramienta actualizada exitosamente!")
            return
    
    mensaje_error("Herramienta no encontrada.")


def eliminar_herramienta(herramientas):
    """Elimina una herramienta del inventario"""
    limpiar_pantalla()
    titulo("ELIMINAR HERRAMIENTA")
    print()
    
    if len(herramientas) == 0:
        mensaje_advertencia("No hay herramientas registradas.")
        return
    
    id_eliminar = input(f"{CYAN}Ingrese el ID de la herramienta a eliminar: {RESET}")
    
    for i, h in enumerate(herramientas):
        if h["id"] == id_eliminar:
            print()
            linea(70, AMARILLO)
            print(f"{AMARILLO}{NEGRITA}⚠ ADVERTENCIA{RESET}")
            linea(70, AMARILLO)
            print(f"\n{BLANCO}Esta a punto de eliminar:{RESET}")
            print(f"  {CYAN}Nombre:{RESET} {h['nombre']}")
            print(f"  {CYAN}Categoria:{RESET} {h['categoria']}")
            print()
            
            confirmacion = input(f"{ROJO}¿Esta seguro? (s/n): {RESET}").lower()
            
            if confirmacion == "s":
                # Registrar en logs antes de eliminar
                log_eliminar_herramienta(h['id'], h['nombre'], "ADMIN")
                
                herramientas.pop(i)
                mensaje_exito("Herramienta eliminada exitosamente.")
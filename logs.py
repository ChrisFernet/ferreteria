"""
Módulo de registro de eventos (logs)
Registra todos los eventos importantes y errores del sistema en un archivo de texto
"""

from datetime import datetime
import os

# ========================================
# CONFIGURACIÓN
# ========================================

ARCHIVO_LOG = "sistema_logs.txt"

# ========================================
# FUNCIONES DE LOGGING
# ========================================

def obtener_fecha_hora():
    """Retorna la fecha y hora actual en formato legible"""
    ahora = datetime.now()
    return ahora.strftime("%Y-%m-%d %H:%M:%S")


def escribir_log(tipo, mensaje, usuario=None):
    """
    Escribe un evento en el archivo de logs
    
    Args:
        tipo (str): Tipo de evento (INFO, ERROR, WARNING, SUCCESS)
        mensaje (str): Descripción del evento
        usuario (str): ID del usuario que realizó la acción (opcional)
    """
    try:
        # Crear el mensaje del log
        fecha_hora = obtener_fecha_hora()
        
        # Si hay usuario, incluirlo
        if usuario:
            linea_log = f"[{fecha_hora}] [{tipo}] [Usuario: {usuario}] {mensaje}\n"
        else:
            linea_log = f"[{fecha_hora}] [{tipo}] {mensaje}\n"
        
        # Escribir en el archivo (modo 'a' = append, agrega al final)
        with open(ARCHIVO_LOG, 'a', encoding='utf-8') as archivo:
            archivo.write(linea_log)
        
        return True
    
    except Exception as e:
        # Si hay error al escribir el log, imprimirlo en consola
        print(f"ERROR al escribir log: {e}")
        return False


# ========================================
# FUNCIONES ESPECÍFICAS POR TIPO DE LOG
# ========================================

def log_info(mensaje, usuario=None):
    """Registra un evento informativo"""
    escribir_log("INFO", mensaje, usuario)


def log_error(mensaje, usuario=None):
    """Registra un error"""
    escribir_log("ERROR", mensaje, usuario)


def log_warning(mensaje, usuario=None):
    """Registra una advertencia"""
    escribir_log("WARNING", mensaje, usuario)


def log_success(mensaje, usuario=None):
    """Registra una operación exitosa"""
    escribir_log("SUCCESS", mensaje, usuario)


# ========================================
# LOGS ESPECÍFICOS DEL SISTEMA
# ========================================

def log_login(usuario_id, nombre_usuario, tipo_usuario):
    """Registra un inicio de sesión"""
    mensaje = f"Inicio de sesión - {nombre_usuario} (Tipo: {tipo_usuario})"
    log_info(mensaje, usuario_id)


def log_logout(usuario_id, nombre_usuario):
    """Registra un cierre de sesión"""
    mensaje = f"Cierre de sesión - {nombre_usuario}"
    log_info(mensaje, usuario_id)


def log_agregar_herramienta(herramienta_id, nombre, cantidad, usuario_id):
    """Registra cuando se agrega una herramienta"""
    mensaje = f"Nueva herramienta agregada - ID: {herramienta_id}, Nombre: {nombre}, Cantidad: {cantidad}"
    log_success(mensaje, usuario_id)


def log_eliminar_herramienta(herramienta_id, nombre, usuario_id):
    """Registra cuando se elimina una herramienta"""
    mensaje = f"Herramienta eliminada - ID: {herramienta_id}, Nombre: {nombre}"
    log_warning(mensaje, usuario_id)


def log_actualizar_herramienta(herramienta_id, nombre, campo, valor_anterior, valor_nuevo, usuario_id):
    """Registra cuando se actualiza una herramienta"""
    mensaje = f"Herramienta actualizada - ID: {herramienta_id}, Nombre: {nombre}, Campo: {campo}, Anterior: {valor_anterior}, Nuevo: {valor_nuevo}"
    log_info(mensaje, usuario_id)


def log_solicitud_creada(solicitud_id, usuario_id, nombre_usuario, herramienta, cantidad):
    """Registra cuando se crea una solicitud"""
    mensaje = f"Nueva solicitud - ID: {solicitud_id}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_info(mensaje, usuario_id)


def log_solicitud_aprobada(solicitud_id, admin_id, usuario_solicitante, herramienta, cantidad):
    """Registra cuando se aprueba una solicitud"""
    mensaje = f"Solicitud aprobada - ID: {solicitud_id}, Usuario: {usuario_solicitante}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_success(mensaje, admin_id)


def log_solicitud_rechazada(solicitud_id, admin_id, usuario_solicitante, herramienta, motivo="No especificado"):
    """Registra cuando se rechaza una solicitud"""
    mensaje = f"Solicitud rechazada - ID: {solicitud_id}, Usuario: {usuario_solicitante}, Herramienta: {herramienta}, Motivo: {motivo}"
    log_warning(mensaje, admin_id)


def log_prestamo_creado(prestamo_id, usuario_id, nombre_usuario, herramienta, cantidad):
    """Registra cuando se crea un préstamo"""
    mensaje = f"Nuevo préstamo - ID: {prestamo_id}, Usuario: {nombre_usuario}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_success(mensaje, usuario_id)


def log_devolucion(prestamo_id, usuario_id, nombre_usuario, herramienta, cantidad):
    """Registra cuando se devuelve una herramienta"""
    mensaje = f"Devolución registrada - ID Préstamo: {prestamo_id}, Usuario: {nombre_usuario}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_success(mensaje, usuario_id)


def log_stock_insuficiente(herramienta, cantidad_solicitada, cantidad_disponible, usuario_id):
    """Registra cuando se intenta solicitar más herramientas de las disponibles"""
    mensaje = f"Stock insuficiente - Herramienta: {herramienta}, Solicitado: {cantidad_solicitada}, Disponible: {cantidad_disponible}"
    log_error(mensaje, usuario_id)


def log_stock_bajo(herramienta_id, nombre, cantidad_actual):
    """Registra cuando una herramienta tiene stock bajo"""
    mensaje = f"ALERTA: Stock bajo - ID: {herramienta_id}, Nombre: {nombre}, Cantidad actual: {cantidad_actual}"
    log_warning(mensaje)


def log_prestamo_vencido(prestamo_id, usuario, herramienta, dias_retraso):
    """Registra cuando un préstamo está vencido"""
    mensaje = f"Préstamo vencido - ID: {prestamo_id}, Usuario: {usuario}, Herramienta: {herramienta}, Días de retraso: {dias_retraso}"
    log_warning(mensaje)


def log_usuario_creado(usuario_id, nombre, tipo, admin_id):
    """Registra cuando se crea un nuevo usuario"""
    mensaje = f"Nuevo usuario creado - ID: {usuario_id}, Nombre: {nombre}, Tipo: {tipo}"
    log_success(mensaje, admin_id)


def log_usuario_eliminado(usuario_id, nombre, admin_id):
    """Registra cuando se elimina un usuario"""
    mensaje = f"Usuario eliminado - ID: {usuario_id}, Nombre: {nombre}"
    log_warning(mensaje, admin_id)


# ========================================
# FUNCIONES AUXILIARES
# ========================================

def leer_logs(cantidad_lineas=50):
    """
    Lee las últimas líneas del archivo de logs
    
    Args:
        cantidad_lineas (int): Número de líneas a leer (por defecto 50)
    
    Returns:
        list: Lista con las últimas líneas del log
    """
    try:
        if not os.path.exists(ARCHIVO_LOG):
            return ["No hay logs registrados aún."]
        
        with open(ARCHIVO_LOG, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        # Retornar las últimas N líneas
        if len(lineas) <= cantidad_lineas:
            return lineas
        else:
            return lineas[-cantidad_lineas:]
    
    except Exception as e:
        return [f"Error al leer logs: {e}"]


def limpiar_logs_antiguos(dias=30):
    """
    Limpia logs más antiguos que X días
    (Esta función es opcional, para mantener el archivo de tamaño razonable)
    
    Args:
        dias (int): Logs más antiguos que esta cantidad de días serán eliminados
    """
    try:
        if not os.path.exists(ARCHIVO_LOG):
            return
        
        # Leer todos los logs
        with open(ARCHIVO_LOG, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        # Filtrar logs recientes (esto es una implementación simple)
        # En una versión más avanzada, se compararían las fechas
        
        # Por ahora, solo mantener las últimas 1000 líneas
        if len(lineas) > 1000:
            lineas_recientes = lineas[-1000:]
            
            with open(ARCHIVO_LOG, 'w', encoding='utf-8') as archivo:
                archivo.writelines(lineas_recientes)
            
            log_info(f"Logs limpiados - Se mantuvieron las últimas 1000 entradas")
    
    except Exception as e:
        print(f"Error al limpiar logs: {e}")


def inicializar_sistema_logs():
    """Crea el archivo de logs si no existe e inicializa el sistema"""
    if not os.path.exists(ARCHIVO_LOG):
        with open(ARCHIVO_LOG, 'w', encoding='utf-8') as archivo:
            archivo.write("========================================\n")
            archivo.write("  SISTEMA DE GESTIÓN DE HERRAMIENTAS\n")
            archivo.write("  Registro de eventos iniciado\n")
            archivo.write(f"  Fecha: {obtener_fecha_hora()}\n")
            archivo.write("========================================\n\n")
    
    log_info("Sistema de logs iniciado correctamente")

# Sistema de logs
# Guarda los eventos del sistema en un archivo

from datetime import datetime
import os

ARCHIVO_LOG = "sistema_logs.txt"

# obtener fecha y hora actual
def obtener_fecha_hora():
    ahora = datetime.now()
    return ahora.strftime("%Y-%m-%d %H:%M:%S")


# escribir en el archivo de logs
def escribir_log(tipo, mensaje, usuario=None):
    try:
        fecha_hora = obtener_fecha_hora()
        
        # abrir archivo y escribir
        archivo = open(ARCHIVO_LOG, 'a')
        
        if usuario:
            archivo.write(f"[{fecha_hora}] [{tipo}] [Usuario: {usuario}] {mensaje}\n")
        else:
            archivo.write(f"[{fecha_hora}] [{tipo}] {mensaje}\n")
        
        archivo.close()
        return True
    except:
        print("ERROR al escribir log")
        return False


# registrar información
def log_info(mensaje, usuario=None):
    escribir_log("INFO", mensaje, usuario)


# registrar error
def log_error(mensaje, usuario=None):
    escribir_log("ERROR", mensaje, usuario)


# registrar advertencia
def log_warning(mensaje, usuario=None):
    escribir_log("WARNING", mensaje, usuario)


# registrar éxito
def log_success(mensaje, usuario=None):
    escribir_log("SUCCESS", mensaje, usuario)


# registrar login
def log_login(usuario_id, nombre_usuario, tipo_usuario):
    mensaje = f"Inicio de sesión - {nombre_usuario} (Tipo: {tipo_usuario})"
    log_info(mensaje, usuario_id)


# registrar logout
def log_logout(usuario_id, nombre_usuario):
    mensaje = f"Cierre de sesión - {nombre_usuario}"
    log_info(mensaje, usuario_id)


# registrar cuando se agrega herramienta
def log_agregar_herramienta(herramienta_id, nombre, cantidad, usuario_id):
    mensaje = f"Nueva herramienta agregada - ID: {herramienta_id}, Nombre: {nombre}, Cantidad: {cantidad}"
    log_success(mensaje, usuario_id)


# registrar cuando se elimina herramienta
def log_eliminar_herramienta(herramienta_id, nombre, usuario_id):
    mensaje = f"Herramienta eliminada - ID: {herramienta_id}, Nombre: {nombre}"
    log_warning(mensaje, usuario_id)


# registrar cuando se actualiza herramienta
def log_actualizar_herramienta(herramienta_id, nombre, campo, valor_anterior, valor_nuevo, usuario_id):
    mensaje = f"Herramienta actualizada - ID: {herramienta_id}, Nombre: {nombre}, Campo: {campo}, Anterior: {valor_anterior}, Nuevo: {valor_nuevo}"
    log_info(mensaje, usuario_id)


# registrar cuando se crea solicitud
def log_solicitud_creada(solicitud_id, usuario_id, nombre_usuario, herramienta, cantidad):
    mensaje = f"Nueva solicitud - ID: {solicitud_id}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_info(mensaje, usuario_id)


# registrar cuando se aprueba solicitud
def log_solicitud_aprobada(solicitud_id, admin_id, usuario_solicitante, herramienta, cantidad):
    mensaje = f"Solicitud aprobada - ID: {solicitud_id}, Usuario: {usuario_solicitante}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_success(mensaje, admin_id)


# registrar cuando se rechaza solicitud
def log_solicitud_rechazada(solicitud_id, admin_id, usuario_solicitante, herramienta, motivo="No especificado"):
    mensaje = f"Solicitud rechazada - ID: {solicitud_id}, Usuario: {usuario_solicitante}, Herramienta: {herramienta}, Motivo: {motivo}"
    log_warning(mensaje, admin_id)


# registrar cuando se crea préstamo
def log_prestamo_creado(prestamo_id, usuario_id, nombre_usuario, herramienta, cantidad):
    mensaje = f"Nuevo préstamo - ID: {prestamo_id}, Usuario: {nombre_usuario}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_success(mensaje, usuario_id)


# registrar devolución
def log_devolucion(prestamo_id, usuario_id, nombre_usuario, herramienta, cantidad):
    mensaje = f"Devolución registrada - ID Préstamo: {prestamo_id}, Usuario: {nombre_usuario}, Herramienta: {herramienta}, Cantidad: {cantidad}"
    log_success(mensaje, usuario_id)


# registrar stock insuficiente
def log_stock_insuficiente(herramienta, cantidad_solicitada, cantidad_disponible, usuario_id):
    mensaje = f"Stock insuficiente - Herramienta: {herramienta}, Solicitado: {cantidad_solicitada}, Disponible: {cantidad_disponible}"
    log_error(mensaje, usuario_id)


# registrar stock bajo
def log_stock_bajo(herramienta_id, nombre, cantidad_actual):
    mensaje = f"ALERTA: Stock bajo - ID: {herramienta_id}, Nombre: {nombre}, Cantidad actual: {cantidad_actual}"
    log_warning(mensaje)


# registrar préstamo vencido
def log_prestamo_vencido(prestamo_id, usuario, herramienta, dias_retraso):
    mensaje = f"Préstamo vencido - ID: {prestamo_id}, Usuario: {usuario}, Herramienta: {herramienta}, Días de retraso: {dias_retraso}"
    log_warning(mensaje)


# registrar usuario creado
def log_usuario_creado(usuario_id, nombre, tipo, admin_id):
    mensaje = f"Nuevo usuario creado - ID: {usuario_id}, Nombre: {nombre}, Tipo: {tipo}"
    log_success(mensaje, admin_id)


# registrar usuario eliminado
def log_usuario_eliminado(usuario_id, nombre, admin_id):
    mensaje = f"Usuario eliminado - ID: {usuario_id}, Nombre: {nombre}"
    log_warning(mensaje, admin_id)


# leer logs del archivo
def leer_logs(cantidad_lineas=50):
    try:
        # verificar si existe el archivo
        if not os.path.exists(ARCHIVO_LOG):
            return ["No hay logs registrados aún."]
        
        # abrir y leer
        archivo = open(ARCHIVO_LOG, 'r')
        lineas = archivo.readlines()
        archivo.close()
        
        # retornar las últimas líneas
        if len(lineas) <= cantidad_lineas:
            return lineas
        else:
            # retornar solo las últimas N líneas
            return lineas[-cantidad_lineas:]
    except:
        return ["Error al leer logs"]

# inicializar sistema de logs
def inicializar_sistema_logs():
    # crear archivo si no existe
    if not os.path.exists(ARCHIVO_LOG):
        archivo = open(ARCHIVO_LOG, 'w')
        archivo.write("========================================\n")
        archivo.write("  SISTEMA DE GESTIÓN DE HERRAMIENTAS\n")
        archivo.write("  Registro de eventos iniciado\n")
        archivo.write(f"  Fecha: {obtener_fecha_hora()}\n")
        archivo.write("========================================\n\n")
        archivo.close()
    
    log_info("Sistema de logs iniciado correctamente")
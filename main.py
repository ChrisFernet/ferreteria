from herramientas_config import agregar_herramienta, mostrar_herramientas, gestionar_herramientas
from menus_config import menu_admin
from usuario_config import agregar_usuario, mostrar_usuario, gestion_usuarios

# ========================================
# COLORES EN ESCALA DE AZULES
# ========================================
AZUL_OSCURO = '\033[34m'      # Azul oscuro para títulos
AZUL_CLARO = '\033[94m'       # Azul claro para opciones
CYAN = '\033[96m'             # Cyan para información
AZUL_BRILLANTE = '\033[1;34m' # Azul brillante para destacar
BLANCO = '\033[97m'           # Blanco para texto normal
RESET = '\033[0m'             # Resetear color
NEGRITA = '\033[1m'           # Negrita

# ========================================
# FUNCIONES DE DISEÑO SENCILLO
# ========================================

def limpiar_pantalla():
    """Simula limpiar la pantalla"""
    print("\n" * 50)

def linea(longitud=60, color=AZUL_CLARO):
    """Crea una línea simple"""
    print(f"{color}{'─' * longitud}{RESET}")

def titulo(texto):
    """Crea un título simple y centrado"""
    longitud = 60
    print(f"\n{AZUL_BRILLANTE}{NEGRITA}{texto.center(longitud)}{RESET}")
    linea(longitud, AZUL_OSCURO)

def mensaje_bienvenida():
    """Mensaje de bienvenida simple"""
    limpiar_pantalla()
    print()
    linea(60, CYAN)
    print(f"{CYAN}{NEGRITA}{'SISTEMA DE GESTION DE HERRAMIENTAS'.center(60)}{RESET}")
    print(f"{AZUL_CLARO}{'Comunidad Vecinal'.center(60)}{RESET}")
    linea(60, CYAN)
    print()
    input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")

def menu(opcion=None):
    """Menú principal"""
    limpiar_pantalla()
    titulo("MENU PRINCIPAL")
    print()
    
    print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Usuario{RESET}")
    print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Administrador{RESET}")
    print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Salir{RESET}")
    
    print()
    linea()

def main_menu():
    """Función del menú principal"""
    herramientas = []
    usuarios = []
    
    # Mostrar mensaje de bienvenida
    mensaje_bienvenida()
    
    while True:
        menu()
        opcion = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion == "1":
            print(f"\n{CYAN}Menu usuario aun no implementado{RESET}")
            input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")
            
        elif opcion == "2":
            menu_administrador(usuarios, herramientas)
            
        elif opcion == "3":
            limpiar_pantalla()
            print()
            linea(60, CYAN)
            print(f"{CYAN}{NEGRITA}{'Gracias por usar el sistema'.center(60)}{RESET}")
            print(f"{AZUL_CLARO}{'Saliendo del programa...'.center(60)}{RESET}")
            linea(60, CYAN)
            print()
            break
            
        else:
            print(f"\n{AZUL_CLARO}Opcion no valida. Intente de nuevo.{RESET}")
            input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")

def menu_administrador(usuarios, herramientas):
    """Menú de administrador"""
    while True:
        limpiar_pantalla()
        titulo("MENU ADMINISTRADOR")
        print()
        
        print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Gestionar usuarios{RESET}")
        print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Gestionar herramientas{RESET}")
        print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Gestionar prestamos{RESET}")
        print(f"{AZUL_CLARO}  4.{RESET} {BLANCO}Consultas y reportes{RESET}")
        print(f"{AZUL_CLARO}  5.{RESET} {BLANCO}Volver al menu principal{RESET}")
        
        print()
        linea()
        
        opcion_admin = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion_admin == "1":
            usuarios = gestion_usuarios(usuarios)
            
        elif opcion_admin == "2":
            gestionar_herramientas(herramientas)
            
        elif opcion_admin == "3":
            print(f"\n{CYAN}Modulo de prestamos en desarrollo{RESET}")
            input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")
            
        elif opcion_admin == "4":
            print(f"\n{CYAN}Modulo de reportes en desarrollo{RESET}")
            input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")
            
        elif opcion_admin == "5":
            print(f"\n{CYAN}Volviendo al menu principal...{RESET}")
            break
            
        else:
            print(f"\n{AZUL_CLARO}Opcion no valida.{RESET}")
            input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")


main_menu()
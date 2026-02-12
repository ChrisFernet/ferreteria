from herramientas_config import gestionar_herramientas
from usuario_config import gestion_usuarios

# Colores
AZUL_OSCURO = '\033[34m'
AZUL_CLARO = '\033[94m'
CYAN = '\033[96m'
AZUL_BRILLANTE = '\033[1;34m'
BLANCO = '\033[97m'
RESET = '\033[0m' # volver al color base
NEGRITA = '\033[1m'

def limpiar_pantalla():
    print("\n" * 50)

def linea(longitud=60, color=AZUL_CLARO):
    print(f"{color}{'─' * longitud}{RESET}")

def titulo(texto):
    longitud = 60
    print(f"\n{AZUL_BRILLANTE}{NEGRITA}{texto.center(longitud)}{RESET}")
    linea(longitud, AZUL_OSCURO)

def mensaje_bienvenida():
    limpiar_pantalla()
    print()
    linea(60, CYAN)
    print(f"{CYAN}{NEGRITA}{'SISTEMA DE GESTION DE HERRAMIENTAS'.center(60)}{RESET}")
    print(f"{AZUL_CLARO}{'Comunidad Vecinal'.center(60)}{RESET}")
    linea(60, CYAN)
    print()
    input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")

def menu():
    limpiar_pantalla()
    titulo("MENU PRINCIPAL")
    print()
    print(f"{AZUL_CLARO}  1.{RESET} {BLANCO}Usuario{RESET}")
    print(f"{AZUL_CLARO}  2.{RESET} {BLANCO}Administrador{RESET}")
    print(f"{AZUL_CLARO}  3.{RESET} {BLANCO}Salir{RESET}")
    print()
    linea()

def main_menu():
    mensaje_bienvenida()
    
    while True:
        menu()
        opcion = input(f"\n{AZUL_BRILLANTE}Seleccione una opcion: {RESET}")
        
        if opcion == "1":
            print(f"\n{CYAN}Menu usuario aun no implementado{RESET}")
            input(f"{AZUL_CLARO}Presione ENTER para continuar...{RESET}")
            
        elif opcion == "2":
            menu_administrador()
            
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

def menu_administrador():
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
            gestion_usuarios()
            
        elif opcion_admin == "2":
            gestionar_herramientas()
            
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

# Ejecutar
main_menu()
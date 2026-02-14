# colores

VERDE = '\033[92m'
AZUL_OSCURO = '\033[34m'
AZUL_CLARO = '\033[94m'
CYAN = '\033[96m'
AZUL_BRILLANTE = '\033[1;34m'
BLANCO = '\033[97m'
AMARILLO = '\033[93m'
ROJO = '\033[91m'
RESET = '\033[0m'
NEGRITA = '\033[1m'


# FUNCIONES DE ESTILO Y APARIENCIA

def limpiar_pantalla():
# limpiar pantalla
    print("\n" * 50)


def linea(longitud=70, color=AZUL_CLARO):
# linea de color
    print(f"{color}{'─' * longitud}{RESET}")


def titulo(texto, longitud=70):

# texto con linea decorativa

    print(f"\n{AZUL_BRILLANTE}{NEGRITA}{texto.center(longitud)}{RESET}")
    linea(longitud, AZUL_OSCURO)


def pausa():
# tecla para continuar
    input(f"\n{AZUL_CLARO}Presione ENTER para continuar...{RESET}")


def mensaje_exito(texto):
    # mensaje de acción exitosa
    print(f"\n{VERDE}✓ {texto}{RESET}")


def mensaje_error(texto):
    # mensaje tipo error
    print(f"\n{ROJO}✗ {texto}{RESET}")


def mensaje_advertencia(texto):
    # mensaje de advertencia tipo señal
    print(f"\n{AMARILLO}⚠ {texto}{RESET}")


def mensaje_info(texto):
    # texto con formato
    print(f"\n{CYAN}ℹ {texto}{RESET}")

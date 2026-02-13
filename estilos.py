
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
    """Simula limpiar la pantalla imprimiendo múltiples líneas en blanco"""
    print("\n" * 50)


def linea(longitud=70, color=AZUL_CLARO):
    """
    Crea una línea horizontal decorativa
    
    Args:
        longitud (int): Longitud de la línea (default: 70)
        color (str): Color ANSI de la línea (default: AZUL_CLARO)
    """
    print(f"{color}{'─' * longitud}{RESET}")


def titulo(texto, longitud=70):
    """
    Crea un título centrado con línea decorativa
    
    Args:
        texto (str): Texto del título
        longitud (int): Ancho total del título (default: 70)
    """
    print(f"\n{AZUL_BRILLANTE}{NEGRITA}{texto.center(longitud)}{RESET}")
    linea(longitud, AZUL_OSCURO)


def pausa():
    """Pausa la ejecución hasta que el usuario presione ENTER"""
    input(f"\n{AZUL_CLARO}Presione ENTER para continuar...{RESET}")


def mensaje_exito(texto):
    """
    Muestra un mensaje de éxito con formato
    
    Args:
        texto (str): Mensaje a mostrar
    """
    print(f"\n{VERDE}✓ {texto}{RESET}")


def mensaje_error(texto):
    """
    Muestra un mensaje de error con formato
    
    Args:
        texto (str): Mensaje a mostrar
    """
    print(f"\n{ROJO}✗ {texto}{RESET}")


def mensaje_advertencia(texto):
    """
    Muestra un mensaje de advertencia con formato
    
    Args:
        texto (str): Mensaje a mostrar
    """
    print(f"\n{AMARILLO}⚠ {texto}{RESET}")


def mensaje_info(texto):
    """
    Muestra un mensaje informativo con formato
    
    Args:
        texto (str): Mensaje a mostrar
    """
    print(f"\n{CYAN}ℹ {texto}{RESET}")

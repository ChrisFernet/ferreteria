from usuario_config import gestion_usuarios
from herramientas_config import gestionar_herramientas 

def menu_admin(usuarios, herramientas):
    print("Menú de administración")
    print("1. Gestionar usuarios")
    print("2. Gestionar herramientas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        gestion_usuarios(usuarios)
    elif opcion == "2":
        gestionar_herramientas(herramientas)
    elif opcion == "3":
        print("Saliendo del menú de administración.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
    

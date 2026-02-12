from herramientas_config import agregar_herramienta, mostrar_herramientas 
from menus_config import menu_admin
from usuario_config import agregar_usuario, mostrar_usuario


def menu(opcion=None):
    print("Bienvenido a la gestión de herramientas")
    print("Ingrese Como un...")
    print("1. Usuario")
    print("2. Administrador     ")
    print("3. Salir")
    print("Seleccione una opción: ")

    return opcion   

def main_menu():
    herramientas = []
    usuarios = []

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if menu() == '1':
            print("Menú de usuario")
            print("1. Agregar usuario")
            print("2. Mostrar usuarios")
            print("3. Volver al menú principal")
            opcion_usuario = input("Seleccione una opción: ")
            if opcion_usuario == "1":
                agregar_usuario(usuarios)
            elif opcion_usuario == "2":
                mostrar_usuario(usuarios)
            elif opcion_usuario == "3":
                print("Volviendo al menú principal.")
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        elif opcion == '2':
            menu_admin(usuarios, herramientas)
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main_menu()
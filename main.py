
from herramientas_config import agregar_herramienta, mostrar_herramientas 

def menu():
    print("Bienvenido a la gestión de herramientas")
    print("Ingrese Como un...")
    print("1. Usuario")
    print("2. Administrador     ")
    print("3. Salir")

def main_menu():
    herramientas = []
    usuarios = []

    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            pass
        elif opcion == '2':
            

        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


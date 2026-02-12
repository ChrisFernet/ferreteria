from json_config import cargar_datos, guardar_datos

def gestionar_prestamos(usuarios, herramientas):
    prestamos = cargar_datos("prestamos.json")
    
    while True:
        print("\n" + "="*50)
        print("Gestión de préstamos")
        print("="*50)
        print("1. Registrar préstamo")
        print("2. Devolver herramienta")
        print("3. Ver préstamos activos")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_prestamo(prestamos, usuarios, herramientas)
            guardar_datos(prestamos, "prestamos.json")
            guardar_datos(herramientas, "herramientas.json")
        elif opcion == "2":
            devolver_herramienta(prestamos, herramientas)
            guardar_datos(prestamos, "prestamos.json")
            guardar_datos(herramientas, "herramientas.json")
        elif opcion == "3":
            ver_prestamos_activos(prestamos)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def registrar_prestamo(prestamos, usuarios, herramientas):
    # falta
    print("Función en desarrollo...")
    pass

def devolver_herramienta(prestamos, herramientas):
    # falta
    print("Función en desarrollo...")
    pass

def ver_prestamos_activos(prestamos):
    activos = [p for p in prestamos if p.get("estado") == "activo"]
    if not activos:
        print("No hay préstamos activos.")
    else:
        for p in activos:
            print(f"ID: {p['id']}, Usuario: {p['usuario']}, Herramienta: {p['herramienta']}")
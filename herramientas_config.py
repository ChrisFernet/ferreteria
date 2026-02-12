def gestionar_herramientas():
    herramientas = []
    
    while True:
        print("\nGestión de herramientas")
        print("1. Agregar herramienta")
        print("2. Mostrar herramientas")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_herramienta(herramientas)
        elif opcion == "2":
            mostrar_herramientas(herramientas)
        elif opcion == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def agregar_herramienta(herramientas):  
    id = input("Ingrese el ID de la herramienta: ")
    nombre = input("Ingrese el nombre de la herramienta: ")
    categoria = input("Ingrese la categoría de la herramienta: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    estado = input("Ingrese el estado de la herramienta (activa, en reparación, fuera de servicio): ")
    valor_estimado = float(input("Ingrese el valor estimado de la herramienta: "))
    
    herramienta = {
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "estado": estado,
        "valor_estimado": valor_estimado
    }
    
    herramientas.append(herramienta)
    print("Herramienta agregada exitosamente.")

def mostrar_herramientas(herramientas):
    if not herramientas:
        print("No hay herramientas registradas.")
        return
    
    for herramienta in herramientas:
        print(f"ID: {herramienta['id']}, Nombre: {herramienta['nombre']}, Categoría: {herramienta['categoria']}, Cantidad: {herramienta['cantidad']}, Estado: {herramienta['estado']}, Valor Estimado: {herramienta['valor_estimado']}")

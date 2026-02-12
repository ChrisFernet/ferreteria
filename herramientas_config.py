from json_config import cargar_datos, guardar_datos

def gestionar_herramientas():
    # ✅ CARGAR datos al inicio
    herramientas = cargar_datos("herramientas.json")
    
    while True:
        print("\n" + "="*50)
        print("Gestión de herramientas")
        print("="*50)
        print("1. Agregar herramienta")
        print("2. Mostrar herramientas")
        print("3. Buscar herramienta")
        print("4. Actualizar herramienta")
        print("5. Eliminar herramienta")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_herramienta(herramientas)
            guardar_datos(herramientas, "herramientas.json")
        elif opcion == "2":
            mostrar_herramientas(herramientas)
        elif opcion == "3":
            buscar_herramienta(herramientas)
        elif opcion == "4":
            actualizar_herramienta(herramientas)
            guardar_datos(herramientas, "herramientas.json")
        elif opcion == "5":
            eliminar_herramienta(herramientas)
            guardar_datos(herramientas, "herramientas.json")
        elif opcion == "6":
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
    
    print("\n" + "="*80)
    for herramienta in herramientas:
        print(f"ID: {herramienta['id']}, Nombre: {herramienta['nombre']}, Categoría: {herramienta['categoria']}, Cantidad: {herramienta['cantidad']}, Estado: {herramienta['estado']}, Valor Estimado: ${herramienta['valor_estimado']}")
    print("="*80)

def buscar_herramienta(herramientas):
    print("\nBuscar herramienta por:")
    print("1. ID")
    print("2. Nombre")
    opcion = input("Seleccione opción: ")
    
    if opcion == "1":
        id_buscar = input("Ingrese el ID: ")
        encontrada = False
        for h in herramientas:
            if h["id"] == id_buscar:
                print("\n--- Herramienta encontrada ---")
                print(f"ID: {h['id']}")
                print(f"Nombre: {h['nombre']}")
                print(f"Categoría: {h['categoria']}")
                print(f"Cantidad: {h['cantidad']}")
                print(f"Estado: {h['estado']}")
                print(f"Valor estimado: ${h['valor_estimado']}")
                encontrada = True
                break
        if not encontrada:
            print("Herramienta no encontrada.")
    
    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre: ").lower()
        encontradas = [h for h in herramientas if nombre_buscar in h["nombre"].lower()]
        if encontradas:
            print(f"\n--- Se encontraron {len(encontradas)} herramienta(s) ---")
            for h in encontradas:
                print(f"ID: {h['id']}, Nombre: {h['nombre']}, Cantidad: {h['cantidad']}")
        else:
            print("No se encontraron herramientas con ese nombre.")

def actualizar_herramienta(herramientas):
    id_actualizar = input("Ingrese el ID de la herramienta a actualizar: ")
    
    for h in herramientas:
        if h["id"] == id_actualizar:
            print("\n--- Herramienta encontrada ---")
            print(f"Nombre actual: {h['nombre']}")
            print("\n¿Qué desea actualizar?")
            print("1. Nombre")
            print("2. Categoría")
            print("3. Cantidad")
            print("4. Estado")
            print("5. Valor estimado")
            print("6. Todo")
            
            opcion = input("Seleccione opción: ")
            
            if opcion == "1":
                h["nombre"] = input("Nuevo nombre: ")
            elif opcion == "2":
                h["categoria"] = input("Nueva categoría: ")
            elif opcion == "3":
                h["cantidad"] = int(input("Nueva cantidad: "))
            elif opcion == "4":
                h["estado"] = input("Nuevo estado (activa, en reparación, fuera de servicio): ")
            elif opcion == "5":
                h["valor_estimado"] = float(input("Nuevo valor estimado: "))
            elif opcion == "6":
                h["nombre"] = input("Nuevo nombre: ")
                h["categoria"] = input("Nueva categoría: ")
                h["cantidad"] = int(input("Nueva cantidad: "))
                h["estado"] = input("Nuevo estado: ")
                h["valor_estimado"] = float(input("Nuevo valor estimado: "))
            
            print("Herramienta actualizada exitosamente.")
            return
    
    print("Herramienta no encontrada.")

def eliminar_herramienta(herramientas):
    id_eliminar = input("Ingrese el ID de la herramienta a eliminar: ")
    
    for i, h in enumerate(herramientas):
        if h["id"] == id_eliminar:
            print(f"\n¿Está seguro de eliminar '{h['nombre']}'? (s/n): ", end="")
            confirmacion = input().lower()
            if confirmacion == "s":
                herramientas.pop(i)
                print("Herramienta eliminada exitosamente.")
            else:
                print("Eliminación cancelada.")
            return
    
    print("Herramienta no encontrada.")
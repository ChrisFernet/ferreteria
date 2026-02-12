# este modulo se encarga de guardar los datos json en el disco

import json

def cargar_datos(nom_archivo="usuarios.json"):
    """
    Carga los datos desde un archivo JSON.
    Si el archivo no existe o está corrupto, devuelve una lista vacía.
    """
    try:
        with open(nom_archivo, "r", encoding="utf-8") as arch:
            datos = json.load(arch)
            # Verificar que sea una lista
            if isinstance(datos, list):
                return datos
            else:
                print(f"Advertencia: {nom_archivo} no contiene una lista. Se creará uno nuevo.")
                return []
    
    except FileNotFoundError:
        # El archivo no existe, esto es normal la primera vez
        print(f"Archivo {nom_archivo} no encontrado. Se creará uno nuevo.")
        return []
    
    except json.JSONDecodeError:
        # El archivo existe pero está corrupto
        print(f"Error: {nom_archivo} está corrupto o mal formateado.")
        print("Se creará un archivo nuevo.")
        return []
    
    except Exception as e:
        # Cualquier otro error
        print(f"Error inesperado al cargar {nom_archivo}: {e}")
        return []


def guardar_datos(datos, nom_archivo="usuarios.json"):
    """
    Guarda los datos en un archivo JSON.
    """
    try:
        with open(nom_archivo, "w", encoding="utf-8") as arch:
            json.dump(datos, arch, indent=4, ensure_ascii=False)
        return True
    
    except Exception as e:
        print(f"Error al guardar {nom_archivo}: {e}")
        return False
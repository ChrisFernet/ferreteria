# guarda datos en el json

import json

def cargar_datos(nom_archivo="usuarios.json"):
    # si no existe: lista vacio
    try:
        archivo = open(nom_archivo, "r")
        datos = json.load(archivo)
        archivo.close()
        return datos
    except Exception:
        return []


def guardar_datos(datos, nom_archivo="usuarios.json"):
    try:
        archivo = open(nom_archivo, "w")
        json.dump(datos, archivo, indent=4)
        archivo.close()
        return True
    except Exception:
        return False
# este modulo se encarga de guardar los datos json en el disco

import json

def cargar_datos(nom_archivo="usuarios.json"):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return [] 

def guardar_datos(usuarios, nom_archivo="usuarios.json"):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(usuarios, arch, indent=4)
    except Exception:
        usuarios = [] 
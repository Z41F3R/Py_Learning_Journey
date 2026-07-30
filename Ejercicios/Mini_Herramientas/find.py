#!/usr/bin/env python3

from pathlib import Path
import argparse

def buscar_archivo(ruta, extension, recursivo):
    ruta_actual = Path(".")
    carpeta = Path(ruta)
    resultado = ""


    if carpeta in ruta_actual.iterdir():
        pass
    else:
        return f"[!] {ruta} no se encuentra en el directorio actual"

    if recursivo:
        archivos_registrados = carpeta.rglob("*")
        for linea in archivos_registrados:
            if linea.suffix == f".{extension}":
                resultado = resultado + f"\n[+] Se encontro una coincidencia en la ruta {linea}"

    else:
        archivos_registrados = carpeta.iterdir()
        for linea in archivos_registrados:
            if linea.suffix == f".{extension}":
                resultado = resultado + f"\n[+] {linea.name}"

    return f"{resultado}\n"

parser = argparse.ArgumentParser()

parser.add_argument("nombre")
parser.add_argument("extension")
parser.add_argument("-r", action="store_true")

argumento = parser.parse_args()


r = buscar_archivo(argumento.nombre, argumento.extension, argumento.r)
print(r)

# CONCEPTOS
# SUFFIX
# ITERDIR
# .NAME
# ENTENDER MAS LIBRERIA PATH

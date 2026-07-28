#!/usr/bin/env python3

from pathlib import Path
import argparse

def buscar_usuario(ruta, nombre, ignore_case, recurrencia):
    verificar_ruta = Path("") / ruta
    if verificar_ruta.exists():
        contenido = verificar_ruta.read_text(encoding="utf-8")
        nombres = contenido.split()
    else:
        return "[!] Archivo no encontado"
  
    #ESTUDIAR LISTA COMPRESION PAR ENTENDER
    if nombre.casefold() in (n.casefold() for n in nombres):
        match (ignore_case, recurrencia):
            case (False, False) | (True, False):
                return f"[+] Se encontro {nombre} en el archivo"

            case (False, True):
                coincidencias = nombres.count(nombre)
                return f"[+] Se encontro {nombre} un total de {coincidencias} veces"

            case (True, True):
                coincidencias = [n.casefold() for n in nombres].count(nombre.casefold())
                return f"[+] Se encontro {nombre} un total de {coincidencias} veces"
    else:
        return "[!] El nombre no se encuentra en el archivo"

parse = argparse.ArgumentParser()

parse.add_argument("ruta")
parse.add_argument("nombre")
parse.add_argument("-i", action="store_true")
parse.add_argument('--count', action="store_true")

argumento1 = parse.parse_args()

result = buscar_usuario(argumento1.ruta, argumento1.nombre, argumento1.i, argumento1.count)
print(result)

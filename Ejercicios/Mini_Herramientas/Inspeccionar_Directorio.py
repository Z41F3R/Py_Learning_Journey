#!/usr/bin/python3 

from pathlib import Path
import argparse

def inspeccionar_directorio(ruta):
    directorio = Path(ruta)
    archivos_encontrados = []
    directorio_encontrados = []
    extensiones_encontradas = {}

    if directorio.exists() and directorio.is_dir():
        pass
    else:
        print( f"[!] La ruta ingresada no corresponde a un directorio valido o existente") # Linea de la nota personal
        exit()

    # Claficacion directorio - archivo
    for recorrido in directorio.rglob("*"):
        if recorrido.is_dir():
            directorio_encontrados.append(recorrido.name)
        elif recorrido.is_file():
            archivos_encontrados.append(recorrido.suffix)

    # Clasificacion archivo - extension
    for extensiones in archivos_encontrados:
        extensiones_encontradas[extensiones] = extensiones_encontradas.get(extensiones, 0) + 1

    return archivos_encontrados, directorio_encontrados, extensiones_encontradas

def imprimir_resultado(archivos, directorio, extension):
    print("\nRESULTADOS OBTENIDOS\n")
    print(f"[+] Directorios : {len(directorio)}")
    print(f"[+] Archivos    : {len(archivos)}\n")

    for clave, valor in extension.items():
        if clave != "":
            print(f"[+] {clave}: {valor}")
        else:
            print(f"[+] Archivos sin extension: {valor}")

    print("\n[+] Gracias por usar la herramienta\n")

# Argumentos parser
parser = argparse.ArgumentParser()
parser.add_argument("ruta")
argumento = parser.parse_args()

# llamado a las funciones
archivos, directorios, extensiones = inspeccionar_directorio(argumento.ruta)
imprimir_resultado(archivos, directorios, extensiones)

# ===========================================================
# NOTA PERSONAL
# ===========================================================
#
# Inicialmente aquí utilizaba:
#
# return "[!] La ruta ingresada no corresponde a un directorio valido o existente", "", ""
#
# para que la función encargada de imprimir el resultado
# mostrara el mensaje de error.
#
# Sin embargo, ocurrió algo curioso.
#
# Al ejecutar:
#
# len(archivos)
#
# obtenía siempre:
#
# [+] Archivos: 71
#
# aunque la carpeta NO existía.
#
# Después de investigarlo entendí el motivo.
#
# La variable 'archivos' ya no contenía una lista,
# sino el string del mensaje de error.
#
# Como len() sobre un string devuelve la cantidad
# de caracteres, Python estaba contando las letras
# del mensaje:
#
# "[!] La ruta ingresada no corresponde a un directorio valido o existente"
#
# Ese texto tiene exactamente 71 caracteres.
#
# Es decir:
#
# len(lista)   -> cantidad de elementos.
# len(string)  -> cantidad de caracteres.
#
# Este bug me enseñó la importancia de que una función
# mantenga siempre el mismo tipo de dato de retorno.
#
# Para esta herramienta decidí simplemente imprimir
# el error y finalizar el programa con exit(),
# evitando que el resto del código continúe ejecutándose.
#
# ===========================================================

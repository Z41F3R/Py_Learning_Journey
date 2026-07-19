#!/usr/bin/env python3

#with open('archivo.txt', 'r') as archivo:
#    contenido = archivo.read()
#    print(contenido)

#archivo = open('archivo.txt', 'r')
#print(archivo.read())

def leer_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError:
        return "No se encontro el archivo"

s = leer_archivo('archivo.txt')
print(s)

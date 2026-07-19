#!/usr/bin/env python3

def buscar_palabra(ruta, palabra):
    validador = False
    try:
        with open(ruta) as archivo:
             for linea in archivo:
                 if palabra == linea.strip():
                     validador = True
                     break
        return validador 
    except FileNotFoundError:
        return "Archivo no encontrado"
    
result = buscar_palabra("archivo.txt", "Steven")
print(result)

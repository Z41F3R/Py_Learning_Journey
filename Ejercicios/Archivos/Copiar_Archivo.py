#!/usr/bin/env python3

def copiar_archivo(origen, destino):
    try:
        with open(origen, 'r') as archivo:
            contenido = archivo.read()
        with open(destino, 'w') as archivo_nuevo:
            archivo_nuevo.write(contenido)
        return "Archivo Creado"
    except FileNotFoundError:
        return "Archivo no encontrado"
    
copiar_archivo("archivo.txt", "New_text.txt")
#!/usr/bin/env python3

def reemplazar_texto(ruta, buscar, reemplazar):
    try:
        with open(ruta, 'r') as lectura:
            texto = lectura.read()

        with open(ruta, 'w') as archivo:
            archivo.write(texto.replace(buscar, reemplazar))
            return "Texto reemplazado correctamente"

    except FileNotFoundError:
        return "Archivo no encontrado"
    
r = reemplazar_texto('archivo.txt', "nuevo", "New")
print(r)
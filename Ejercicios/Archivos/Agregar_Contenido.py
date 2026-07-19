#!/usr/bin/env python3

def agregar_contenido(ruta, contenido):
    try:
        with open(ruta, 'a') as archivo:
            archivo.write(f"\n{contenido}")
            return "Contenido agregado correctamente"
    except OSError:
        return  "No  fue posible agregar el contenido"
    
result = agregar_contenido("archivo.txt", "Nuevo texto")
print(result)
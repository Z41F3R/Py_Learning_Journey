#!/usr/bin/env python3

def escribir_archivo(ruta, contenido):
    try:
        with open(ruta, 'w') as archivo:
            archivo.write(contenido)
        return "Archivo creado"
    except OSError:
        return "No fue posible escribir el archivo"
    
resultado = escribir_archivo("saludo.txt", "hola mundo")
print(resultado)
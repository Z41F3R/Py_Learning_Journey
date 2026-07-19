#!/usr/bin/env python3

def filtrar_errores(origen, destino):
    try:
        with open(origen, 'r') as logs:
           with open(destino, 'w') as errores:
               for linea in logs:
                   if 'error' in linea.lower():
                       errores.write(f"{linea.strip()}\n")
        return "Archivo generado de manera correcta"            
    except OSError:
        return "Archivo No Encontrado"
    
result = filtrar_errores("logs.txt",  "errores.txt")
print(result)
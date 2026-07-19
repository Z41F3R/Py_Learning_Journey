#!/usr/bin/env python3

def contar_lineas(ruta):
    contador = 0
    try:
        with open(ruta) as archivo:
            for linea in archivo:
                contador = contador + 1
        return contador
    except FileNotFoundError:
        return "Archivo no encontrado"
    
resultado = contar_lineas('archivo.txt')
print(resultado)

# Puedes usar esta variante con len()
# print(len(open('archivo.txt').readlines()))
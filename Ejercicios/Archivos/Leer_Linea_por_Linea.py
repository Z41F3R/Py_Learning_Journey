#!/usr/bin/env python3

def leer_lineas(ruta):
    try:
        with open(ruta, 'r') as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        return "Archivo no encontrado"
    
leer_lineas('archivo.txt')

def leer_Lineas(ruta):
    try:
        with open(ruta) as archivo:
            linea = archivo.readline()
            while linea != '':
                print(linea.strip())
                linea = archivo.readline()
    except FileNotFoundError:
        return "Archivo no encontrado"
    
leer_Lineas('archivo.txt')

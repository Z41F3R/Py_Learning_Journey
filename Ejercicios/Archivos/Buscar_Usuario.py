#!/usr/bin/env python3

def buscar_usuario(ruta, usuario):
    contador = 0
    recurrencia = []
    try:
        with open(ruta) as archivo:
            for linea in archivo:
                contador += 1
                if linea.strip().casefold() == usuario.casefold():
                    recurrencia.append(contador)
        if recurrencia != []:
            mostrar = f"[+] Usuario encontrado en las lineas {recurrencia}"
        else:
            mostrar = f"[!] Usuario no encontrado en el archivo"
        return mostrar
    except FileNotFoundError:
        return "[!] Archivo no encontrado"

resultado = buscar_usuario('logs.txt', 'Steven')
print(resultado)

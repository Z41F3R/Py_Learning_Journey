#!/usr/bin/env python3

def buscar_ip(ruta, ip):
    contador = 0
    try:
        with open(ruta) as ips:
            for linea in ips:
                contador += 1
                if ip == linea.strip():
                    return f"[+] {linea.strip()} Encontrada en la linea {contador}"
            return "[!] No se encontro la direccion IP"      
    except FileNotFoundError:
        return "[!] No existe el archivo"

result = buscar_ip('ips.txt', '172.16.0.3')
print (result)

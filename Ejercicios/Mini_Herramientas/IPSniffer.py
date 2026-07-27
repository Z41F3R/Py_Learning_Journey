#!/usr/bin/env python3

from ipaddress import ip_address

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


def extraer_ips(origen, destino):
    val = True
    try:
        with open(origen, 'r') as logs:
            with open(destino, 'w') as ipv4:
                for linea in logs:
                    for palabra in linea.split():
                        try:
                            ip_address(palabra)
                            ipv4.write(f"{palabra}\n")
                            print(f"[+] {palabra} Encontada. Guardando...")
                            val = False
                        except ValueError:
                            pass
        if val is True:
            return "[!] No se encontraron direcciones IP"
        else:
            return "[+] Archivo Generado de manera Exitosa"
    except FileNotFoundError:
        return "[!] Archivo no encontrado"

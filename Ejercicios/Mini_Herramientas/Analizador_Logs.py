#!/usr/bin/env python3

def analizar_logs(ruta):
    logs = {}
    total_eventos = 0
    try:
        with open(ruta) as archivo:
            for linea_texto in archivo:
                valor = linea_texto.split()
                if valor[0] not in logs:
                    logs[valor[0]] = 1
                else:
                    logs[valor[0]] += 1
                total_eventos = total_eventos + 1
        if logs != {}:
            recurrencia = max(logs, key=logs.get)
        else:
            recurrencia = ""
        return logs, total_eventos, recurrencia
    except FileNotFoundError:
        return "Archivo no encontrado", 0, ""
    
def mostrar_reporte(resultado, evento, recurrente):
    print("\n[+] REPORTE DE LOGS FUE EJECUTADO CON EXITO\n")
    
    if isinstance(resultado, str):
        print(f"[!] {resultado}")
    elif resultado != {}:
        for clave, valor in resultado.items():
            print(f"[+] {clave}: {valor}")
        print(f"\n[+] Total de eventos recorridos {evento}")
        print(f"[+] Estado mas frecuente {recurrente}")
    else:
        print("[!] No se encontraron nada por aqui")
    
    return '\n[+] GRACIAS POR USAR LA HERRAMIENTA\n'
    
result, eventos, recurrencia = analizar_logs("logs.txt")
print(mostrar_reporte(result, eventos, recurrencia))

# ===========================================
# En desarrollo aun
# ===========================================

#!/usr/bin/env python3

logs = [
    {"ip": "192.168.1.10", "estado": "OK"},
    {"ip": "10.0.0.5", "estado": "ERROR"},
    {"ip": "192.168.1.10", "estado": "ERROR"},
    {"ip": "172.16.0.3", "estado": "OK"},
    {"ip": "10.0.0.5", "estado": "ERROR"},
    {"ip": "10.0.0.5", "estado": "OK"},
]

def ip_con_mas_errores(logs):
    ip_con_estado_error = {}
    valor_variable = 0
    ip_con_mas_intentos = 0
    # Frequency Counter
    for ips in logs:
        if ips.get("estado", "") == "ERROR":
            intento = ips.get("ip", "")
            ip_con_estado_error[intento] = ip_con_estado_error.get(intento, 0) + 1
    
    # Maximum Search
    for ip, valor in ip_con_estado_error.items():
        if valor_variable < valor:
            valor_variable = valor
            ip_con_mas_intentos = ip

    return ip_con_mas_intentos
    ######CON MAX#######
    #return max(ip_con_estado_error, key=ip_con_estado_error.get)
    ####################

s = ip_con_mas_errores(logs)
print(s)

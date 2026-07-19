#!/usr/bin/env python3

intentos = [
    {"usuario": "juan", "estado": "fallido"},
    {"usuario": "pedro", "estado": "exitoso"},
    {"usuario": "juan", "estado": "fallido"},
    {"usuario": "ana", "estado": "fallido"},
    {"usuario": "juan", "estado": "exitoso"},
]

lista_de_logs = {}

def contar_fallidos(intentos):
    for fallido in intentos:
        if fallido.get("estado", "") == "fallido":
            yield fallido

for valor in contar_fallidos(intentos):
    nombre = valor.get("usuario", "")
    lista_de_logs[nombre] = lista_de_logs.get(nombre, 0) + 1

print(lista_de_logs)

################ NUEVO CONCEPTO ###############
#
# lista_de_logs[nombre] = lista_de_logs.get(nombre, 0) + 1
#
# Registra o incrementa los intentos fallidos por usuario.
# Busca el 'nombre' en el diccionario: si no existe, toma 
# el valor inicial de 0; si ya existe, recupera su valor actual.
# Finalmente, le suma 1 al resultado obtenido.

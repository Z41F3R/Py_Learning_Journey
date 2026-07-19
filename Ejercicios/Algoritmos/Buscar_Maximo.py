#!/usr/bin/env python3

usuarios = [
    {"nombre": "Juan", "edad": 20},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "Steven", "edad": 25}
]

def usuario_mayor(usuarios):
    valor = 0
    nombre_mayor = ""

    for usuario in usuarios:
        variable = usuario.get("edad", 0)
        if variable > valor:
            valor = variable
            nombre_mayor = usuario.get("nombre", "")
        else:
            continue
    
    return nombre_mayor

#ENTENDER#
def usuario_mayor_m(usuarios):
    valor = max(usuarios, key=lambda usuario: usuario.get("edad", 0))
    return valor.get("nombre", 0)

s = usuario_mayor_m(usuarios)
print(s)

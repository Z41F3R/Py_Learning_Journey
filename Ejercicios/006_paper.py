#!/usr/bin/env python3

def convertir_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return "Entrada Invalida"


    

res = convertir_entero("444")
print(type(res))
print(res)
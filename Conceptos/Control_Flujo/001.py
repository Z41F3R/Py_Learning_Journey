#!/usr/bin/env python3

def clasificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    elif num == 0:
        return "Cero"

resultado = clasificar_numero(0)
print(resultado)
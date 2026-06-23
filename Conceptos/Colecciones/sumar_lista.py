#!/usr/bin/env python3

def sumar_lista(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i

    return resultado

resultado = sumar_lista([1, 2, 3, 4, 5])
print(resultado)

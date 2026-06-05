#!/usr/bin/env python3

duplicar = lambda texto: texto + texto

def transformar_lista(lista, funcion):
    lista_local = []
    for i in lista:
        resultado = funcion(i)
        lista_local.append(resultado)

    return lista_local

resultado = transformar_lista(["a", "bro", "python"], duplicar)
print(resultado)
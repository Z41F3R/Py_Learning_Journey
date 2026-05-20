#!/usr/bin/env python3

invertir = lambda texto: (texto[::-1])

def aplicar_lista(lista, funcion):
    lista_vacia = []
    for i in lista:
        resultado = funcion(i)
        lista_vacia.append(resultado)

    return lista_vacia

lista = ["hola", "python", "bro"]
resultado = aplicar_lista(lista, invertir)
print(resultado)

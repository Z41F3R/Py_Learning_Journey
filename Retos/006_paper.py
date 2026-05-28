#!/usr/bin/env python3

def contador_regresivo(valor):
    for numero in range(valor, 0, -1):
        yield numero

    yield "Despegar"

for resultado in contador_regresivo(6):
    print(resultado)
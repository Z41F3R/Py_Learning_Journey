#!/usr/bin/env python3

def analizar_numero(numero):
    signo = "positivo" if numero >= 0 else "negativo"
    paridad = "par" if numero % 2 == 0 else "impar"
    return f"{paridad} {signo}"

resultado = analizar_numero(-4)
print(resultado)    

# Uso de operadores Ternarios
# Como usar el/if en una sola linea

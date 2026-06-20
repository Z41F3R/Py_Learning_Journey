#!/usr/bin/env python3

validar_password = lambda texto: "a" in texto and "@" in texto and len(texto) == 8

resultado = validar_password("lolal@l")
print(resultado)
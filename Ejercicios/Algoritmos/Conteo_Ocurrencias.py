#!/usr/bin/env python3

contar_vocales = lambda texto: sum(1 for letra in texto if letra.lower() in 'aeiou')

contar_vocales_en_texto = contar_vocales("Hola, ¿cómo estás?")
print(contar_vocales_en_texto)

#!/usr/bin/env python3

puede_votar = lambda edad, documento: edad >= 18 and documento

resultado = puede_votar(19, True)
print(resultado)

# Concepto Short-Circuit
# Python no evalua mas de lo necesario
# Si uno es False ya no evalua la siguiente operatoria
# False and True = False
# True and False = False

# and documento > No se pone (== True) por que documento
# ya contiene un valor bool 


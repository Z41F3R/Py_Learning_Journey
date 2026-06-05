#!/usr/bin/env python3

def dividir(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "No se puede dividir para cero"

resultado = dividir(10, 0)
print(resultado)

# 1. Funciones
# 2. Manejo de excepciones
# 3. Tipos de errores/exception
# 4. Llamada a funciones
# 5. Entrada/Salida básica
# 6. Programación defensiva
# 7. Control de flujo

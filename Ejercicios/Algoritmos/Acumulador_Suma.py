#!/usr/bin/env python3

usuarios = [
    {"nombre": "Juan", "edad": 20},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "Steven", "edad": 25}
]

def sumar_edades(usuarios):
    suma = 0
    for usuario in usuarios:
        suma = suma + usuario.get("edad", 0)
        
    return suma
        

resultado = sumar_edades(usuarios)
print(resultado)

# ==============================================================================
# La expresión 'usuario.get("edad", 0)' dentro del bucle funciona igual que acceder
# manualmente a cada posición de la lista, por ejemplo: 'usuarios[0].get("edad", 0)'.
# 
# La diferencia clave es el proceso de automatización:
# 1. Manual: Tendríamos que escribir un código por cada índice (0, 1, 2...) de la lista.
# 2. Bucle FOR: Automatiza la tarea. Recorre la lista de inicio a fin y, en cada vuelta,
#    asigna automáticamente el elemento actual a la variable temporal 'usuario'.
#
# En este ejercicio, el bucle realiza internamente estas tres asignaciones:
# - Vuelta 1: 'usuario' toma el valor de 'usuarios[0]' -> Juan (20 años)
# - Vuelta 2: 'usuario' toma el valor de 'usuarios[1]' -> Pedro (30 años)
# - Vuelta 3: 'usuario' toma el valor de 'usuarios[2]' -> Steven (25 años)
# ==============================================================================

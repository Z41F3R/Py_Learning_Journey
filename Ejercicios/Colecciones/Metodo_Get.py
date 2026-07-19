#!/usr/bin/env python3

usuario = {
    "nombre": "Steven",
    "edad": 25
}

def obtener_nombre(usuario):
    return usuario.get("nombre", "No")
    
r = obtener_nombre(usuario)
print(r)

# .get("clave", valor_por_defecto)
#
# Python intenta buscar la clave "nombre".
#
# Si la clave existe:
# devuelve su valor asociado.
#
# Si la clave NO existe:
# devuelve el valor por defecto indicado.
#
# Este patrón se conoce como:
# - Default Value
# - Fallback Value
#
# y permite acceder a diccionarios de forma segura
# sin provocar un KeyError.

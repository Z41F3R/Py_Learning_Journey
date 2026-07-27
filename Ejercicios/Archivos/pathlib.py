#!/usr/bin/env python3

from pathlib import Path

def buscar_archivo_global(valor):
    ruta_global = Path.home()
    busqueda = ruta_global.rglob(valor)

    return busqueda

def buscar_archivo_local(valor):
    ruta = Path(".")
    busqueda = any(ruta.rglob(valor))

    return busqueda

def manera(valor):
    ruta = Path("proyecto_01") / valor
    return ruta.exists()

result = buscar_archivo_global("l.txt")
print(result)

# ruta.exists()
#   Existe ?

# ruta.is_file()
#   Es un archivo?

# ruta.is_dir()
#   Es un directorio?

# ruta.name()
#   Solo el nombre

# ruta.suffix()
#   La extension

# ruta.steam()
#   El nombre sin la extension

# ruta.parent()
#   La carpeta padre

# ruta.mkdir()
#   Crear directorio

# ruta.unlink()
#   Eliminar archivos

# ruta.glob("*.txt")
#   Buscar todos los txt

# ruta.rglob("*.log")
#   Buscar recursivamente

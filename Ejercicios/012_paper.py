#!/usr/bin/env python3

#def comprobar(numero):
#    for n in range(2, numero):
#        if numero % n == 0:
#            print("RESIDUO 0")
#        else:
#            print("RESIDUO //")

#comprobar(11)

numero = 100
mitad = int(numero ** 0.5) + 1

print(mitad)


# ==============================================================================
# CONCEPTO 1: PROPIEDAD DE LOS FACTORES EMPAREJADOS (Los divisores van en parejas)
# ==============================================================================
# Explicación: En matemáticas, los números que dividen a otro siempre vienen tomados 
# de la mano (ej: en el 100 las parejas son 2x50, 4x25, 5x20). Al llegar a la raíz 
# cuadrada (10x10), las parejas se agotan y simplemente se repiten a la inversa 
# (20x5, 25x4, 50x2). No existen divisores "solitarios".

# ==============================================================================
# CONCEPTO 2: EL "PIVOTE" O "PUNTO DE INFLEXIÓN" (El espejo del producto)
# ==============================================================================
# Explicación: Los matemáticos se refieren a la raíz cuadrada como el pivote del 
# producto. Es el espejo exacto donde las multiplicaciones dejan de avanzar hacia 
# números nuevos y empiezan a repetirse a la inversa (como ocurre con 6x6=36 o 
# 10x10=100). Es el punto de quiebre donde la búsqueda de divisores se vuelve redundante.

# ==============================================================================
# CONCEPTO 3: EL LÍMITE DE LA RAÍZ CUADRADA (Freno de mano para el código)
# ==============================================================================
# Explicación: Es la aplicación práctica del Pivote en programación. Escribir 
# 'numero ** 0.5' le ordena a Python calcular ese centro exacto de multiplicación 
# para usarlo como límite máximo de búsqueda. Evita que la computadora camine por 
# tramos infinitos de forma innecesaria.

# ==============================================================================
# CONCEPTO 4: LA REGLA DEL FACTOR MENOR (Garantía matemática de descarte)
# ==============================================================================
# Explicación: Dice que si un número no es primo, obligatoriamente tiene que tener 
# al menos un divisor pequeño antes de su Pivote. Si recorres el camino desde el 2 
# hasta el centro y no encuentras ningún divisor, es FISICAMENTE IMPOSIBLE que 
# aparezca uno después, porque necesitaría un compañero pequeño que ya descartaste.

# ==============================================================================
# CONCEPTO 5: DIVISIÓN POR TENTATIVAS OPTIMIZADA (Trial Division)
# ==============================================================================
# Explicación: Es el nombre formal de este algoritmo. Consiste en probar residuos 
# uno por uno, pero reduciendo el recorrido de forma masiva gracias al Pivote. 
# Convierte una búsqueda que tardaría días enteros con números gigantes (del usuario loco) 
# en un cálculo instantáneo de apenas unos milisegundos para la CPU.

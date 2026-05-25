### Descripción del reto

Implementar una función que recorra un texto y cuente cuántas vocales contiene utilizando loops, condicionales y acumuladores.

El ejercicio también introduce el concepto de **Generadores (Generators)** y la **Evaluación Perezosa (Lazy Evaluation)** en Python.

---
### Funciones a implementar

**1. `contar_vocales(texto)`**

**Descripción:**  
Recibe una cadena de texto y retorna la cantidad total de vocales encontradas.

**Vocales válidas**
```python
a e i o u
```

**Input a enviar:**
```python
contar_vocales("murcielago")
```

**Output esperado**
```python
5
```

---
### Restricciones
**No usar:**

- Regex
- Librerías externas

---
### Conceptos practicados

- `for`
- `if`
- `in`
- acumuladores
- strings iterables
- generadores
- lazy evaluation
---
### Solución implementada

**Código Completo**

```python
#!/usr/bin/env python3

contar_vocales = lambda texto: sum(
    1 for letra in texto if letra.lower() in 'aeiou'
)

contar_vocales_en_texto = contar_vocales("Hola, ¿cómo estás?")
print(contar_vocales_en_texto)

# A este comportamiento en programación se
# le llama Evaluación Perezosa (Lazy Evaluation).
# No trabaja hasta que no es estrictamente necesario.
```

---
### Explicación paso a paso

**1. Función lambda**

```python
contar_vocales = lambda texto: ...
```

Uso una función lambda porque toda la lógica puede resolverse en una sola expresión.

La función recibe un texto y retorna directamente el total de vocales encontradas.

---

**2. Uso de `sum()`**

```python
sum(...)
```

La función `sum()` actúa como acumulador.

Va sumando los valores generados uno por uno.

Cada vocal encontrada aporta:

```python
1
```

Al total final.

---
**3. Uso del generador**

```python
1 for letra in texto if letra.lower() in 'aeiou'
```

Aquí ocurre lo más importante del ejercicio.

Esto NO crea una lista completa en memoria.

En cambio, crea un **Generador**, que produce valores uno a uno únicamente cuando `sum()` los necesita.

---
### ¿Qué es un Generador?

Un Generador en Python es un objeto especial que produce elementos bajo demanda.

En lugar de calcular todo de una vez, entrega los datos poco a poco.

---
### Diferencia conceptual

**Lista tradicional**

```python
[1 for letra in texto if letra.lower() in 'aeiou']
```

- Calcula TODO inmediatamente.
- Guarda todos los resultados en memoria RAM.
- Consume más memoria.

**Generador**

```python
(1 for letra in texto if letra.lower() in 'aeiou')
```

- Produce valores uno a uno.
- No almacena todos los resultados.
- Consume mucha menos memoria.

---
### Evaluación Perezosa (Lazy Evaluation)

Este comportamiento se conoce como:

> **Lazy Evaluation**

El generador no trabaja hasta que alguien solicita el siguiente valor.

En este caso:

```python
sum()
```

va pidiendo cada elemento individualmente.

---
### Flujo interno del programa

**Paso 1**
Recorrer cada letra:

```python
for letra in texto
```

**Paso 2**
Convertir cada letra a minúscula:

```python
letra.lower()
```

Esto permite detectar vocales mayúsculas y minúsculas.

**Paso 3**
Validar si es vocal:

```python
if letra.lower() in 'aeiou'
```

**Paso 4**
Si es vocal, generar:

```python
1
```

**Paso 5**
`sum()` acumula todos los unos generados.

---
### Investigación adicional realizada

Durante la resolución del ejercicio investigué cómo funcionan las expresiones generadoras en Python y descubrí el concepto de:

- **Generators**
- **Lazy Evaluation**

Esto me permitió entender que:

```python
sum(1 for letra in texto if letra.lower() in 'aeiou')
```

no crea una lista completa en memoria, sino que genera valores uno por uno únicamente cuando `sum()` los necesita.

Gracias a esto, la solución resulta más eficiente en consumo de memoria y más cercana a prácticas modernas de Python.

---
### Aprendizajes y decisiones técnicas

**¿Por qué usar un generador?**
Porque es más eficiente en memoria.
Especialmente útil cuando trabajas con textos enormes o millones de datos.

**¿Por qué usar lower()?**
Para evitar problemas entre:
`"A" y "a"`
Así ambas cuentan como vocales válidas.

**¿Por qué usar in?**
`in 'aeiou'`
Porque permite verificar pertenencia de forma limpia y legible.

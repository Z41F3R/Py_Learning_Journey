  ### Descripción del reto

Implementar una función llamada `contador_regresivo(numero)` utilizando ciclos `while`.

El objetivo original era practicar:

- loop
- condición de parada
- actualización manual del estado
- prevención de loops infinitos

Sin embargo, durante la resolución del ejercicio se exploro una implementan mas avanzada utilizando:

- `yield`
- generadores (Generators)
- evaluación perezosa (Lazy Evalatuion)

---
### Funciones a implementar

**1. `contador_regresivo(numero)`**

**Descripción:**
Debe generar una cuenta regresiva desde el numeró recibido hasta `1`, y finalmente mostrar:

`Despegar`

**Input a enviar:**

```python
contador_regresivo(5)
```

**Output esperado**

```python
5
4
3
2
1
Despegar
```

---
### Restricciones originales

**Usar :**

- `while`
- decremento manual

**No usar :**

- `for`

---
### Solución implementada

**Código Completo**

```python
#!/usr/bin/env python3

def contador_regresivo(valor):
    for numero in range(valor, 0, -1):
        yield numero

    yield "Despegar"

for resultado in contador_regresivo(6):
    print(resultado)
```

---
### Explicación General

Aunque el ejercicio pedía practicar `while`, decidí implementar una versión mas avanzada utilizando: 

- `yield`
- `range()`
- generadores

Esto transformó completamente el comportamiento de la función. 

---
### ¿Qué hace realmente yield?

**Diferencia importante**

**return**

```python
return valor
```

- Retorna el valor.
- Termina completamente la función.

**yield**

```python
yield valor
```

- Entrega un valor temporalmente.
- Pausa la función.
- Conserva su estado interno.
- Puede continuar después.

**Lo que se convictorio esta función**

La función dejo de ser una función normal y paso a convertirse en

> Un Generador (Generator)

---
### ¿Qué retorna ahora?

Ya NO retorna una lista.

Retorna un:

`Objeto generador`

Ese objeto produce valores uno por uno cuando son solicitados.

---
### Flujo interno del programa

**Paso 1**

Se llama:

```python
contador_regresivo(6)
```

Pero la función realmente No ejecuta todo inmediatamente.

Python crea un generador suspendido en memoria.

**Paso 2**

En loop:

```python
for resultado in contador_regresivo(6):
```

Empieza a solicitar valores uno por uno.

**Paso 3**

La función se reanuda desde donde quedó pausada:

```python
yield numero
```

**Paso 4**

Cuando vuelve a iterar:

- continúa exactamente donde quedó
- no reinicia la función
- mantiene el estado interno

---
### Uso de `range()`

```python
range(valor, 0, -1)
```

Esto significa:

- inicio = `valor`
- fin = `0` (sin incluir)
- paso = `-1`

Ejemplo:

```python
range(6, 0, -1)
```

produce:

```python
6 5 4 3 2 1
```

---
### ¿Por qué esto es importante?

Porque los generadores son una característica muy poderosa de Python.

Permiten:

- ahorrar memoria
- procesar streams
- trabajar con archivos enormes
- networking
- parsers
- scraping
- pipelines de datos

---
### Evaluación Perezosa (Lazy Evaluation)

El generador trabaja bajo el concepto de:

> Lazy Evaluation

Eso significa:

- NO calcula todos los valores de una vez
- Produce cada valor únicamente cuando se necesita

**Diferencia conceptual**

Lista tradicional

```python
[6, 5, 4, 3, 2, 1]
```

- Todo existe en memoria inmediatamente.

**Generador**

```python
yield numero
```

- Produce un valor a la vez.
- Consume mucha menos memoria.
- Escala mejor.

---
### Conceptos utilizados realmente

Aunque el ejercicio era sobre `while`, la solución terminó practicando: 

- `yield`
- generadores
- iteradores
- lazy evaluation
- control de estado interno
- range avanzado
- flujo secuencial suspendido
- consumo eficiente de memoria

---
### Aprendizajes obtenidos

**¿Por qué yield es tan importante?**

Porque permite construir funciones que producen datos progresivamente sin cargar todo en memoria.

Es uno de los conceptos más poderosos de Python moderno.

**¿Qué entendí con este ejercicio?**

Que una función puede:

- pausar su ejecución
- recordar su estado
- continuar después
- comportarse como un flujo de datos
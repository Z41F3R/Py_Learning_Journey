### Descripción del reto

Implementar dos funciones que trabajen juntas: una para invertir cadenas de texto y otra para aplicar esa transformación a una lista completa usando el concepto de **callback**.

### Funciones a implementar

 **1. `invertir(texto)`**

 **Descripción:**  
Recibe una cadena de texto y retorna su versión invertida.

**2. `aplicar_lista(lista, funcion)`**

**Descripción:**  
Recibe una lista de textos y una función callback. Aplica la función a **todos** los elementos de la lista y retorna una nueva lista con los resultados.

**Input a enviar:**

```python
aplicar_lista(["hola", "python", "bro"], invertir)
```

**Output esperado**

```python
['aloh', 'nohtyp', 'orb']
```

---
### Solución implementada

**Código Completo**

```python
#!/usr/bin/env python3  

invertir = lambda texto: (texto[::-1])

def aplicar_lista(lista, funcion):
	lista_vacia = []
	for i in lista:
		resultado = funcion(i)
		lista_vacia.append(resultado)

	return lista_vacia

  

lista = ["hola", "python", "bro"]
resultado = aplicar_lista(lista, invertir)
print(resultado)
```

---
### Explicación paso a paso

**1. Función `invertir` (lambda)**

```python
invertir = lambda texto: texto[::-1]
```

- Uso de **función anónima (lambda)** porque solo necesito retornar el texto invertido.

- El slicing `[::-1]` invierte la cadena de manera eficiente.

- Al ser una expresión simple, la lambda queda **limpia y directa**.

---

**2. Función `aplicar_lista`**

```python
def aplicar_lista(lista, funcion):
    lista_vacia = []
    for i in lista:
        resultado = funcion(i)
        lista_vacia.append(resultado)
    return lista_vacia
```

**Flujo de ejecución:**

1. Creo una `lista_vacia` como **acumulador local**.

2. Recorro cada elemento `i` de la lista original.

3. Aplico el callback `funcion(i)` (en este caso `invertir`) y guardo el retorno en `resultado`.

4. Agrego `resultado` a `lista_vacia` usando `.append()`.

5. Terminado el bucle, **retorno la lista transformada**.

---
### Aprendizajes y decisiones técnicas

**¿Por qué lambda y no `def`?**  
Porque solo necesito retornar `texto[::-1]` sin lógica adicional. La lambda es más concisa y legible para este caso.

**¿Por qué `lista_vacia` como acumulador?**  
Para no modificar la lista original (principio de **inmutabilidad** de los datos de entrada).

**¿Por qué `resultado` dentro del bucle?**  
Para dejar explícito que cada llamada al callback genera un nuevo valor.


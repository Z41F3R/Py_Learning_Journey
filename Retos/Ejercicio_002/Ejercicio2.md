### Descripción del reto

Implementar dos funciones que trabajen juntas: una para duplicar textos y otra para aplicar esa transformación a una lista completa usando el concepto de callback.

### Funciones a implementar

**1. `duplicar(texto)`**

**Descripción:**
Recibe una cadena de texto y retorna el texto duplicado.

 **2. `transformar_lista(lista, funcion)`**
 
 **Descripción:**
Recibe una lista de textos y una función callback. Aplica la función a todos los elementos de la lista y retorna una nueva lista con los resultados.

**Input a enviar:**

```python
transformar_lista(["a", "bro", "python"], duplicar)
```

**Output esperado**

```python
['aa', 'brobro', 'pythonpython']
```

---
### Solución implementada

**Código Completo**

```python
#!/usr/bin/env python3

duplicar = lambda texto: texto + texto

def transformar_lista(lista, funcion):
	lista_local = []
	for i in lista:
		resultado = funcion(i)
		lista_local.append(resultado)

	return lista_local

resultado = transformar_lista(["a", "bro", "python"], duplicar)
print(resultado)
```

---
### Explicación paso a paso

**1. Función `duplicar` (lambda)**

```python
duplicar = lambda texto: texto + texto
```

Uso una función lambda porque solamente necesito retornar el texto concatenado consigo mismo.

Ejemplos:

```python
"a" + "a" = "aa""bro" + "bro" = "brobro"
```

La lambda queda compacta y fácil de leer para una operación simple.

---

**2. Función `transformar_lista`**

```python
def transformar_lista(lista, funcion):
	lista_local = []
	for i in lista:
		resultado = funcion(i)
		lista_local.append(resultado)

return lista_local
```

**Flujo de ejecución:**

1. Creo `lista_local` como acumulador vacío.

2. Recorro cada elemento `i` de la lista original.

3. Ejecuto el callback usando:

```python
funcion(i)
```

4. El resultado se guarda en `resultado`.

5. Agrego el nuevo valor a `lista_local` usando `.append()`.

6. Al terminar el recorrido, retorno la nueva lista transformada.

---
### Aprendizajes y decisiones técnicas

**¿Por qué lambda y no def?**
Porque la lógica es extremadamente simple:

```python
texto + texto
```

No necesito múltiples líneas ni lógica compleja, así que lambda hace el código más limpio y directo.

**¿Por qué usar una lista nueva?**

```python
lista_local = []
```

Porque así no modifico la lista original recibida como parámetro.
Esto mantiene los datos de entrada intactos y evita efectos secundarios innecesarios.

**¿Por qué usar resultado dentro del bucle?**

```python
resultado = funcion(i)
```

Porque deja explícito que el callback genera un nuevo valor en cada iteración.
Eso ayuda a entender mejor el flujo de transformación de datos usando callbacks.

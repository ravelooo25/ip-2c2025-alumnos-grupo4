# Algoritmo de ordenamiento por inserción
El algoritmo de ordenamiento por inserción es un método sencillo para ordenar una lista de elementos. Funciona construyendo una parte ordenada de la lista, elemento por elemento. En cada paso, el algoritmo toma el siguiente elemento de la parte no ordenada y lo inserta en la posición correcta dentro de la parte ordenada.

# Fases del algoritmo:
El algoritmo avanza elemento por elemento. Para cada elemento, se divide el trabajo en dos fases precisas. El código implementa estas fases mediante las variables i y j y las decisiones dentro de step().
- Fase "buscar": La primera fase comienza cuando el algoritmo selecciona el elemento que quiere insertar en la parte ya ordenada. Esto ocurre cuando j es None. En ese momento, el código fija j en el valor de i y señala que items[i] es el elemento que se intentará insertar hacia la izquierda. Esta fase no realiza intercambios. Su función es preparar el proceso de inserción marcando el punto de partida desde el cual se moverá el elemento si corresponde. El algoritmo muestra la comparación entre j y j menos uno para indicar cuál será el próximo paso.
```
if j is None:
        j = i
        return {"a": j, "b": j - 1 if j > 0 else None, "swap": False, "done": False}
```
- Fase "insertar": Aquí el algoritmo compara el elemento actual items[j] con el elemento ubicado a su izquierda. Si el valor a la izquierda es mayor, el código realiza un intercambio y mueve j una posición hacia atrás. Esto desplaza el elemento seleccionado hacia su posición correcta dentro de la parte ya ordenada. Este proceso se repite mientras el valor de la izquierda sea mayor. Cuando el elemento ya no necesita seguir moviéndose, el algoritmo da por completada la inserción y avanza i para trabajar sobre el siguiente valor. En ese momento j vuelve a None y el ciclo retorna a la fase inicial pero con un nuevo elemento.
```
if j > 0 and items[j - 1] > items[j]:
        items[j - 1], items[j] = items[j], items[j - 1]
        j -= 1
        return {"a": j + 1, "b": j, "swap": True, "done": False}

    i += 1
    j = None
    return {"a": None, "b": None, "swap": False, "done": False}
```
Finalmente, cuando i alcanza el final de la lista (n), el algoritmo ha terminado y devuelve {"done": True}.
```
if i >= n:
        return {"a": None, "b": None, "swap": False, "done": True}
```
---
# Problemas ocurridos:
1. Error lógico en la fase de inserción. No se definió j=None al finalizar la inserción de un elemento, lo que causaba que el algoritmo no avanzara correctamente al siguiente elemento. Se corrigió agregando j = None después de completar la inserción.
2. Error en la condición de finalización. La condición if i >= n: estaba mal ubicada dentro del bloque de inserción, lo que impedía que el algoritmo reconociera correctamente cuando había terminado de ordenar toda la lista. Se corrigió moviendo esta condición al inicio de la función step().

# CONCLUSIÓN GENERAL DE ERRORES: 
El algoritmo fallaba principalmente por problemas de manejo de índices y condiciones lógicas en las fases del algoritmo. Estos errores afectaban la correcta ejecución del algoritmo y su capacidad para ordenar la lista paso a paso. Al corregir estos problemas, el algoritmo pudo funcionar correctamente, permitiendo visualizar el proceso de ordenamiento por inserción de manera efectiva.
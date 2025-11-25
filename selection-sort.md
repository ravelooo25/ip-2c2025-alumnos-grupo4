# Algoritmo de ordenamiento por selección
El algoritmo de ordenamiento por selección es un método sencillo para ordenar una lista de elementos. Funciona dividiendo la lista en dos partes: una parte ordenada y otra no ordenada. En cada paso, el algoritmo busca el elemento más pequeño en la parte no ordenada y lo intercambia con el primer elemento de esa parte, expandiendo así la parte ordenada.

# Fases del algoritmo:
- Fase "buscar": En esta fase, el algoritmo compara los elementos de la lista para encontrar el índice del elemento más pequeño (min_idx) en la parte no ordenada. Se avanza el índice j para recorrer los elementos restantes.
```
    if fase == "buscar":
            if j >= n:
                fase = "swap"
                return {"a": min_idx, "b": j-1, "swap": False, "done": False}
            b=j
            if items[j] < items[min_idx]:
                min_idx = j
            j += 1
            return {"a": min_idx, "b": b, "swap": False, "done": False}
```            
- Fase "swap": En esta fase, si el índice del elemento más pequeño (min_idx) es diferente del índice actual (i), se realiza un intercambio entre estos dos elementos. Luego, se da valor a "a=i" y "b=min_idx", se avanza el índice i para pasar al siguiente elemento y se reinician los índices j y min_idx para continuar con el proceso de búsqueda en la siguiente iteración.
```
if fase == "swap":
        swap=min_idx != i
        if swap:
            items[i], items[min_idx] = items[min_idx], items[i]
        a=i
        b=min_idx
        i+=1
        ...
        j = i + 1
        min_idx = i
        fase = "buscar"

        return {"a": a, "b": b, "swap": swap, "done": False}
```
- El algoritmo continúa alternando entre las fases "buscar" y "swap" hasta que toda la lista esté ordenada.
- Cuando el índice i alcanza el final de la lista (n - 1), el algoritmo ha terminado y devuelve {"done": True}. Se usó (n - 1) porque la lista tiene n cantidad de elementos, entonces el último valor del índice es (n - 1).
```
if i >= n-1:
            return {"a": a, "b": b, "swap": swap, "done": True}
```
---
# Problemas ocurridos:
1. No se había implementado el global i, j, min_idx, fase en la función step(), lo que causaba errores al intentar acceder a estas variables.
2. Error de indentación en el bloque swap. Una línea dentro del if que controla el intercambio quedó con más espacios que el resto del bloque. Esto alteró la estructura del código y provocó que Visual Studio Code reacomode automáticamente varias líneas. Por lo que (i = i + 1, j = i + 1, min_idx = i) quedaron fuera del bloque al que pertenecen. El error se resolvió corrigiendo los espacios y alineando todas las líneas correctamente.
3. Error de sincronización en fase swap y buscar. En la fase de búsqueda, cuando el cursor j llegaba al final de la lista (j >= n), el código hacía: fase = "swap" y luego devolvía el diccionario. Pero al volver a entrar en step(), el código seguía en fase "buscar" porque no se había actualizado la variable fase antes de devolver el diccionario. Esto causaba que el algoritmo no avanzara correctamente a la fase de intercambio. El error se resolvió agregando un return inmediatamente después de actualizar la variable fase a "swap", asegurando que el cambio de fase se reflejara en la siguiente llamada a step(). Este error causaba que el visualizador sea informado que estaba en fase buscar cuando en realidad ya había pasado a fase swap.
4. Se colocó el return {"done": True} al inicio de la función step() lo que impedía la ultima fase swap de ejecutarse. Se corrigió moviendo el return al final de la función, permitiendo que la fase swap se ejecute correctamente antes de finalizar el algoritmo.
5. Se rehízo la fase swap con el objetivo de simplificarla, ya que tenia demasiadas variables temporales que hacían el código mas difícil de leer y entender.

# CONCLUSIÓN GENERAL DE ERRORES:
El algoritmo fallaba principalmente por problemas de indentación y errores de flujo de control entre las fases del algoritmo. Estos errores afectaban la correcta ejecución del algoritmo y su capacidad para ordenar la lista paso a paso. Al corregir estos problemas, el algoritmo pudo funcionar correctamente, permitiendo visualizar el proceso de ordenamiento por selección de manera efectiva.


# Documentación del Algoritmo MergeSort --- Implementación Paso a Paso
## Objetivo

Esta implementación de MergeSort está diseñada para funcionar paso a
paso, generando una única acción por ejecución de `step()`, ideal para
visualizadores educativos.

------------------------------------------------------------------------

## Sobre el Algoritmo

El algoritmo se basa en la ideología "divide y vencerás", donde divide a la mitad hasta que queden con 2 o 3 elementos, se ordenan y se unen.

Visualmente, se observa cómo 8 segmentos ordenados pasan a 4, luego a 2 y finaliza uniendo todo.

------------------------------------------------------------------------

## Funcionamiento General

-   Implementación **iterativa** (bottom-up), sin recursión.
-   El array se procesa en segmentos de tamaño creciente:
    `1, 2, 4, 8...`
-   Cada merge es progresivo, sin ordenar el segmento completo de golpe.
-   `step()` produce:
    -   un swap,
    -   un highlight,
    -   o un avance de etapa.

------------------------------------------------------------------------

## Variables del Sistema

  Variable      Propósito
  ------------- ------------------------------------------------
  `items`       Lista actual
  `n`           Tamaño total
  `width`       Tamaño de subarray actual
  `left`        Inicio del merge
  `mid`         Punto medio
  `right`       Final del merge
  `merged`      Resultado temporal
  `t_ptr`       Índice donde colocar el próximo valor correcto
  `done_flag`   Indica fin del algoritmo

------------------------------------------------------------------------

## Función `init(vals)`

Inicializa el estado:

``` python
def init(vals):
    global items, n, width, left, mid, right, merged, t_ptr, done_flag
    items = list(vals)
    n = len(items)
    width = 1
    left = 0
    mid = 0
    right = 0
    merged = None
    t_ptr = 0
    done_flag = False
    return True
```

------------------------------------------------------------------------

## Función `step()`

Motor del merge sort paso a paso.

### 1. Finalización

``` python
if done_flag:
    return {"done": True}
```

### 2. Preparar un merge

Cuando `merged == None`, se analiza el próximo segmento y se genera la
lista ordenada `merged`.

### 3. Verificar si el segmento ya coincide

Si el contenido entre `left` y `right` ya coincide con `merged`, avanza
al próximo merge.

### 4. Resaltar valores correctos

Permite señalar en la UI que ese índice ya está ordenado.

### 5. Swaps controlados

Un solo swap por ejecución:

``` python
items[t_ptr], items[p] = items[p], items[t_ptr]
return {"a": t_ptr, "b": p, "swap": True}
```

### 6. Terminación total

Cuando `width >= n`:

``` python
return {"done": True}
```
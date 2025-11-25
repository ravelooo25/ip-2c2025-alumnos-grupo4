
# Documentación del Algoritmo QuickSort — Implementación Paso a Paso

Este archivo documenta el funcionamiento del script de QuickSort provisto, diseñado para funcionar **paso a paso** junto a un frontend visualizador.

---

## Sobre el Algoritmo

El algoritmo se basa en la ideología `divide y vencerás`, donde con un elemento llamado `pivote` divide en 2 segmentos, mayor y menor; luego se agarra el mayor y se divide de la misma forma, y así sucesivamente hasta que esté ordenado y se pasa al menor. 

---

## Objetivo del Script

El propósito de esta implementación es permitir que **cada llamada** al método `step()` produzca **una única acción del algoritmo**, ya sea:

- Un swap entre dos elementos  
- Una comparación resaltada  
- Una transición entre fases de la partición  
- O bien indicar que el algoritmo ha finalizado  

Esto lo hace ideal para animaciones y aprendizaje visual del funcionamiento de QuickSort.

---

## Estructura General

El archivo define:

- Una lista global `items` con los valores a ordenar  
- Un stack llamado `stack` que simula las llamadas recursivas  
- Un conjunto de etapas (`stages`) para permitir que QuickSort continúe paso a paso  
- Dos funciones principales:
  - `init(vals)` — inicializa todo el estado interno  
  - `step()` — ejecuta una única acción del algoritmo

---

## Función `init(vals)`

Inicializa todos los valores globales:

```python
def init(vals):
    global items, n, stack
    items = list(vals)
    n = len(items)
    stack = [(0, n - 1, "partition", None, None, None)]
```

Crea una única tarea inicial para ordenar el segmento completo `[0, n-1]`.

---

## Función `step()`

Es el corazón del sistema.  
Cada llamada procesa **un micro-paso** del algoritmo.

### Etapas del algoritmo:

### 1. **partition**
Define:

- `pivot_index`
- `i`
- `j`

Y pasa inmediatamente a la etapa `"partition_step"`.

Devuelve una acción de highlight sobre el pivot.

---

### 2. **partition_step**
Se ejecuta repetidamente hasta completar una partición.

Dentro de esta etapa:

#### ✔ Comparaciones (`items[j] <= pivot`)
Si el elemento es menor o igual que el pivot:

- Se incrementa `i`
- Puede haber swap si `items[i] != items[j]`

Luego se devuelve una acción del tipo:

```json
{"a": i, "b": j, "swap": true/false, "done": false}
```

#### ✔ Cuando `j` alcanza el final
Se intercambia el pivot a su posición final.

Luego se agregan dos nuevas tareas al stack:

- Ordenar la mitad izquierda  
- Ordenar la mitad derecha  

El algoritmo continúa hasta que no queden más tareas.

---

## Finalización

Cuando no quedan tareas en el stack, `step()` devuelve:

```json
{"done": true}
```

---
# Quick Sort By Santiago Casellas
items = []
n = 0

#Pila de tareas pendientes (Estados de la partición):
#(left, right, stage, i, j, pivot_index)
#left y right son los índices del segmento que estamos ordenando.
#stage es la etapa del algoritmo.
#i y j son los índices de la partición.
# pivot_index es el índice del pivot stack = []

def init(vals):
    global items, n, stack
    items = list(vals)
    n = len(items)

    # Cargar la tarea inicial. todo el array
    # stages: "partition", "subcalls"
    stack = [(0, n - 1, "partition", None, None, None)]

def step():
    global items, stack
    #--------------------------------------------------
    #            ETAPA 0: Inicializar
    # Realizamos un filtro antes de procesar
    #--------------------------------------------------
    # Si ya no quedan tareas > terminamos
    if not stack:
        return {"done": True}
    
    left, right, stage, i, j, pivot_index = stack.pop()

    # Si ek segmento es inválido o de 1 elemento > continuar
    if left >= right:
        return {"done": False, "a": 0, "b":0, "swap": False}
    #--------------------------------------------------
    #            ETAPA 1: Inicializar partición
    # Seleccionamos el pivot y los índices de la partición
    #--------------------------------------------------
    if stage == "partition":
        pivot_index = right
        i = left - 1
        j = left

        # Guardar reanudación
        stack.append((left, right, "partition_step", i, j, pivot_index))

        return {"done": False, "a": pivot_index, "b": pivot_index, "swap": False}
    
    #--------------------------------------------------
    #            ETAPA 2: Hacer pasos de partición
    # Realizamos la partición
    #--------------------------------------------------
    if stage == "partition_step":

        # Si el segmento es inválido o de 1 elemento > continuar
        if j > right - 1:
            new_pivot = i + 1

            # Guardar reanudación
            swap = False
            a = new_pivot
            b = pivot_index

            # Si el pivot es menor que el nuevo pivot > intercambiar
            if items[new_pivot] > items[pivot_index]:
                items[new_pivot], items[pivot_index] = items[pivot_index], items[new_pivot]
                swap = True
            
            # Guardar reanudación
            stack.append((left, new_pivot - 1, "partition", None, None, None))
            stack.append((new_pivot + 1, right, "partition", None, None, None))

            return {"done": False, "a": a, "b": b, "swap": swap}
        
        pivot_val = items[pivot_index]

        # Si el elemento es menor o igual al pivot > continuar
        if items[j] <= pivot_val:
            i += 1
            
            # Si los elementos son diferentes > intercambiar
            swap = False
            if items[i] != items[j]:
                items[i], items[j] = items[j], items[i]
                swap = True

            # Guardar reanudación
            stack.append((left, right, "partition_step", i, j + 1, pivot_index))
            return {"done": False, "a": i, "b": j, "swap": swap}
        
        # Guardar reanudación
        stack.append((left, right, "partition_step", i, j + 1, pivot_index))
        return {"done": False, "a": j, "b": pivot_index, "swap": False}
# MergeSort By Santiago Casellas
# Merge Sort iterativo (bottom-up) paso a paso

items = []
n = 0

# estado del algoritmo
width = 1 # tamaño actual de subarrays a mergear
left = 0 # índice izquierdo del merge actual
mid = 0 # índice medio del merge actual
right = 0 # índice derecho del merge actual
merged = None # lista objetivo para el segmento [left:right]
t_ptr = 0 # posición objetivo dentro del segmento para aplicar swaps
done_flag = False

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


def step():
    
    # Cada llamada realiza UNA acción:
    # - si hay que swapear para colocar el valor correcto en t_ptr -> devuelve swap=True con (a=t_ptr,b=pos)
    # - si no hay swap necesario pero hay una comparación/posición a marcar -> devuelve swap=False (a,b)
    # - cuando termina devuelve {"done": True}
    
    global items, n, width, left, mid, right, merged, t_ptr, done_flag

    # ya terminado
    if done_flag:
        return {"done": True}

    # si la longitud es 0 o 1 -> termina
    if n <= 1:
        done_flag = True
        return {"done": True}

    # si no hay un merge preparado, preparar el siguiente merge para el width actual
    while True:
        if merged is None:
            # Si width ya cubre todo, terminamos
            if width >= n:
                done_flag = True
                return {"done": True}

            # buscar el siguiente segmento [left:mid:right] para mergear
            if left >= n:
                # procesamos todos los merges de este width -> incrementar width y reiniciar
                width *= 2
                left = 0
                continue

            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            # preparar merged (resultado deseado)
            i = left
            j = mid
            temp = []
            while i < mid and j < right:
                if items[i] <= items[j]:
                    temp.append(items[i]); i += 1
                else:
                    temp.append(items[j]); j += 1
            if i < mid:
                temp.extend(items[i:mid])
            if j < right:
                temp.extend(items[j:right])

            merged = temp
            t_ptr = left

        # Si el segmento ya está igual que merged -> finalizar este merge y preparar siguiente
        equal = True
        for idx in range(left, right):
            if items[idx] != merged[idx - left]:
                equal = False
                break
        if equal:
            # terminar merge actual
            merged = None
            left += 2 * width
            # loop para preparar siguiente merge or finish/width bump
            continue

        # buscar la próxima posición t_ptr dentro [left,right) que no coincida con merged
        while t_ptr < right and items[t_ptr] == merged[t_ptr - left]:
            # podemos devolver una comparación/highlight si querés
            # aquí devolvemos una marca (swap=False) para que el frontend pueda resaltar
            ret = {"a": t_ptr, "b": t_ptr, "swap": False, "done": False}
            t_ptr += 1
            return ret

        if t_ptr >= right:
            # todo coincide en este segmento, loop para acabar
            merged = None
            left += 2 * width
            continue

        # necesitamos poner merged[t_ptr-left] en items[t_ptr]
        desired_val = merged[t_ptr - left]

        # buscar una posición p > t_ptr dentro del segmento donde esté desired_val
        p = -1
        for k in range(t_ptr + 1, right):
            if items[k] == desired_val:
                p = k
                break

        if p == -1:
            # como fallback (muy raro): si no encontramos, puede ser que el valor ya esté en otra parte
            # para no fallar, devolvemos una marca sin swap
            ret = {"a": t_ptr, "b": t_ptr, "swap": False, "done": False}
            t_ptr += 1
            return ret

        # realizamos el swap en el array interno y devolvemos la acción (una sola swap por step)
        items[t_ptr], items[p] = items[p], items[t_ptr]
        # No actualizamos merged ni t_ptr aquí: en la próxima llamada veremos si items[t_ptr] quedó correcto
        return {"a": t_ptr, "b": p, "swap": True, "done": False}

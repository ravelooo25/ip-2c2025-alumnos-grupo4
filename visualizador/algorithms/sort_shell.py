
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
intervalo = 0
i = 0
j = None

def init(vals):
    global items, n, intervalo, i, j
    items = list(vals)
    n = len(items)
    intervalo = n // 2        # Primer intervalo, vale la mitad del largo de la lista
    i = intervalo            
    j = None           

def step():
    global items, n, intervalo, i, j

    # PASO 1: Verificamos que "intervalo" sea igual a 0, en ese caso el algoritmo ya termino.
    if intervalo == 0:
        return {"done": True}

    # Si "j" , todavia no existe, iniciamos una nueva insercion
    if j is None:
        if i >= n: #En el caso que "i", valga el largo de la lista
            # Reducir intervalo
            intervalo //= 2
            if intervalo == 0: #Volvemos a verificar que todavia queden pasadas.
                return {"done": True}
            i = intervalo
            j = None
            return {"a": 0, "b": 0, "swap": False, "done": False}
        j = i
        return {"a": j - intervalo, "b": j, "swap": False, "done": False}

    # Comparamos y hacemos el cambio
    if j - intervalo >= 0 and items[j] < items[j - intervalo]:
        a = j
        b = j - intervalo
        items[a], items[b] = items[b], items[a]
        j -= intervalo
        return {"a": a, "b": b, "swap": True, "done": False}

    # En caso, de no haber realizado un cambio, avanzamos al siguiente elemento
    i += 1
    j = None
    return {"a": 0, "b": 0, "swap": False, "done": False}
     



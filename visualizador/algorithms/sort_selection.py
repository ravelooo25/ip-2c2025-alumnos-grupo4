# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    
     # FASE BUSCAR
    if fase == "buscar":
        if j >= n:
            fase = "swap"
            return {"a": min_idx, "b": j-1, "swap": False, "done": False}
        b=j
        if items[j] < items[min_idx]:
            min_idx = j
        j += 1
        return {"a": min_idx, "b": b, "swap": False, "done": False}
    
    # FASE SWAP
    if fase == "swap":
        swap=min_idx != i
        if swap:
            items[i], items[min_idx] = items[min_idx], items[i]
        a=i
        b=min_idx
        i+=1
        if i >= n-1:
            return {"a": a, "b": b, "swap": swap, "done": True}
    
        j = i + 1
        min_idx = i
        fase = "buscar"

        return {"a": a, "b": b, "swap": swap, "done": False}
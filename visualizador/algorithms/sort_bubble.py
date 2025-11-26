# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0
cont = 0

def init(vals):
    global items, n, i, j, cont
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    # TODO:
    global items, n, i, j, cont
   

   #PASO 1: Verificamos que: 
    if j >= n -1 : # "j" llega al final de la lista, pero no esta terminado el algoritmo
        i = i + 1  
        j = 0 
        return {"a": 0, "b": 0, "swap": False, "done": False}
    

    #PASO 2: Asignamos las variables y comparamos
    a = j 
    b = j +1
    swap = False

    #Verificamos orden y sumamos al contador
    if(items[a]<items[b]):
        cont += 1

    #Si el contador, es >= que el largo de la lista, ya se ordeno completamente.
    if (cont >= n-1):
        return {"done": True}

    if items[a]>items[b]: #Comparo 2 indices de la lista
        items[a], items[b] = items[b], items[a] #Si el derecho es mayor al izquierdo, se cambian.
        cont = 0   # Al estar desordenados, el contador vuelve a 0.
        swap =True
  
    # Avanzo el puntero
    j = j+1 

    return {
        "a":a, "b":b, "swap":swap, "done": False,
    }

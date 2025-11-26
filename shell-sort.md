# ShellSort - Ordenamiento por insercion mejorado

El algoritmo Shell, es una version mejorada del InsertionSort, ya que compara elementos separados por un intervalo de varias posiciones, permitiendo que un elemento haga paso mas grandes hacia su posicion correcta. 

# Implementacion : 
Para este algoritmo, primero tuve que enteder como funciona el Insertion Sort ya que este es una version mejorada. En este caso el intercambio se realiza desde el valor "intervalo", que empieza valiendo la mitad del largo de la lista, y se compara con el primer elemento de la lista.
En caso de ser menor, se realiza el intercambio y se avanza al siguiente elemento para seguir comparando con el mismo intervalo de distancia.

En las proximas vueltas, el intervalo se reduce a la mitad, pero una vez que se realiza el intercambio, se cambian los punteros para que el elemento que debe ser reubicado encuentre su posicion correcta. Esta segunda comparacion, se realiza desde el numero inicial y el inicial menos el intervalo, es decir que si el cambio se realizo entre los indices [5] y [8], se ajustaran los punteros en el valor de "intervalo" hacia la izquierda, en este caso el intervalo es "3" y los punteros a comparar serian [3] y [5], en caso de que se realize el "swap", los proximos punteros serian [0] y [2].

La ultima pasada, tendra al intervalo como valor "1". En donde se comparan elementos adyacentes y se van trayendo los elementos mas chicos al principio de la lista. 
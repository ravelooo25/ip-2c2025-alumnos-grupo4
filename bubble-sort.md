# BubbleSort - Ordenamiento por burbujeo 

El algoritmo de burbujeo funciona comparando elementos adyacentes de una lista y los ordena si no estan en el orden correcto. Este proceso se repite hasta que la lista esta completamente ordenada, haciendo que los valores mas grandes se vayan moviendo al final de la lsita en cada comparacion.

# Implementacion : 
Empece por buscar como se usaba el algoritmo y como se escribiria en un programa normal, en base a eso la dificultad fue adaptar cada paso del algoritmo que tiene 2 ciclos anidados a hacer todo en un step(). 

En este caso, los valores los valores iniciales que utilize fueron los dados en el README.MD y ademas le agregue un contador para verificar que que la lista este totalmente ordenada. 

Como primer paso, verificamos "j >= n -1" , es decir que el puntero llego al ultimo lugar de la lista, se utiliza "n-1" ya que el la funcion "len()" nos da el valor entero de la lista, pero no tiene en cuenta que el primer indice es 0.
En caso de ser verdadero, le sumamos 1 al valor "i", que representa cada pasada que de el algoritmo y volvemos "j" a 0, para que en la proxima pasada, empiece desde el primer lugar de la lista.


Para el paso 2, asignamos las variables a y b para que tomen el valor del puntero j y j+1, es decir que toma 2 valores adyacentes. 

Como verificacion de orden utilizo el contador, y primero comparo el puntero "a" de la lista con el puntero "b". Se pide que el puntero "a" sea menor que el "b", y si es asi, el contador crece en una unidad.

Si el contador llega al valor del largo de la lista, el programa se detiene ya que la lista esta completamente ordenada.

En la comparacion, pedimos que el puntero "a", sea mayor al puntero b. En caso verdadero, se intercambian las posiciones y el contador vuelve a 0 ya que no estaban ordenados. 

Como ultimo paso, se incrementa el valor de "j" en una unidad, para que el proximo paso avance un lugar en la lista, y se hace el return con el valor de "done": False. 

El uso del contador, sirve para que el algoritmo no siga dando la cantidad de vueltas indicadas por el n = len(lista), una vez que esta está completamente ordenada. 
Cada enrutador mantiene una *tabla de enrutamiento (o de reenvío)* indizada por cada enrutador en la subred. Cada entrada comprende la línea preferida de salida hacia ese destino y una estimación del tiempo o distancia a ese destino.
A partir de su tabla de enrutamiento un enrutador E puede obtener *unv ector de distancia* que contiene una lista de pares <destino, retardo estimado>.
El retardo de un enrutador a un vecino suyo, puede medirlo con *paquetes de ECO* que el receptor simplemente marca con la hora y los regresa tan rápido como puede.

Cada $t$ mseg, cada enrutador envía a todos sus vecinos un vector de distancia y también recibe un vector de distancia de cada vecino.

**NOTACIÓN:**
- El vector de distancia del enrutador X se denota con $VD_X$.
- $VD_X$ es una función: $VC_X(i)$ que es la "distancia estimada" para llegar al enrutador i desde X
- Si X vecino de E, el retardo de E a X se denota con $R_{E,X}$ y se obtiene mediante un paquete ECO
- Entonces la distancia estimada desde E enrutador a i a traves de X es $R_{E,X} + VD_X(I)$

Si tengo muchas estimaciones del camino mas corto de E hasta i pasando por $X_n$, claramente la mejor va a ser la menor de todas ellas, siendo entonces el vecino de E con mejor estimación quien conviene que sea la línea de salida a usar desde E para ir a i

El enrutador E estima la *distancia* desde E al enrutador de destino i de la siguiente manera: 
$d(E, i) = \min (\{ R_{E,X} + VD_X(i) | X vecino de E  \})$

El mejor vecino para ir desde E a I se define como: 
$MV(E,i) = \text{elegir} \{ V:R_{E,V} + VD_V(i) = d(E,i)\}$

Entonces para actualizar la tabla de enrutamiento de E se va a seguir la secuencia:
- E recibió de todo vecino X suyo: $VD_X$ y $R_{E,X}$
- La tabla de enrutamiento de E en la fila del enrutador de destino i va a tener los valores: $d(E,i)$ y $MV(E,i)$
- Observar que la vieja tabla de enrutamiento no se usa en este cálculo


Lo malo del Algoritmo de Enrutamiento de Vector de Distancia, es que reacciona con rapidez a las buenas noticias, pero con lentitud ante las malas

Esto se debe a que si tengo por ejemplo N nodos, y todos los estan operativos y **ALCANZABLES** entonces como en cada paso todos comparten información, en a lo sumo N saltos todos sabran la topologia de la red y los caminos. El problema viene cuando hay un nodo inalcanzable o inoperativo, ya que como los nodos solo hablan con los vecinos directos (a distancia de 1 salto) siempre pretenderan que hay algun vecino lejano que sabra como llegar al nodo inalcanzable, haciendo que nunca se detecte el error
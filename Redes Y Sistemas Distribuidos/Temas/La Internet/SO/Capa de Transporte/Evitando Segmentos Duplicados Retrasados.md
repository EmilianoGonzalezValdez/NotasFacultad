Hay 2 razones por las que pueden llegar segmentos duplicados a un host receptor:
1. Si se pierde un ack y el segmento se retransmite
2. Si el segmento se demora debido a la congestión y su temporizador expira, el emisor lo retransmitira

Como no se puede entregar segmentos duplicados a la capa de aplicación, es necesario saber si un segmento que llega al host receptor es duplicado o no.

¿Como hacer para saber eficientemente si doss egmentos son diferentes o no?
La solución inviable es comparar ambos segmentos bit a bit ya que esto requeriria almacenar todos los segmentos que llegaron previamente, y eso es muy ineficiente.

Una mejor solución es numerar los segmentos con números de secuencia. Entonces los paquetes con n° de secuencia diferentes son distintos. Esta idea funcionaria bien si tenemos un n° de secuencia de tamaño arbitrario O números de secuencia lo suficientemente largos como para estar seguros de que no se van a reutilizar

Aun así los npumeros de secuencia no pueden ser de tamaño arbitrario porque queremos que los segmentos tengan longitud máxima. Por lo tanto el espacio de números de secuencia es finito; porque queremos que el número de secuencia sea un campo del encabezado de longitud fija

Esta idea de solo usar un espacio de secuencia finito y numerar los segmentos con n° de secuencia no siempre funciona bien
Por ejemplo, en la situación que pasa cuando un segmento S con n° de secuencia X queda demorado debido a que la red esta congestionada. El temporizador de retransmisiones asociado a S expira y se retransmite S. El protocolo de enrutamiento cambia las rutas y la retransmisión de S llega rápido a destino. Pero aun quedo en la red un *duplicado retrasado* de S (el que tiene número de secuencia X). Este duplicado retrasado de S más adelante llega a destino generando problemas.
Este tipo de problemas son tan serios que deben ser evitados


Entonces ¿Como encaramos los problemas de duplicados retrasados?
La idea es asegurar que ningun paquete viva más allá de T sec (tiempo de vida de paquete).
Esto se refiere a paquetes de datos, retransmisiones de ellos y a confirmaciones de recepción. Eliminar paquetes viejos que andan dando vueltas por ahí.
Veremos que esta idea hace que la solución de los problemas de duplicados retrasados sea manejable


**Para resolver el problema de duplicados retrasados dentro de una conexión:**
Asumiendo que T es el tiempo de vida de paquete, el origen etiqueta los segmentos con n° de secuencia que no van a reutilizarse dentro de T sec.
Para lograr que al regresar al principio de los n° de secuencia, los segmentos viejos con el mismo n° de secuencia hayan desaparecido hace mucho tiempo, el espacio de secuencia debe ser lo suficientemente grande para garantizar eso

Normalmente la cantidad de números de secuencia debe ser mayor a la cantidad de segmentos que puedo enviar en el tiempo de vida de cada segmento. Tendrá que ser potencia de 2 porque el número de secuencia es un campo del encabezado del segmento

**¿Como evitar que un duplicado retrasado que pasa de una conexión a otra genere problemas?**
Como al establecer una conexión se usan segmentos, una conexión debería tener un *N° inicial de secuencia* con el que comienza a operar

Una idea de solución seria escoger como número inicial de secuencia de la conexión nueva un n° de secuencia que haga imposible o improbable que el duplicado retrasado de n° de secuencia X genere problemas. Además se mantiene dentro de una conexión que el origen etiqueta los segmentos con n° de secuencia que no van a reutilizarse dentro de T sec (tiempo de vida del paquete).

Una implementación dada en el libro de Comer dice que:
Al crear una nueva conexión cada extremo genera un número de secuencia de 32 bits aleatorio que pasa a ser el npumero inicial de secuencia para todos los datos enviados. Alguna implementación de TCP usa esta solución.
Esta implementación tiende a funcionar debido a que la probabilidad de que un paquete duplicado retrasado genere problemas en una conexión siguiente es baja debido a la elección aleatoria del número inicial de secuencia de la conexión siguiente


Otra implementación diferente es dada en el libro de Tanembaum, donde:
Vincular el número de secuencia de algún modo al tiempo y para medir el tiempo usar un reloj de modo que:
- Cada host tiene un *reloj de hora del dia*
- Los relojes de los host no necesitan ser sincronizados, pues se supone que cada reloj es un contador binario que se incrementa a si mismo en intervalos uniformes.
- El reloj continua operando aun ante la caída del host
Cuando se establece una conexión los k bits de orden mayor del reloj = *Número inicial de secuencia*

Esto funciona debido a que si el reloj se mueve más rapido que la asignación de npumeros de secuencia a los paquetes que se envían, entonces el número inicial de secuencia de una nueva conexión va a ser mayor al número de secuencia de cualquier duplicado retrasado de la conexión previa

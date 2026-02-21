**Control de flujo:** Hay que evitar que un host emisor rápido desborde a un host receptor lento.

La capa de enlace de datos se ocupa del control de flujo entre dos máquinas directamente conectadas entre sí(pueden ser enrutador o host)

Podemos asumir que el receptor maneja búferes para los mensajes que llegan. Esto es necesario porque:
- Si la llegada de segmentos del emisor es mucho más rapida que el receptor para procesar los segmentos recibidos, entonces el receptor necesitará poder almacenar segmentos antes de procesarlos.
- El receptor puede acumular una cantidad de segmentos suficientes antes de pasarlos a la capa de aplicación para que loss procese
- Los segmentos pueden llegar desordenados, por lo tanto, si llegan un grupo de segmentos y faltan segmentos previos a ellos, habrá que almacenar los segmentos de ese grupo en buffer.

La capa de aplicación lee los mensajes que llegan, pero no necesariamente al instante en que los datos llegan. En lugar de eso, la aplicación receptora puede estar ocupada con otra tarea y puede no intentar leer los datos hasta bastante después que estos llegaron. Si la aplicación es demasiado lenta en leer los datos, el emisor puede saturar los búferes del receptor.
La capa de red puede tornar al receptor más lento y con menos capacidad de almacenamiento.

Aquí tenemos 2 situaciones:
1. Un enrutador en la rita entre el emisot y receptor daña un paquete; este error se va a detectar por la capa de transporte cuando el paquete dañado llegue al receptor. Si luego de ese paquete dañado llegan varios buenos, la capa de transporte tendrá que almacenarlos y el receptor va a ponerse más lento y con menos capacidad del búfer
2. El algoritmo de enrutamiento hace que cambien las rutas, rutas más lentas son remplazadas por rutas más rápidas; esto puede hacer que paquetes lleguen al receptor fuera de orden. Si esto sucede, entonces va a obligar a la capa de transporte a almacenar paquetes fuera de orden en búfer y el receptor va a ponerse más lento y con menos capacidad de búfer.

La capa de transporte puede tornar al receptor más lento y con menos capacidad de almacenamiento. Por ejemplo, si la cantidad de conexiones abiertas aumenta drasticamente; por ende, la cantidad de b+ufer para cada conexion disminuye y el receptor se pone más lento por la cantidad de aplicaciones aumentada. Esta situación sumada a las anteriores puede producir desbordamiento de búferes.


Si bien la capa de enlace de datos maneja el control de flujo, no maneja ninguna de las situaciones anteriores, por lo tanto necesitan ser tenidas en cuenta por la capa de transporte.

Si nos quedamos solo con los protocolos de comunicación confiable anteriores, estos no son suficientes para evitar desbordamiento de búferes en el receptor. Hace falta definir un protocolo especial para el control de flujo.

Si el receptor tiene varias conexiones, debe usar los búferes a medida que llegan los segmentos. Se dedican conjuntos de búferes especificos a conexiones especificas


**¿Como maneja el receptor el uso de búferes cuando entra un segmento?**
Cuando entra un segmento, el receptor intenta adquirir un búfer nuevo; si hay uno disponible se acepta el segmento, de otro modo se lo descarta.



Hasta ahora sabemos que se pueden dar las situaciones anteriores. El receptor y el emisor deben ajustar dinámicamente sus alojamientos de búferes, es decir, deben tener ventanas de tamaños variables. Ahora el emisor no sabe cúantos datos mandar en un momento dado, pero sí sabe cuántos datos le gustaría mandar.


**Entonces,¿Como se comportaria un protocolo de control de flujo?**
La solución se basa en que el host emisor *solicita espacio en búfer en el otro extremo* para estar seguro de no enviar de más y sobrecargar al receptor, porque solo el receptor sabe cuanto necesita.
El receptor sabe cuál es su situación y cuánto espacio puede otorgar, por ello cuando este recibe el pedido del emisor le reserva una cierta cantidad de búferes al emisor. Estos búferes podrian repetirse por conexión o no.
Si los búferes se reparten por conexión y aumenta la cantidad de conexiones abiertas el receptor necesita ajustar dinámicamente sus reservas de búferes


**Funcionamiento de la comunicación entre host emisor y host receptor usando la solución anterior**
1. Inicialmente el emisor solicita una cierta cantidad de búferes, con base en sus necesidades percibidas
2. El receptor otorga entonces tantos búferes como puede
3. El receptor, sabiendo su capacidad de manejo de búferes podría indicar al emisor "te he reservado X búferes"

Para no generar conflicto con los ACK, el receptor puede incorporar tanto las ack como las reservas de búfer en el mismo segmento.
El emisor lleva la cuenta de su *asignación de búferes* con el receptor; por lo que cada vez que el emisor envía un segmento este ultimo debe disminuir su asignación de buferes disponible. Cuando la asignación de búferes disponibles llega a 0, el emisor debe detenerse por completo

Una situación que puede pasar es que el receptor otorgue una cantidad de bufferes pero este mensaje se pierda terminando asi en un deadlock. ¿Como podemos evitar esto?. Bueno pues cada host puede enviar periódicamente un *segmento de control* con el ack y estado de búferes de cada conexión, de esta forma el estancamiento se romperá tarde o temprano
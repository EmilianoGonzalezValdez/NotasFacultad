En la situacion que tengamos latencia grande, proporción de errores o pérdida de paquetes importante y que los paquetes puedan demorar, va a ser necesario hacer que el código del receptor maneje eficientemente los problemas de la red, por más que esto signifiqie complicar el código del receptor. Veremos el protocolo de repetición selectiva que adopta este enfoque

Si ocurre que un paquete T se pierde a mitad de una serie, la capa de transporte receptora debe entregar paquetes a la capa de aplicación en secuencia. Ocurre lo mismo que con el protocolo de repetición-N. En este caso la solución es distinta, los paquetes en buen estado recibidos después de un paquete dañado E se almacenan en un búfer. Cuando el paquete E llega correctamente, el receptor entrega a la capa de aplicación, en secuencia, todos los paquetes posibles que ha almacenado en el búfer. 
Para ello el mecanismo mas común de retransmisiones es esperar a que el temporizador de E termine y el emisor lo mande de nuevo. Aunque, una mejor solución es usar un ack negativo (NAK) por el receptor, estimulando asi la retransmisión de paquetes antes que los temporizadores terminen y así se mejora el rendimiento.

El receptor confirma individualmente todos los paquetes recibidos correctamente. Hay búferes para paquetes según se necesiten para su entrega eventual en orden a la capa de aplicación. El emisor solo reenvía paquetes para los cuales el ACK no fue recibido o se recibió un NAK. Hay un temporizador del emisor para cada paquete no confirmado

La ventana del emisor contiene N números de secuencias consecutivos, además los limita a enviar paquetes no confirmados

**Tipos de paquetes que puede haber en la ventana del emisor:**
- Paquetes enviados y confirmados porque antes hay paquetes no confirmados
- Paquetes enviados y no confirmados
- Paquetes listos para enviarse en búfer

Es necesario almacenar en búfer paquetes porque puede perderse un pquete y llegar otros a continuación del mismo y en repetición selectiva estos se almacenan. Para representar el conjunto de paquetes que puede almacenar en búfer el receptor se usan intervalos de números de secuencia dentro del espacio de npumeros de secuencia. Un intervalo de esos recibe el nombre de *ventana corrediza*

**Tipos de paquetes que puede haber en la ventana del receptor:**
- Paquetes esperados y no recibidos
- Paquetes recibidos fuera de orden
- Paquetes aceptables en la ventana que no han llegado aun

Se mantiene en búfer un paquete aceptado por la ventana receptora hasta que todos los que le preceden hayan sido pasados a la capa de aplicación

**Algunos detalles de la repetición selectiva:**
- tamaño de ventana emisora comienza en 0 y crece hasta MAX_SEQ
- el receptor tiene un búfer para cada número de secuencia en su ventana
- cuando llega un paquete, su número de secuencia es revisado para ver si cae dentro de la ventana, de ser así, y no ha sido recibido aun, se acepta y almacena

El tamaño de la ventana receptora = (MAX_SEQ + 1)/2. Con tamaños mayores no funciona
En el encabezado de paquete hay número de secuencia de k bits
**¿Como transmitir datos entre dos maquinas y en ambas direcciones eficientemente?**
Para ello se "lleva a caballito (piggybacking)". Consiste en que cuando llega un segmento S con datos, el receptor se aguanta y espera hasta que la capa de aplicación le pasa el siguiente paquete P. La confirmación de recepción de S se anexa a P en un segmento de salida (usando el campo ack en el encabezado del segmento de salida).

Sabiendo esto, para extender repetición selectiva para tener flujo de datos entre 2 maquinas en las dos direcciones hay que usar el piggybacking, es decir, la capa de transporte para mandar un ack, debe esperar por un paquete al cual superponer un ack.
Esto nos trae otro problema, ¿Como evitar retrasar demasiado el envío de confirmaciones de recpción por no tener trafico de regreso? Bueno, se usa un temporizador auxiliar de modo que tras llegar un paquete de datos en secuencia, se arranca un temporizador auxiliar mediante start_ack_timer. Si no se ha presentado tráfico de regreso antes de que termine este temporizador, se envía un paquete de ack independiente. Esto siempre con el tiempo de temporizador auxiliar mucho menor a el tiempo de temporizador de retransmisiones, para asegurarse que el ack de un paquete correctamente recibido llegue antes que el emisor termine su temporización y retransmita el paquete

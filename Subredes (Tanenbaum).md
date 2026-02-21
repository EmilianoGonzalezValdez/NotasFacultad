*Uso de subredes:* permitir una red que sea dividida envarias partes para uso interno pero que todavia actúe como una red simple para el mundo externo. Cada subred puede ser una LAN que tiene un enrutador. Los enrutadores de una subred conectados a un *enrutador principal*. Fuera de la red, una subred no es visible

Una subred típica de un campus universitario podría tener un enrutador principal conectado a un ISP o a una red regiónal, y numerosas Ethernet dispersas en diferentes departamentos. Cada una de las Ethernet tiene su propio enrutador conectado al enrutador principal, posiblemente mediante una LAN de red dorsal.

Cuando un paquete entra en el enrutador principal,¿Cómo sabe a cual subred pasarlo?
Una solución seria tener una tabla en el enrutador principal que indique cuál enrutador usar para cada host. Para ellos e requeriria una tabla muy grande en el enrutador principal y mucho mantenimiento manual conforme se argegan, movieran o eliminaran hosts.

En otra solución, algunos bits se eliminan del N° de host para crear un número de subred. Por ejemplo, si la universidad tiene 35 departamentos, se usan 6 bits para el número de subred y 10 bits para el número de host, lo que permite hasta 64 Ethernets, cada una con a o mas 1022 hosts

Ahora, ¿Como expresamos las subredes?
Para ello el enrutador principal usa una *máscara de subred* que indique la división entre el número de red + número de subred y el host. Las máscaras de subred también se pueden escribir en notación decimal con puntos, o agregando a la dirección IP una diagonal seguida del número de bits usado para los números de red y subred.

Fuera de la red, la subred no es visible, por lo que la asignación de una subred nueva no requiere comunicación con el ICANN (Corporación de Internet para la Asignación de Nombres y Números) ni la modificación de bases de datos extremas.

¿Como serían las tablas de enrutamiento para el enrutador principal?
Se tienen entradas con forma de: (dirección IP inicio subred, máscara).
Cuando un paquete llega al enrutador principal, el enrutador hace un AND booleano de la dirección de destino con la máscara de subred para deshacerse del número de host y buscar la dirección resultante en sus tablas.

**OBSERVACIÓN:** El origen de una subred denota el tamaño máximo de hosts que puede albergar. Por ejemplo, supongamos que inicia en 130.50.8.0, que en binario es 10000010.00110010.00001000.000000000. Esta red puede crecer hasta 2^11 host = 2048, y dicha mascara es 255.255.248.0

Moraleja: la cantidad máxima de hosts se da por la cantidad de 0 a la derecha del ultimo 1 de la dirección de origen yendo de izquierda a derecha
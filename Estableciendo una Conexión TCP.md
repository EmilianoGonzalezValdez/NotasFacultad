El número de secuencia inicial de una conexión no es 0, se usa un *esquema basado en reloj* con un pulso de reloj cada 4 usec. Al caerse un host, no podra reiniciarse durante el tiempo máximo de paquete, para asegurar que no haya paquetes de conexiones previas vagando por internet.

El campo *SYN* en el encabezado TCP se usa para establecer conexiones.
La solicitud de conexión es con SYN = 1, y ACK = 0.
La respuesta de conexión si lleva una confirmación de recepción, por lo que tiene SYN = 1 y ACK = 1. Recordar además que hay un campo con número de secuencia confirmado.

En TCP las conexiones usan el *acuerdo de 3 vias*:
1. Para establecer una conexión, el servidor, espera pasivamente una conexión entrante ejecutando LISTEN y ACCEPT y especificando cierto origen o bien nadie en particular
2. En el lado del cliente ejecuta CONNECT, la cual envía un segmento TCP con el bit SYN encendido y el bit ACK apagado, y espera una respuesta
3. Al llegar el segmento al destino, la ETCP allí revisa si hay un proceso que haya ejecutado un LISTEN en el puerto indicado en el campo puerto de destino
4. Si no lo hay, envía una respuesta con el bit RST encendido para rechazar la conexión
5. Si algún proceso está escuchando en el puerto ese proceso recibe el segmento TCP entrante y puede entonces aceptar o rechazar la conexión; si la acepta se envía un segmento de ack
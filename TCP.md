*TCP (protocolo de control de transmisión)* tiene como meta el proporcionar un flujo de bytes confiable de extremo a extremo a través de una interred no confiable. TCP se adapta dinámicamente a las propiedades de la inter-red y se sobrepone a muchos tipos de fallas. Existe tambien la *Entidad de transporte TCP (ETCP)*, por lo que hay veces que diremos TCP para referirnos a la ETCP y a veces al protocolo TCP.

**Problemas que resuelve TCP:**
- Retransmisión de paquetes: uso de números de secuencia, confirmaciones de recepción y temporizadores
- Fijar la duración de temporizadores de retransmisiones(algoritmo complejo)
- Manejo de conexiones entre pares de procesos
- Direccionamiento
- Control de congestión
- Control de flujo

Una ETCP acepta *flujos de datos* a transmitir de procesos locales. Cada flujo de datos se *divide en fragmentos* llamados segmentos que no exceden los 64KB, y se envía cada segmento dentro de un datagrama IP.

El servicio TCP se obtiene al hacer que tanto el servidor como el cliente creen sockets
- Dirección de un socket = IP + Puerto
- Para obtener el servicio TCP se debe *establecer una conexión* explicitamente entre el socket en la maquina emisora y uno en la maquina receptora.

Un socket puede usarse para múltiples conexiones al mismo tiempo:
- dos o más conexiones pueden terminar en el mismo socket
- Las *conexiones se identifican* mediante los identificadores de sockets de los dos extremos (socket1,socket2)

Es importante saber que cada byte de un flujo de datos a enviar en una conexión TCP tiene su propio *número de secuencia* de 32 bits, lo cual impone un límite en el tamaño de un flujo de datos. Este número de secuencia es importante para confirmaciones de recepción y para otros asuntos según veremos.
La ETCP emisora y la receptora intercambian datos en forma de segmentos, donde cada segmento es el *encabezado TCP* ++ (0 o mas bytes) de datos.

Existen **limites que restringen el tamaño de un segmento**, especificamente cada segmento debe caber en la carga útil de 65.515 bytes del IP. Cada red tiene una *unidad máxima de transferencia(MTU)* y cada segmento debe caber en la MTU (en la practica la MTU es usualmente 1500 bytes).

Otro problema que surge en la capa de transporte al confiar en la capa de red es que, la capa de red (que incluye IP) no proporciona ninguna garantía de que los datagramas se entregarán de manera apropiada, tampoco garantiza que se entregarán.
La solución que aplica TCP es:
- Si un datagrama se recibe correctamente se confirma su recepción
- Si no se confirma la recepción de un datagrama luego de un intervalo de tiempo entonces se debe retransmitir
- Corresponde a TCP terminar los temporizadores y retransmitir los datagramas conforme sea necesario

Otro problema es que los datagramas que llegan podrían hacerlo en el orden incorrecto, lo cual para cuando se trabaja con redes de datagramas. Esto es un problema principalmente porque usualmente la capa de aplicación del receptor necesita procesar los mensajes en el orden en que fueron enviados.
Para solucionarlo TCP se encarga de reensamblar los mensajes en la secuencia apropiada.

Cuando un transmisor envía un segmento, también inicia un temporizador. Cuando llega el segmento a destino, la ETCP receptora devuelve un segmento que contiene un *número de confirmación de recepción* igual al siguiente número de secuencia que espera recibir. Si el temporizador expira antes de llegar el ack, el emisor envía de nuevo el segmento

También pueden llegar segmentos fuera de orden, por lo que habrá que esperar antes de entregar segmentos a la capa de aplicación y antes de enviar confirmaciones de recepción.
Tambien pueden retardarse segmentos en tránsito durante tanto tiempo que el temporizador del emisor expira y los segmentos se retransmiten

Además las retransmisiones podrían incluir rangos de bytes a los de la transmisión original. Esto puede suceder porque hay nuevos datos para enviar y se los puede mandar. Por ello se requiere una administración cuidadosa para llevar el control de os bytes que se han recibido correctamente en un momento determinado
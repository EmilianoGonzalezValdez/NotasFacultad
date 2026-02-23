**Proposito de la capa de transporte**
La *capa de transporte(CT)* provee comunicación lógica entre procesos de aplicación que se ejecutan en diferentes sistemas finales. Esto no lo puede hacer la capa de red. La CT se implementa solo en los sistemas finales.
Se busca una *comunicación Lógica*, como si los hosts ejecutando los procesos estuvieran directamente conectados
La capa de transporte busca mejorar la calidad de los servicios de la CR

La capa de transporte confía en los servicios de la Capa de Red.
Llamamos *Entidad de transporte(ET)* al software/hardware de la capa de transporte

**¿Por qué conviene estudiar la capa de transporte?**
Al desarrollar una aplicación de red, hay que pensar en qué requisitos ella tiene referentes a la capa de transporte
Ayuda a hacer aplicaciones más eficientes y de mejor calidad al conocer cómo funciona la capa de transporte.
Para usar la API de los sockets ahce falta entender cómo funcionan algunos protocolos de capa de transporte
Para mejorar protocolos de capa de transporte o diseñar nuevos protocolos
 

**Problemas que soluciona la capa de transporte**
- Uso de *temporizadores* y las  *retransmisiones de paquetes*
- El direccionamiento explícito de los destinos
- 	¿Cómo hacer para que un proceso adecuado atienda a las necesidades de una máquina cliente?
- 	El proceso podría no estar activo, el cliente podría no saber cuál proceso usar, etc.
- Uso de búferes para lograr comunicación confiable eficiente
- Control de flujo (evitar que los emisores saturen a los receptores)
- Evitar congestionar la red poniendo demasiados paquetes en ella.
- 	Cuando la CR pierde paquetes, la CT puede solucionarlo

*Segmento* es una unidad de datos del protocolo de transporte
*Confirmaciones de recepción* de paquetes enviados
Los tipos de paquetes que deben ser confirmados son:
- paquete de datos
- paquetes con información de control


Un problema que se presenta es que la capa de transporte deberia permitir la entrega de segmentos al host destino, y que la entrega de segmentos sea ordenada (respetando el orden del flujo de datos a enviar recibido de la capa de aplicación).

Una solución para la entrega ordenada de segmentos al host destino puede ser que:
- El emisor numera los segmentos enviados, usando *números de secuencia*, respetando el orden del flujo de datos recibido de la capa de acplicación.
- Para cada número de segmento enviado el emisor dispara un *temporizador de retransmisiones*.
- El receptor manda *confirmaciones de recepción (ACK)* para segmentos recibidos correctamente.
- Si expira el temporizador de un segmento sin recibir el ACK, el emisor retransmite el segmento correspondiente
- El receptor *re-ensambla en orden* los segmentos recibidos y los entrega a la capa de aplicación.
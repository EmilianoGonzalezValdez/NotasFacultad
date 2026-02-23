¿Cuál es la responsabilidad de un AP?
- Un AP es responsable de *enviar y recibir datos* desde y hacia hosts inalámbricos que están asociados con el AP
- Un AP va a ser responsable para *coordinar la transmisión* de varios hosts inalámbricos asociados
- El orden de transmisión se controla por la AP, luego *no ocurren colisiones*

**Requisitos para los canales en que operan las AP:**
- Cada AP opera en un canal en un rango de frecuencias apropieado
- Cada AP va a estar en un canal diferente que sus vecinos

**Relación que hay entre hosts y APs:**
- Cada nodo está asociado con un AP. O sea el host está dentro de la distancia de comunicación de la AP y el host usa la AP para enviar datos entre él y el resto del mundo

Para enterarse una AP cuales hosts desea enviar:
- La AP sondea los nodos, preguntandoles si tienen tramas para enviar


Componente fundamental: Conjunto de Servicio Básico (o Basic Service Set, BSS)

Un *servicio de distribución (SD)* conecta las AP entre sí.
- SD puede ser un conmutador, una red cableada, o una red inalámbrica
- El SD opera en la CED y no depende de protocolos de nivel más alto

*Conjunto de servicios básicos (BSS)*
- Consiste de un npumero de nodos ejecutando el mismo protocolo MAC y compitiendo por el acceso al mismo medio inalámbrico.
- Puede estar aislado o conectado a un SD a través de un AP

*Conjunto de servicios extendido (ESS):* esta compuesto por 2 o más BSS interconectados por el SD

*Servicio de integración*
- Para integrar la arquitectura IEEE 802.11 con una LAN cableada, se usa un *portal*
	- La lógica del portal es implementada en un puente o enrutador, que es parte de la LAN cableada y que es conectado al SD

En PCF:
- Cada host necesita asociarse con una AP antes de poder enviar o recibir datos de la capa de red.
- El SD necesita identificar los nodos de destino. Los nodos deben mantener una asociación con una AP dentro del BSS actual

**3 servicios relacionados de asociación:**
- *Asociación:* establece asociación inicial entre nodo y AP
- *Reasociación:* para transferir una asociación a otro AP (handoff)
- *Desasociación:* notificación por nodo o AP que una asociación existente terminó
El estandar 802.11 no especifica un algoritmo para elegir con cual de las AP disponibles reasociarse

¿Cómo hacen las AP para saber qué estaciones quieren enviar?
Para eso está el **sondeo:** En *PCF* la AP sondea las demás estaciones, preguntándoles si tienen tramas para enviar.
- El orden de transmisión se controla por completo por la AP y no ocurren colisiones
- 802.11 prescribe el *mecanismo para sondeo*, pero no la frecuencia del sondeo, el orden del sondeo, ni el hecho de que las estaciones necesiten obtener un servicio igual

**Funcionamiento del mecanismo de sondeo:**
- El AP toma control del medio y bloquea todo el tráfico mientras realiza sondeos y recibe respuestas
- El AP puede realizar sondeos en round-robin a todas las estaciones configuradas para sondeo.
- Cuando se hace un sondeo, el nodo sondeado puede responder
	- Si el AP recibe respuestas, emite otro sondeo
 - Si no se recibe respuesta durante el tiempo esperado para ella, el AP realiza un sondeo

**Para configurar las estaciones para sondeo:**
- El AP invita a los nuevos nodos a suscribirse al *servicio de sondeo*.
	- Una vez que un nodo se inscribe para el *servicio de sondeo* a cierta tasa, se le garantiza de manera efectiva cierta fracción de ancho de banda y se hace posible proporcionar garantías de calidad de servicio

El estandar 802.11 no especifica un algoritmo para elegir con cual de las AP disponibles asociarse.
Pueden pasar 2 cosas debido a esto:
1. Un nodo puede no estar asociado a ningun AP y necesita asociarse a alguna
2. Un nodo puede pasar a estar insatisfecho con su AP y quiere cambiar
	- ¿Cuál puede ser la causa de la insatisfacción?
 - La señal del AP actual se ha debilitado debido a que el nodo se alejó de ella
 - La red puede estar muy cargada (mucho trafico)
 - Podría ser que hay otra AP que tiene señal más fuerte con el nodo

¿Como hace un host para asociarse a la AP más conveniente?

*Método de escaneo activo* iniciado por el host:
1. El nodo manda una *trama de prueba*
2. Todos los AP que están en alcance responden con una *trama de respuesta a la prueba*
3. El nodo elige uno de los AP y envía a tal AP una *trama de pedido de asociación*
4. El AP responde con una *trama de respuesta de asociación*
	- El nuevo AP notifica al AP anterior del cambio


Aun cuando no se haya debilitado la señal de la AP con la que un host está conectada, puede convenir cambiar de AP. Ya que otra AP puede estar más desocupada por ejemplo

¿Cómo obtiene una estación información para decidir si le conviene re-asociarse y cómo es el proceso de re-asociación?

*Método de escaneo pasivo* iniciado por el AP:
1. La AP difunde una *trama guía* periódicamente para advertir de capacidades del AP. Esta trama contiene parámetros de sistema, como identificador del AP, la hora, cuánto falta para la próxima trama guía, etc.
2. Basado en la información anterior el nodo escoge un nuevo AP y envía una *trama de pedido de asociación* al nuevo AP
3. El AP responde con una *trama de respuesta de asociación*

Con 802.11 el tiempo se alterna entre:
- *Período sin contentios (PCF):*
	- Implementada en AP, quien coordina el acceso al medio
 - Nodos transmitén sólo si lo pide el AP
 - El AP tiene una lista de nodos "privilegiados"
 - Los nodos se registran para estar en la lista
- *Período de contention (DCF):*
	- Implementado en todos los nodos
 - Los nodos compiten por el medio

El AP inicia el período sin contención transmitiendo una *trama Beacon*
- Este Beacon contiene información sobre la capacidad de PCF del AP y la duración del período libre de contención
- Antes de transmitir el Beacon, el AP espera un intervalo de tiempo llamado PIFS (PCF Interframe Space)
	- PIFS es más corto que el DIFS (Distributed Interframe Space) utilizado en DCF, lo que le da prioridad al AP para acceder al medio e iniciar el período libre de contención

**Polling (sondeo)** por el AP:
- Durante el período sin contención el AP controla qué estación puede transmitir usando un esquema de sondeo
- El AP mantiene una lista de las estaciones que pueden ser sondeadas
- El AP envía una trama de "CF-Poll" (Contention-Free-Poll) a una estación especifica. Esta trama otorga permiso a la estación para transmitir

*Transmisión de la Estación Polleada:* Cuando una estación recibe una trama CF-Poll dirigida a ella:
- Si la estación tiene datos para enviar, puede transmitir sus datos inmediatamente después de un corto intervalo de tiempo llamado SIFS (Short Interframe Space). Opcionalmente, puede incluir un ACK si está respondiendo a una transmisión anterior del AP
- Si la estación no tiene datos para enviar, puede responder con una trama nula o simplemente no responder dentro del tiempo asignado

*Control del AP y Secuencia de Comunicación:*
- Después de que la estación polleada transmite (o si no tiene nada que transmitir), el AP puede realizar una de las siguiente acciones:
	- Si el AP tiene datos para enviar a la misma estación, puede incluir los datos en la trama CF-Poll
 - El AP puede enviar una trama CF-Poll a otra estación en su lista de polling
 - Si el período sin contención ha llegado a su fin o el AP no tiene más estaciones para sondear o datos para enviar, transmite una trama "CF-End" para indicar el final del período libre de contención
 - Después de esto, el emdio vuelve al modo contención (CP) utilizando DCF

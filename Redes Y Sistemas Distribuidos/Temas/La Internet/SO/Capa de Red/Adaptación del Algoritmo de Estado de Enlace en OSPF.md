Al ejecutarse OSPF los enrutadores dentro de un área ejecutan una adaptación del *protocolo de estado de enlace*.
Los vecinos de un enrutador en un área son:
- Enrutadores conectados por líneas punto a punto con el enrutador
- Si el enrutador está en LAN de enrutadores, los otros enrutadores en la LAN son también vecinos suyos

Cuando un enrutador se inicia, envía *mensajes hello* a todas las líneas punto a punto y  si está en una LAN de enrutadores, al grupo de todos los enrutadores de su LAN.
De las respuestas de cada enrutador aprende quiénes son sus vecinos


¿Cómo se fijan los pesos de los enlaces?
OSPF no fija una política de cómo los pesos de los enlaces son fijados. Este es el trabajo del administrador de la red.
OSPF trabaja intercambiando información entre enrutadores adyacentes.

Cada enrutador tiene una *base de datos de estado de enlace (BDEE):*
- La BDEE contiene todos los AEE que el enrutador ha recibido
- La BDEE debe ser creada y luego mantenerse
- Dentro de un área cada enrutador debe tener el mismo grafo (BDEE) para construir la tabla de re-envío

**Consecuencias de tener la BDEE:**
- En la BDEE se guarda la información que un enrutador puede intercambiar con sus vecinos
- La información de una BDEE puede ser actualizada luego que un enrutador reciba AEE de sus vecinos

**Tipos de paquetes usados para intercambio de información entre enrutadores adyacentes:**
- *Paquete de descripción de base de datos (PDBD):* llevan resumen de la descripción de todos los AEE de la BDEE del enrutador emisor, o sea, números de secuencia de los AEE del enrutador emisor. El receptor puede determinar cuáles AEE de ese grupo necesita, comparando número de secuencia de un AEE con número de secuencia de AEE que ya tiene
- *Paquete de pedido de estado de enlace (PPEE):* se usan para solicitar AEEs
- *Paquete de actualización de estado de enlace (PAEE):* para mandar AEE asociado al enrutador emisor. Estos AEE tienen número de secuencia, usando dicho npumero de secuencia del receptor puede ver si un AEE es más nuevo o más viejo que el que ya tiene
- *Paquete de confirmación de estado de enlace (PCEE):* para confirmar los PAEE

Para actualizar sus BDEE dos enrutadores vecinos deben *sincronizar sus BDEE:*
- Un vecino es el *maestro* y el otro es el *esclavo*
- El maestro controla el intercambio de PDBD
- Se intercambian PDBD, PPEE, PAEE, PCEE para asegurar que ambos vecinos tienen igual información en sus BDEE

Usando inundación cada enrutador informa a todos los otros enrutadores de su área de sus enlaces a todos los otros enrutadores y redes, y el costo de esos enlaces.
Esto permite a un enrutador construir el grafo de su área.

La red dorsal hace este trabajo también. Este intercambio se hace periodicamente o cuando una línea se cae, o regresa, o su costo cambia

El problema es que es ineficiente tener cada enrutador en una LAN que intercambie mensajes con todos los otros enrutadores de la LAN.
Para evitar hacer todo ese trabajo, un enrutador de la LAN se elige como el *enrutador designado*, siendo este quien intercambia mensajes con todos los enrutadores de la LAN mediante sincronización

**Consecuencias para enrutadores internos a un área de organizar jerarquicamente un SA:**
- Los enrutadores internos a un área no van a conocer detalles acerca de la topología de otras áreas
- Los AEE de enrutadores que no son EBA no dejan el área en el que se originan

Un EBA necesita los grafos para todas las áreas a las cuales está conectado

Para un enrutador R dentro de un área se puede ejecutar el algoritmo de Dijkstra. Para esto se debe usar la BDEE de R. Dijkstra calcula el camino más corto desde R a cualquier otro enrutador de su área y red en el SA entero.
Sin embargo, queremos que si hay varios caminos más cortos a un destino, que se pueda balancear la carga entre ellos.
¿Cómo es un algoritmo adecuado para ello?
OSPF recuerda el conjunto de caminos más cortos entre dos nodos y durante el envío de paquetes el tráfico se divide entre ellos.
Para esto se usa una adaptación especial del algoritmo de Dijkstra que usa una cola de prioridades. Para ello es necesario modificar la tabla de enrutamiento ya que necesitamos tener para und estino varias líneas de salida. A esto se le llama *ECMP (multicamino de igual costo)*

**Un EBA ejecuta Dijkstra adaptado** para el grafo de cada área separadamente.
En conclusión, OSPF es valioso porque ayuda a balancear la carga.

**Para enviar un paquete de un área a una red en otra área:**
1. El paquete viaja de su red local al área dorsal
2. Luego cruza el área dorsal
3. Luego viaja del área dorsal a la der de destino
"Recordar que para las tablas de re-envío se usa CIDR"
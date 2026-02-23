Actualmente con mecanismos simples como confirmaciones de recepción, temporizadores y retransmisiones quedan lagunas en como se hace la entrega de datos confiables. Y quedan preguntas como: ¿Que se confirma exactamente en un ACK?, ¿Cuantos paquetes se envian antes de recibir un ACK?, ¿Que hace el receptor cuando se pierde o daña un paquete?.

Para responder estas preguntas hay que definir un *protocolo de datos confiable*. Hay varios de estos porque hace falta *optimizar el rendimiento según las características de la red*, como la latencia, proporcion de errores, y capacidad de la red.

La capa de transporte debe soportar al menos un protocolo para *entrega de datos confiable*. Veremos varios de estos protocolos de mas simple a mas complejo. Estos protocolos asumen que el canal puede:
- Corromper paquetes
- Perder paquetes
- La transferencia de datos es en un sentido, o sea hay un emisor y un receptor

El protocolo mas simple es el de *parada y espera*, aunque luego vermos mas complejos como los de *tubería*. Estos protocolos se pueden usar tanto en capa de transporte como en capa de enlace de datos, pues entrega confiable de datos es un problema de esas capas.

Vimos que la Capa de Transporte se ocupa del uso de temporizadores y retransmisiones de paquetes, ya que los paquetes perdidos deben retransmitirse.
Sabemos que un paquete no se perdio porque fue confirmado con un *paquete de confirmación de recepción(ACK)*. Por ello podemos asumir que un paquete se perdio si pasa un cierto tiempo y no fue confirmado, entonces se perdió y hay que retransmitirlo. Para medir este tiempo se usan temporizadores.

Se puede prestar la situación donde el mensaje que se pierde es un ACK, y el paquete fuera retransmitido innecesariamente, por lo que llegaria mas de una vez el mismo paquete para terminar siendo transmitido a la capa de aplicación mas de una vez. Para solucionar esto se le asigna *números de secuencia* a los paquetes que salen con la idea de que dado un número de secuencia de un segmento que acaba de llegar, el receptor puede usar ese número de secuencia para decidir si el segmento es un duplicado y en ese caso descartarlo

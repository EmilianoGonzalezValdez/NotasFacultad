Si tenemos una latencia grande, la proporcion de errores o pérdida de paquetes es muy baja y rara vez se demoran paquetes, entonces se puede hacer el código del receptor mas sensillo y eficiente, usando la solución más fácil a estos problemas. Si estos problemas ocurren con cierta frecuencia, será necesario complicar el código del receptor para que se manejen eficientemente esos problemas.

Si un paquete T a la mitad de una serie larga se daña o pierde, como la CT receptora debe entregar los paquetes a la capa de aplicación en secuencia, no puede entregarle los paquetes que llegaron bien despues de T.
En estos casos, con *Retroseso-N* el receptor descarta todos los paquetes subsecuentes al paquete perdido, sin enviar ack para los paquetes descartados

Entonces, el receptor envía *ack acumulativo*, el mayor número de secuencia tal que los segmentos anteriores se recibieron bien.
El emisor tiene un solo temporizador para el paquete mas víejo no confirmado. Al expirar el temporizador retransmite todos los segmentos no confirmados. Si llega ACK nuevo y hay segmentos enviados no confirmados, el temporizador es reiniciado. Si llega ACK nuevo y no hay segmentos sin confirmar, el temporizador es detenido.
Asumimos en el emisor que voy a tener varios bufferes, todos los del mismo tamaño. Como el RTT es fijo, estos representarián la cantidad de segmentos a enviar por ráfaga para aprovechar el canal al maximo. Para referirnos a los números de secuencia de esos búferes usamos el concepto de *ventana del emisor*
Dicha "ventana" permite hasta N paquetes consecutivos sin confirmar. Llamamos *ventana emisora* a las tramas enviadas sin ack positivo o tramas listas para ser enviadas

Si el espacio de secuencia es de MAX_SEQ + 1 números de secuencia no se puede hacer la ventana emisora de tamaño MAX_SEG + 1, como mucho puede ser de MAX_SEQ


Para evitar que haya mas MAX_SEQ paquetes sin ack pendientes la solución es prohíbir a la capa de red que moleste con más trabajo, para ello se usa un "enable_network_layer" y "disable-network_layer"

El principal problema de retroceso N es el uso ineficiente del canal frente a segmentos perdidos o demorados
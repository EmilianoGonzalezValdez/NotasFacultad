¿Como puede hacer un enrutador para darse cuenta si tiene algún puerto de salida congestionado?
Para ello cada enrutador monitorea la demora de la cola de línea de salida.
Se asocia a cada línea d = *demora reciente de cola de esta línea*
Tomar periodicamente una muestra de la *longitud de cola instantanea de la línea*
Actualizar d periodicamente usando: $d_{nvo} = a \space d_{ant} + (1-a) * s$ donde $a$ determina la rapidez con que el enrutador olvida la historia reciente

Siempre que $d$ rebasa un umbral, la línea de salida entra en un *estado de advertencia*.
Cada paquete nuevo que llega se revisa para ver si su línea de salida está en estado de advertencia. Si es así, se realiza alguna acción
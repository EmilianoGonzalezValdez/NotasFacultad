No se requiere:
- que los emisores envíen datos tan pronto como llegan a la aplicación
- que los receptores envíen confirmaciones de recepción tan pronto como sea posible
- que los receptores entreguen datos a la aplicación apenas los reciben

Con TCP no podemos usar el protocolo de control de flujo anteriormente visto, puesto que en TCP los números de secuencia no significan número de paquete. Anted cada búfer ocupado tenía un número de paquete. Ahora los números de secuencia son posiciones en el flujo de datos a enviar. El receptor a lo más ´puede saber qué rangos de números de secuencia de bytes recibidos tiene en búfer


Para acondicionar el protocolo de control de flujo anterior se le pueden hacer algunas mejoras:
- Los encabezados de los segmentos recibidos ocupan espacio y no hace falta almacenarlos en el búfer. En su lugar se pueden almacenar datos recibidos del flujo de datos
- No es necesario que el emisor solicite espacio del búfer al receptor. El receptor sabe de cuanto espacio dispone y cuanto espacio puede otorgar


Como no se almacenan encabezados de segmentos, no hace falta gaurdar segmentos en búferes. En su lugar se necesita guardar datos y no hace falta usar varios búferes para esto. TCP maneja un *búfer de recepción circular* en el receptor para la conexión

Como TCP usa este búfer único no le puede decir al emisor "te he reservado x búferes". Entonces para anunciar al emisor la reserva de espacio en búfer:
- El receptor puede indicar al emisor la cantidad de bytes consecutivos que se pueden enviar, comenzando por el byte cuya recepción se ha confirmado
- A esto se le llama en TCP *tamaño de ventana*
- En el encabezado TCP un *campo de tamaño de ventana* se usa para indicar esta información.

El TCP del emisor también usa un búfer circular.
**La cantidad de bytes que el emisor puede enviar al receptor depende** del tamaño del búfer del emisor y del tamaño de ventana. La cantidad de bytes a enviar no debe superar el mínimo de ambos valores

La formula para calcular el tamaño de ventana del receptor es: 
- Tamaño de ventana = RcvBuffer - [LastByteRcvd - LastByteRead]

**El receptor:**
- Cuando la conexión TCP recibe bytes en el orden correcto y en secuencia, coloca los datos en el buffer de recepción
- El receptor puede confirmar la llegada de datos nuevos y anunciar el nuevo tamaño de ventana al emisor
- Si el búfer de recepción está lleno, avisar tamaño de ventana de cero
- Una vez que el receptor entrega a la capa de aplicación X datos de búfer de recepción lleno, puede avisar al emisor de un tamaño de ventana de X

**El emisor:**
- Si el tamaño de ventana anunciado es cero el emisor no podra enviar datos
- El emisor envía segmentos cumpliendo la siguiente propiedad: LastByteSent - LastByteAcked $\le$ tamaño de ventana


Con este nuevo protocolo ¿Como manejamos las perdidas de segmentos en TCP?

Para esto hay varias soluciones. En la primera el receptor solicita segmentos especificos mediante  un segmento especial llamado NAK.
Tras recibir segmentos faltantes, el receptor puede enviar una confirmación de recepción de todos los datos que tiene un búfer. Cuando el receptor nota una brecha entre el número de secuencia esperado y el número de secuencia del paquete recibido, el receptor envía un NAK en un campo de opciones.


En la otra solución (ack selectivos) el receptor le dice al emisor que piezas recibio.
El emisor puede así reenviar los datos no confirmados que ya envío. Se usan dos campos de opciones:
- *Sack permited option:* se envía en segmento SYN para indicar que se usarán acks selectivos
- *Sack option:* con lista de rangos de números de secuencia recibidos

Cuando la ventana es de 0, el emisor no puede enviar segmentos, salvo en dos situaciones:
1. pueden enviarse *datos urgentes*
2. el emisor puede enviar un segmento de 1B para hacer que el receptor re-anuncie el siguiente byte esperado y el tamaño de la ventana. TCP proporciona esta opción para evitar un bloqueo irreversible si llega a perderse un anuncio de ventana


En las líneas con alto ancho de banda, alto retardo o ambas cosas, la ventana de 64KB con frecuencia es un problema. El problema viene cuando si bien un tamaño de ventana más grande permitira al emisor continuar enviando datos, pero como el campo de tamaño de ventana es de 16 bits, es imposible expresar tal tamaño.

La solución a esto es permitir al emisor y al receptor negociar un factor de escala de ventana.
Ambos lados pueden desplazar el tamaño del campo de ventana hasta 14 bits a la izquierda, permitiendo por lo tanto ventanas de hasta 2^30 bytes. La myoria de las implementaciones actuales de TCP manejan esta opción

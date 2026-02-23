En una red de computadoras la red se usa para la comunicación entre estas. Para ello se pueden usar nodos intermediarios como conmutadores, enrutadores y puertas de enlace, un claro ejemplo es la *internet* 

Primero veremos cómo sería una jerarquía de protocolos para una red de computadoras.
- *Procesos de aplicación* (capa 5 o **capa de aplicación**): Produce un mensaje y lo pasa a la capa 4 para su transmisión 
- La capa 4 (**capa de transporte**): Pone un encabezado en el mensaje para identificarlo y pasa el resultado a la capa 3. Este encabezado contiene *números de secuencia* para que la capa 4 de la máquina destino entregue los mensajes en el orden correcto 
- La capa 3 (**capa de red**): Debido a que hay limitaciones en el tamaño de los mensajes de esta capa, divide en *paquetes* los mensajes entrantes colocándole un encabezado a cada paquete. Además, si la maquina es un enrutador, decide cuál de las lineas de salida existentes usar. Luego pasa los paquetes a la capa 2
- La capa 2 (**capa de enlace de datos**):Agrega un encabeza y un terminador a cada pieza, luego pasa las unidades resultantes a la capa 1 para su transmisión
- Luego en la máquina receptora el mensaje pasa de abajo hacia arriba de capa en capa, perdiendo los encabezados conforme avanza 

En las redes de computadoras hay varios problemas a resolver:
- **Como identificar las máquinas de una red?:**
	- *Solución:* Se usan direcciones para las máquinas
- **Control de flujo:** un emisor rápido satura de datos al receptor hasta que este ya no puede almacenar más datos que le llegan y comienza a perder datos 
	- *Solución:* Uso de retroalimentación al emisor, es decir, indicarle cuándo y cuánto puede enviar
- **Los mensajes que llegan no pueden ser aceptados por un protocolo de capa por ser demasiado grandes:** el mensaje grande llega de una red diferente que tiene un tamaño máximo de mensaje mayor al de la red actual, o hay capas consecutivas que aceptan distintos tamaños de mensajes 
	- *Solución:* fragmentar los mensajes, transmitir fragmentos y reensamblar los mensajes. Hay 2 tipos de soluciones, la *fragmentación transparente* y la *fragmentación no transparente*. En la primera los paquetes se van fragmentando y reensamblando luego de cada capa, mientras que en la segunda los paquetes no se vuelven a reensamblar hasta que no lleguen a su destino 
- **Congestión:** a veces en la red hay que enviar demasiados mensajes por la misma línea de salida de un enrutador y esta se pone más lenta o no puede mandarlos a todos(la red no puede manejar la carga de paquetes que recibe)
	- *Solución:* las computadoras emisoras se enteran de la congestión y reducen el tráfico de salida 
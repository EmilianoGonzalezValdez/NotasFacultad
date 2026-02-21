En el esquema anterior cuando se satura una línea de salida de un enrutador, se pierden paquetes indiscriminadamente. Esto claramente es un problema a solucionar ya que no todos los paquetes tienen la misma importancia.

Una solución seria descartar los paquetes inteligentemente antes de que se ocupe todo el espacio del búfer cuando hay estado de advertencia en una línea de salida

Algunos criterios para escoger qué paquetes descartar:
- **Según el tipo de aplicación que se está usando:**
- 	Estrategia Vino: descartar primero los paquetes más nuevos
- 	Estrategia Leche: descartar primero los paquetes mas viejos
- **Según la importancia de los paquetes:**
- 	Marcar los paquetes con clases de prioridades
- 	Los enrutadores primero se desprenden de paquetes de la clase más baja, luego los de la siguiente clase, etc.

Se suele usar desprendimiento de carga junto con reducción de tráfico. La respuesta a paquetes perdidos por desprendimiento de carga es que el origen disminuya su tasa de transferencia.
Si expira el temporizador de retransmisiones, el emisor lo toma como pérdida de paquete. Vemos ahora una implementación de esta solución

**Implementación del Algoritmo de detección temprana aleatoria (RED)** para detectar cuándo comenzar a descartar paquetes, los enrutadores mantienen un *promedio móvil de sus longitudes de cola*. Cuando este promedio de una cola C sobrepasa el umbral, una pequeña fracción de los paquetes son descartados al azar. Con cada uno de esos paquetes:
1. El enrutador *elige un paquete al azar* de C
2. Se descarta el paquete seleccionado
3. El origen notará falta de ACK y la capa de transporte disminuirá la velocidad de transmisión.

El elegir paquetes al azar hace más probable que los host emisores más rápidos pierdan un paquete, lo noten, y reduzcan su tasa de transferencia.

El método RED se usa en internet cuando los hosts no pueden recibir señales explicitas de congestión. Tanenbaum dice que la mayoría de los host de internet no reciben mensajes explicitos de congestión de los enrutadores

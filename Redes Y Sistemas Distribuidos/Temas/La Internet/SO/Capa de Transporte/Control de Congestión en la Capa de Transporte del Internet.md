Si un emisor manda a un receptor más información que la capacidad de carga de la subred, esta ultima se congestionará, pues será incapaz de entregar los segmentos a la velocidad con que llegan

Para solucionar esto necesitaremos un mecanismo de control de congestión basado en la capacidad de carga de la subred, el cual debe aplicarse al emisor.
Entonces para controlar la congestión en TCP algunos hosts dismunuiran la tasa de datos.

Para llevar la cuenta de cúantos datos un host puede enviar por la red TCP maneja una *ventana para la congestión (VC)* cuyo tamaño es el número de bytes que el emisor puede tener en la red en un momento dado. En TCP el host tiene una forma de detectar congestión, y al hacerlo el host ajusta el tamaño de la VC


**La expiración de un temporizador causada por un paquete perdido se puede deber a:**
1. ruido en la linea de transmisión
2. el descarte de paquetes en el enrutador congestionado

Hoy la p+erdida de paquetes por errores de transmisión es rara debido a que las troncales de larga distancia son de fibra óptica. Luego, la mayoría de las expiraciones de tiempo en internet se deben a la congestión
En TCP todos los algoritmos de congestión suponen que las expiraciones de tiempo son causados por congestión


¿Como calcular un tamaño para ña ventana de congestión?
Una idea seria probar con un mínimo de datos e ir duplicando gradualmente hasta que no se pueda más. Un algoritmo basado en esta idea se le llama *"arranque lento"*

**Algoritmo de arranque lento (Jacobson 1988):**
- El emisor asigna a la VC el segmento de tamaño maximo (STM) usado por la conexión: entonces envía 1 STM. Emisor y receptor se ponen de acuerdo en el tamaño del STM.
- Si se recibe el ack de este segmento antes que expire el temporizador, el emisor agrega el equivalente en bytes de un segmento a la VC para hacerla de 2 STM y envía dos segmentos
- Cuando la VC es de n segmentos, si de todos los n se reciben acks a tiempo, se aumenta la VC en la cuenta de bytes correspondiente a n segmentos
- La VC sigue creciendo exponencialmente hasta expiración del temporizador o hasta alcanzar el tamaño de la ventana receptora
- Si ocurre un timeout se recorta la VC a tamaño VC/2, o sea no se enviarán rafagas de segmentos mayores a VC/2


Este algoritmo no es perfecto y tiene varios problemas:
- *Critica 1:* Recortar la ventana de congestión a la mitad porque hubo una expiración de temporizador y quedarse ahí, puede ser demasiado, porque puede ser que la red tenga una capacidad mayor a esa mitad y así se desaprovecharia esa capacidad de la subred
- *Critica 2:* con la retransmisión disparada por expiración de temporizador el tiempo de espera puede ser relativamente grande. Cuando se pierde un paquete el emisor se demora en reenviar el paquete perdido.


Para que el emisor reconozca rapidamente que uno de sus paquetes se perdió vamos a asumir que cada paquete que llega al receptor dispara un paquete ack. De esta forma si se pierde un paquete pero los siguientes llegan bien, el emisor recibira acks duplicados.
Igualmente esto podria significar 1 de 2 cosas:
- Como los segmentos pueden tomar distintos caminos, pueden llegar fuera de orden y esto va a disparar acks duplicados incluso cuando no se ha perdido ningún segmento
- Si se pierde un segmento, habrá probablemente varios acks duplicados.

Para solucionar esto TCP asume que 3 acks duplicados implican que el paquete se perdio. Luego ese paquete retransmite inmediatamente y antes de que expire el temporizador.
Esta heuristica se llama *retransmisión rápida*


Otra solución es el **Algoritmo de control de congestión de internet (TCP Tahoe):**
- Usa un *umbral* además de las ventanas de recepción y congestión
- Al ocurrir una expiración del temporizador o detectarse 3 acks duplicados, se fija el umbral en la mitad de la ventana de congestión actual, y la ventana de congestión se restablece a un segmento máximo
- Luego se usa el arranque lento para determinar lo que puede manejar la red, excepto que el crecimiento exponencial termina al alcanzar el umbral
- A partir del punto en el que se alcanza el umbral las transmisiones exitosas aumentan linealmente la ventana de congestión (en un segmento máximo por ráfaga)
- Recomenzar con una ventana de congestión de un paquete toma un RTT (para todos los datos previamente transmitidos que dejen la red y para ser confirmados, incluyendo el paquete retransmitido)
- Si no ocurren más expiraciones de temporizador/3 acks duplicados, la ventana de congestión continuará creciendo hasta el tamaño de la ventana del receptor. En ese punto dejará de crecer y permanecera constante mientras no ocurran más expiraciones de temporizador y la ventana del receptor no cambie de tamaño

Aunque esto mejore un poco la congestión, aun se puede criticar que comenzar con arranque lento cada vez que se pierde un paquete puede ser demasiado. Ya que por ahora el algoritmo TCP Tahoe se basa en:
- *invariante:* tamaño ventana de congestión $\le$ tamaño ventana receptor
1. Se usa arranque lento hasta alcanzar el umbral
2. Luego vienen incrementos aditivos hasta alcanzar timeout o 3 ack duplicados
3. Luego el umbral se fija a la mitad del tamaño de la ventana de congestión
4. Goto 1

Para solucionar el arranque lento del principio existe el *Algoritmo de TCP Reno (1990)*
Cuya idea es evitar el arranque lento (exceptuando cuando la conexión es comenzada) cuando expira el temporizador de re-envios.
Su funcionamiento es:
1. Luego de iniciada la conexión se comienza con arranque lento
2. A continuación la ventana de congestión crece linealmente hasta que se detecta una pérdida de paquete. Se cuentan acks duplicados y se considera perdida de paquete el recibir 3 acks duplicados
3. El paquete perdido es retransmitido (usando retransmisión rápida)
4. *Recuperación rapida:* Se manda un paquete por cada ack duplicado recibido. Un RTT luego de la retransmisión rápida el paquete perdido es confirmado. La recuperación rápida termina con esa confirmación de recepción
5. Luego de recibir el nuevo ack: la ventana de congestión de una conexión se achica a la mitad de lo que era cuando se encontraron 3 duplicados (decrecimiento multiplicativo). El conteo de ack duplicados se pone en 0
6. Luego la ventana de congestión va incrementando de a un segmento por cada RTT (crecimiento aditivo)
7. Este comportamiento continua indefinidamente

Luego se hicieron ajustes menores a TCP Reno que no veremos.

En resumen **TCP Reno:**
- Invariante: tamaño v¿de la ventana de congestión $\le$ tamaño de la ventana de receptor
1. Luego de iniciada la conexión viene arranque lento hasta alcanzar umbral
2. Luego vienen incrementos aditivos de hasta 3 ack duplicados
3. Luego viene recuperación rapida
4. Luego se reduce la ventana de congestión a la mitad
5. GOTO 2


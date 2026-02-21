Suponemos que la latencia es lo suficientemente baja como para mandar solo un paquete anted de que llegue el ACK. En dicha situación un protocolo óptimo para manejarla se llama protocolo de *parada y espera*

Tambien supondremos que el canal de comunicaciones subyacente puede perder paquetes. Los paquetes tienen números de secuencias, se trabaja con ACKs y se usan retransmisiones de paquetes.

Con estas suposiciones el **comportamiento del emisor sera:**
1. El emisor envía paquete P y *para* de enviar
2. El emisor *espera* una cantidad "razonable" de tiempo para el ACK
3. Si llega el ACK a tiempo, se envía siguiente paquete. GO TO 2
4. Si no, se retransmite paquete P. GO TO 2
Si hay paquete o ACK demorado pero no perdido la retransmisión va a ser un duplicado con igual número de secuencia, luego se descartara en el receptor


Para evaluar un protocolo para comunicación confiable podemos simplificar un poco las cosas y además hacer un análisis de mejor caso. Para ello vamos a asumir que hay un canal de comunicación que une el emisor con el receptor y que la transmisión entre el emisor y el receptor es sin errores(no se ppierden paquetes, no se demoran paquetes, no se alteran paquetes en curso).

Entonces, vamos a denominar como L la longitud de los segmentos, T a la tasa de transmisión del canal, RTT es el tiempo entre la salida del ultimo bit del mensaje y la llegada del primer bit del ack(pudiendose calcular a partir de "D" o *demora de propagación del emisor al receptor*) y $U_{sender}$ sera la utilización del canal

De esta forma nos queda que:
- *Tiempo de transmisión del segmento:* $L/T$
- RTT = 2 * D
- $U_{sender} = {L/R}/{RTT + L/R}$
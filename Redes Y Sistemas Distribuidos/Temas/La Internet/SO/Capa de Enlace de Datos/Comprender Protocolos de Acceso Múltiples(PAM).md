En **ALOHA PURO** el emisor:
- Transmite cuando tiene datos para enviar
- Escucha el canal por un tiempo igual a la demora de propagación de ida y vuelta máxima en la red + un incremento fijo de tiempo
- Si se escucha un ack en ese tiempo, todo anduvo bien
- Sino se espera un tiempo aleatorio y la trama se manda de nuevo
- Si se falla en recibir un ack luego de varias retransmisiones se tira la toalla

El receptor:
- Al recibir una trama chequea su validez y si lo es, inmediatamente manda un ack
- Si la trama es inválida el receptor la ignora, la trama puede sern invalida por ruido o por colisión

**Evaluación de ALOHA puro:**
- El método ALOHA puro bajo carga baja es eficiente y tiene una demora baja
- En ALOHA puro una estación no escucha el canal antes de transmitir, esto generará probablemente muchas colisiones
- El número de colisiones crece rápidamente a medida que aumenta la carga

**Protocolo CSMA persistente-1 para el emisor:**
- Si una estación tiene datos por enviar, primero escucha el canal para saber si otra está transmitiendo en ese momento.
- Si el canal está ocupado, entonces la estación espera hasta que se desocupe
- Cuando la estación detecta un canal inactivo, transmite una trama
- Si ocurre una colisión, la estación espera una cantidad aleatoria de tiempo y comienza de nuevo
- La estación espera un tiempo razonable por un ack. Teniendo en cuenta el tiempo de propagación de ida y vuelta máximo en la red y el hecho que la estación receptora también debe competir por el canal para responder
- Si no recibe ack en ese tiempo, la estación espera una cantidad aleatoria del tiempo y comienza de nuevo

**Protocolo CSMA persistente-1 para el receptor:**
- Al recibir una trama chequea su validez y si lo es, manda un ack (para eso hay que competir por el canal)
- Si la trama es inválida el receptor la ignora. La trama puede ser inválida por ruido o por colisión

El **Retardo de propagación** tiene un efecto importante en el desempeño de CSMA persistente 1.
En el caso de que justo después de que unae stación comienza a transmitir, otra estación está lista para enviar; si la señal de la primera estación no ha llegado aún a la segunda, esta última detectará un canal inactivo y comenzará a enviar también, eso producira una colisión.
Cuanto mayor sea el tiempo de propagación, más importante será este efecto
Aun si el retardo de propagación es cero, habrá colisiones. Si dos estaciones quieren enviar y detectan que una tercera está transmitiendo, cuando está termine de transmitir las otras dos detectarán el canal inactivo y enviarán sus tramas, provocando así, una colisión

Por ello estudiaremos el PAM **CSMA/CD (Acceso múltiple con Detección de Portadora y Detección de Colisiones)**, la cual es la base de la LAN Ethernet

En CSMA/CD el emisor:
1. Antes de transmitir una trama detecta la portadora
2. Si el canal está libre transmite
3. Sino espera hasta que el canal se desocupe para transmitir
4. Si el emisor detecta una colisión, aborta la transmisión, espera un tiempo aleatorio y una vez que pasó ese tiempo, goto 1

En CSMA/CD el receptor
1. Recibe una trama buena si no hubo colisión y el medio no cometió errores
2. En caso contrario (hubo colisión o el medio cometió errores) recibirá una trama dañada la cual será descartada
3. Al mandar una confirmación de recepción hace los pasos del emisor

El uso del canal con CSMA/CD tiene períodos alternantes de contención y transmisión, ocurriendo períodos de inactividad cuando todas las estaciones no necesitan enviar tramas. Las colisiones en CSMA/CD ocurren durante las ranuras de contención

Se dice que una estación ha *tomado el canal* cuando todas las demás estaciones sabían que estaba transmitiendo y no interfirieron.
Ahora, ¿Si dos estaciones comienzan a transmitir en momento t = 0, en cuánto tiempo se darán cuenta de que ha habido una colisión?. El tiempo mínimo en detectar la colisión es el tiempo que tarda la señal para propagarse de una estación a otra.

¿Cuál es el peor caso de demora de una estación en enterarse que ha habido una colisión?
Si t es el tiempo que tarda una señal en propagarse entre las dos estaciones más lejanas A y B, **¿Cómo ocurre una colisión en CSMA/CD y cuándo se enteran las estaciones de ella:?**
1. A comienza a transmitir en t = 0
2. En t-e un instante antes de que la señal llegue a B, B comienza a transmitir.
3. B detecta la colisión casi de inmediato y se detiene. (En ethernet se genera una ráfaga de ruido de 48 bits)
4. La ráfaga de ruido causada por la colisión no regresa a A hasta pasados 2*t-e

En conclusión, en el peor caso una estación no puede estar segura de que ha tomado el canal hasta que ha transmitido durante 2*t sin detectar una colisión

¿Las tramas pueden ser tan chicas como uno quiera?

Si una estación E intenta transmitir una trama demasiado corta y ocurre una colisión. la transmisión de E se completa antes de que la ráfaga de ruido llegue de regreso, en el momento 2t. El emisor entonces supondrá incorrectamente que la trama se envió con éxito

¿Cómo evitar que la situación anterior ocurra?
Para ello, las tramas deberán tardar más que 2t para enviarse, de manera que la transmisión aun esté llevándose a cabo la ráfaga de ruido regrese al emisor.
Por lo tanto, las tramas tienen un requisito de tamaño mínimo

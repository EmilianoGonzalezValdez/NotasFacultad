A medida que se agregan más y más estaciones a Ethernet, aumenta el tráfico. En algun momento la LAN se saturará.
¿Comó evitar este fenómeno dentro de Ethernet?
Una idea seria tener varios dominios de colisiones y aumentar significativamente la velocidad para mandar de una máquina de un dominio de colisiones a una máquina en otro dominio de colisiones. Hacer todo esto de modo que la estación no se entere

De esta forma se llega a la solución usando una *Ethernet Conmutada* donde:
- Un *conmutador (switch)* contiene una matriz de conmutación de alta velocidad y de 4 a 32 *tarjetas de línea*
- Cada tarjeta de línea contiene de 1 a 8 *conectores*
- Hay matrices de conmutación que funcionan a más de 1 Gbps

Los conmutadores se encargan del almacenamiento y reenvío de tramas de Ethernet.
Los hosts no son conscientes de la presencia de conmutadores.
Los conmutadores no necesitan ser administrados, estos aprenden por si solos sin necesidad de configuración

Si dos máquinas conectadas a la misma tarjeta de conexión transmiten tramas al mismo tiempo:
- Si todos los puertos de la tarjeta forman una LAN local dentro de la tarjeta, las colisiones en esta LAN en tarjeta se detectan y manejan igual que en una red CSMA/CD. Las tarjetas pueden estar transmitiendo en paralelo
- Si cada puerto de entrada se almacena en un *búfer*, todos los puertos de entrada reciben y transmiten tramas al mismo tiempo, para una operación en paralelo dúplex. Cada puerto es un dominio de colisión independiente.

Cada conmutador tiene una *tabla de conmutador:*
- <dirección MAC del host, interfaz para alcanzar el host, estampilla de tiempo>

Un conmutador *aprende* cuáles hosts pueden ser alcanzados a través de cuales interfaces:
- Cuando el conmutador recibe una trama registra el par emisor/localizzación en la tabla del conmutador
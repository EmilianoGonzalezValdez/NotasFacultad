Ethernet e IEEE 802.3 son casi idénticos; usaremos esos dos términos indistintamente.
Asuntos de la CED se pueden hacer por hardware: Entramado, control de errores, detección de portadora, detección de colisiones.
Para esos asuntos conviene tener 2 componentes de hardware:
- *Transceptor:* maneja detección de portadora y detección de colisiones
- *Tarjeta controladora:* se encarga de:
- 	ensamblar los datos en el formato de trama adecuado
- 	calcular el terminador de las tramas de salida
- 	comprobar las tramas de entrada

**Tipos de cableado en Ethernet**

Cada cableado de Ethernet tiene una longitud máxima de cable por segmento.
Una señal a medida que se va propagando por un cable se va debilitando. Llega un punto a partir del cual la señal es demasiado débil como para continuar su viaje.
Para hacer que la señal pueda viajar mucho más alla de ese punto se usan *Repetidores:*
- Un repetidor es un dispositivo de capa física que recibe, amplifica y retransmite señales en ambas direcciones.
- Los repetidores introducen un retardo
- Para permitir redes mayores que un segmento en Ethernet conectar múltiples cables mediante repetidores

**Diferentes formas de cablear un edificio:**
1. Un cable pasa entre cuarto y cuarto y cada estación se conecta a él en el punto más cercano
2. Una *columna vertical* corre del sótano a la azotea y en cada piso se conectan cables horizontales a dicha columna, además en cada piso se conecta un cable a la columna con un repetidor entre ambos
3. Topología de *árbol:* El medio de transmisión es un cable que se divide en ramas. El árbol tiene puntos conocidos como *headends*, donde uno o más cables comienzan (a su vez cada uno de estos podrá tener ramas). La transmisión desde una estación se propaga por el medio y puede ser recibida por todas las otras estaciones

**Restricción de Ethernet:** puede haber múltiples segmentos de cable y múltiples repetidores, pero ningpun par de transceptores puede estar separado por más de 2.5 km y ninguna ruta entre dos tranceptores puede atravesar más de 4 repetidores.

**Ejercicio:** Para una LAN de 10 Mbps con una longitud máxima de 2500 m y cuatro repetidores, el tiempo de ida y de vuelta es aproximadamente de 50 useg en el peor caso. ¿Qué tamaño conviene que tenga la trama mínima?
**Solución:** La trama mínima debe tomar por lo menos 20 useg en transmitir. A 10 Mbps, un bit tarda 100 nseg por lo que 500 bits es la trama mas pequeña que se garantiza que funcionará. Para agregar algún margen de seguridad, este número se redondeó a 512 bits o 64 bytes

**La razon para tener una trama de longitud minima es:** evitar que una estación complete la transmisión de una trama corta anted de que el primer bit llegue al extremo más alejado del cable, donde podría tener una colisión con otra trama

En el caso de que diseñaramos una red de mayor velocidad, ¿Qué cambios necesitamos hacer?.
- Supongamos que aumenta la velocidad de la red, y la longitud máxima del cable permanece igual. La longitud mínima de trama debe aumentar
- Supongamos que aumenta la velocidad de la red y la longitud de trama mínima no cambia. La longitud máxima del cable debe disminuir, de manera proporcional

Conclusión a tener en cuenta para el diseño de una red local cableada:
- A medida que aumente la velocidad de la red, la longitud mínima de la trama debe aumentar o la longitud máxima del cable debe disminuir, de manera proporcional
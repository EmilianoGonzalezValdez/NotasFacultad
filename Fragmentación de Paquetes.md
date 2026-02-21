Cada red impone un tamaño máximo a sus paquetes (las cargas útiles máximas suelen ir desde los 48 bytes con las celdas ATM hasta los 65515 bytes para paquetes IP)

¿Que pasa si un paquete grande P quiere viajar a través de una red cuyo tamaño máximo de paquete es bastante más pequeño que P?.
Bueno, en este caso las puertas de enlace dividen los paquetes en *fragmentos*, enviando cada fragmento como paquete de interred individual, aunque las redes luego tienen el problema de unir nuevamente los fragmentos

Existen 2 estrategias opuestas para recombinar los fragmentos y recuperar el paquete original:
- *Hacer transparente la fragmentación causada por una red de "paquete pequeño"* (a las demás redes subsiguientes por las que debe pasar el paquete para llegar a su destino final).
- 	Con este método la red de paquete pequeño tiene las puertas de enlace que interactúan con otras redes.
- 	Cuando un paquete de tamaño excesivo llega a una puerta de enlace, esta lo divide en fragmentos.
- 	Todos los fragmentos se dirigen a la misma puerta de enlace de salida, donde se recombinan las piezas.
- 	Las redes ATM (de circuitos virtuales) tienen hardware especial para esta estrategia
- *Abstenerse de recombinar los fragmentos en las puertas de enlace intermedias*.
- 	Una vez que se ha fragmentado un paquete, cada fragmento se trata como si fuera un paquete original. Todos los paquetes pasan por la puerta de enlace de salida.
- 	La recombinación ocurre en el host de destino.
- 	IP funciona de este modo

Desventajas de la fragmentación transparente:
- La puerta de enlace de salida debe saber cuándo ha recibido todas las piezas por lo que debe incluirse un *campo de conteo* o un *bit de fin de paquete* en cada paquete
- Todos los paquetes deben salir por la misma puerta de enlace; esto puede bajar un poco el desempeño.
- Hay una sobrecarga para reensamblar y volver a fragmentar repetidamente un paquete grande que pasa por varias redes de paquete pequeño

Desventajas de la fragmentación no transparente:
- Requiere que todos los host sean capaces de hacer el reensamble
- Al fragmentarse un paquete grande, aumenta la sobrecarga total, pues cada fragmento debe tener un encabezado


**Esquema de numeración de fragmentos:**
- El protocolo de interred define un *tamaño de fragmento elemental*. Al fragmentarse un paquete todas las partes iguales al tamaño de fragmento elemental, excepto la última que puede ser más corta
- Para saber a qué paquete pertenece un fragmento se numera el paquete original
- Para referirme a un fragmento puedo poner en el encabezado el desplazamiento del bit o byte inicial en el paquete original
- Para saber si vienen más fragmentos se debe poner un bit que indica si el fragmento es el último del paquete original
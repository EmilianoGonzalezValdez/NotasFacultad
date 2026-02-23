Una red corresponde a un bloque contiguo del espacio de direcciones IP llamado *prefijo*.
Los prefijos se escriben dando la dirección IP más baja en el bloque y la cantidad de bits usadas para la dirección de la red.
Por ejemplo en el prefijo 128.208.0.0/24 la dirección IP más baja en el bloque es 128.208.0.0, la porción de la red es de 24 bits y hay 2^8 máquinas en la red

En el libro de *Kurose* se define una subred como un conjunto de interfaces de dispositivos con la misma parte de red de la dirección IP.
Otra definición seria máquinas que se pueden alcanzar físicamente entre sí *sin la necesidad de un enrutador interviniente*

La **"Receta"** para determinar las subredes es:
Desacoplar cada interfaz de su host o enrutador, creando islas de redes aisladas. Cada red aislada se llama una *subred*. Las subredes se indican usando prefijos
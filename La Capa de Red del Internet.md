La capa de red tiene como proposito el llevar paquetes de un host de origen a uno de destino siguiendo una ruta conveniente.
Los asuntos de los que se encarga esta capa son:
- Almacenamiento y reencío
- Enrutamiento
- Control de Congestión
- Conectar redes de distintas tecnologías
- Fragmentación

**¿Por que estudiamos la capa de red?**
- Para entender cómo están organizadas las redes
- Para entender cómo se intercoenctan redes de distintas recnologías
- Para aprender algunos conceptos fundamentales como proveedores de servicios de red, enrutadores, etc.
- Para entender la necesidad de los enrutadores y cómo funcionan
- Para entender cómo se hacen asignaciones de direcciones de red a máquinas en una red local, a instituciones varias. El por qué y cómo se lo hace
- Para entender algunos problemas fundamentales y algoritmos alternativos para su solución. Enrutamiento, control de congestión, fragmentación

El hardware subyacente de la capa de red se compone de varias subredes de distinta tecnología unidas entre sí usando puertas de enlace.
Recordemos que un paquete no puede pasar tal cual de una red a otra porque los formatos de paquete difieren de una red a otra, y porque los tamaños maximos de paquetes difieren de una red a otra


**Enfoques para mandar un conjunto de paquetes desde un host de origen a un host de destino**

Hay dos bandos en relación a cómo se debe hacer esto:
- Usar una ruta fija para mandar todos los paquetes (*servicio orientado a la conexión*)
- La ruta puede cambiar, por lo que distintos paquetes pueden seguir distintos caminos (*servicio no orientado a la conexión*)

*Servicio no orientado a la conexión:*
- Alentado por la comunidad de internet
- Los paquetes se enrutan de manera independiente. La ruta a usar entre los host va a cambiar cada cierto tiempo. Cada paquete debe llevar una dirección de destino completa
- La nomenclatura usada es: Paquetes = *datagramas*, Subredes = *subredes de datagramas*
-  Para ver el **Diseño de la tabla de un enrutador** vamos a suponer que: Existe un procedimiento que dada la dirección del host de destino me retorna dirección del enrutador destino, y que el enrutador de destino sabe cómo entregar el paquete a host de destino (por mas que el host de destino esté en una LAN)
-  *Tabla del enrutador:* La tabla del enrutador solo necesita entradas para los enrutadores de la subred. cada entrada de la tabla de enrutador esta formada por filas "<enrutador de destino, línea de salida>" donde la linea de salida es la dirección de un enrutador

Cuando lelga un paquete a un enrutador:
1. Se lo almacena y se comprueba que llegó bien
2. Se determina el enrutador de destino asociado al host de destino
3. Se usa fila de ese enrutador de destino para reenviar el paquete por linea de salida de esa fila

Podemos pensar que *dirección de un host* es un número con dos partes, <dirección de red, número de máquina>, donde:
- La *dirección de red* sirve para identificar una red
- El *número de máquina* sirve para identificar una máquina dentro de la red
- Por ejemplo direcciones de 8 bits, red de 4 máquinas viene dada por las direcciones: 11010000, 11010001m 11010010 y 11010011 (dirección de red es 110100)
- IP respeta esta convención pero con direcciones de 32 bits

Podemos pensar que los enrutadores que están conectados a hosts de una misma red tambien forman parte de esa red. O sea que tienen el mismo valor en la parte de dirección de red (cuentan como máquinas tambien).
Todo host de destino va a tener un enrutador con igual dirección de red y hay que usar ese enrutador de destino para llegar al host de destino

Dada la dirección de host de destino, para encontrar enrutador de destino apropiado se debe buscar el enrutador de destino cuya dirección concuerde con la mayor cantidad de bits desde la izquierda con la dirección de host de destino.

Por ejemplo, en el ejemplo anterior suponemos que tenemos enrutadores de destino de direcciones: 10010000, 110000001, 11110010 y 11010011. Suponemos que nos llega un paquete dirigido al host de destino 11010010. El enrutador de destino que concuerda en más bits con ese host de destino es 11010011 y ese es el que se va a considerar para llegar al host de destino

**Servicio orientado a la conexión:**
- Alentado por las compañias telefonicas
- Todos los paquetes se mandan por la misma ruta
- *Trabajo a realizar antes de mandar paquetes:*
- 	Hay que configurar una ruta del host de origen al de destino
- 	Esto se llama crear una conexión
- 	*circuito virtual (CV)* = conexión
- Cada paquete lleva un *identificador* que indica a cual CV pertenece
- Cuando no se necesita enviar más paquetes se *libera la conexión*. Al hacer eo, también se termina el CV

Se elige una ruta de la máquina de origen a la de destino. Esta ruta se almacena en tablas dentro de los enrutadores

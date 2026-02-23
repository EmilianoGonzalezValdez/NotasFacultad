**Efecto sobre el reenvío de paquetes de tener una tabla de reenvío grande:**
- Los enrutadores deben buscar en la tabla de reenvío grande para enviar cada paquete, la eficiencia de esta búsqueda es afectada
- Los enrutadores en un proveedor de servicios de internet (PSI) grande pueden tener que enviar millones de paquetes por segundo. Este gran volumen de paquetes a enviar empeora más las cosas. Para esto hace falta hardware especial y una computadora de propósito general no alcanza.

**Efecto sobre el algoritmo de enrutamiento de tener una tabla grande:**
El costo de actualizar las tablas de enrutamiento es grande
En **CONCLUSIÓN:** hay que evitar tablas de reenvío demasiado grandes.

Se nos genera un nuevo problema, ¿Cómo asignar una red a una organización sin que se desperdicien demasiadas direcciones y sin que las tablas de enrutamiento crezcan demasiado?
- Si se le da una red demasiado chica a una organización, esta puede expandirse y terminar con más de un prefijo, lo cual qumentará el tamaño de algunas tablas de reenvío. Por lo tanto, cada organización debe tener un solo prefijo de red
- Si se le da una red demasiado grande a una organización, entonces se pueden desperdiciar muchas direcciones IP.
- Colocar todas las subredes del mundo en una tabla de reenvío hace que las tabla sea demasiado grande. Esto no es necesario, porque veremos que un enrutador en una región no necesita saber de subredes en regiones muy alejadas de ella

Esto nos genera un **subproblema:** ¿Cómo asignar una red a una organización sin que se desperdicien demasiadas direcciones?.
La idea de la solución es alojar las direcciones IP de una red en un bloque contiguo que permite 2^k máquinas. Por ejemplo, si un sitio necesita 2000 direcciones, se le da un bloque de 2048 direcciones

**Implementación de la solución: CIDR (Classles Inter Domain Routing):**
En todas las máquinas de la red, la parte de la dirección IP para identificar la red es la misma. Se presenta la red asignada con un *único prefijo*
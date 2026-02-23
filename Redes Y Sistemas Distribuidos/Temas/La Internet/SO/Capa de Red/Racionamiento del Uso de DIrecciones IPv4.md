En la situación en la que un provedor de servicios de internet (PSI) tiene una red de c bits (de dirección); esto quiere decir que se le dan $2^{32-c}$ números IP para máquinas. Con el esquema actual los clientes no pueden tener más de $2^{32-c}$ máquinas usando el servicio del PSI en un momento dado.

¿Como podemos aumentar la cantidad de máquinas que usan el servicio del PSI bien por arriba de las $2^{32-c}$ a pesar de tener una red de c bits?.
Resolverlo aumentaría drásticamente la cantidad de máquinas que pueden acceder a internet IPv4


La solución viene con la *traducción de dirección de red (NAT)*.
Asignar un solo N° de IP a cada organización para el tráfico de internet.
1. Dentro de la organización cada computadora tiene una dirección IP única que se usa para el tráfico interno. (O sea, estos números IP no se usan en internet - solo adentro de la organización y pueden repetirse en distintas organizaciones)
2. Cuando un paquete sale de la organización y va al PSI, se presenta una traducción de dirección (de la dirección de la computadora en la organización a la dirección IP usada por la organización en internet)

**Implementación:** Para hacer posible este esquema los 3 rangos de direcciones IP se han declarado como privados. Las organizaciones pueden usarlos internamente cuando deseen. La única regla es que ningún paquete que contiene estas direcciones pueda aparecer en la internet. Los 3 rangos reservados son:
- 10.0.0.0 -10.255.255.255/8 (16,777,216 hosts)
- 172.16.0.0 - 172.31.255.255/12 (1,048,576 hosts)
- 192.168.0.0 - 192.168.255.255/16 (65,536 hosts)

Supongamos que en una organización cada máquina tiene una dirección 10.x.y.z.
Cuando un paquete sale de las instalaciones, este pasa a través de una *caja NAT* que convierte la cirección interna de origen de IP a la dirección IP de la organización.

Cada *mensaje TCP saliente* contiene puertos de origen y de destino que sirven para identificar los procesos que usan la conexión en ambos extremos.
¿Que pasa con el uso de puertos cuando un proceso quiere establecer una conexión TCP con un proceso remoto?. Este se asocia a un puerto TCP sin usar en su máquina conocido como *puerto de origen* (indica dónde enviar mensajes entrantes de esta conexión). El proceso proporciona también un *puerto de destino* para decir a quién dar los mensajes en el lado remoto

Con esto se genera un problema, cuando la respuesta vuelve, por ejemplo de un servidor web, se dirige naturalmente a la dirección IP de la compañia, ¿como sabe ahora la caja NAT con qué dirección se reemplaza?
Una idea que no siempre funciona seria guardar la asociación en la caja NAT del número IP al puerto de origen que viene en el mensaje TCP/UDP dentro del paquete. Estas asociaciones se pueden guardar en una tabla en la caja NAT. Esto no suele funcionar puesto que podría ocurrir que dos conexiones de las máquinas 10.0.0.1 y 10.0.0.2 usaran el puerto de origen 5000 por ejemplo. Luego el puerto de origen no sirve para identificar el N° de IP.

La solución adoptada en la práctica es distinguir entre el N° de puerto usado para identificar la máquina (o sea IPs en la red interna) y el N° de puerto usado por TCP/UDP para identificar la conexión. Cuando llega un paquete con puerto de origen, se busca en la tabla del IP del nodo y el N° del ouerto que se usa para la conexión.

*Tabla de traducción de la caja NAT:*
- Los indices en la tabla son números de puerto para identificar la máquina
- Una entrada de la tabla contiene: (número de puerto para identificar la conexión, dirección IP)


**Tratamiento de un paquete que llega a la caja NAT desde el ISP:**
- El puerto de origen en el encabezado TCP se extrae y usa como un índice en la tabla de traducción de la caja NAT. Desde la entrada localizada, la dirección IP interna y el puerto TCP se extraen e insertan en el paquete. Entonces el pquete se pasa al enrutador de la compañia para su entrega normal usando la dirección 10.x.y.z

**Tratamiento de un paquete saliente que entra en la caja NAT:**
- La dirección de origen 10.x.y.z se remplaza por la verdadera dirección IP de la compañia y el campo puerto de origen TCP se reemplaza por un índice en la tabla de traducción de la caja NAT

**Criticas a NAT:**
- Viola el modelo de IP que dice que cada dirección IP identifica una sola máquina globalmente
- Si la caja NAT se cae y se pierde su tabla de traducción, todas sus conexiones TCP se destruyen
- Atrasa la adopción de IPv6

*Nat 444:*
- Los proveedores de servicio de internet (ISP) tambíen pueden tener una NAT. Esto hace que las direcciónes IPv4 puedan racionarse más aun y durar aun más tiempo
- El espacio de direcciones IP reservado para NAT 444 es 100.64.0.0/10

El espacio de direcciones de 32-bits ya ha sido agotado en varias regiones del mundo, por lo que hay que empezar a considerar un espacio de direcciones mucho mas grande

Un problema con IPv4 es que algunos campos del encabezado hacen que el procesamiento de datagramas en los enrutadores lleve tiempo.
*datagrama IP* = encabezdo + texto
*encabezado* = parte fija de 20 bytes + parte opcional
Un encabezado tiene varios campos. Cada tipo de información que necesito va en uno o más campos. La parte opcional tiene longitud variable

Entre las partes obligatorias estan:
- Campo *IHL* (4b). Se maneja igual que el mismo campo en TCP, longitud del encabezado en palabras de 32b o 5 cuando no hay opciones.
- Campo *longitud total:* 2B de encabezado + datps $\le$ 65535 B
- Campo *tipo de servicio:* Los ultimos 2 bits se usan para información de notificación de congestión. Los 6 primeros bits se usan para indicar la clase de servicio
- Campo *protocolo* (8b): dice a cuál proceso de transporte entregar el paquete
- Campo *identificación:* se usa para que el host de destino determine a qué paquete un fragmento pertenece
- Campo *tiempo de vida:* se usa para limitar el tiempo de vida de un paquete. Debe decrementarse en cada salto. Cuando llega a cero el paquete es descartado y se manda un paquete de advertencia al host de origen. Esto evita que los paquetes anden dando vueltas demasiado tiempo
- Campo *suma de verificación:* se usa para detectar errores en el encabezado cuando el paquete viaja a lo largo de la red. Deve recalcularse en cada salto, porque el campo tiempo de vida siempre cambia. Es solo sobre el encabezado porque en capa de transporte se chequea el segmento entero con otro campo checksum.
- En un datagrama IP tambien estan los campos *direcciones de origen y de destino*, cada una tiene 32 b e indican el número de red y el número de máquina. Como consecuencia de esto se usan npumeros IP diferentes para distinguir las máquinas de una red, además las direcciones IP son jerárquicas
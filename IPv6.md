**Requisitos:**
- Que el formato de encabezado ayude a aumentar la velocidad de procesamiento y reenvío
- Cambios en el encabezado para facilitar la calidad de servicio

Hace falta que el procesamiento de encabezados sea más rápido, porque las redes cada vez son más rápidas, en cambio la velocidad de los procesadores se está estabilizando. Entonces para compensarlo hay que agilizar el procesamiento de los datagramas

**Formato de datagrama IPv6:**
- *Encabezado de longitud fija* de 40 bytes para procesamiento más ráoido de datagramas
- *Capacidad de direccionamiento expandida:* direcciones de 128 bits
- *Etiquetado de flujos:* se etiquetan paquetes que pertenecen a un mismo flujo para los cuales el emisor requiere manejo especial
- 	**Consecuencia del etiquetado de flujos:**
- 	Cuando un paquete con una etiqueta de flujo de cero aparece, los enrutadores pueden ver tablas internas para ver a qué tipo de tratamiento especial requiere
- *Etiqueta de flujo:* (20 b) para identificar datagramas en el mismo "flujo".
- La *prioridad* tiene dos usos: para dar prioridad a ciertos datagramas dentro de un flujo o para dar prioridad a datagramas de ciertas aplicaciones sobre datagramas de otras aplicaciones
- *Longitud de carga útil:* (16 b) número de bytes en el datagrama IPv6 luego del encabezado (de 40 B)
- *Limites de Saltos:* (8 b) el contenido de este campo se decrementa en 1 por cada enrutador que entrega el datagrama. Si el contador alcanza 0, el datagrama se descarta
- *Próximo encabezado:* (8 b) significa cúal de los 6 encabezados de extensión de opciones actuales le sigue al encabezado. Si este encabezado es el último encabezado IP, el campo dice a cuál protocolo de transporte entregar el datagrama. Los encabezados de opciones también tienen este campo

**Direcciones IPv6:**
- Son escritas como 8 grupos de 4 dígitos hexadecimales
- Para separar los grupos se usa ":"
- Para optimizarlos los ceros a la izquierda de cada grupo pueden ser omitidos. Grupos con 16 bits iguales a 0 pueden remplazarse con dos ":"

**Otros cambios de IPv6 en realción a IPv4:**
- No se permite fragmentación ni re-ensamblado en enrutadores intermedios. Esto solo puede hacerse por el origen y el destino
- *Suma de Verificación:* removido para reducir el tiempo de procesamiento en cada salto, ya que trabajar con este campo era costoso en IPv4
- *Opciones:* están permitidas, pero fuera del encabezado, indicado por el campo de próximo encabezado

**¿Que se puede hacer si un datagrama es demasiado grande para pasar por una línea de salida de un enrutador?**
Un enrutador descarta paquetes que son demasiado grandes para la línea de salida y manda al emisor un mensaje de paquete demasiado grande. Luego el emisor puede reenviar los datos usando datagramas IP más chicos

Una dirección IPv6 la podemos dividir en:
- *Identificador de red:* identifica la red principal en la que se encuentra el dispositivo
- *Identificador de subred:* ayuda a dividir la red principal en subredes mas pequeñas
- *Identificador de interfaz:* identifica de manera única al dispositivo dentro de la subred

**Esquema lógico de una red IPv6:**
- *Nivel de red global:*
- 	El ISP asigna un prefijo global a una organización
- *Nivel de red interna:*
- 	La organización asigna subredes dentro de ese espacio
- *Nivel de subred:*
- 	Son subredes divididas a partir del prefijo interno
- 	Pueden usarse para departamentos

Una organización recibe un *prefijo global*. El mismo también puede ser de /48. Un prefijo global de /48 puede ser dividido en subredes más pequeñas de /64 para uso interno

En IPv6 no se usan prefijos para enlaces entre enrutadores. En lugar de eso se usan *direcciones link-local*. Las cuales:
- Todas comienzan con el prefijo fe80::/10
- Los primeros 10 bits son: 1111111010
- El resto puede completarse para crear una dirección única dentro del enlace.

Además, si dos dispositivos están conectados al mismo enrutador, pueden comunicarse entre sí usando direcciones link local. Las direcciones link local se configuran automáticamente. Los 64 bits menos signifiactivos suelen derivarse de la dirección MAC de la interfaz de red usando el método EUI-64

Los *enrutadores de un ISP* manejan prefijos globales asignados a sus cplientes y otras redes conectadas.
Los *enrutadores de una organización* (nivel interno y subred) manejan un prefijo global asignado por el ISP (por ejemplo 2001:db8:1::/48), y lo dividen en subprefijos mas pequeños (por ejemplo 2001:db8:1:1::/64).
Sus tablas incluyen rutas para estos subprefijos.
Los enrutadores distribuyen el trafico entre subredes internas(de /64)
Estos enrutadores tienen rutas hacia el Gteway del ISP representadas por el prefijo global

Las *direcciones ULA* están diseñadas para proporcionar conectividad privada dentro de una organización. Una dirección ULA siempre comienza con FC o FD en los bits mas significativos. Estas direcciones no pueden salir hacia la internet ni ser vistas fuera de la red interna, además son únicas dentro de la red local. Se usan para redes locales aisladas que no necesitan conectar la internet. También se pueden usar como respaldo de las direcciones globales. Si la conexión a internet falla, ULA permite que la conexión interna siga funcionando

Por ejemplo: supongamos que tienes un prefijo ULA generado automaticamente como FD00:1234:5678::/48. Puedes dividirlo en redes internas:
- subred A: FD00:1234:5678:1::/64
- subred B: FD00:1234:5678:2::/64

Un mismo dispositivo puede tener una direción ULA para comunicación interna y dirección global unicast para acceso externo
Los dispositivos usan automaticamente la dirección adecuada según el tipo de comunicación. Los recursos internos pueden estar protegidos y aislados mediante direcciones ULA.

**Asignación de redes globales en IPv6:**
- *IANA (Internet Assigned Numbers Authority):* asigna bloques enormes de direcciones IPv6 a los registros regionales
- *RIR (Registros Regionales de Inetrnet):* distribuyen bloques mas pequeños a los ISP, tipicamente de /32
- *ISPs:* dividen estos bloques y asignan prefijos más pequeños a sus clientes
- *Organizaciones:* divide el prefijo recibido en subredes

En IPv6 las tablas de reenvío son diferentes que en IPv4. En IPv6 se usan los siguientes valores en una fila de la tabla de reenvío:
- *El prefijo de destino*
- *la interfaz de salida*
- La *dirección del siguiente salto hacia el destino* que puede ser un enrutador adyacente
- *Métrica:* medida del costo asociado con la ruta usada para elegir la mejor ruta disponible si hay mas de una
Se pueden usar prefijos global, link-local, ULA, etc. en una misma interfaz

En IPv6 las subredes suelen usar prefijos estándar de /64 lo que simplifica las búsquedas en las tablas de enrutamiento.
Los prefijos globales, regionales y locales están organizados jerparquicamente. Eso permite una mayor agregación de rutas, reduciendo la cantidad total de entradas en las tablas.
Las búsquedas en las tablas de reenvío suelen ser bastante eficientes y pueden lograrse en orden logarítmico del tamaño de la tabla en muchas implementaciones modernas.
Los routers de alto rendimiento usan memoria TCAM (Ternary Content Addressable Memory) que permite realizar busquedas en paralelo en múltiples entradas de la tabla, alcanzando velocidades aún mayores.
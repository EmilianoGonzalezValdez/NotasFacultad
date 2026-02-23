La naturaleza de los PPEE es muy distinta a la de los protocolos de enrutamiento de puerta de enlace interior. Lo que lleva a quesurjan problemas no considerados antes a resolver.
No hemos estudiado ningún PPEE, aunque acabamos de ver las caracteristicas de estos

*BGP (Border Gateway Protocol)* es el PPEE de facto que usa internet

**Tareas que realiza BGP:**
- BGP provee a cada SA un medio para:
- 	Obtener *información de alcanzabilidad* de subredes desde SA vecinos.
- 	Propagar la información de alcanzabilidad a todos los enrutadores dentro del SA
- 	Determinar "buenas" rutas a las subredes basándose en la información de alcanzabilidad y en las políticas del SA
- 	BGP permite a casa subred publicar su existencia al resto de la internet. BGP se asegura que todos los SA de la internet conozcan acerca de la subred y cómo llegar allí
- BGP permite a casa SA aprender cuáles destinos son alcanzables vía sus SA vecinos
- En BGP los destinos son prefijos donde cada prefijo representa una subred (según Kurose) o una colección de subredes (definida usando la agregación de prefijos-CIDR)

En BGP un SA es identificado por un número globalmente único lamado *número de sistema autónomo (ASN)*

Cuando un enrutador avisa de un prefijo a lo largo de una sesión BGP incluye con el prefijo una ruta que pasa por varios SA para llegar al prefijo. Una *ruta* se compone de un prefijo más *atributos BGP*.
**Algunos atributos importantes:**
- *AS-PATH:* contiene los SA por los cuales el aviso del prefijo ha pasado. Cuando un prefijo para por un SA, el SA agrega su ASN al atributo AS-PATH
- *NEXT-HOP:* es el IP de la interfaz del enrutador que comienza el AS-PATH hacia el destino


¿Cómo hacer para propagar la información de rutas en BGP?
En BGP pares de enrutadores intercambian información de rutas sobre conexiones TCP semipermanentes usando el puerto 179.
Hay tipicamente una conexión BGP TCP para cada enlace que conecta directamente dos *enrutadores EBSA (o enrutadores BGP)* en dos SA diferentes y para enlaces entre enrutadores dentro del SA.
Para cada conexión TCP, los 2 enrutadores al final de la conexión se llaman *compañeros BGP*. Estos compañeros BGP se avisan rutas

**Sesiones BGP:**
- La conexión TCP con todos los mensajes BGP enviados por la conexión se llama *sesión BGP*
- Una sesión BGP entre enrutadores de dos SA se llama *sesión externa BGP (eBGP)*
- Una sesión BGP entre enrutadores de dos SA se llama *sesión interna BGP (iBGP)*
- Las líneas de las sesiones BGP no siempre se corresponden con los enlaces físicos

Cuando una puerta de nelace P recibe rutas:
- P usa las sesiones iBGP para distribuir las rutas a los otros enrutadores del SA de P
- Las sesiones iBGP se usan para distribuir rutas a los enrutadores dentro del SA

En BGP, **un vecino de un enrutador** es otro enrutador con el cual se establece una sesión BGP para intercambiar información de enrutamiento.
El vecino se configura manualmente mediante la definición de su dirección IP y número de AS en la configuración BGP del enrutador
En algunos casos, especialmente con IPv6, existen mecanismos de descubrimiento automatico de vecinos para simplificar la configuración
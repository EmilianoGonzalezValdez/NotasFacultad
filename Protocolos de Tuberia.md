En esta situación tenemos una latencia alta, el RTT es muy alto comparado con el tiempo de copiar un paquete. Por lo tanto se pueden mandar varios paquetes antes de que llegue el ACK del primer paquete enviado.
Unos protocolos adecuados para dicha situación se los conocen como *protocolos de tubería*. En nuetro caso veremos 2:
- Protocolo Retroseso-N
- Protocolo de Repetición Selectiva

Los protocolos de tubería se caracterizan debido a que el emisor puede enviar múltiples paquetes al vuelo a ser confirmados. Por lo cual hay que usar bufferes en el emisor y tener un número de secuencia de mas de un bit


La ET emisora debe manejar *buferes para los mensajes de salida* porque puede hacer falta retransmitirlos. El emisor almacena en bufér todas los segmentos hasta que se confirma su recepción
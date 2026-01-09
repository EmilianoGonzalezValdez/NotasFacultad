
# Sistemas operativos de Redes

Los sistemas operativos de redes son importantes, pues son estos los cuales manejan los tipos de redes en si. En cada tipo de red existen problemas los cuales son resueltos por los sistemas operativos de redes(SOR). También cada SOR tienen contenidos los protocolos de comunicación de su tipo de red respectivo

Los SOR estan distribuidos siguiendo un modelo de capas o niveles cuya cantidad, nombres y contenidos dependen del tipo de red. De esta forma una determinada capa puede ofrecer sus servicios a la capa superior ocultando su implementación . Estos servicios que una capa provee a las capas superiores se los denomina **Interfaces entre Capas**

Una capa n se piensa como una comunicación entre la capa n de varias maquinas. Para especificar como es esta conversación se definen **protocolos**, es decir que se definen **reglas y convenciones usadas en la conversación entre la capa n de una maquina y la capa n de otra maquina**

Las comunicaciones entre capas sucesivas ocurren durante el envió de mensaje, donde las capas del proveedor del mensaje interactuan de forma descendente, y al recibir el mensaje donde las capas del receptor interactuan ascendentemente 

> debajo de la capa 1 esta el medio físico

De esta forma podemos definir una **Arquitectura de Red**  como el conjunto de capas y protocolos, es decir una **pila de protocolos**


# *Sistemas operativos para redes de computadoras*



- En una red de computadoras existen 5 capas:

    - Capa 5 o Capa de Aplicación: Produce un mensaje y lo envía a la capa 4 para su transmisión

    - Capa 4 o Capa de Transporte: Pone un encabezado en el mensaje con un orden de secuencia para que al llegar se sepa el orden correcto de este, y luego pasa el resultado a la capa 3

    - Capa 3 o Capa de Red: En esta capa existen limitaciones de tamaño para los mensajes, por lo cual divide el mensaje en paquetes colocandole un encabezado a cada uno, ademas si la maquina es un enrutador decide que linea usar. Luego pasa los paquetes a la capa 2

    - Capa 2 Capa de Enlace De Datos: Agrega un enlace y un terminador a cada paquete, luego pasa los paquetes modificados a la capa 1

    - Capa 1 es la Capa Física


#### ***Problemas de las redes de computadoras***



- Identificar maquinas en una red

    Una vez desarrollado el protocolo a utilizar nos hace falta una forma de identificar cada maquina en una misma red. Para ello se le asigna una dirección a cada maquina

- Control de flujo: 

    Otro problema a tener en cuenta es el control de flujo, ya que no queremos que se pierdan algunos paquetes enviados. Lo cual pasa cuando algun emisor satura de datos al receptor hasta que este ya no puede almacenar mas, por ende, se empiezan a perder datos

    Para solucionar esto se usa la **retroalimentación al emisor**, es decir, le indicamos al emisor cuando puede enviar mensajes

- Tamaño de mensaje:

    Este problema se puede dar el mensaje es demasiado grande al llegar de una red diferente o cuando 2 capas consecutivas aceptan distintos tamaños de mensajes

    La solución es fragmentar los mensajes, transmitir los fragmentos y luego reensamblar los mensajes

    La fragmentacion puede ser:

    - Transparente

    - No Transparente

- Congestion: 

    Ocurre cuando una red no puede manejar la carga de paquetes que recibe de manera aceptable

    La solución es hacer que las computadoras emisoras se enteren de la congestión y reduzcan el trafico de salida 


#### ***Modelo de capas en un SOR de computadoras***

![alt text](image(1).png)

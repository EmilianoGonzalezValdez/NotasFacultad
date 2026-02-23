La cola en un búfer que precede a un enlace tiene capacidad finita.
¿Que pasa con un paquete cuando llega a una línea de salida con buffer lleno?
El paquete que llega a un búfer lleno se pierde. Los paquetes perdidos deben ser retransmitidos por el enrutador previo o el host emisor.

Si comienzan a llegar muchos paquetes por algunas líneas de entrada y todas necesitan la misma línea de salida, se irán acumulando los paquetes en una cola. Si no hay suficiente memoria para almacenar todos los paquetes, muchos de ellos se perderán


Si bien vimos control de congestión en TCP, estos algoritmos tienen problemas:
- El host destino demora demasiado en enterarse de la congestión (solo por expiración de temporizador de retransmisiones o 3 ack duplicados)
- Los hosts solo se enteran de pérdidas de paquetes, no pueden controlar qué paquetes perder y cuáles no

Tenemos varias razones para estudiar el control de congestión en la capa de red:
- Para resolver los problemas de los protocolos de control de congestión de TCP mencionados
- Para entender las medidas que pueden tomar los enrutadores para detectar la congestión y colaborar con la capa de transporte para ayudar a controlar mejor la congestión

Hay 2 tipos de soluciones que son las primeras que se nos ocurren:
- Aumentar los recursos
- Disminuir la carga en la subred (nos concentramos en esto)

Formas de disminuir la carga en la subred:
- **Regulación del tráfico:** hacer que hosts responsables de la congestión se enteren más rápido (que con protocolos de TCP) de la congestión y reduzcan su tasa de transferencia
- **Desprendimiento de carga:** enrutadores descartan paquetes inteligentemente antes que se saturen los buferes
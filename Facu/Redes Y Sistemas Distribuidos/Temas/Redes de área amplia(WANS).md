
# Redes de área amplia(WANS) 



 Cubre un área geográfica grande, como un país o hasta un continente



Esta organizada de la siguiente manera:

- Consta de una subred compuesta por varios enrutadores conectados entre si formando un "grafo"

- A una subred pueden estar conectadas computadoras individuales o una LAN entera logrando una interconexion entre ellas

- Hay distintas rutas para llegar de un dispositivo a otro

Un paquete enviado en una WAN sigue una ruta de enrutadores. En cada enrutador se almacena el paquete antes de ser enviado. Pero hay muchos caminos que conectan 2 enrutadores, entonces ¿Que camino se usa? Bueno, eso lo decide el algoritmo de enrutamiento 

Si la tasa de enlace excede la tasa de transmision puede pasar que el buffer del enrutador se llene. En consecuencia los paquetes encolados en el buffer que están esperando para ser enviados pueden llegar a ser descartados 

¿Cuanto demora el envio y almacenamiento de estos paquetes? , la formula geenral para aproximar esto es la siguiente:

$$
d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}

$$

donde 

$$
d_{proc} \space  \text{es el tiempo de procesamiento del nodo, chequeo de errores}. \atop \text {Se determina la linea de salida y normalmente este tiempo es menor que milisegundos}

$$



$$
d_{queue} \space  \text{es el tiempo de encolado, Tiempo de espera en el enlace
de salida para transmisión}. \atop \text {Depende de cuán
congestionado está el
enrutador}
$$



## SIstema telefonico

Cada domicilio esta conectado a una oficina central y cada una de estas esta conectada a una Toll office, las cuales , ademas de estar interconectadas entre si, son usadas para el reenvio de mensajes. Con una DSL se logra que de los datos de voz que viajan por la DSL y llegan a la oficina central DSLAM puedan dividirse y la voz vaya a la red telefonica y los datos a internet



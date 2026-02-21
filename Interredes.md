Tener diferentes redes implica tener diferentes protocolos. Por ello existen enrutadores que pueden conectar dos redes de distinta tecnología llamados *enrutadores multiprotocolo (puertas de enlace)*. Para enviar paquetes de una red a otra con diferente tecnología las puertas de enlace traducen o convierten paquetes de un protocolo a otro, aunque hay otra solución, que seria construir una capa arriba de las diferentes redes que oculte las diferencias entre las distintas capas redes. Esta ultima idea fue la que dio lugar a TCP/IP de forma tal que IP provee un formato de paquete universal que todos los enrutadores multiprotocolo reconocen y puede ser pasado a través de casi toda la red


**Problemas que surgen al pasar de una red a otra de tecnología distinta:**
- Paquetes de una red de circuitos virtuales deben transitar a una red sin conexiones
- Con frecuencia se necesitarán *conversiones de protocolo*
- Se necesitan *conversiones de direcciones*
- *Diferentes tamaños máximos de paquetes* usados por las diferentes redes
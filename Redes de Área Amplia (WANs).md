Una **red de área amplia (WAN)** cubre un área geográfica grande, típicamente un país o hasta un continente 

Una **WAN** está organizada de la siguiente manera:
- *Subred:* Varios enrutadores conectados entre si forman un grafo 
- A una subred pueden estar conectadas computadoras o LAN enteras, permitiendo de esta forma interconectar varias LANs
- Para ir de una maquina a otra hay varias rutas alternativas 

Para enviar mensajes en una WAN existe el **algoritmo de almacenamiento y reenvío**. En este un paquete sigue una ruta de enrutadores, el paquete se almacena enteramente en cada enrutador de dicha ruta. De esta forma el paquete almacenado en un enrutador espera allí hasta que la línea requerida de salida esté libre  luego se reenvía al siguiente enrutador

Si la tasa de llegada al enlace excede la tasa de transmisión del enlace por un periodo de tiempo, los paquetes se van a encolar y esperarán a ser transmitidos en el enlace. Si el buffer del enrutador se llena, los nuevos paquetes serán descartados y se perderán 

Normalmente hay varios caminos que conectan 2 enrutadores. El ==***algoritmo de enrutamiento***== es quien decide cual de todos ellos usar 

Para saber cuanto demora el almacenamiento y reenvío se utiliza la formula: $$d_{nodal}=d_{proc}+d_{queue}+d_{trans}+d_{prop}$$
donde $d_{proc}$ es el tiempo de procesamiento del nodo:
- Chequeo de errores
- Determinar la linea de salida
- normalmente < mili-segundos 

Y $d_{queue}$ es la demora por encolado:
- Tiempo de espera en el enlace de salida para transmisión
- Depende de cuán congestionado está el enrutador 

###### Sistema telefónico fijo:
Cada domicilio está conectado por un cable de cobre a una **End Office**. Toda oficina central está conectada a una **Toll Office**. Estas ultimas son usadas para el reenvío de mensajes y están unidas por cables de fibra óptica
Algunos ejemplos de aplicaciones P2P se usan para:
- *Distribución de archivos:* la aplicación distribuye un archivo de una única fuente a un gran número de compañeros
- *Bases de datos distribuidas:* sobre una gran comunidad de compañeros
- *Streaming:* Video on demand
- *VoIP:* voz sobre IP

*¿Cuanto tiempo se requiere para distribuir un archivo de un servidor a N compañeros?*. Para responder dicha pregunta debemos considerar ciertos parámetros como:
- Tasa de subida del enlace de acceso al compañero i: $u_i$
- Tasa de subida del enlace de acceso al servidor: $u_s$
- Tasa de descarga del enlace de acceso al compañero i: $d_i$
- Tamaño del archivo a ser distribuido: $F$
- Número de compañeros que quieren adquirir una copia del archivo: $N$

**Distribución de archivos en cliente-servidor:**
El *tiempo de distribución* es el tiempo que toma obtener una copia del archivo por los $N$ compañeros. Para calcularlo podemos dividir el problema en 2 partes:
- **Transmisión del servidor:** el servidor debe enviar secuencialmente $N$ copias de archivo a cada peer.
	- Tiempo para enviar 1 copia: $F/u_s$
	- Tiempo para enviar $N$ copias: $NF/u_s$
	- Demasiado trabajo del servidor
- **Descarga del cliente:** cada cliente debe descargar una copia del archivo
	- $d_{min}= \min({d_1,d_2,...,d_n})$ 
	- Tiempo de descarga del cliente con $d_{min}$: $F/d_{min}$ segs
	- Este es el peor tiempo de descarga

Por ende el Tiempo para distribuir F a N clientes usando enfoque cliente servidor es:$$D_{c-s}\ge \max({NF/u_s},{F/d_{min}})$$ Aumentando linealmente en N

**Distribución de Archivos en P2P:**
Al comienzo de la distribución solo el servidor tiene el archivo. Para que la comunidad de compañeros reciba este archivo, el servidor debe enviar cada bit del archivo al menos una vez en su enlace de acceso.
En P2P cada compañero puede redistribuir cualquier porción del archivo que ha recibido a cualquierasea otros compañeros, así los compañeros asisten al servidor en el proceso de distribución. Cuando un compañero recibe algo de datos de un archivo, puede usar su capacidad de subida para redistribuir los datos a los otros compañeros. Por ende, la capacidad total de subida del sistema es:$u_{total}=u_s+\sum{u_i}$. De esta forma el tiempo mínimo de distribución es: $$NF/u_{total}$$
De esta forma podemos partir el problema en 3:
- **Transmisión de servidor:** debe subir al menos una copia, lo cual tarda:$F/u_s$
- **Cliente:** cada cliente debe descargar la copia de una archivo, lo cual minimamente tarda: $F/d_{min}$. Como agregado cada cliente debe poder subir NF bits donde la tasa de subida maxima es de $u_s + \sum{u_i}$.

De esta forma el tiempo para distribuir F a N clientes usando enfoque P2P nos queda como: $$D_{P2P}\ge \max({F/u_s}\space ,{F/d_{min}}\space,NF/(u_s+\sum{u_i}))$$
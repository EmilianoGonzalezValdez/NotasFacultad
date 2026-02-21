**Relación proveedor-consumidor:** Supongamos que tenemos un PSI cliente o (PSI consumidor) y un PSI proveedor. El PSI cliente paga al PSI proveedor para entregar paquetes a otros destinos y recibir paquetes enviados de otros destinos.
- Tipos de rutas que publica el PSI proveedor: El PSI proveedor debe dar publicidad de rutas a todos los destino en internet al PSI cliente sobre el enlace que los conecta, así el PSI cliente va a tener rutas para enviar paquetes para todos lados
- Tipos de rutas que publica el PSI consumidor: El PSI cliente debe publicar rutas a los destinos en su red al PSI proveedor. Esto permite al PSI proveedor enviar tráfico al PSI cliente solo para esas direcciones

**Relación de compañerismo:** los PSI compañeros no se cobran por mandarse mensajes entre sus destinos.
- Tipos de rutas que publica un PSI a sus compañeros: Los SA compañeros mandan publicidad de enrutamiento de uno al otro para los destinos que residen en sus redes. El compañero no es transitivo

*Multihoming* significa que un PSI está conectado con varios PSI. Esta técnica es usada para mejorar la confiabilidad, por si el camino por uno de los PSI falla
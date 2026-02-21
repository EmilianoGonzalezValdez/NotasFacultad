Es necesario estudiar los protocolos de puerta de enlace exterior (PPEE) porque:
- Las tablas de reenvío deben permitir mandar mensajes entre máquinas concetadas a SA diferentes. El PPEE permite agregar información a ser usada con ese fin a las tablas de reenvió de los enrutadores.
- El enrutamiento de PPEE se preocupa de establecer las rutas a usar (que pasan por diferentes SA) para permitir que se comuniquen máquinas pertenecientes a distintos SA

Hay que tener en cuenta que PPEE es diferente a un protocolo intra-SA debido a que para el enrutamiento intra-SA encontrar un camino óptimo es imposible en la practica. ¿Por qué?.
Debido a que cada SA corre su propio protocolo interno y usa cualquier esquema para asignar métricas a los caminos. Por lo tanto es imposible calcular costos de caminos significativos para caminos que cruzan varios SA

Debido a que no se puede manejar información de caminos óptimos, el enrutamiento inter-SA nos va a permitir avisar alcanzibilidad de prefijos desde un SA, y considerar caminos formados por SAs para ir de un origen a un destino
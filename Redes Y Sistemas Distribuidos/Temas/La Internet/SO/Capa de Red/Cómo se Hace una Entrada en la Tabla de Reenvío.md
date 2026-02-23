¿Cómo un enrutdor hace una entrada en la tabla de reenvío de un prefijo x perteneciente a otro SA?
Solución:
1. La tabla RIB contiene la ruta óptima R al prefijo x a considerar para la tabla de reenvío
2. Determinar el puerto de salida del enrutador para el prefijo x:
- Usar OSPF para encontrar la mejor ruta intra-SA que lleva a NEXT_HOP de R
- El enrutador identifíca el puerto de salida del enrutador para esa mejor ruta
3. Ingresar el puerto del prefijo en la tabla de reenvío
La tabla de reenvío se **sincroniza continuamente** con la RIB para reflejar cambios en la topología o en las rutas

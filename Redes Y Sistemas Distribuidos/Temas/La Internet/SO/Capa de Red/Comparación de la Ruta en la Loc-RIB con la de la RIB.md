Las *rutas iBGP* son las rutas intercambiadas entre enrutadores que pertenecen al mismo sistema autónomo.
Las *rutas eBGP* son las rutas intercambiadas entre enrutadores que pertenecen a diferentes sistemas autónomos.
Las *rutas estáticas* son rutas configuradas manualmente por el administrador de red en cada enrutador. Estas indican explicitamente el camino que deben seguir los paquetes hacia una red destino, especificando el siguiente salto o la interfaz de salida. No cambian automaticamente, si hay un cambio en la tipología, el administrador debe actualizar las rutas manualmente.
Las *rutas IGP* son rutas aprendidas automáticamente mediante protocolos de enrutamiento internos al sistema autónomo.

El criterio usado para comparar una ruta en la Loc_RIB con la ruta existente en la RIB es la distancia administrativa y la métrica del protocolo.
La *distancia administrativa* es un valor que indica la preferencia relativa entre rutas aprendidas por diferentes protocolos. Por ejemplo las rutas eBGP tienen una distancia administrativa por defecto de 20, las rutas iBGP de 200, y las rutas estáticas o IGPs tienen otros valores.
La ruta con menor distancia administrativa se prefiere para instalarse en la RIB y usarse para el reenvío
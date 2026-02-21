Un *sistema autónomo* (SA) consiste de un grupo de enrutadores bajo el mismo control administrativo. A menudo los enrutadores de un proveedor de servicios de internet (PSI) y los enlaces que los interconectan constituyen un SA. A veces un PSI divide su red en varios SA. Los enrutadores dentro de un SA corren el mismo algoritmo de enrutamiendo llamado *protocolo de enrutamiento intra-SA*

*Internet* es un conjunto de SAs. En internet los SA están numerados, cada uno con un número que lo identifica

¿Por qué se necesita definir un protocolo intra-SA especial para internet?. Razones:
- Los protocolos de enrutamiento estudiados no son compatibles con IP por la forma de las tablas de enrutamiento que se usaban.
- Los protocolos de enrutamiento anteriores no son adecuados cuando un SA es demasiado grande (se hace pesado consultar y actualizar las tablas de enrutamiento)
- El modelo de grafo para los protocolos de enrutamiento vistos no es adecuado cuando se trabaja con IP (los destinos son subredes con prefijo en lugar de enrutadores)
- A veces hay más de un camino más corto a un destino y no se saca provecho de esta situación para balancear la carga que tiene un enrutador


Para ello en 1988 se definió *OSPF (Open Shortest Path First):*
- Es un *protocolo de puerta de enlace interior (IGP)* - OSPF trabaja dentro de un SA
- Ahora la mayoría de vendedores de enrutadores lo apoyan
- Supera los problemas anteriores
- OSPF considera una adaptación del método de *enrutamiento de estado de enlace*

**¿Por qué estudiar OSPF?**
Porque OSPF introduce mejoras interesantes al protocolo de enrutamiento de estado de enlace:
- Es compatible con IP
- En OSPF el modelo de grafo asociado a una SA es bastante más flexible que el usado para los protocolos de enrutamiento anteriores al considerar redes de distintos tipos 
- Para permitir SA grandes OSPF organiza un SA como una jerarquía de niveles
- Con OSPF para un destino se puede considerar más de una línea de salida (cuando hay más de un camino óptimo) para balancear la carga en la red 
Estas mejoras introducen problemas nuevos para diseñar un algoritmo de enrutamiento 

**Aprenderemos:**
1. Organización de los sistemas autónomos en OSPF. Para entender cómo se organiza un SA autónomo jerárquicamente y cómo esto da lugar a distintos tipos de enrutadores
2. Estructura de redes soportadas por OSPF. Para entender tipos de redes soportadas por OSPF y cómo se combinan entre si
3. Distintos tipos de avisos de estado de enlace. Para entender cómo la estructura jerárquica de un SA fuerza a ocultar la información, lo que da a lugar a distintos tipos de avisos de estado de enlace
4. Adaptación del algoritmo de estado de enlace en OSPF. Para comprender los cambios necesarios a hacer al algoritmo de estado de enlace para contemplar la estructura jerárquica de los SA y la distribución de carga entre varios caminos (de mejor costo) hacia un destino
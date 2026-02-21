Cuando crece mucho el tamaño de las subredes, también lo hacen las tablas de enrutamiento.
Estas tablas consumen memoria del enrutador, necesitan más tiempo de CPU para examinarlas en base a que tan grandes son


¿Cómo hacer para que las tablas de enrutamiento no crecan demasiado cuando crece mucho el tamaño de la subred?
La solución a esto se llama *enrutamiento jerárquico:*
- Los enrutadores se dividen en *regiones*
- Un enrutador sabe cómo enrutar paquetes a destinos de su región
- Tambien sabe cómo enrutar a otras regiones
- Pero no sabe nada de la estructura interna de las regiones en las que no está

El precio a pagar del enrutamiento jerárquico es una longitud de ruta mayor, de esta forma no podemos aspirar a encontrar la mejor ruta

Las tablas de enrutamiento jerárquico se presentan por tener una columna para el host destino, una para la linea por la que se va a enviar el paquete y una para la cantidad de "hops" que se necesitan para llegar. De esta forma tenemos entradas para todos los enrutadores locales, y entradas para las demás regiones en las que no está el enrutador

Aun asi en las redes enormes, una jerarquía de dos niveles es insuficiente; la solución para esto es agrupar las regiones en clústeres, los clústeres en zonas, las zonas en grupos, etc.
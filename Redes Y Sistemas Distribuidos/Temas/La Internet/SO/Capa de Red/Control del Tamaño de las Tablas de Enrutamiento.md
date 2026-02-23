Hasta aquí se ponen los prefijos de todas las subredes en tablas de reenvío, lo cual hace que las tablas de reenvío crezcan demasiado

Para evitar que las tablas de reenvío crezcan demasiado, se combinan varios prefijos en un prefijo único más grande (conocido como superred). A esto se le llama *agregación de prefijos*

**A distintas regiones geográficas se asignan distintos espacios de direcciones. Esto se puede aprovechar en la agregación de prefijos:**
La idea seria combinar prefijos de varias redes que están en una misma región geográfica en un prefijo para un enrutador que está en otra región alejada.


Cuando se usa agregación de prefijos, éste es un proceso automático. La agregación de prefijos es fuertemente usada en el internet y puede reducir el tamaño de las tablas de los enrutadores en alrededor de 200.000 prefijos.

**Esta idea de agregación de prefijos no interfiere con redes más chicas que no fueron agregadas  que caen en bloques agregados**. Esto debido a que los paquetes son enviados en la dirección de la ruta más específica o el prefijo más largo a cazar (longest matching prefix). El trabajar de este modo provee flexibiidad


Ejemplo de agregación de prefijos:
- 192.168.1.0/24
- 192.168.2.0/24
- 192.168.3.0/24

Debemos busacar la mayor cantidad de bits iguales en las 3 direcciones desde la izquierda hacia la derecha. En este caso, si pasamos a binario vamos a ver que los primeros 22 bits coinciden. Por lo cual para representar la nueva agregación se usa la dirección: 192.162.0.0/22
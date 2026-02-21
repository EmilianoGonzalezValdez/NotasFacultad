Requerimos un algoritmo de enrutammiento que se adapte a cambios en la topología y el trafico de la red.

La idea es que al usar el algoritmo de Dijkstra periódicamente y cada vez que cambia la topología en la red, se va a tener en cuenta la topología y el tra¿áfico. En cada una de esas veces se necesita conocer la topología de la subred y los retardos de las líneas.
El algoritmo de enrutamiento de estado de enlace implementa esta idea

**Enrutamiento de estado de enlace (Link state routing-LSR):**
- En cada enrutador usar *algoritmo de Dijkstra* para encontrar la ruta más corta de un enrutador a los demás enrutadores
- La topología y retardos en las líneas se distribuyen a cada enrutador.
- Este algoritmo es valioso porque responde rapido frente a cambios en la topología de la red y es amplicamente usado en internet (como parte del protcolo OSPF)
- **¿Que tareas debe hacer un enrutador LSR?**
1. Descubrir sus vecinos
2. Medir el costo a cada uno de sus vecinos
3. Construir un paquete diciendo lo que ha aprendido
4. Enviar este paquete a todos los demás enrutadores
5. Computar el camino más corto a cada uno de los otros enrutadores

Para averiguar quiénes son los vecinos de un enrutador se envía un *paquete hello* a cada línea punto a punto. Se espera que el enrutador del otro extremo regrese una respuesta indicando quién es


Para que un enrutador conozca el retardo hasta sus vecinos se puede enviar un paquete ECHO especial a través de la linea. Una vez que llegue al otro extremo, éste debe regresarlo inmediatamente. Se usan temporizadores para medir el tiempo, normalmente midiendo el tiempo de ida y vuelta y se divide por 2.
El único problema de este metodo es que asume implícitamente que los retardos son simétricos

Cada enrutador construye un *paquete de estado de enlace (LSP)* que contiene:
- Identidad del emisor (para saber de quien se trata)
- Número de secuencia (para distinguir entre distintos LSP de un enrutador)
- Edad
- Lista de <vecino, retardo al vecino>

Los LSP se contruyen a intervalos irregulares. Normalmente construirlos cuando ocurra un evento significativo, como la caída o la reactivación de la línea o de un vecino, o el cambio apreciable de sus propiedades

Para la **Distribución confiable de los LSP** se utiliza inundación, pero se lleva *registro de los paquetes difundidos*.
- Cada paquete contiene un *Número de secuencia* que se incrementa con cada paquete nuevo enviado. Los enrutadores llevan el registro de todos los pares <enrutador de origen, secuencia> que ven.

Cuando llega un LSP a un enrutador, si es nuevo (nuevo número de secuencia mayor que los anteriores) se reenvia a través de todas las líneas, excepto aquella por la que llegó.
Si es un duplicado (número de secuencia mayor visto, pero repetido) se descarta.
Si llega un paquete con número de secuencia menor que el mayor visto hasta el momento, se rechaza como obsoleto debido a que el enrutador tiene datos más recientes.

Se puede construir la tabla de enrutamiento de un enrutador una vez que el enrutador ha acumulado un grupo completo de paquetes de estado del enlace.
Primero usando los LSP construir el grafo de la subred completa. Cada enlace se representa dos veces, una para cada dirección. Los dos valores pueden promediarse o usarse por separado.
Se ejecuta el algoritmo de Dijkstra para construir la ruta mas corta a todos los destinos posibles.
Con los resultados del mismo se actualiza la tabla de enrutamiento

El algoritmo de inundación de paquetes de estado de enlace tiene algunos problemas que mencionamos a continuación:

**Primer problema:** Si los números de secuencia vuelven a comenzar, reinará la confusión. La solución es usar un número de secuencia de longitud suficiente para que el problema anterior no suceda. Por ejemplo 32 bits

**Problema 2:** Si llega a corromperse un número se secuencia y se escribe 65540 en lugar de 4 (un error de un bit), los paquetes 5 a 65540 serán rechazados como obsoletos, dado que se piensa que el número de secuencia actual es 65540. Para solucionar esto, como protección contra los errores en las líneas enrutador-enrutador, se confirma la recepción de todos los paquetes de estado del enlace. Antes de actualizarse el número de secuencia más grande, el enrutador manda una confirmación de recepción al transmisor y luego espera una respuesta afirmativa o negativa del transmisor. En el primer caso se actualiza el número de secuencia mas grande, en el segundo caso se descarta el paquete que se recibió por estar errado

**Problema 3:** Si llega a caerse un enrutador (de origen), perderá el registro de su número de secuencia. Si comienza nuevamente en 0, se rechazará el siguiente paquete.
Para solucionarlo, la información de los enrutadores sólo expira (a lo largo de la red) cuando el enrutador está caido

**¿Cuando se puede detectar que un enrutador está caído?**
Cuando se actualicen las tablas de enrutamiento y se manden los paquetes Hello.

Una vez identificado que enrutador está caído se hace lo siguiente:
- Se propaga la información de este hecho por toda la red.
- Se hace que la información asociada al enrutador caído expire (paquetes pendientes a enviar, número de secuencia más grande recibido, etc.)
- Así que cuando ese enrutador vuelva a la vida, puede comenzar con número de secuencia 0

**Problema 4:** ¿Cómo hacer para asegurar que no pueda perderse ningún paquete y sobrevivir durante un período indefinido?
Para ello se debe incluir un campo de *edad en cada paquete* tal que:
- Se disminuye la edad una vez cada segundo
- Los enrutadores también decrementan el campo edad durante el proceso inicial de inundación
- Se descarta el paquete cuya edad sea 0

Para hacer el algoritmo de inundación de paquetes más eficiente:
- Una vez que un paquete de estado del enlace llega a un enrutador para ser inundado, no se encola para transmisión inmediata. En vez de ello, entra en un *búfer de almacenamiento* donde espera un tiempo breve.
Sia ntes de transmitirlo, llega otro paquete de estado del enlace proveniente del mismo origen, se comparan sus números de secuencia. Si son iguales se decarta el duplicado, si son diferentes se desecha el más viejo


El *buffer de paquetes para un enrutador* contiene una celda por cada paquete de estado de enlace recién llegado, pero aún no procesado por completo.
Una fila de la tabla del búfer de paquetes de un enrutador contiene:
- Origen del paquete, número de secuencia, edad, datos de los estados de enlaces.
- Puede tener ciertas *Flags* o *banderas* como:
- 	Banderas de confirmación de recepción: indica a dónde tiene que enviarse la confirmación de recepción del paquete
- 	Banderas de envío: significan que el paquete debe enviarse a través de las líneas indicadas.
- 	Si llega un duplicado mientras el original aún está en el bufer, los bits de las banderas tienen que cambiar

El número de secuencia y edad son usados para inundación confiable.
Los paquetes LSP nuevos son confirmados en las líneas que son recibidos y enviados por todas las demás lineas
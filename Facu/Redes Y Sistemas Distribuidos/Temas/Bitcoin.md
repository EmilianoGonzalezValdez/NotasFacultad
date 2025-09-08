
# Bitcoin



## ***Caracteristicas de Bitcoin***

- **Blockchain Publica:** Cualquiera puede unirse a la red, ejecutar un nodo y verificar transacciones

- **Permissionless:** No requiere permisos para participar como usuario, minero o nodo

- Usa el mecanismo de **PoW**

- **Oferta Limitada:** Solo habra 21 millones de bitcoins

- Las transacciones normalmente duran minutos

- **Estructura de Incentivos:** Los mineros reciben recompensas en BTC y tarifas de transaccion para mantener la red segura y operativa

- **Tiempo de bloque:** Aproximadamente 10 minutos para minar un nuevo bloque


Bitcoin utiliza una **Función Hash**, la cual es un algoritmo matemático que transforma datos de entrada de longitud variable en una cadena alfanumerica fija y única, conocida como código hash



*Propiedades de una función hash:*

- **Determinismo:** UNa función de hash produce siempre el mismo resultado para una entrada dada

- **Eficiencia:** Las funciones de hash deben ser rápidas para calcular

- **Resistencia a colisiones:** Es prácticamente imposible encontrar dos entradas diferentes que produzcan el mismo código de hash



SHA-256 es un tip especifico de función hash criptografica que se usa en Bitcoin y produce un código de hash de 256 bits

Para generar una direccion pública la calve publica pasa por dos funciones hash secuenciales. Esto produce un hash que luego es codificado en Base58Check para crear una cadena alfanumerica. Cada bloque y transaccion en la red se identifica mediante un hash SHA-256 único

En bitcoin SHA-256 se aplica a los datos de la transaccion para crear un hash único que representa la transaccion especifica. Cada bloque contiene en su encabezado el hash SHA-256 del bloque anterior y el Merkle Root

**Mineria de Bitcoin:**

1. Los mineros agrupan transacciones pendientes en un bloque candidato

2. Se crea el encabezado del bloque, el cual, tiene el hash del bloque anterior, la raiz de Merkle, marca de tiempo actual y el nonce, el cual es un número de 32 bits que se modifica repetidamente durante el proceso de mineria

3. Se aplica el algotirmo SHA-256 dos veces al encabezado del bloque

4. Si el hash obtenido no cumple con los requisitos de dificultad establecidos por la red, el nonce se incrementa aleatoriamente y se repite el proceso hasta encontrar un hash valido

5. Una vez encontrado un hash válido el minero difunde el nuevo bloque a la red

6. Los nodos verifican el trabajo realizado y añaden el bloque a la blockchain

7. Los otros nodos mineros que estaban tratando de crear sus bloques válidos pierden el trabajo realizado hasta el momento

8. El minero recibe una **recompensa** en bitcoins por su trabajo, así como las **tarifas de las transacciones** incluidas en el bloque

Para ser valido el hash encontrado durante la minería debe cumplir que el doble has SHA-256 del bloque completo debe tener un número específico de ceros iniciales. Esta cantidad de ceros se ajusta periódicamente, aprox cada 2 semanas/2016 bloques, para tener el tiempo de generación de bloques cercano a 10 minutos. Mientras mas ceros se requieran mayor será la dificultad y mas trabajo computacional será necesario para encontrar un hash valido



**Problema:** Si dos nodos mineros generan un bloque valido al mismo tiempo ¿Coḿo evitar que generen blockchains diferentes?

Para ello se usan **firmas digitales** las cuales se generan en función de los datos de transacción, siendo esta firma, única para cada transacción



**Caracteristicas del Bitcoin:**
- *Blockchain pública:* cualquiera puede unirse a la red, ejecutar un nodo y verificar transacciones
- *Permissionless:* no requiere permisos para aprticipar como usuario, minero o nodo
- Usa el mecanismo de consenso *Proof of Work*
- *Oferta limitada:* solo habra 21 millones de bitcoins
- Las transacciones suelen resolverse en minutos, aunque puedan tardar más dependiendo de la congestión de la red
- *Estructura de incentivos:* Los mineros reciben recompensas en BTC y tarifas de transacción para mantener la red segura y operativa
- *Tiempo de bloque:* aproximadamente 10 minutos en promedio para minar un nuevo bloque

**Servicios provistos:**
- *Transferencia de valor:* permite enviar y recibir bitcoins de manera rapida y segura entre pares P2P, sin intermediarios como bancos
- *Almacenamiento de valor:* debido a su oferta limitada y sus eguridad, Bitcoin es considerado como una reserva de valor similar al oro
- *Pagos internacionales:* facilita pagos internacionales con menores costos y tiempos de procesamiento comparado con los métodos tradicionales
- *Seguridad y verificación de transacciones:* usa un sistema público y transparente para evitar fraudes y dobles gastos
- *Bitcoin script:* soporta contratos inteligentes básicos a través de su lenguaje de scripting, aunque con restricciones para mantener la seguridad

Un bloque tiene un tamaño máximo que por ahora es de 1MB, lo cual limita la cantidad de transacciones por bloque. Cada usuario tiene un par de claves:
- *Clave privada* secreta: Se genera un número aleatorio de 256bits que es dificil de adivinar. Generalmente las billeteras digitales generan esta clave privada
- *Clave pública* compartida en la red: Se aplica una formula matematica a la clave privada para generar la clave pública correspondiente. Generalmente se usa para ello el algoritmo ECDSA(Elliptic curve digital signature algorithm)

Para garantizar que se cumplan los siguientes requisitos:
- *Integridad:* hay que garantizar que los datos no han sido alterados
- Es necesario generar *direcciones de Bitcoin* que son una forma de identificar las cuentas para poder enviar y recibir bitcoins
- Proteger la red contra ataques y asegurar la *confidencialidad de los datos*
- Hace falta un *mecanismo para validar* que los mineros han realizado una cantidad significativa de trabajo computacional antes de añadirse un nuevo bloque a la blockchain

Se utiliza una función de hash, la cual es un algoritmo matematico que transforma datos de entrada de longitud variable en una cadena alfanumerica fija y única, conocida como código hash. Esta función tiene como propiedades:
- *Determinismo:* una función hash produce siempre el mismo resultado para una entrada dada
- *Eficiencia:* las funciones de hash deben ser rápidas para calcular
- *Resistencia a colisiones:* es prácticamente imposible encontrar dos entradas diferentes que produzcan el mismo código de hash.

La función hash que usa bitcoin es la **SHA-256 (secure hash algorithm 256)**, la cual es un tipo especifico de funcion hash criptografica que produce un código de hash de 256 bits

Para *generar una dirección pública* la clave pública pasa por dos funciones hash secuenciales. Primero SHA-256 y luego RIPEMD160, lo cual produce un hash que luego es codificado en Base58Check para crear una cadena alfanumerica.
Cada bloque y transacción en la red Bitcoin se identifica mediante un hash SHA-256 único

En bitcoin SHA-256 se aplica a los datos de la transacción para crear un hash único que representa esa transacción especifica. Cada bloque contiene en su encabezado el hash SHA-256 del bloque anterior. El encabezado de un bloque además contiene el Merkle Root:
- Las transacciones en un bloque se organizan en pares y se aplica SHA-256 a cada par para crear un hash
- Este proceso se repite, combinando y volviendo a hashear los resultados, hasta que queda un único hash llamado Merkle Root

**Minería de Bitcoin:** Así se usa SHA-256 en la minería de Bitcoin:
1. Los mineros agrupan las transacciones pendientes en un bloque candidato
2. Se crea el encabezado del bloque. El mismo contiene el hash del bloque anterior, raiz de Merkle, marca de tiempo actual, nonce. Este ultimo es un número de 32 bits que se modifica repetidamente durante el proceso de mineria, normalmente comienza desde 0
3. Se aplica el algoritmo SHA-256 dos veces al encabezado del bloque
4. Si el hash obtenido no cumple con los requisitos de dificultad establecidos por la red, el nonce se incrementa aleatoriamente y se repite el proceso hasta encontrar un hash valido. Para que un hash sea valido el doble hash SHA-256 del bloque completo debe tener un npumero específico de ceros iniciales. Dicha cantidad se ajusta periódicamente, manteniendo el tiempo de generación de bloques cercano a 10 minutos. Cuantos más ceros se requieren, mayor será la dificultad y más trabajo computacional será necesario para encontrar un hash válido

Una vez encontradoun hash valido, el minero *difunde el nuevo bloque* a la red. Los nodos verifican el trabajo realizado y *añaden* el bloque a la blockchain. Los otro nodos mineros que estaban trtando de crear sus bloques válidos pierden el trabajo realizado hasta ese momento. El minero recibe una recompensa en bitcoins por su trabajo, así como las tarifas de las transacciones incluidas en el bloque.

Una situación problematica es cuando dos nodos mineros generan un bloque válido al mismo tiempo. ¿Como evitar que se generen blockchains diferentes?. Bueno pues diferentes nodos reciben uno u otro bloque y lo añaden a su copia local de la blockchain. El siguiente minero en encontrar un bloque válido lo añadira a la cadena que está usando. La cadena que se extiende más rápido se convierte en la principal. El bloque que no fue extendido se convierte en un bloque huerfano y es descartado. Los nodos que tenían la cadena mas corta abandonan esa cadena y se pasan a la cadena mas larga. El minero cuyo bloque se convierte en huerfano no recibe la recompensa por su trabajo.

Ahora veremos como garantizar:
- *Autenticidad:* hay que verificar que una transacción ha sido enviada por la persona que afirma haberla enviado
- *Integridad:* hay que asugirar que las transacciones no han sido alteradas desde que fueron creadas
- *No repudio:* imposibilitar a los creadores de las transacciones puedan negar haberlas hecho
- *Seguridad:* proveer protección contra falsificaciones y otros tipos de ataque
- *Verificación descentralizada:* cualquier participante de la red debe poder verificar la validez de las transacciones

La solución a estos requerimiento es el uso de *firmas digitales*, donde una de estas se genera en función de los datos de una transacción, siendo unicas para cada transacción. 
La clave privada del ususario es usada para firmas transacciones y demostrar la propiedad de los bitcoins. La clave pública se usa para verificar la firma.
El remitente crea un hash de la transacción y lo cifra con su clave privada, produciendo la firma digital.
*Verificación de la firma:* los nodos de la red utilizan la clave pública del remitente para descifrar la firma y comparar el hash resultante con el de la transacción, si coinciden, la firma es válida.

¿Como esto ayuda al cumplimiento de los requisitos?
- *Autenticidad:* solo el propietario de una clave privada correspondiente a una clave pública puede generar una firma válida
- *Integridad:* si los datos de la transacción se modifican en cualquier forma luego de la firma, la firma se vuelve invalida
- *No repudio:* una vez que el firmante ha creado la firma no puede negar haberlo hecho, ya que solo su clave privada podría haber creado esa firma específica
- *Seguridad:* se usa un proceso llamado ECDSA que usa matematicas avanzadas de curvas elípticas para crear la firma digital
- *Verificación descentralizada:* cualquier nodo de la red puede usar la clave pública del firmante para verificar la fírma de la transacción

**Ejemplo de proceso de firma digital en Bitcoin:**
1. Alice quiere enviar 1 bitcoin a bob, entonces Alice crea una transacción
2. Alise usa su clave privada para generar una firma digital de la transacción
3. Alice transmite la transacción firmada a la red bitcoin
4. Los nodos de la red usan la clave pública de Alice para verificar la firma digital y asegurarse que la transacción no ha sido alterada y que Alice es la legítima propietaria de los fondos.

**Tipos de nodos:**
- *Nodos completos:* validan y transmiten transmisiones y bloques. Mantienen copia completa de la blockchain
- *Nodos mineros:* crean nuevos bloques a través de la mineria
- *Nodos ligeros:* verifican transacciones usando información resumida. Obtienen información necesaria de nodos completos. Consultan saldos, envían y reciben BTC
- *Supernodos:* actúan como hubs de alta capacidad, conectandose a muchos otros nodos y facilitando la distribución de datos

**Escenario 1: envío y validación de una transacción:**
1. *Usuario:* envía transacción a nodo completo
2. *Nodo completo:* verifica la validez de la transacción recibida, luego difunde la transacción a otros nodos completos y supernodos
3. *Supernodo:* retransmite la transacción recibida de nodo completo a muchos otros completos y ligeros a los que está conectado
4. *Nodo logero:* recibe transacción de supernodo, la verifica usando información resumida, si la verificación es exitosa, la acepta
5. *Nodo minero:* recibe la transacción del nodo completo o supernodo. Incluye la transacción en un bloque candidato y empieza a minar
6. *Nodo completo y supernodo:* continúan propagando a otros nodos en la red hasta que todos la hayan recibido

Los nodos mineros y completos transmiten una transacción a sus nodos vecinos.


**Escenario 2: Minería y propagación de un nuevo bloque:**
1. *Nodo de mineria:* Resuelve problema criptografico y crea un nuevo bloque con las transacciones recientes. Difunde el nuevo bloque a un nodo completo
2. *Nodo completo:* verifica la validez del bloque recibido. Si el bloque es válido, lo agrega a su blockchain. Difunde el bloque a otros nodos completos y sepernodos
3. *Supernodo:* recibe y verifica bloque que recibió del nodo completo, y si todo está bien lo añade a su copia de la blockchain. Retransmite el bloque a muchos otros nodos completos y ligeros a los que está conectado
4. *Nodo ligero:* recibe bloque del supernodo y verifica el bloque usando la cabecera del mismo y la cadena de bloques resumida. Si es valido, almacena su información resumida

**Escenario 3: respuesta a un ataque de doble gasto:**
1. *Usuario malicioso:* envía dos transacciones conflictivas a diferentes nodos completos
2. *Nodo completo 1:* recibe la primera transacción y la verifica. Difunde esa transacción a otros nodos completos y supernodos
3. *Nodo completo 2:* recibe la segunda transacción conflictiva y la verifica. Detecta el conflicto con la primera transacción y no la difunde
4. *Supernodo:* recibe la primera transacción válida del nodo completo 1 y le difunde a otros nodos
5. *Nodo de minería:* recibe la primera transacción válida y la incluye en un bloque candidato. Si la segunda transacción llega después de la primera y detecta el conflicto y la rechaza

Se asume que el usuario malicioso demora bastante entre la primera transacción y la segunda. Si esto no fuera cierto, podria pasar que dos mineros generan bloques en simultaneo con las dos transacciones diferentes. En este caso el escenario se complica, pero hay solución
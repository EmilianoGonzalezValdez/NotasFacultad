La capa de protocolo base es la blockchain en si misma. Tiene su propia cadena de bloques con un diseño especifico, incluyendo su propio token nativo. Es responsable de la seguridad y el funcionamiento operativo de la red blockchain. Establece las reglas fundamentales de consenso y la estructura de datos principal. Facilita la comunicación entre nodos y el envío de transacciones. 
Es en esta capa donde se llevan a cabo las transacciones.

Un **mecanismo de consenso** establece las reglas y mecanismos mediante los cuales los nodos llegan a un acuerdo sobre el estado del libro mayor. Sus beneficios son:
- Usar mecanismo de consenso previene problemas como el doble gasto al garantizar que solo una versión del libro mayor sea aceptada por todos los nodos
- Usar mecanismos de consenso aumenta la resistencia a ataques maliciosos al requerir que un número significativo de nodos coincida en el estado del sistema. Algunos ejemplos de protocolos en esta capa son:
	- Bitcoin
	- Ethereum
	- Cardano
	- Solana

Las blockchains en esta capa suelen enfrentar limitaciones en su capacidad para procesar un gran número de transacciones por segundo, lo cual puede resultar en tiempos de espera prolongados y tarifas elevadas, especialmente en períodos de alta demanda. Para resolver esto se definen soluciones de escalabilidad.


## Explicación de la capa en mas detalle

Asumimos que hay un *registro de transacciones*. Veremos ciertos *requisitos a alcanzar* por el sistema en lo que se refiere al registro. Luego veremos que usar cadenas de bloques es una **solución**

**Requisitos:**
- *Registro de transacciones:* capacidad de almacenar transacciones
- *Consistencia del estado del sistema:* todos los participantes deben tener una visión unificada del estado actual del sistema
- *Descentralización:* queremos que el registro opere sin una autoridad central que controle el sistema
- *Inmutabilidad:* una vez que las transacciones se agregan al registros, no pueden ser modificados ni eliminados
- *Seguridad:* los datos del registro deben estar protegidos contra alteraciones y accesos no autorizados
- *Transparencia:* todos los participantes deben poder ver y verificar las transacciones y los datos en el registro
- *Consenso:* los nodos de la red deben acordar la validez de grupos de transacciones antes de agregarlas al registro
- *Escalabilidad:* el registro debe ser capaz de manejar un número creciente de transacciones y nodos sin una disminución significativa en el rendimiento
- *Rendimiento:* el tiempo de procesamiento de las transacciones y la actualización del registro debe ser eficiente
- *Resiliencia:* el sistema debe ser robusto y capaz de recuperarse rapidamente frente a fallas o ataques
- *Privacidad:* debe garantizarse la confidencialidad de ciertos datos y transacciones cuando sea necesario

La solución a dichos requisitos es usar una cadena de bloques (blockchain):
- Es una estructura de datos descentralizado y cronologica que almacena información en forma de bloques.
- Cada bloque contiene un conjunto de transacciones
- Se tiene una red de nodos distribuidos donde cada nodo tiene una copia completa de la blockchain
- El *hash de un bloque* es un identificador único del bloque generando mediante un algoritmo criptografico. Funciona como una huella digital del bloque y cambia si se modifica cualquier dato del bloque. Un hash hace extremadamente dificil alterar un bloque sin ser detectado
- Los bloques de una cadena de bloques están enlazados mediante *hashes*. Cada bloque contiene el hash del bloque anterior
- Todos los participantes pueden ver los bloques de la blockchain
- Se usan *mecanismos de consenso* para asegurar que los nodos acuerden la validez de los nuevos bloques
- **Estructura de un bloque:**
- 	*Encabezado del bloque:* contiene metadatos cruciales para la integridad y verificación
- 	*Cuerpo del bloque:* almacena las transacciones realizadas
- 	*Hash del bloque:* generado a partir de todos los datos contenidos en el bloque. Este hash garantiza que cualquier cambio resultaria en un nuevo valor completamente diferente, protegiendo así la integridad e inmutabilidad del registro de la blockchain
- **Encabezado del bloque:**
- 	*Hash del bloque anterior*
- 	*Merkle Root:* es un hash que resume todas las transacciones dentro del bloque
- 	*Nonce:* número aleatorio usado durante el proceso de minería para encontrar un hash valido
- 	*TimeStamp:* marca temporal indicando cuando se creo el bloque

**Como se logran los requisitos:**
- *Distribución:* uso de varios nodos con copia de blockchain
- *Inmutabilidad:* los bloques no pueden alternarse una vez agregados a la blockchain, cualquier cambio sería detectable porque alteraria el hash del bloque
- *Transpariencia:* todas las transacciones son visibles públicamente
- *Consenso:* por medio de los mecanismos de consenso
- *Rendimiento:* la eficiencia en la creación de bloques y la validación de transacciones depende de la impelmentación y su algoritmo de consenso
- *Privacidad:* se pueden implementar mecanismos para la privacidad como transacciones confidenciales
- *Escalabilidad:* es un desafío por eso se desarrollaron soluciones de escalabilidad y otras tecnologías
- *Seguridad:* se emplean algoritmos criptograficos para proteger los datos y las transacciones.
- 	Además el uso de mecanismos de consenso como proof-of-work o proof-of-stake asegura que se necesita una cantidad significamente de recursos para comprometer la red.
- 	La descentralización ayuda, un atacante tendría que comprometer mas del 50% de los nodos
- *Consistencia:* mediante mecanismo de consenso todos los nodos acuerdan que bloque es el siguiente en añadirse a la cadena

**Principales mecanismos de consenso:**
- *Proof of Work(PoW):* hay *nodos mineros* que compiten por resolver problemas criptograficos complejos. El primero en resolverlo valida un bloque y recibe recompensas. Hay un alto costo energetico necesario para alterar bloques. Puede ser lento
- *Proof of Stake(PoS):* hay nodos validadores que son elegidos según su participación en la red. Los nodos validadores verifican si las transacciones dentro de un bloque propuesto son validas y si cumplen con las reglas de la red. Despues de validar las transacciones, los nodos validadores crean nuevos bloques. Cuando un nodo validador propone un bloque nuevo, otros nodos validadores revisan y validan ese bloque. Luego solo los bloques válidos serán propagados por la red y añadidos a la blockchain. Los validadores mantienen una copia de la blockchain. Los validadores reciben recompensas. Tienen mayor consumo enérgetico que PoW. Puede concretar poder entre grandes stakeholders.
- *Delegated Proof of Stake(DPoS):* Los usuarios votan por *delegados* para validar bloques; estos delegados reciben recompensas por su trabajo. Los delegados pueden validar y agregar nuevas transacciones a la blockchain. Esto incluye validación de bloques y confirmación de transacciones. DPoS es rápido y eficiente. Permite votaciones directas por parte del usuario final. DPoS puede ser menos descentralizado si pocos delegados dominan las votaciones.
- *Byzantine Fault Tolerance(BFT):* un *lider* propone nuevos bloques mientras otros nodos verifican su validez antes del consenso generalizado. Luego de la validación, se hace una votación por nodos participantes del consenso para determinar si aceptan o rechazan el bloque propuesto. Para alcanzar el consenso se requiere que mas del 66% de los nodos honestos estén de acuerdo. Existen mecanismos para detectar nodos deshonestos e ignorarlos durante el proceso de consenso. BFT garantiza alta velocidad y tolerancia a fallos bizantinos, incluso con presencia significativa de actores maliciosos. BFT requiere confianza inicial en el líder o estructura jerárquica establecida dentro del sistema

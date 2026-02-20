**Características estructurales de la blockchain:**
- *Estructura descentralizada:* No hay un nodo central que controle la red, hay varios nodos con copias del libro mayor que participan en el proceso de validación de transacciones 
- *Uso de modelo P2P:* Cada nodo se conecta directamente a otros nodos sin intermediarios, por lo que hay una comunicación directa y eficiente entre los participantes 
- *Consenso distribuido:* La red usa mecanismos de consenso para validar transacciones y mantener la integridad del libro mayor (todos los nodos deben llegar a un acuerdo antes de agregar nuevos bloques a la blockchain) 

En una red blockchain hay nodos de distintos tipos que cumplen un conjunto de roles cada uno. Veremos una clasificación de los tipo de estos nodos, aunque normalmente una red blockchain va a tener un subconjunto de todos ellos.

**Tipos de nodos en una red blockchain:**
- *Nodos completos:* Mantienen una copia completa del libro mayor de la blockchain. Son esenciales para la estabilidad y seguridad de la red, ya que validan todas las transacciones y bloques 
- *Nodos ligeros:* No almacenan toda la blockchain, sino solo partes necesarias para verificar transacciones. Son ideales para dispositivos con recursos limitados como los celulares
- *Creadores de bloques:* Participan en el proceso de minera, resolviendo problemas matemáticos complejos para añadir nuevos bloques a la blockchain y recibir recompensas en criptomonedas 
- *Nodos de usuario:* Representan los usuarios finales de la red blockchain, participando en transacciones y validaciones según sus permisos y roles
- *Nodos validadores:* Verifican y validan transacciones y bloques, asegurando que se sigan las reglas de la red
- *Billeteras:* Son nodos que almacenan claves privadas y públicas necesarias para realizar transacciones en la blockchain. Permiten a los usuarios enviar y recibir criptomonedas
- *Autoridades de certificación:* Nodos que emiten y gestionan certificados digitales, asegurando la autenticidad y seguridad de las comunicaciones y transacciones en la red
- *Nodos que ejecutan contrtos inteligentes:* Ejecutan el código de los contratos inteligentes, permitiendo la automatización de acuerdos y transacciones sin intervención humana 
- *Gateways:* Actúan como puertas de entrada entre la blockchain y otros sistemas, facilitando la transferencia de datos y transacciones 
- *Masternodes:* En algunas redes los masternodes tienen funciones adicionales como la ejecución de transacciones anónimas y la gestión de la red
- *Super Nodos:* Son nodos con mayor capacidad y recursos que ayudan a mejorar la eficiencia y velocidad de la red. Pueden comunicarse a muchos otros nodos y facilitar la distribución de datos. También pueden tener su copia de la blockchain
- *Nodos balanceadores de carga:* Distribuyen la carga de trabajo entre diferentes nodos para mejorar la eficiencia y rendimiento de la red 

**Ejemplos de redes blockchain con sus tipos de nodos:**
- *Bitcoin*: nodos completos, nodos mineros, nodos ligeros, super nodos.
- *Ethereum*: nodos completos (además ejecutan contratos inteligentes), nodos ligeros, nodos mineros, balanceadores de carga.
- *Ripple*: nodos validadores, nodos Gateway, nodos usuario
- *Hyperledger fabric*: nodos peer (con completos y ejecutan contratos inteligentes), nodos servicio de ordenamiento (ordenan transacciones y crean bloques que se distribuyen a los nodos peer), autoridades de certificación.

Para cada red blockchain existe la comunicación entre nodos de distintos tipos, la cual es diferente en cada red, por ello saber la comunicación en una blockchain requiere estudiar cada blockchain en particular. Para ello hay que estudiar diferentes casos de uso de la red como una secuencia de mensajes entre nodos de la red. Normalmente las redes blockchain individuales tienen ciertos problemas.
Las aplicaciones descentralizadas que interactúan con varias blockchain se las conoce como dApps y son necesarias por varias razones:
- *Permitir la comunicación y transferencia de datos entre diferentes blockchain* facilita el uso de múltiples servicios y aplicaciones
- *Se pueden usar varias blockchains para almacenar datos y realizar transacciones* incrementando así la seguridad y redundancia. Si una falla los datos seguirán en la otra
- *Permite distribuir la carga de trabajo y transacciones entre diferentes blockchains* reduciendo la congestión 
- *Aprovechan las características únicas de diferentes blockchain*
- *Optimización de costos* debido a que se elige la blockchain mas adecuada para cada transacción 

Existen varios enfoques para manejar mas de una blockchain, pero nosotros veremos 2. **Cosmos y Polkadot** 

**Cosmos (La internet de blockchains)** es una plataforma diseñada para interconectar blockchains de manera eficiente y segura. Para esto se usa el protocolo de comunicación interblockchain (IBC), lo cual permite crear aplicaciones descentralizadas que pueden interactuar con varias blockchain. Cada blockchain en Cosmos es independiente y diferente denominando a cada una como *"zonas"*. Hay nodos centrales que conectan varias zonas y facilitan la conexión entre ellas. También hay nodos clientes que usan la red para enviar y recibir transacciones, consultar datos y ejecutar contratos inteligentes. Por ultimo también hay nodos validadores que participan en el consenso y validan transacciones, estos nodos se conectan con los nodos centrales

Como para realizar contratos inteligentes es necesitan datos externos, del mundo real, se invento el *ChainLink*, el cual conecta datos externos con contratos inteligentes en diversas blockchains a través de nodos que recopilan datos de fuentes externas y los envían a la blockchain denominados *oráculos*. Hay diferentes tipos de oráculos:
- *Oraculo de datos:* recopilan datos de fuentes externas
- *Oraculo de computación:* realizan cálculos complejos que no pueden ser procesados directamente por los contratos inteligentes en la blockchain
- *Oraculo de eventos:* proporcionan información sobre eventos específicos que ocurren fuera de la blockchain como la finalización de un contrato o la confirmación de una entrega
- *Oraculos de procesamiento de pagos:* facilitan la transferencia de valor entre diferentes sistemas, permitiendo pagos entre contratos inteligentes y sistemas externos

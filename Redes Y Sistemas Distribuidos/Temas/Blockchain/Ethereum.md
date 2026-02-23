**Proposito de Ethereum:**
- La red Ethereum fue diseñada para *descentralizar la web* y permitir la creación de *aplicaciones descentralizadas* y contratos inteligentes
- Su objetivo principal es eliminar intermediarios y proporcionar una plataforma transparente, segura y autónoma para transacciones y acuerdos digitales
- Ethereum busca ser la base de la **Web 3.0**, ofreciendo una infraestructura para una internet más abierta y descentralizada.

**Caracteristicas salientes:**
1. *Contratos inteligentes:* códigos autoejecutables que se activan cuando se cumplen condiciones predefinidas. Eliminan la necesidad de confinza entre partes y reducen costos de intermediación
2. *Descentralización:* opera mediante una red global de nodos que validan y registran transacciones sin una autoridad central
3. *Token nativo(ETH):* utilizado como "combustible" para pagar transacciones y ejecutar contratos inteligentes
4. *Máquina Virtual Ethereum(EVM):* proporciona un entorno seguro para ejecutar contratos inteligentes
5. *Inmutabilidad y transparencia:* todas las transacciones y contratos son registrados en la blockchain, lo que los hace verificables y resistentes a alteraciones

**Servicios provistos:**
1. *Desarrollo de DApps:* permite a los desarrolladores crear aplicaciones descentralizadas en áreas como finanzas, juegos y gestión de datos
2. *Tokens personalizados:* facilita la creación de tokens ERC-20 y ERC-721 para representar activos digitales o físicos
3. *Finanzas descentralizadas(DeFi):* plataforma para servicios financieros como prestamos, intercambios y seguros sin intermediarios
4. *Mercados descentralizados:* permite la creación de plataformas de comercio P2P para bienes digitales y físicos
5. *Gestión de identiad y datos:* ofrece soluciones para almacenar y compartir datos de forma segura y descentralizada

El *staking en ethereum* es el proceso mediante el cual los usuarios bloquean una cantidad especifica de Ether para participar en la validación de transacciones y la creación de nuevos bloques en la red. Este mecanismo forma parte del modelo de consenso de *prueba de participación*, que ethereum 2.0 adoptó como alternativa a la prueba de trabajo

En ethereum hay una *máquina virtual de Ethereum(EVM)* cuyo estado es aceptado por todos los participantes de la red de ethereum. Cada nodo de la red de ethereum mantiene una *copia del estado* de la EVM.
Cualquier participante puede enviar una solicitud para que esta EVM realice un cálculo arbitrario. Cuando se transmite una solicitud de este tipo, otros participantes de la red verifican, validan y llevan a cabo el cálculo. Esta ejecución provoca un cambio de estado en la EVM, que se registra y propaga por toda la red. Las solicitudes de cálculo se llaman *solicitudes de transacción*.
El registro de todas las transacciones y el estado actual de la EVM se almacenan en la blockchain.
Todas las transacciones son *firmadas* y ejecutadas con los *permisos adecuados*. Nadie debería poder enviar activos digitales desde la cuenta de una persona P, excepto la propia persona P
Cualquier participante que envíe una solicitud de transacción debe ofrecer una cantidad de ETH a la red como *recompensa*. La red *quemará una parte* de esta recompensa y otorgara el resto a quien finalmente realice el trabajo de verificar a la transición, ejecutarla registrarla en la blockchain y transmitirla a la red. La cantidad de ETH pagada corresponde a los recursos necesarios para hacer el cálculo. Asi, nadie puede bloquear la red con cálculos infinitos


Los desarrolladores de aplicaciones cargan programas en ele stado de la EVM y los usuarios realizan solicitudes para ejecutar estos fragmentos de código con parámetros variados. A estos programas cargados en la red y ejecutados por ella se los llama *contratos inteligentes*. Un contrato inteligente es como un script que cuando se usa con ciertos párametros realiza acciones o cálculos si se cumplen determinadas condiciones.
Cualquier desaroolador puede crear un contrato inteligente y *hacerlo público en la red*, utilizando la blockchain como capa de datos, a cambio de una tarifa pagada a la red.
Cualquier usuario puede luego invocar el contrato inteligente para ejecutar su código, también pagando una tarifa a la red.
Asi, mediante los contratos inteligentes, los desarrolladores pueden crear y desplegar aplicaciones y servicios complejos orientados a los usuarios, como mercados, instrumentos financieros, juegos, etc.
Una vez que un contrato inteligente es desplegado en la red, no se lo puede cambiar. Ser muy cuidadoso al diseñar y testear un contrato inteligente
Una *aplicación descentralizada* combina un contrato inteligente con un frontend conteniendo una interfaz de usuario.
Una dApp tiene su *código backend* funcionando en la red descentralizada de ethereum que es de igual a igual. Ninguna persona tiene el control de ethereum y las dApps se ejecutan en la EVM
Una dApp puede tener *código frontend* e *interfaces de usuario* escritas en cualquier lenguaje para realizar *llamadas a su backend*
Si el contrato tiene un error, no afectara el funcionamiento normal de la red de ethereum

**Cuentas:**
Una cuenta de ethereum es una entidad con un saldo de ether que puede enviar transacciones en ethereum
Las cuentas pueden ser controladas por usuarios o implementadas como contratos inteligentes.
Ehereum tiene dos tipos de cuentas:
- **Cuenta propiedad externa(EOA):** controlada por cualquier persona con las claves privadas
- **Cuenta de contrato:** un contrato inteligente implementado en la red, controlado por código.

Ambos tipos de cuentas tienen la capacidad de recibir ETH y tokens, y de interactuar con contratos inteligentes implementados

Para una **cuenta de propiedad externa:**
- crear una cuenta no tiene costo
- puede iniciar transacciones
- las transacciones entre cuentas de propiedad externa solo pueden ser transferencias de ETH o tokens
- se compone de un par criptografico de claves: *claves públicas* y *privadas* que controlan las actividades de la cuenta

Para una **cuenta de contrato:**
- crear un contrato tiene un costo, ya que utiliza almacenamiento en la red
- solo puede enviar transacciones en respuesta a recibir una transacción
- Las transacciones desde una cuenta externa a una cuenta de contrato pueden activar código que puede ejecutar muchas acciones diferentes como transferir tokens o incluso crear un nuevo contrato
- las cuentas de contrato no tienen claves privadas. En cambio don controladas por la lógica del código del contrato inteligente

Una cuenta tiene un *Nonce*, el cual es un contador y especifica diferentes cosas dependiendo del tipo de cuenta. Si es una cuenta de propiedad externa expresa la cantidad de transacciones enviadas desde ella, y si es una cuenta de contrato expresa la cantidad de contratos creados por ella.
Cada cuenta tiene un balance, que es la cantidad de wei que tiene, habiendo 1e+18 wei por cada ETH.
Las cuentas de contrato tienen *fragmentos de código* programados que pueden realizar diferentes operaciones. Un fragmento de código se ejecuta si la cuenta de contrato recibe una *llamada de mensaje*. Los fragmentos de código están contenidos en una base de datos de estado bajo sus hashes correspondientes llamados *codehash*
En una cuenta de propiedad externa el campo codehash es el hash de una cadena vacia
Además hay un hash asociado al almacenamiento de una cuenta llamado *storehash*
Solo una transacción con un nonce especifico puede ejecutarse para cada cuenta, lo que protege contra ataques de repetición, donde transacciones firmadas se transmiten y ejecutan repetidamente

Una cuenta está compuesta por un par de *claves criptograficas*, una pública y otra privada.
Estas claves ayudan a demostrar que una transacción fue firmada realmente por el remitente y previenen falsificaciones.
Tu clave privada es la que utilizas para firmar transacciones, lo que te otorga la custodia de los fondos asociados a tu cuenta. En realidad no posees criptomonedas directamente, posees claves privadas, los fondos siempre están en el registro de ethereum.
Eso impide que actores malintencionados transmitan transacciones falsas, ya que siempre puedes verificar el remitente de una transacción.

Cuando deseas crear una cuenta, la mayoria de las bibliotecas generarán para ti una *clave privada aleatoria*, la cual está compuesta por 64 caracteres hexadecimales y puede ser encriptada con una contraseña
La *clave pública* se genera a partir de la clave privada utilizando el algoritmo de Elliptic Curve Digital Signature Algorithm
Obtienes una *dirección pública para tu cuenta* tomando los ultimos 20 bytes del hash Keccak-256 de la clave pública agregando un "0x" al comienzo. Una cuenta de propiedad externa tiene una dirección de 42 caracteres-segmento de 20 bytes, que son 40 caracteres hexadecimales mas el prefijo 0x. Es vital mantener las claves privadas seguras y como el nombre lo sugiere, privadas

La clave privada se usa para *firmar mensajes y transacciones*, lo cual produce una *firma*
Otros pueden tomar la firma para derivar tu clave pública, proveyendo el autor del mensaje
Las cuentas de contrato tambien tienen una dirección de 42 caracteres hexadecimales
La dirección del contrato se proporciona cuando un contrato se implementa en la blockchain de ethereum.
La dirección proviene de la dirección del creador y el numero de transacciones enviadas desde esa direccion.
En ethereum existe otro tipo de claves llamadas claves *BLS* QUE SE UTILIZAN PARA IDENTIFICAR VALIDADORES. Estas claves pueden agregarse de manera eficiente para reducir el ancho de banda necesario para que la red alcance el consenso

Una cuenta no es una billetera. Una billetera es una interfaz o aplicación que te permite interactuar con tu cuenta de ethereum, ya sea una cuenta de propiedad externa o una cuenta de contrato

**Transacciones:**
Las *transacciones* son instrucciones firmadas criptograficamente provenientes de cuentas.
Una cuenta iniciara una transacción para *actualizar el estado* de la red ethereum.
La transacción mas sencilla es transferir ETH de una cuenta a otra
Una transacción de ethereum se refiere a una acción iniciada por una cuenta de propiedad externa.
Las transacciones que modifican el estado de la EVM necesitan ser transmitidas a toda la red
Cualquier nodo puede enviar una solicitud para que se ejecute una transacción en la EVM, una vez hecho esto, un validador ejecutara la transacción y propagara el cambio de estado resultante al resto de la red.

Una transacción enviada por una *cuenta de propiedad externa* contiene:
- *from:* la dirección del remitente, quien firmara la transacción
- *to:* la dirección del destinatario, si es una cuenta de propiedad externa la transacción transferira el valor, si es una cuenta de contrato la transición ee¿jecutara el código del contrato
- *signature:* el identificador del remitente. Este se genera cuando la clave privada del remitente firma la transacción y confirma que este ha autorizado dicha transacción
- *nonce:* un contador que incrementa secuencialmente y que indica el número de transacciones enviadas desde la cuenta
- *value:* cantidad de ETH a transferir del remitente al destinatario(denominado wei)
- *input data:* campo opcional para incluir datos arbitrarios
- *gasLimit:* la cantidad maxima de unidades que puede consumir la transacción. La EVM especifica las unidades de gas requeridas para cada paso computacional
- *maxPriorityFeePerGas:* el precio máximo del gas consumido que será incluido como propina al validador

**Tipos de transacciones:**
- *Transacciones regulares:* una transacción de una cuenta a otra
- *Transacciones de implementación de contratos:* una transacción sin una dirección "to", donde el campo de datos se utiliza para el código del contrato
- *Ejecución de un contrato:* una transacción que interactua con un contrato inteligente ya implementado. En este caso, la dirección "to" es la dirección del contrato inteligente

**Ciclo de vida de una transacción:** Una vez que la transacción ha sido enviada ocurre lo siguiente:
1. Se genera criptograficamente un hash de la transacción
2. La transacción se transmite a la red y se agrega a un grupo de transacciones que incluye todas las demás transacciones pendientes en la red
3. Un validador debe elegir tu transacción e incluirla en un bloque para verificarla y considerarla "exitosa"
4. A medida que pasa el tiempo, el bloque que contiene tu transacción será actualizado a "justificado" y luego a "finalizado"

**Maquina virtual de Ethereum(EVM):**
La maquina virtual de ethereum(EVM) es un entorno virtual descentralizado que ejecuta código de manera consistente y segura en todos los nodos de ethereum.
Los nodos ejecutan la EVM para realizar contratos inteligentes, utilizando "gas" para medir el esfuerzo computacional requerido para las operaciones, lo que asegura una asignación eficiente de recursos y la seguridad de la red
El *estado de Ethereum* es una gran estructura de datos que contiene no solo todas las cuentas y balances, si no también un *estado de máquina*, el cual puede cambiar de un bloque a otro según un conjunto de reglas predefinidas y puede ejecutar código de máquina arbitrario
Las reglas especificas para cambiar el estado de bloque a bloque son definidas por la EVM
En el contexto de Ethereum, el estado es una enorme estructura de datos llamada *Merkle Patricia Trie modificada*, que mantiene todas las cuentas enlazadas mediante hashes y reducibles a un único hash raiz almacenado en la blockchain

La EVM se ejecuta como una *maquina transitoria* que no persiste entre transacciones.
El código de bytecode de contratos inteligentes compilados se ejecuta como una serie de opcodes de la EVM que realizan operaciones estándar de pila como XOR, AND, ADD, SUBB, etc. La EVM también implementa una serie de operaciones de pila especificas de blockchain, como ADDRESS, BALANCE, BLOCKHASH, etc.

**Nodo:**
Un "*nodo*" es cualquier instancia del software cliente de ethereum que está conectado a otras computadoras que también ejecutan el software de thereum, formando una red
Un *cliente* es una implementación de Ethereum que verifica los datos según las reglas del protocolo y mantiene la seguridad de la red
Un nodo debe ejecutar dos clientes: un cliente de consenso y un cliente de ejecución:
- **Cliente de ejecución:** escucha las nuevas transacciones transmitidas en la red, las ejecuta en la EVM y mantiene el estado más reciente y la base de datos de todos los datos actuales de Ethereum
- **Cliente de consenso( o nodo Beacon):** implementa el algoritmo de consenso basado en prueba de participación, que permite a la red alcanzar un acuerdo basado en los datos validados por el cliente de ejecución

Tambien existe una tercera pieza de software conocida como "*validador*", que se puede agregar al cliente de consenso, permitiendo que un nodo participe en ña seguridad de ña red. Estos clientes trabajan juntos para realizar un seguimiento de la cabeza de la cadena de Ethereum y permitir que los usuarios interactúen con la red Ethereum

**Tipos de Nodos:**
- *Nodos completos:*
- 	Participan en validación de bloques y estados
- 	Mantienen una copia actualizada de la blockchain
- 	Proveen acceso a datos de la blockchain a nodos ligeros
- 	Almacena el estado global
- *Validadores:*
- 	Los validadores crean bloques
- 	Un validador es elegido aleatoriamente en cada ranura para que proponga un bloque
- 	Distribuyen bloques creados a otros nodos de la red
- 	Además actualizan el estado global
- 	Son recompensados con ETH por producir bloques
- *Nodos ligeros:* proporcionan una forma menos demandante de interactuar con la red ethereum, ideal para dispositivos con recursos limitados
- 	no participan en el consenso
- 	no requieren de staking
- 	descargan solo los encabezados de los bloques
- 	verifican la validez de bloques
- 	solicitan datos especificos a nodos completos
- *Nodos de archivo:* mantienen copia completa del historial de la blockchain, incluyendo estados antiguos y datos detallados. Almacenan datos historicos para consultas y auditorias. Facilitan el acceso a la información antigua por aplicaciones. Además almacenan el estado global actual


**Prueba de participación:** es una forma de demostrar que los validadores han puesto algo de valor en la red que puede ser destuido si actúan deshonestamente. Los validadores *apuestan capital* en forma de ETH mediante un contrato inteligente de Ethereum. El validador verifica que los nuevos bloques propagados por la red son válidos y ocasionalmente crean y propagan bloques por si mismas
Para *participar como validador* un usuario deposita 32 ETH en el contrato de depósito y ejecuta tres piezas de software por separado. Un cliente de ejecución, un cliente de consenso, un cliente de validación
Al depositar sus ETH, el usuario entra en *cola de activación* que limita la tasa de nuevos validadores que se unen a la red
Una vez activados, los validadores reciben nuevos bloques de los pares en la red
Se verifica el bloque y el validador *envía un voto(llamado atestación)* a favor de ese bloque a través de la red

En la prueba de participación el tiempo se divide en ranuras de 12 segundos y epochs que corresponden a 32 ranuras.
En cada ranura, se selecciona aleatoriamente a un validador para que sea el proponente de un bloque
Este validador es responsable de crear un nuevo bloque y enviarlo a otros nodos en la red
Ademas, en cada slot, se elige aleatoriamente a un *comité de validadores* cuyas votaciones se utilizan para determinar la validez del bloque propuesto
Dividir el conjunto de validadores en comités es importante para mantener la carga de la red manejable
Los comités organizan a los validadores de manera que cada validador activo realiza atestaciones en cada epoch, pero no en cada slot.

Suponiendo que todos los validadores están en línea y funcionando, va a haber un bloque en cada ranura, significando que el tiempo de bloque es 12 segundos

**Prueba de participación- ejecución de transacciones:**
El usuario crea y firma una transacción con su clave privada(esto generalmente lo gestiona una billetera o una biblioteca)
El usuario define la *cantidad de gas* que está dispuesto a pagar como propina a un validador para incentivarlo a incluir la transacción en un bloque. Las propinas se pagan el validador, mientras que la tarifa base se quema
La transacción se envía a un cliente de ejecución de Ethereum que verifica su validez. Esto significa asegurarse de que el remitente tenga suficiente ETH para cumplir con la transacción y que la haya firmado con la clave correcte
Si la transacción es válida, el cliente de ejecución la agrega a su *lista de transacciones pendientes(mempool local)* y también la transmite a otros nodos a través de la red
Cuando otros nodos escuchan sobre la transacción, la agregan a su lista de transacciones pendientes

Uno de los nodos validador en la red es el *proponente de bloques* para el slot actual, habiendo sido seleccionado previamente de forma pseudoaleatoria mediante el algoritmo RANDAO
Este nodo es responsable de construir y transmitir el siguiente bloque que se añadira a la cadena de bloques de Ethereum y de actualizar el estado global
El nodo se compone de tres partes: un cliente de ejecución, un cliente consenso y un cliente de validación
El cliente de ejecución* agrupa las transacciones del mempool local en un "execution payload" y las ejecuta localmente para generar un *cambio de estado*
Esta información se pasa al *cliente de consenso*, donde el "execution payload" se envuelve como parte de un *bloque raro*, que también contiene información sobre recompensas, penalizaciones, slashing, atestaciones, etc., que permite que la red acuerde la secuencia de bloques en la cabeza de la cadena

Otros nodos reciben el nuevo bloque faro en la red de difusipon de la capa de consenso. Lo pasan a su cliente de ejecución, donde las transacciones se vuelven a ejecutar localmente para garantizar que el cambio de estado propuesto sea valido
El *cliente de validación* luego atesta que el bloque es válida y es el siguiente bloque lógico según su vista de la cadena. El bloque se añade a la base de adtos local en cada nodo que lo atesta
Los *checkpoints* ocurren al inicio de cada epoch y existen para tener en cuenta el hecho de que solo un subconjunto de validadores activos realizan atestaciones durante cada epoch
El primer bloque de cada epoch es un checkpoint. Los validadores votan por pares de checkpoints que consideran validos
Si un par de checkpoints recibe votos que representan al menos dos tercios del total de ETH apostados, los checkpoints son actualizados
El más reciente de los dos se convierte en "*justificado*"
El mas antiguo de los dos ya esta justificado porque er el "objetivo" en el epoch anterior. Ahora se actualiza a "*finalizado*"


**Campos en un bloque al nivel más alto:**
- *Slot:* la ranura a la cual pertenece el bloque
- *Proposer_index:* el ID del validador proponiendo el bloque
- *Parent_root:* el hash del bloque previo
- *State_root:* el hash de la raíz del objeto de estado
- *Body:* contiene numerosos campos como:
- 	*Randao_reveal:* valor usado para elegir el siguiente nodo que va a proponer bloques
- 	*Attestations:* lista de atestaciones a favor del bloque corriente
- 	*Execution_payload:* transacciones pasadas por el cliente de ejecución

**Estado global**
El estado global de Ethereum usa una estructura de datos llamada *árbol de Merkle-Patricia*. La cual es una estructura de *pares clave-valor*, donde las claves representan direcciones, y los valores representan datos asociados
El campo *raíz de estado(state root)* es un hash de la estructura del árbol de Merkle-Patricia. El mismo se almacena en el encabezado del bloque

El árbol de Merkle-Patricia se compone de tres *tipos de nodos:*
- *Nodos hoja:* contienen el valor asociado a una clave específica, donde las claves son hashes que identifican cuentas o datos de contratos
- *Nodos de ramificación:* contienen hasta 16 enlaces. Sirven para enrutar claves hacia sus valores asociados
- *Nodos de extensión:* optimizan el árbol almacenando secuencias consecutivas de caracteres en una sola ruta, en lugar de usar múltiples nodos


La clave como una dirección especifica guía la ruta a través del árbol, pasando por los nodos de ramificación hasta llegar a las hojas que contienen los valores correspondientes para esa clave.
Un nodo hoja puede contener informaciones como: el saldo de la cuenta, el nonce, datos especificos de almacenamiento de un contrato.
El **cálculo del State Root** en el árbol de Merkle-Patricia sigue una metodología de *hashing jerárquico*, donde los hashes se aplican progresivamente desde las hojas hasta llegar a la raíz del árbol. Para cada hoja se calcula un hash de su contenido. Los hashes de los nodos hijos se combinan para formar los hashes de los nodos superiores. Este proceso se repite hasta llegar al nodo raíz del arbol, que genera el state root.
**Actualizar el estado global** requiere recalcular los nodos directamente afectados por las transacciones del nuevo bloque. Luego los hashes de los nodos modificados se propagan hacia arriba en el árbol, para obtener el state root


**Calculo eficiente del state root**
En el árbol de Merkle´Patricia, cada nodo tiene su propio hash que representa su contenido y la relación con sus hijos. Los hashes de los nodos que no fueron modificados permanecen igual, y pueden ser reutilizados al calcular el nuevo *state root*. Los cambios en los nodos afectados se propagan hacia arriba en el árbol, recalculando los hashes de los nodos superiores hasta llegar a la raíz. Los nodos que no están en la ruta de las modificaciones no necesitan ser recalculados.

El **estado de un contrato inteligente** contiene:
- *Variables de estado:* definidas en el contrato inteligente
- También puede haber *saldo en ETH asociado al contrato*
- **Actualizaciones del estado de un contrato:**
- 	El estado de un contrato cambia cuando se ejecuta una transacción que interactúa con el contrato
- 	*Las interacciones pueden incluir:*
- 		llamadas a funciones del contrato que modifican las variables de estado
- 		transferencias de ETH al contrato
- 		ejecución de operaciones lógicas definidas en el contrato

**Construcción del estado global:**
Cada nodo completo almacena el *estado global* actualizado en sus discos que incluye: saldos de las cuentas, estado de los contratos inteligentes. Calculan el nuevoe stado global procesando las transacciones del bloque y actualizan el estado global de acuerdo
Los *nodos validadores* ejecutan todas las transacciones en el bloque propuesto y actualizan el estado global. Esto incluye:
- Actualizar los saldos de las cuentas
- Actualizar las variables de los contratos inteligentes

Para consultar el estado global sin ejecutar un nodo propio se pueden consultar servicios de terceros que operan como nodos completos, como *Infura* o *Alchemy*
Recordar que en la red de Ethereum solo se difunden bloques y no estados globales completos

**Información de estado global en la blockchain**
En Ethereum la blockchain almacena tanto las transacciones como información relacionada al estado global. Interesa guardar solo:
- Valores nuevos de los saldos modificados y de variables de contratos inteligentes
- *Raíz de Merkle del estado:* o sea un hash del estado global actualizado

En Ethereum cada bloque contiene un hash conocido como *raíz del estado*. Este hash es una representación compacta del estado global
Cuando un bloque se propaga por la red, los nodos que lo reciben ejecutan las mismas transacciones del bloque y verifican que el estado que resulta coincide con el hash del estado contenido en el bloque

**Aclaraciones sobre los nodos archivo**
Los *nodos de archivo* pueden proporcionar datos como:
- El estado de una cuenta en cualquier bloque específico
- Los valores de las variables de un contrato inteligente en un bloque pasado

Muchos usuarios y desarrolladores dependen de servicios de terceros como *Infura* y *Alchemy* que operan nodos de archivo para cceder a la información histórica de estado.
Los nodos de archivo almacenan el árbol de Merkle-Patricia, pero no necesitan duplicar el árbol entero para cada estado historico.
- En lugar de eso, reutilizan las partes del árbol que no han cambiado entre estados
- En vez de almacenar el estado completo de cada bloque, los nodos de archivo guardan las *diferencias(deltas)* entre estados
- Solo registran los cambios que ocurrieron como resultado de las transacciones en un bloque especifico


Igual que los nodos completos, los nodos de archivo procesan cada bloque recibido, ejecutando las transacciones incluidas en él y calculando el nuevo estado global.
A diferencia de los nodos completos, los nodos de archivo no descartan los estados anteriores.
Al calcular el nuevo estado global, guardan también los cambios incrementales(deltas) que se producen en el estado para poder reconstruir cualquier estado histórico
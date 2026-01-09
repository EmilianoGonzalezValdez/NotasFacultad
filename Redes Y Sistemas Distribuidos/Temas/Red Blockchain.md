
# Red Blockchain



> #### Una red blockchain es un conjunto de nodos interconectados
que operan en un sistema descentralizado que permite la
creación de un registro digital de transacciones descentralizado
y seguro.



#### ¿Que quiere decir esto? 

Básicamente quiere decir que las transacciones se agrupan en bloques que se encadenan siendo esta accesible y verificable por participantes de la red. Permitiendo asi la validación del registro de transacciones usando mecanismos de consenso para asegurar la integridad y seguridad de los datos. Ademas de proporcionas funcionalidades avanzadas como contratos inteligentes que automatizan procesos mediante  algunas condiciones predefinidas



#### Hay varios tipos de dispositivos en una Red Blockchain:

1. Nodos completos los cuales tienen copias del registro de transacciones, participando en la validación de estas (transacciones ) y pudiendo también ejecutar contratos inteligentes

2.  Los nodos mineros se encargan de validar transacciones y crear nuevos bloques resolviendo un problema matemático complejo; estos nodos también poseen una copia completa de la blockchain. De no tener nodos mineros, los nodos completos se pueden encargar de crear mas bloques pero usando otro mecanismo

3. Los nodos ligeros solo pueden verificar y procesar transacciones solicitando datos a los nodos completos al operar

4. Las billeteras digitales son aplicaciones o dispositivos físicos que le permiten a los usuarios almacenar y administrar criptomonedas, interactuando de esta forma, con la red blockchain



#### Los objetivos de las redes blockchain:

1. Transparencia, al permitirle a los usuarios verificar las transacciones en tiempo real

2. Inmutabilidad, garantizar que los datos una vez registrados no pueden ser alterados

3. Descentralización, eliminar la dependencia de un único punto de control reduciendo así el riesgo de fraude y bajando el costo de estas, ademas de evitar la intervención del estado en las cuentas de las personas

4. Interoperabilidad, facilitar la comunicación entre distintas blockchains creando así un sistema más integrado



#### Para hacer todo esto la blockchain se conecta en otras tecnologías, siendo estas:

- [[La Internet]], donde se apoya la blockchain para lograr la comunicación entre nodos y permitir el acceso global

- [[La nube]], donde a menudo se integra para mejorar el almacenamiento y el procesamiento

- Bases de datos, de donde la blockchain se inspira, pero utilizando una base de datos distribuida donde hay nodos que mantienen una copia del registro



# Estructura de las Redes Blockchain

- **Estructura descentralizada:** No hay un nodo central que controle la red, hay varios nodos con copias del libro mayor que participan en el proceso de las transacciones

- **Uso de modelo P2P:** Cada nodo se conecta directamente con los demás, sin intermediarios

- **Consenso distribuido:** La red usa mecanismos de consenso para validar transacciones y mantener la integridad del libro mayor.

### Tipos de nodos en una red blockchain

- **Nodos completos:** Lo mismo que antes

- **Nodos ligeros:**  Lo mismo que antes

- **Creadores de bloques:** Lo mismo que los nodos mineros

- **Nodos de usuarios:** son los usuarios finales de la red blockchain, quienes aprticipan en transacciones

- **Nodos validadores:** verifican y validan transacciones asegurando que sigan las reglas de la red

- **Billeteras:** Lo mismo que antes

- **Autoridades de certificacion:** Emiten y gestionan certificados digitales, asegurando la autenticidad y seguridad de las comunicaciones y transacciones dentro de la red

- **Nodos que ejecutan contrato inteligentes:** Ejecutan el codigo de contratos inteligentes, automatizandolos

- **Gateways:** Actúan como puertas entre la blockchain y otros sistemas

- **Masternodes:** en algunas redes (p.ej: Dash) los masternodes tienen
funciones adicionales como la ejecución de transacciones anónimas y la
gestión de la red.

- **Super Nodos:** Son nodos con mayor capacidad que sirven para mejorar la eficiencia de la red, ya que pueden comunicarse a muchos nodos facilitando la comunicación

- **Nodos balanceadores de carga:** Distribuyen la carga de trabajo entre
diferentes nodos para mejorar la eficiencia y rendimiento de la red.



### Ejemplos de redes blockchain con sus tipos de nodos

- **Bitcoin:** nodos completos, nodos mineros, nodos ligeros, super nodos

- **Ethereum****:** nodos completos(ademas ejecutan contratos inteligentes), nodos ligeros, nodos mineros, balanceadores de carga

- **Ripple:** Nodos validadores, nodos Gateway, nodos usuario

- **Hyperledger fabric:** Nodos peer(con complejos y ejecutan contratos inteligentes), nodos servicio de ordenamiento(ordenan transacciones y crean bloques que se distribuyen a los nodos peer), autoridades de certificación



Para cada red blockchain existe la comunicación entre nodos de distintos tipos



Para interactuar con varias blockchain se utilizan dApps. las cuales son necesarias por varias razones:

- Permiten la comunicacion y transferencia de datos y valor entre diferentes blockchain

- Se pueden utilizar varias blockchain para almacenar datos y  realizar transacciones distribuyendo asi la carga de trabajo

- Aprovechan las diferencias de cada blockchain optimizando asi los costos

Ejemplo **Cosmos** y **Polkadot**



Para integrar datos del mundo externo a la red blockchain se utiliza ChainLink, el cual conectda estos datos con los contratos inteligentes a traves de nodos llamados Oraculos, los cuales son los encargados de recopilar la información.

Hay varios tipos de oraculos:

- Oraculos de Datos: recopilan datos de fuentes externas

- Oraculos de computacion: realizan calculos complejos que no pueden ser procesados por los contratos inteligentes

- Oraculos de eventos: Proporcionan data sobre eventos especificos fuera de la blockchain, como la finalizacion de un contrato

- Oraculos de procesamiento de pagos: Son los que se encargan de procesar las transferencias entre diferentes sistemas, por ejemplo un oraculo que paga un servicio con criptomonedas  



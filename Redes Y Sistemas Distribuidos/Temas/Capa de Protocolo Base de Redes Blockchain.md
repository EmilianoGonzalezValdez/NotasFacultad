
# Capa de Protocolo Base de Redes Blockchain



#### Requisitos:

- **Registro de transacciones:** capacidad de almacenar transacciones

- **Consistencia del estado del sistema:** Todos los participantes deben tener una vision unificada del estado actual del sistema

- **Descentralización:** Quere que el registro opere sin una autoridad central que controle el sistema

- **Inmutabilidad:** Una vez que las transacciones se agregan al registro, no pueden ser modificados ni eliminados

- **Seguridad:** Los datos del registro deben estar protegidos contra alteraciones y accesos no autorizados

- **Transpariencia:** Todos los participantes deben poder ver y verificar las transacciones y los datos en el registro

- **Consenso:** Los nodos de la red deben acordar la validez de grupos de transacciones antes de agregarlas al registro

- **Escalabilidad:** El registro debe ser capaz de manejar un número creciente de transacciones y nodos sin una disminución significativa en el rendimiento

- **Rendimiento:** El tiempo de procesamiento de las transacciones y la actualización del registro debe ser eficiente

- **Resiliencia:** El sistema debe ser robusto y capaz de recuperarse rápidamente frente a fallas o ataques

- **Privacidad:** Debe garantizarse la confidencialidad de ciertos datos y transacciones cuando sea necesario

#### Solución:

Usar una **cadena de bloques (**blockchain**).** El **hash** de un bloque es un identificados único del bloque generado mediante un **algoritmo criptográfico,** el cual funciona como una huella digital del bloque y cambia si se modifica el bloque. Los bloques de una blockchain están enlazados mediante **hashes** de modo que cada bloque contiene el **hash** del bloque anterior. Ademas todos los participantes pueden ver los bloques de dicha blockchain. Se usan **mecanismos de consenso** para asegurar que los nodos acuerden la validez de los nuevos bloques.



#### Estructura de un bloque:

- **Encabezado** **Del Bloque:** Contiene metadatos cruciales para la integridad y verificación. Esta conformado por:

    - **Hash del bloque anteior:** Es un hash que resume todas las transacciones dentro del bloque

    - **Nonce:** Número aleatorio usado durante el proceso de mineria para encontrar un hash válido

    - **TimeStamp:** Marca temporal indicando cuando se creó el bloque

- **Cuerpo del Bloque:** Almacena las transacciones realizadas

- **Hash del bloque:** Generando a partir de todos los datos contenidos en el bloque. Este garantiza que cualquier cambio resultaría en un nuevo valor completamente diferente, protegiendo así la integridad e inmutabilidad del registro blockchain



#### Como se logran los requisitos:

- **Distribución** -> Uso de varios nodos con copia de la blockchain

- **Inmutabilidad ->** Losbloques no pueden alterarse una vez agregados a la blockchain, cualquier cambio sería detectable porque alteraria el hash del bloque

- **Transpariencia ->** Todas las transacciones son visibles públicamente

- **Consenso ->** Por medio de los mecanismos de consenso

- **Rendimiento ->** La eficiencia en la creacion de bloques y la validación de transacciones depende de la implementación especifica de la blockchain y su algoritmo de consenso

- **Privacidad ->** Se pueden implementar mecanismos para la privacidad como transacciones confidenciales

- **Escalabilidad ->** Es un desafío por eso se desarrollaron soluciones de escalabilidad y otras tecnologías

- **Seguridad ->** Se emplean algoritmos criptograficos para proteger los datos y la transacciones

- **Consistencia ->** Mediante mecanismos de consenso todos los nodos acuerdan qué bloque es el siguiente en añadirse a la cadena



## ***Mecanismos de consenso***

#### Principales mecanismos de consenso:


- **Delegated Proof of Stake(DPoS):**

Los usuarios votan **delegados** para validar bloques. Estos delegados reciben recompensans por su trabajo. DPoS es rapido y eficiente pero puede ser poco descentralizado si pocos delegados dominan las votaciones


- **Proof of Stake(PoS):**

Hay nodos **Validadores** que son elegidos según su participacion en la red. Estos nodos verifican si las transacciones dentro de un bloque propuesto son válidas y si cumplen con las reglas de la red. Luego crean nuevos bloques. Cuando un nodo validador propone un nuevo bloque, otros nodos validadores revisan y validan dicho bloque. Solo los bloques válidos serán propagados por la red y añadidos a la blockchain.

Los validadores mantienen una copia de la blockchain y reciben recompensas al generar un nuevo bloque. Tienen menor consumo energetico que PoW



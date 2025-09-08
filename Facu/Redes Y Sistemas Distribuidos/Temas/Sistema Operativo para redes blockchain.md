
# Sistema Operativo para redes blockchain



La organizacion de las capas en bastante diferente que en las redes de computadoras. Ademas la capa de aplicacion resuelve problemas adicionales tipicos de las redes blockchain

## Capa de infraestructura base

Proporciona la infraestructura subyacente para la creacion y operacion de blockchains. Incluye componentes físicos y de red



## Capa de Protocolo Base

Es la blockchain en si misma. Tiene su propia cadena de bloques. Es responsable de la seguridad y el funcionamiento operativo de la red blockchain. Establece las reglas fundamentales de consenso y la estructura de datos principal. Facilita la comunicacion entre nodos y el envio de transacciones, las cuales se llevan a cabo en esta capa

Un **Mecanismo de consenso** establece las reglas y mecanismos mediante los cuales los nodos llegan a un acuerdo sobre el estado del libro mayor.

**Beneficios:**

- **Previene problemas como el doble gasto**

- **Aumenta la resistencia a ataques maliciosos**



#### Ejemplos de mecanismos de consenso:

- PoS

- PoW

- PoH

#### Ejemplos de protocolos:

- Bitcoin(usa PoW)

- Ethereum(usa PoS)

- Cardano(usa PoS)

- Solana(combina PoS con PoH)



#### Limitaciones:

Las blockchains de esta capa suelen enfrentar limitaciones en su capacidad para procesar un gran numero de transacciones por segundo. Para resolver esto se definen **soluciones de escalabilidad**



## Capa de Comunicacion entre Redes Blockchain

Se usan protocolos que facilitan la interoperabilidad y la comunicación entre diferentes redes blockchain. Facilita la creación de redes interconectadas. Aborda problemas como la escalabilidad e interoperabilidad



**Ejemplos:**

- **Polkadot**: Utiliza relay chain

- **Cosmos**: Facilita el intervalo de activos y datos sin necesidad de soluciones centralizadas

- **Avalanche**: Ofrece cadenas como P-Chain, X-chain, C-Chain

- **LayerZero:** Permite la interoperabilidad entre blockchains

- **Wormhole:** protocolo de puente que permite transferencias de activos entre diferentes blockchains

## Capa de soluciones de Escalabilidad

Mejora el rendimiento y la capacidad de procesamiento de transacciones al construirse sobre una blockchain existente. Permite realizar un mayor numero de transacciones **Fuera de la cadena principal**, reduciendo asi la carga de la blockchain



#### Protocolos:

- **Rollups:** agrupan varias transacciones en un paquete. Este se valida en una red secundaria y luego solo se registran los resultados finales en la blockchain base

- **Cadenas Laterales:** Blockchains independientes que estan conectadas a una blockchain principal

- **Canales de Estado:** permiten transacciones rapidas y privadas entre 2 partes sin necesidad de registrar cada transaccion en el bloque principal. Un canal de estado es un entorno temporal donde dos o mas partes pueden ejecutar varias transacciones directamente entre ellas sin involucrar a la blockchain principal

#### Ejemplos:

- **Lighting Network(**para bitcoin**):** usa canales de estado

- **Polygon:** Usa cadenas laterales y rollups

- **Arbitrum(para ethereum):** usa rollups

## Capa de aplicaciones:

Permite la ejecucion y el acceso a alas aplicaciones que interactuan con las blockchain. Aqui se encuentran las dApps que operan sobre la blockchain

#### Caracteristicas de las dApps:

- No dependen de servidores y operan sobre la blockchain

- Usan contratos inteligentes y APIs para la interaccion

- Pueden seguir funcionando incluso si una parte de la red es atacada o censurada

- Operan sin la necesidad de intermediarios permitiendo a los usuarios interactuar directamente con la aplicacion

- Tienen codigo abierto

Los **contratos inteligentes** permiten la ejecucion automatica de acuerdos cuando se cumplen ciertas **condiciones predefinidas**. Los contratos inteligentes son registrados en la blockchain, haciendolos **inmutables y transparentes** y al ser automaticos reducen el riesgo de errores humanos



#### Ejemplos de aplicaciones descentralizadas:

- **Finanzas descentralizadas(DeFi):** Los contratos inteligentes son fundamentales para gestionar prestamos, intercambios y otros servicios financieros sin intermediarios

- **Gestion de cadenas de suministro:** Pueden rastrear productos a lo largo de la cadena de suministro, registrando cada paso en la blockchain para garantizar la autenticidad y trazabilidad. Si usa contratos inteligentes, entonces es una dApp

- **Redes Sociales:** ofrecen mayor privacidad y control sobre los datos personales

- **Votacion:** redes que usan blockchain para mejorar la transparencia y la seguridad de la votación

- **ALmacenamiento descentralizado:** permiten el almacenamiento y distribucion de datos descentralizados

- **Mercados de NFTs:** plataformas que permiten compar tokens no fungibles (NFT)

- **Juegos:** permiten a los ususarios jugar y ganar recompensas en forma de criptomonedas

#### Ejemplos de aplicaciones no descentralizadas:

- **Interfaces de usuario:** permiten interactuar con la blockchain de manera intuitiva

- **Wallets:** Alicaciones que permiten administrar criptomonedas

## Capa de Desarrollo:

Proporciona herramientas necesarias apra el desarrollo y despliegue de aplicaciones sobre blockchains

#### Tecnologias especificas usadas:

- **APIs**

- **Bibliotecas**

- **Plataformas de desarrollo**

- **Frameworks para dApps**

#### Lenguajes de programacion:

- **Solidity**

- **JavaScript**

- **Python**

- **C+**

- GO


# Redes de Dispositivos 
Una red de dispositivos es una estructura compuesta por dispositivos interconectados. Dos dispositivos o nodos están interconectados si estos pueden intercambiar información. Estos nodos también pueden compartir recursos, aplicaciones y servicios, facilitando así la colaboración y el funcionamiento conjunto de los dispositivos conectados. La conexión se hace por medios de transmisión, los cuales pueden usar medios físicos o inalámbricos, luego la comunicación entre nodos conectados se realiza mediante protocolos específicos que aseguran la correcta y eficiente transmisión de datos. En la materia nos interesan los siguientes ejemplos de redes de dispositivos:
- *La Internet*: sirve para conectar computadoras entre si por medio de **proveedores de servicio de Internet**
- *La nube*: Por medio de una **red de servidores** interconectados se proveen servicios a organizaciones o personas como almacenamiento y ejecución de aplicaciones
- *La Internet de las cosas*: Dispositivos físicos llamados **dispositivos IoT** se conectan a internet y comparten datos entre si y con sistemas en la nube
- *Red blockchain*: Es un conjunto de nodos interconectados usados para mantener y validar un registro digital descentralizado de transacciones  

#### ¿Como entender un tipo de red de dispositivos?
Para lograr entender un tipo de red de dispositivos es necesario entender diferentes aspectos del tipo de red de dispositivos:
- Entender su **propósito**
- Entender cómo está organizada la red en cuanto a sus tipos de nodos y cómo se conectan entre si
- Entender el **sistema operativo de la red**:
	- Un sistema operativo de la red se usa para gestionar el uso de los recursos de la res y la comunicación entre los nodos 
- Entender los **protocolos** más importantes que componen el sistema operativo de la red
	- Estos protocolos, entre otras cosas, definen *formatos de mensajes y reglas de comunicación* entre los nodos participantes 
	- Cada protocolo además resuelve un conjunto de *problemas* como veremos mas adelante 


# La internet

La *internet* es una red que cubre todo el globo y consiste de varias **redes de área local (LAN)** conectadas entre sí por medio de **proveedores de servicios de internet (PSI)**, donde cada **LAN** sirve como una red localizada que conecta dispositivos dentro de un área física específica. 
- Los **PSI** proveen los servicios e infraestructura necesarios para que los usuarios conecten sus LAN a la internet mas amplia. 
- Estos **PSI** usan dispositivos como enrutadores y puertas de enlace. 
- Los **PSI** también se encargan de manejar el tráfico de datos entre usuarios y la red global, ademas de facilitar la conexión a través de arios medio incluyendo cable, DSL, fibra óptica y tecnologías inalámbicas 

EN internet hay **aplicaciones de red** que permiten:
- *Compartir recursos*: Sean de hardware o información
- La *comunicación entre personas*: mail, mensajería, etc.
- *Socializar*
- *Trabajo colaborativo*
- *Comercio electrónico*
- *Entretenimiento*

Distintas redes de computadoras se pueden interconectar entre sí. Para poder aprovechar y gestionar los distintos tipos de redes se define el **sistema operativo de la red** de la internet.

En la internet para proveer servicios se crean *aplicaciones de red*. Para programarlas se usan *APIs* como los sockets y middlewares como la web y llamadas a procedimientos remotos. Estos últimos se basan en el sistema operativo de la red. El sistema operativo de la red se apoya en el hardware de redes de computadoras que forman las LAN y ISP

### Estructura de la Internet

La *internet*  está formada por billones de dispositivos de computación conectados entre si, pues esta es una red de redes que a su vez interconecta redes entre sí, donde para el envío y recepción de mensajes entre computadoras se usan *protocolos*  

Los hosts acceden a la internet a través de un *ISP de acceso* de alguno de los siguientes tipos:
- *ISP residenciales*
- *ISP empresarial*
- *ISP universitario*
- Celulares
- *ISP que proveen acceso a WiFi*

Para que 2 hosts que están conectados a diferentes ISP de acceso puedan enviarse paquetes entre si es necesario que dichos ISPs estén interconectados. Para eso las ISP de acceso son interconectadas a través de redes ISP nacionales e internacionales de más alto nivel llamados *ISPs de capa superior* o *globales de tránsito*. Estas mismas son ISP que proveen *servicios de tránsito* compitiendo entre si. Las mismas consisten en enrutadores de alta velocidad interconectados con enlaces de fibra óptica de alta velocidad.
Las ISP global de transito deben estar interconectadas entre si, y cada ISP debe ser manejada independientemente.
Como no todas los ISP globales de tránsito tienen presencia en cada ciudad o región del mundo, existen los *ISP regionales* a los cuales se conectan los *ISP de acceso de dicha región*, para luego conectar el ISP regional a los ISP globales de tránsito. En esta solución los ISP de acceso le pagan a su respectivo ISP regional, los cuales a su vez le pagan al ISP global de tránsito al que estén conectados.
Finalmente tenemos las redes proveedoras de contenido, las cuales se usan para reducir pagos a redes de tránsito global y para tener control sobre cómo sus servicios son entregados a los usuarios finales. Estas redes se conectan a las ISP regionales e ISP de acceso, y como ultima opción a una ISP de tránsito si no tiene de otra  

Si pensamos al internet como una red formada por niveles de jerarquía veríamos claramente 3 niveles tal que:
- En el **Nivel 1** tenemos: *ISP comerciales(globales de tránsito)* y *Redes proveedoras de contenido* 
- En el **Nivel 2** tenemos: *ISP regionales*
- En el **Nivel 3** tenemos: *ISPs de acceso*

Otra forma de ver la estructura del internet es como un conjunto de redes de distintos tamaños interconectadas entre si. Así las redes pueden tener diferentes tamaños, formas y cumplir distintos propósitos, donde varias redes pueden interconectarse entre sí para formar redes más grandes 

#### Redes de área amplia (WANs) 

Una **red de área amplia (WAN)** cubre un área geográfica grande, típicamente un país o hasta un continente 

Una **WAN** está organizada de la siguiente manera:
- *Subred:* Varios enrutadores conectados entre si forman un grafo 
- A una subred pueden estar conectadas computadoras o LAN enteras, permitiendo de esta forma interconectar varias LANs
- Para ir de una maquina a otra hay varias rutas alternativas 

Para enviar mensajes en una WAN existe el **algoritmo de almacenamiento y reenvío**. En este un paquete sigue una ruta de enrutadores, el paquete se almacena enteramente en cada enrutador de dicha ruta. De esta forma el paquete almacenado en un enrutador espera allí hasta que la línea requerida de salida esté libre  luego se reenvía al siguiente enrutador

Si la tasa de llegada al enlace excede la tasa de transmisión del enlace por un periodo de tiempo, los paquetes se van a encolar y esperarán a ser transmitidos en el enlace. Si el buffer del enrutador se llena, los nuevos paquetes serán descartados y se perderán 

Normalmente hay varios caminos que conectan 2 enrutadores. El ==***algoritmo de enrutamiento***== es quien decide cual de todos ellos usar 

Para saber cuanto demora el almacenamiento y reenvío se utiliza la formula: $$d_{nodal}=d_{proc}+d_{queue}+d_{trans}+d_{prop}$$
donde $d_{proc}$ es el tiempo de procesamiento del nodo:
- Chequeo de errores
- Determinar la linea de salida
- normalmente < mili-segundos 

Y $d_{queue}$ es la demora por encolado:
- Tiempo de espera en el enlace de salida para transmisión
- Depende de cuán congestionado está el enrutador 

###### Sistema telefónico fijo:
Cada domicilio está conectado por un cable de cobre a una **End Office**. Toda oficina central está conectada a una **Toll Office**. Estas ultimas son usadas para el reenvío de mensajes y están unidas por cables de fibra óptica

#### Redes de Área Metropolitana 

Una **MAN** cubre una ciudad, hay de 2 tipos:
- *Redes de cable:* Se basan en la red de TV por cable
- *WiMAX:* Son redes inalámbricas de alta velocidad 

**MAN basada en TV por cable:**
- El cable coaxial sirve para unir varias casas
- Elementos de conmutación son para comunicar viviendas en distintos cables coaxiales
- Elementos de contaminación se unen por cables de fibra óptica
- El servicio es asimétrico en la bajada y subida de datos
- Hay un divisor entre TV y cable modem 
- En una red estas casas de conectan a un ISP mediante un *cable headend* compartido entre las casas

**MAN Wimax:**
- Hay una estación base que permite enviar paquetes por el aire en lugar de usar cable o redes telefónicas 
- La estación base se conecta a internet
- Se puede acceder a la red Wimax desde computadoras en casas o edificios

#### Redes de Área local

Una *red de área local (LAN)* es una red operada privadamente dentro e un edificio o casa. Las LAN usadas por compañías se llaman *redes empresariales*.
Las LAN se usan para comunicar dispositivos, donde la idea es que los host puedan compartir recursos e intercambiar información. Existen las LAN:

- *LAN inalámbricas:* En su forma más simple las maquinas se comunican entre sí  por medio de una estación base
- *La Ethernet:* En su forma mas simple las maquinas se conectan por medio de cables a un conmutador(switch) 

Las maquinas se comunican mediante *Difusiónes* de forma tal que si una máquina envía un mensaje, todas las demás lo reciben. Aunque pueda ser que este mensaje estaba destinado para solo una máquina, o para todas ellas o solo para un grupo reducido 

Puede pasar que al enviarse mensajes en una red de difusión estos se pierdan debido a *colisiones*, esto pasa cuando mas de una maquina manda simultáneamente un mensaje. Uno siempre quiere minimizarlas o evitarlas, para ello es necesario detectarlas y saber como tratarlas 


Normalmente en el internet hay redes dorsales o backbones, las cuales estan conectadas a varias WANs, las cuales a su vez estan conectadas a redes MANs. De esta forma las LANs se conectan a WANs o MANs formando asi una red de redes jerarquicamente distribuida

# La Nube

La *nube* permite el acceso remota  un conjunto de **recursos informáticos** incluyendo almacenamiento, procesamiento de datos y aplicaciones a través de una **red de servidores** interconectados.
Estos servidores se asignan y usan dinámicamente para comunicarse entre sí y con los usuarios, lo que facilita la entrega eficiente y escalable de servicios  
Los recursos se asignan y usan dinamicamente según las necesidades cambiantes de los servicios ofrecidos, permitiendo a las organizaciones optimizar su infraestructura tecnológica sin necesitas de gestionar físicamente el hardware
Los usuarios pueden acceder a estos recursos desde cualquier lugar y en cualquier momento, usando dispositivos conectados a internet
La nube permite a individuos y empresas acceder a la tecnología avanzada bajo demanda 

**Clasificación de las nubes:**
- *Nube pública:* Infraestructura compartida proporcionada por proveedores como AWS, Azure y Google cloud. Los recursos son compartidos entre múltiples usuarios 
- *Nube Privada:* Infraestructura dedicada a una sola organización proporcionando mayor control y seguridad 
- *Nube Híbrida:* Combina nubes públicas y privadas, permitiendo a las organizaciones aprovechar lo mejor de ambos mundos 

### Estructura de la Nube 

Una nube se la puede considerar una red jerárquica compuesta por 4 niveles:
- *Regiones:* Son ubicaciones geográficas donde los proveedores de servicios en la nube tienen centros de datos, aunque cada región puede albergar múltiples zonas de disponibilidad 
- *Zonas de disponibilidad:* Son centros de datos aislados dentro de una región que están diseñados para operar independientemente, proporcionando redundancia y alta disponibilidad, ya que si una zona falla, las aplicaciones pueden seguir funcionando en otra 
- *Nube privada virtual (VPC):* Una VPC es una red virtual lógicamente aislada dentro de una nube pública que permite a los usuarios definir su propio entorno de red. Dentro de una VPC se pueden crear subredes públicas y privadas, lo que permite un control granular sobre el acceso a los recursos 
- *Subredes:* Las subredes son divisiones dentro de una VPC que permiten organizar y aislar recursos. Estas pueden ser públicas o privadas en relación al acceso al internet, lo cual facilita la gestión del trafico y la seguridad 


Hay diferentes tipos de nodos en una nube:
- *Servidores web:* Manejan las solicitudes HTTP/HTTPS y sirven contenido web
- *Servidores de aplicaciones:* Procesan la lógica de la aplicación y acceden a la base de datos 
- *Servidores de bases de datos:* Manejan las bases de datos
- *Almacenamiento de Objetos:* Utilizado para almacenar archivos estáticos como imágenes, vídeos y archivos de configuración
- *Balanceadores de carga:* Distribuyen el trafico entre múltiples servidores para optimizar el uso de los recursos y mejorar la disponibilidad 

Existe una **clasificación de los balanceadores de carga:**
- *Balanceador de carga Externo:* Se usa para distribuir tráfico de clientes externos hacia los servidores web
- *Balanceador de carga Interno:* Se usa para distribuir el tráfico entre servidores internos, como entre servidores web y entre servidores de aplicaciones o bases de datos, sin exponer estos recursos al público. Solo está accesible desde una VPC 

**Tipos de enrutadores en la nube:**
- *Enrutador de la VPC:* Se encarga de la comunicación entre las subredes dentro de la misma VPC y de dirigir el tráfico hacia y desde internet o hacia otras VPCs. De esta forma los servidores de diferentes subredes dentro de una misma VPC se comunican a través del enrutador de la VPC
- *Puerta de enlace de internet:* Se conecta a la internet y permite que los servidores en las subredes publicas envíen y reciban trafico de internet 
- *Puerta de enlace de VPCs:* Se usan para comunicar diferentes VPCs entre si

# La Internet de las Cosas

La *internet de las cosas(IoT)* es un sistema interconectado que permite que dispositivos físicos, conocidos como **dispositivos IoT** se conecten a internet y compartan datos entre sí y con sistemas en la nube 
Los dispositivos IoT se conectan a internet a travéß de diferentes tecnologías como WiFi, Bluetooth, redes de celulares para enviar y recibir datos
Los datos recopilados por los dispositivos IoT pueden enviarse a plataformas en la nube donde se almacenan y procesan y analizan.
Las computadoras tradicionales se usan para gestionar la red IoT, analizar los datos recopilados y proporcionar interfaces de usuario para el control y monitoreo

**Ejemplos de dispositivos IoT son:**

- **Sensores:** Miden variables físicas o químicas
- **Actuadores:** Ejecutan acciones físicas basadas en señales eléctricas 
- **Wearables:** Dispositivos portátiles que monitorean la salud y actividad física 
- Electrodomésticos inteligentes 
- Cámaras de seguridad interconectadas   

El **propósito de la IoT** es crear una red de objetos conectados que recopilen, compartan y actúen con información para mejorar a la vida cotidiana y eficiencia en diferentes contextos:
- *Recopilar, compartir y actuar con información:* Los dispositivos recopilan datos del entorno, los comparten con otros dispositivos o sistemas, y actúan en base a esa información 
- *Mejorar la vida cotidiana:* La IoT busca simplificar tareas cotidianas, reducir el esfuerzo humano, y hacer que la tecnología sea más accesible
- *Aumentar la eficiencia en diversos contextos:* La IoT beneficia a los hogares, las industrias, ciudades, la salud, la logística

Las **Metas de la IoT:**
- *Automatización:* realizar tareas automáticamente sin intervención humana
- *Monitoreo:* Proporcionar datos en tiempo real sobre condiciones especificas
- *Optimización de recursos:* Como energía, agua, tiempo, costos 
- *Mejora de la vida cotidiana:* 
- *Sostenibilidad Ambiental:* Reducir emisiones, reducir ruido
- *Análisis de datos:* Para tomar decisiones informadas
- *Mejorar la seguridad física:* Detección de intrusiones, detección de fallos importantes y actuar rápidamente

### Estructura de la Internet de las Cosas 

Las redes IoT se pueden clasificar según diferentes criterios:
1. **Por tipo de conectividad:**
	- *Redes de celulares:* Usan tecnologías como 4G y 5G para proporcionar alta velocidad y cobertura amplia (Ideales para aplicaciones que requieren gran ancho de banda y baja latencia )
	- *Redes de medio alcance:* Como WiFi
	- *Redes de corto alcance:* Incluyen tecnologías como Bluetooth y Zigbee, que son adecuadas para entornos pequeños como hogares y oficinas, teniendo un alcance limitado pero un eficiente consumo energético
	- *Redes de área amplia de baja potencia (LPWAN):* Estas redes están diseñadas para dispositivos que requieren largas distancias de comunicación con bajo consumo energético
2. **Por propósito o aplicación:**
	- *Redes de salud:* Se usan en aplicaciones de telemedicina y monitores de pacientes, permitiendo la recopilación y transmisión de datos médicos en tiempo real. Suelen usar dispositivos wearables que envían datos a profesionales médicos
	- *Redes industriales:* Diseñadas para el monitoreo y control de maquinaria en fabricas, Usan redes celulares o Ethernet industrial
	- *Redes de agricultura inteligente:* Usadas para la monitorización de cultivos y ganado, aprovechando la tecnología LPWAN. Suelen usar sensores para recopilar datos
	- *Redes de hogar inteligente:* Integran dispositivos domésticos conectados como termostatos, cámaras de seguridad. Usan Zigbee o Zwave 
	- *Redes para ciudades inteligentes:* Usadas para gestionar servicios urbanos como el trafico, la iluminación pública y la gestión de residuos. Suelen usar sensores para recolectar datos. Pueden incluir redes celulares o LPWAN
	- *Redes de transporte y logística:* Se usan para optimizar el transporte y la gestión de la cadena de suministro.
	- *Redes IoT de retail:* Se usan para mejorar la experiencia del cliente y la eficiencia operativa en el comercio minorista
3. **Por consumo energético:**
	- *Bajo consumo:* Redes que priorizan la eficiencia energética, como:
		- Zigbee: Usada en automatización del hogar
		- LoRaWAN: Usada en agricultura y ciudades inteligentes, son ideales para dispositivos que funcionan con baterías durante largos periodos 
		- Bluetooth: Usado en wearables y dispositivos médicos portátiles 
		- Sigfox: Para transmitir pequeñas cantidades de datos con cobertura extensa 
	- *Muy bajo consumo:* Como RFID (para rastrear ubicación y movimiento de productos en tiendas, etc.) y NFC (Para pagos móviles, compartir información entre celulares, etc.) 
	- *Alto consumo:* Redes que pueden soportar dispositivos con mayor demanda energética. Suelen usar WiFi o redes de celulares, ejemplos:
		- Cámaras de seguridad: Conectadas a WiFi
		- Lo sistemas de monitoreo y control de maquinaria pesada o procesos de fabricación avanzados pueden consumir mucha energía debido a la necesidad de mantener comunicaciones constantes y procesar grandes volúmenes de datos
		- Automóviles conectados y autónomos, porque generan y procesan grandes cantidades de datos en tiempo real lo que lleva a un alto consumo energético 


Las redes clasificadas según su propósito y aplicación pueden ser redes de sensores o sistemas ciberfísicos(CPS), ambos tienen sus propias características que veremos a continuación:

#### Redes IoT de Sensores 

Una red IoT de sensores generalmente incluye diversos dispositivos de monitoreo y comunicación para recopilar, procesar y transmitir datos. Estas redes suelen incluir los siguientes tipos de dispositivos:
- *Sensores:* Son dispositivos que recopilan datos específicos
- *Gateways IoT:* SOn dispositivos que actúan como intermediarios entre los sensores y la nube, recopilando y transmitiendo datos 
- *Servidores en la nube:* Almacenamiento y procesamiento de datos, análisis y ejecución de algoritmos
- *Dispositivos de usuario:* Celulares, tablets, computadoras usadas ara monitorear y controlar la red de sensores 

Estos dispositivos se conectan de las siguientes maneras:
- *Sensores a Gateways IoT:* Usualmente conectados mediante redes inalámbricas de corto o medio alcance o redes de baja potencia y largo alcance
- *Gateways IoT a servidores de la nube:* Conectados a través de internet usando TCP/IP, generalmente mediante WiFi, Ethernet o redes de celulares
- *Servidores en la nube a dispositivos de usuarios:* Conexión a través de internet usando TCP/IP, permitiendo el acceso remoto a los datos desde cualquier lugar 

Normalmente los sensores recopilan datos específicos y los envían a las Gateways IoT. Estas reciben los datos y los transmiten a los servidores de la nube para que allí estos sean analizados y almacenados, para luego de ejecutar ciertos algoritmos se generen informes al respecto. Luego los dispositivos de usuario pueden acceder a dichos datos e informes desde la nube 


#### Sistemas CPS (Cyber-Physical Systems) 

Los sistemas CPS son sistemas que integran componentes físicos y computacionales. Estos sistemas están diseñados para interactuar con el mundo físico a través de sensores y actuadores y están controlados por algoritmos computacionales . Sus principales características son:
- Capacidad para interactuar y controlar procesos físicos
- Alta fiabilidad y seguridad
- Procesamiento distribuido y en tiempo real 

Los dispositivos involucrados en un CPS son:
- *Sensores:* recopilan datos del entorno físico
- *Actuadores:* Dispositivos que realizan acciones basadas en los datos 
- *Controladores:* Dispositivos que procesan los datos de los sensores y envían comandos a los actuadores
- *Servidores en la nube:* Se encargan del almacenamiento y procesamiento de datos
- *Dispositivos del usuario:* Lo mismo que las redes de sensores

Estos dispositivos también se conectan de una determinada manera:
- *Sensores a controladores:* conexión por cables o inalámbrica 
- *Controladores  actuadores:* conexión por cables o inalámbrica
- *Controladores a servidores en la nube:* conexión por Ethernet o redes de celulares
- *Conexión entre servidores en la nube y dispositivos de usuario* 

Normalmente los sensores recopilan datos del entorno y envían esos datos a los controladores. Estos procesan los datos y determinan la acción a realizar, enviando el respectivo comando a los actuadores. Ademas envían los datos y acciones realizadas a los servidores en la nube para su almacenamiento y análisis. Luego los dispositivos de usuario permiten a los operadores monitorear y controlar el sistema en tiempo real mediante una conexión a internet.

Para ello el controlador debe de lograr realizar ciertas funciones especificas:
- *Recopilación y procesamiento de datos* provenientes de sensores 
- *Control y ejecución de acciones* basados en los datos de sensores y las condiciones programadas, el controlador envía comandos a los actuadores
- *Monitoreo y supervición* manteniendo un monitoreo constante del estado de los dispositivos conectados incluyendo los sensores y actuadores 
- *Comunicación y coordinación* facilitando la comunicación entre diferentes dispositivos y sistemas en la red, actuando como intermediario para la transmisión de datos. Se cordina con Gateways IoT y servidores en la nube para análisis y almacenamiento de datos
- *Retroalimentación a Gateways IoT en la nube* transmitiendo datos recopilados y procesados a los servidores en la nube para análisis adicional y almacenamiento. Puede sincronizar datos con otros sistemas de control y monitoreo remoto

# Redes BlockChain 

Una **red blockchain** es un conjunto de nodos interconectados que operan en un **sistema descentralizado** que permite la creación de un **registro digital de transacciones** descentralizado y seguro 
Las transacciones se agrupan en **bloques que se encadenan** unos con otros. Esta cadena es *accesible* y *verificable* por participantes de la red
Una red blockchain permite la **validación del registro de transacciones** usando *mecanismos de consenso* para poder asegurar la integridad y seguridad de los datos
Una red blockchain puede proporcionar funcionalidades avanzadas como *contratos inteligentes* que **automatizan procesos** mediante **condiciones predefinidas**  

***Tipos de dispositivos en una red blockchain:***

- *Nodos completos* que tienen copias del registro y participan en la validación de transacciones y también pueden ejecutar contratos inteligentes 
- Los *Dispositivos mineros* se usan para validar transacciones y crear nuevos bloques en redes blockchain una vez que resolvieron un problema matemático complejo
	- Los dispositivos mineros tienen una copia completa de la blockchain 
	- Si la blockchain no tiene nodos mineros, los nodos completos pueden cumplir el rol de crear y agregar nuevos bloques a la blockchain pero usando otro mecanismo distinto de resolver problemas matemáticos
- *Nodos ligeros:* Pueden verificar y procesar transacciones, solicitan datos a nodos completos para sus operaciones
- Las *Billeteras digitales* son aplicaciones o dispositivos físicos que permiten a los usuarios almacenar, enviar y recibir criptomonedas, interactuando con la red blockchain

Los **Objetivos de las redes blockchain:**

- *Transparencia:* Permitir a los usuarios verificar las transacciones en tiempo real, aumentando la confianza entre las partes involucradas 
- *Inmutabilidad:* Garantizar que una vez que los datos son registrados, no puedan ser alterados ni eliminados sin el consenso de la red 
- *Descentralización:* Eliminar la dependencia de un único punto de control, lo que reduce el riesgo de fraude y mejora la resiliencia del sistema
- *Interoperabilidad:* Facilitar la comunicación y el intercambio de datos entre diferentes blockchains, creando así un ecosistema más integrado

La blockchain se basa y se conecta con tecnologías anteriores como: 
- *Internet:* La internet proporciona la infraestructura necesaria para la comunicación entre nodos distribuidos. La blockchain opera sobre a internet, utilizando sus protocolos para transmitir datos y permitir acceso global 
- *Nubes:* Aunque la blockchain puede funcionar independientemente, a menudo se integra con servicios en la nube para almacenamiento adicional y procesamiento, mejorando su escalabilidad y flexibilidad
- *Bases de Datos:* A diferencia de las bases de datos tradicionales que son centralizadas, la blockchain actúa como una base de datos distribuida donde hay nodos que mantienen una copia del registro, lo que mejora la seguridad y la transparencia 


### Estructura de las redes blockchain 

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
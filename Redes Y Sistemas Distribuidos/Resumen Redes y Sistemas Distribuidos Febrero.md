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
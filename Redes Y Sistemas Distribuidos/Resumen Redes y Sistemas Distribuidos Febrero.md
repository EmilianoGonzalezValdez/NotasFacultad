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

## Estructura de la Nube 

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


## Sistema Operativo para la nube 

antes de ver los detalles de la pila de protocolos en la nube es necesario ver conceptos importantes sobre el cómputo en la nube, facilitando así la comprensión de algunas capas
### Cómputo en la Nube 

Tenemos varias alternativas de servicios en la nube:
- **Infraestructura como servicio (Iaas)**
	- - Ambiente formado por recursos informáticos básicos que pueden ser accedidos/manejados vía interfaces basadas en servicios de la nube y herramientas. 
	- Los usuarios pueden aprovisionar, configurar y gestionar sus propios recursos informáticos
	- Se pueden escalar los recursos según las necesidades del negocio 
	- Los proveedores del IaaS son responsables del mantenimiento del hardware
- **Plataforma como servicio (PaaS)**
	- Plataforma completa par que los desarrolladores creen, desplieguen y gestionen aplicaciones sin preocuparse por la infraestructura subyacente 
	- Proporciona herramientas y servicios para el desarrollo de aplicaciones, como bases de datos, middleware y entornos de ejecución 
	- El proveedor se encarga del mantenimiento del entorno de desarrollo
- **Software como servicio**
	- Permite a los usuarios acceder a las aplicaciones completas alojadas en la nube mediante una suscripción, sin necesidad de instalación o mantenimiento local
	- Los usuarios pueden acceder al software desde cualquier dispositivo con conexión a internet
	- El proveedor se encarga de todas las actualizaciones, mantenimiento y seguridad del software

Para mejorar la infraestructura de la nube tenemos 2 opciones regulares:
- **Virtualización:**
	- La virtualización permite dividir un servidor físico en varias máquinas virtuales donde cada una es capaz de ejecutar si propio sistema operativo y aplicaciones
	- *Hipervisor:* software especializado que permite que múltiples instancias se ejecuten en un solo servidor físico
	- Tanto el sistema operativo invitado y el software de aplicación ejecutado en servidor virtual no son conscientes del proceso de virtualización
	- Si una maquina falla, no afecta a las demás
	- Se pueden agregar o eliminar maquinas virtuales según se necesite
- **Containerización:**
	- Se empaqueta el código de la aplicación junto con los archivos de configuración relacionados, librerías y dependencias requeridas para que se pueda ejecutar
	- Las aplicaciones son desplegadas en contenedores. Cada contenedor se ejecuta en un proceso
	- Usar contenedores permite varios servicios de la nube ejecutándose como un servidor único mientras se accede al mismo SO
	- Los contenedores pueden ejecutarse en cualquier plataforma que soporte el motor de contenedores
	- Si un contenedor falla, no afecta a los otros
	- Como comparten el núcleo de un sistema operativo, los contenedores requieren menos recursos que las maquinas virtuales

### Ahora si, sistemas operativos para la nube 

#### Capa de red

La capa de red está formada por protocolos que facilitan la conectividad y el enrutamiento dentro de la infraestructura de red de cada proveedor.
También se preocupa de la seguridad de estas redes. Los protocolos usados son:
- *Protocolos de internet:* Son importantes para que los datos puedan moverse entre redes conectadas a través de internet. Se usan BGP e IP
- *Protocolos para redes privadas virtuales (VPN):* Las VPN permiten establecer conexiones seguras entre las redes del cliente y la nube a través de internet. Los protocolos mas comunes incluyen:
	- *OpenVPN:* Cifra los datos y asegura que viajen protegidos a través de una conexión pública
	- *WireGuard:* También cifra conexiones VPN, ofreciendo mayor velocidad y simplicidad
- *Protocolos para conexiones privadas entre cliente y proveedor de la nube:* Cuando las empresas necesitan conexiones más rápidas y seguras, pueden optar por métodos privados que no usan internet. Por ejemplo:
	- *MPLS:* crea rutas privadas dedicadas para enviar datos directamente entre las instalaciones del cliente y el proveedor de nube
	- *Tuneles VPN:* permiten crear una conexión segura sobre internet público hacia el proveedor de nube, utilizando protocolos como IPsec o L2TP
	- *Conexiones dedicadas:* establecen líneas privadas entre el centro de datos del cliente y la nube, siendo estas conexiones mas rápidas, confiables y seguras que las basadas en internet público

#### Capa de infraestructura 

La capa de infraestructura se refiere a los protocolos básicos que permiten la comunicación y transferencia de datos entre servidores y clientes. Incluye los siguiente tipos de protocolos:
- Protocolos de capa de aplicación de internet como HTTP, HTTPS, SFTP, FTP
- Protocolos de capa de transporte de internet como TCP, UDP

#### Capa de almacenamiento 

La capa de almacenamiento consiste de protocolos usados para acceder y gestionar datos almacenados en la nube. Se usan protocolos diferentes para diferentes tipos de almacenamiento. Estos tipos de almacenamiento pueden ser:
- *En bloque:* se almacenan datos en bloques individuales
- *De archivos:* permite acceso a sistema de archivos
- *De objetos:* para grandes cantidades de datos no estructurados como:
	-  Archivos multimedia
	- Copias de seguridad
	- Datos de IoT

#### Capa de plataforma

La capa de plataforma es un conjunto de herramientas y servicios que los desarrolladores pueden usar para construir y ejecutar aplicaciones sin tener que preocuparse por los detalles técnicos de cómo funcionan los servidores o la infraestructura detrás de escena.
Esta capa permite que las aplicaciones se conecten y trabajen con servicios en la nube utilizando *APIs* como puentes

Esta capa proporciona todo lo necesario para que los desarrolladores puedan fácilmente:
- *Escribir Código* de sus aplicaciones
- *Probarlas* para asegurarse de que funcionan correctamente
- *Desplegarlas*

Gracias a esta capa los desarrolladores no tienen que preocuparse por configurar servidores, gestionar redes o resolver problemas complejos de infraestructura pudiendo es esta forma enfocarse únicamente en crear las funcionalidades y características de su aplicación

En esta capa se usan los siguientes protocolos:
- *REST:* se usa para que las aplicaciones pidan o envíen información a los servicios en la nube
- *gRPC (google remote procedure call):* permite a los programas ejecutar funciones o procedimientos en servidores remotos como si estuvieran en la misma máquina local

#### Capa de funciones sin servidor

La capa de funciones sin servidor involucra protocolos que permiten ejecutar código en respuesta a eventos sin necesidad de gestionar servidores, ni la infraestructura. Siendo ideal para aplicaciones que requieren escalabilidad rápida y eficiente.
Los eventos son fundamentales para activar y ejecutar las funciones. Los tipos mas comunes de estos son:
- *Evento HTTP:* cuando un usuario hace una solicitud a través de una API o un browser
- *Cambios en la base de datos:* cuando hay modificaciones en los datos
- *Eventos de almacenamiento en la nube:* cuando se hacen acciones sobre objetos almacenados
- *Eventos de mensajería:* sistemas de mensajeria o colas que mandan notificaciones sobre nuevos mensajes o tareas
- *Eventos de IoT:* cuando dispositivos IoT mandan datos o notificaciones 
- *Eventos a intervalos regulares:* evento que pasó un tiempo T
- *Eventos de aplicaciones externas:* aplicaciones externas mandan notificaciones sobre eventos relevantes

#### Capa de contenedores

La capa de contenedores esta compuesto por los protocolos y tecnologías usadas para la gestión y orquestación de contenedores en la nube, refiriendo a la gestion y orquestación de aplicaciones en la nube usando tecnologías como docker.
Los contenedores permiten empaquetar las aplicaciones y sus dependencias, lo que facilita su despliegue y escalabilidad.

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

## Sistema Operativo para el Internet de las Cosas

*Diferencias de los protocolos de IoT con os protocolos de internet:*
- Muchos dispositivos IoT son de baja potencia y tienen recursos limitados. Por lo tanto los protocolos para IoT están diseñados para ser ligeros y eficientes en el uso de energía y recursos. Mientras que los dispositivos conectados a internet generalmente tienen recursos relativamente abundantes en términos de energía, capacidad de procesamiento y memoria
- La IoT se enfoca en la comunicación entre dispositivos IoT heterogéneos en entornos específicos. La internet está diseñada para la comunicación entre computadoras y servidores, facilitando el intercambio de información a gran escala y el acceso a servicios en linea
- Se necesitan protocolos para escalar a una gran cantidad de dispositivos IoT, gestionando transmisiones de datos recuentes y a menudo en tiempo real. Mientras que los protocolos de internet permiten escalar a muchas maquinas y gestionar grandes volúmenes de tráfico de datos, pero solo para computadoras y servidores y no para dispositivos IoT

Para la internet de las cosas veremos un *modelos e capas de referencia* con las mismas capas que las de redes de computadoras, pero se añaden dos capas mas, además las capas con el mismo nombre resuelven problemas adicionales típicos de internet de las cosas:

### Capa Física

La capa física del IoT se encarga de la transmisión de bits a partir de medios físicos. Los problemas a resolver en esta capa son:
- *El consumo energético:* hay dispositivos IoT que son alimentados por batería y necesitan ser eficientes en el uso de la energía. Implementando de esta forma técnicas como el modo sueño
- *Interferencias y ruido:* las comunicaciones inalámbricas pueden ser afectadas por interferencias y ruido. Se usan técnicas de modulación adaptativa para optimizar la transmisión según las condiciones del canal ajustando el tipo de modulación según el nivel de interferencia o ruido
- *Conectividad:* garantizar que los dispositivos pueden mantenerse conectados en entornos difíciles. Se puede implementar una *malla* de modo que todos los dispositivos se comuniquen entre sí directamente

Los protocolos de esta capa son:
- *Zigbee:* diseñado para ser eficiente en el consumo de energía, siendo ideal para dispositivos alimentados por baterías
- *LoRaWAN:* permite la comunicación de largo alcance con un bajo consumo de energía
- *NB-IoT:* permite baja potencia y larga duración de la batería

### Capa de enlace de datos

La capa de enlace de datos es responsable de la transmisión de datos entre dispositivos dentro de la misma red local. Los problemas considerados son:
- *Control de errores:* igual que antes
- *Control de acceso al medio:* igual que antes
- *Retrasos y variaciones en el tiempo de transmisión:* pueden afectar a las aplicaciones en tiempo real. Una idea de solución es ajustar el tamaño y la estructura de las tramas para minimizar la latencia
- *Desconexiones frecuentes:* los dispositivos IoT al ser móviles o ubicarse en áreas con mala cobertura pueden sufrir desconexiones frecuentes
- *Seguridad de la comunicación:* los datos transmitidos no deben ser interceptados ni alterados. Se puede aplicar cifrado y autenticación en la capa de enlace de datos para asegurar la comunicación  

Los protocolos usados son: 
- *Ya vistos o conocidos:* Wi-Fi, Ethernet, Bluetooth
- *También en capa física:* Zigbee, LoRaWAN
- *Bluetooth Low Energy(BLE):* muy eficiente en consumo de energía, ideal para dispositivos que necesitan durar mucho tiempo con baterías pequeñas. Tiene un menor costo de implementación en comparación con otras tecnologías 
- *6LoWPAN:* permite encapsular y enviar paquetes IPv6 sobre redes de baja potencia. Se puede usar en sensores y actuadores. Implementa técnicas de comprensión de encabezado y fragmentación para permitir que los paquetes IPv6 se transmitan eficientemente en redes WPAN de baja potencia 


### Capa de Red

La capa de red gestiona el direccionamiento y el enrutamiento de los dados entre diferentes redes. Sus problemas son:
- *Enrutameinto:* en redes con dispositivos móviles y topologías cambiantes
- *Escalabilidad:* gestión eficiente de un gran número de dispositivos
- *Movilidad en redes inalámbricas:* soporte para dispositivos que se mueven fuera y dentro de la red

Sus protocolos son:
- *De internet:* IPv4, IPv6
- *6LoWPAN:* permite que los dispositivos de baja potencia usen IPv6. Resuelve problemas de enrutamiento y direccionamiento. Facilita la integración con redes IP tradicionales
- *RPL:* optimizado para redes de dispositivos con baja potencia y alta tasa de pérdida de paquetes. Soporta redes con gran número de nodos

### Capa de Transporte

La capa de transporte Asegura la transmisión de datos confiable y ordenada entre dispositivos. Problemas:
- *Fiabilidad de la transmisión:* asegurar que los datos lleguen de manera confiable, en especial en redes con alta tasa de pérdida de paquetes
- *Control de flujo y congestión*
- *Compatibilidad de protocolo:* integración con protocolos específicos de IoT

Protolocos:
- *De internet:* TCP, UDP
- *MQTT:* optimizado para redes con ancho de banda limitada, diseñado para minimizar el consumo de energía durante la transmisión de datos, proporciona varios niveles de calidad de servicio para garantizar la entrega de mensajes. Usa formato de mensaje compacto para minimizar el tamaño de los datos enviados, esto reduce el consumo de energía. MQTT usa TCP como base para la transmisión de datos. Se centra en la comunicación en tiempo real
- *CoAP:* optimizado para dispositivos con recursos limitados, como baja capacidad de procesamiento y memoria. Proporciona confirmaciones de entrega y retransmisión de mensajes perdidos. Esta optimizado para minimizar el uso de ancho de banda, también usa formato binario de mensaje compacto. Generalmente se implementa sobre UDP 

### Capa de aplicación
La capa de aplicación define los protocolos de comunicación usados por las aplicaciones de IoT facilitando la interacción entre el usuario y el sistema IoT. Sus problemas son:
- *Interoperabilidad:* asegurar que los dispositivos y aplicaciones de diferentes fabricantes puedan comunicarse entre si
- *Seguridad y privacidad:* garantizar que los datos sean transmitidos y almacenados de manera segura. Puede usarse SSL y TLS para asegurar las comunicaciones
- *Gestión de dispositivos:* administración eficiente de un gran número de dispositivos. Se pueden usar plataformas de gestión que facilitan la gestión y monitoreo de dispositivos
- *Eficiencia energética:* para dispositivos con recursos limitados y consumo de energía bajo
- *Fiabilidad y calidad de servicio:* entrega de mensajes confiables para aplicaciones criticas 
- *Escalabilidad y ancho de banda:* poder manejar la demanda cuando el número de dispositivos IoT aumenta
- *Simplicidad:* simples de implementar en dispositivos con capacidades limitadas
- *Complejidad:* suficientes complejos como para manejar las necesidades de las aplicaciones

Protocolos:
- *De la web:* HTTP, HTTPS
- *MQTT:* facilita la comunicación de dispositivos y servidores, facilita la comunicación entre diferentes fabricantes, soporta grandes cantidades de datos solo cuando es necesario en lugar de mantener conexión constantes
- *CoAP:* proporciona un enfoque ligero para la comunicación entre dispositivos y servidores. Es ideal para dispositivos con baterías. Ligero y fácil de implementar
- *Websocket:* WenSocket se basa en TCP y permite streams de mensajes a ser enviados en ambos sentidos entre cliente y servidor, mientras se mantiene la conexión TCP abierta
- *DDS (Data Distribution Server):* es un middleware centrado en datos para la comunicación de dispositivos a dispositivos o maquina a maquina
- *XMPP (extensible messaging presence protocol):* es un protocolo para comunicación de tiempo real y streaming de datos XML entre entidades de red. XMPP soporta caminos de comunicación cliente a servidor y servidor a servidor

### Capa de procesamiento y almacenamiento
La capa de procesamiento y almacenamiento es responsable de procesar, almacenar y analizar los datos recopilados por los dispositivos IoT. Problemas:
- *Procesamiento en tiempo real:* capacidad para procesar y analizar datos rápidamente. **Edge computing:** procesamiento de datos cercanos a la fuente para reducir la latencia. Reduce la carga de la red al procesar datos localmente antes de enviarlos a la nube
- *Almacenamiento masivo:* manejo eficiente del almacenamiento de grandes volúmenes de datos. **Cómputo en la nube:** uso de servicios de la nube para almacenar y analizar grandes volúmenes de datos. Permite el acceso a datos desde cualquier lugar 

Los componentes de esta capa son: Servidores locales, edge computing, las nubes.
Las tecnologías: Bases de datos, sistemas de procesamiento de datos en tiempo real, análisis de grandes cantidades de datos


### Capa de gestión y orquestación 

La capa de gestión y orquestación se encarga de la gestión y orquestación de recursos de la red IoT. Proporciona herramientas para la configuración, monitoreo, actualización y administración de dispositivos y aplicaciones IoT.
La funcion de esta capa es la gestión de dispositivos, seguridad, actualizaciones de firmware y monitoreo de rendimiento.
Las *plataformas IoT*: proveen herramientas para la gestión centralizada de dispositivos. 
Los problemas de esta capa son:
- *Configuración y monitoreo:* necesidad de configurar y monitorear dispositivos de manera eficiente
- *Actualización de firmware:* capacidad de actualizar el software de los dispositivos de manera remota
Sus protocolos son:
*LwM2M:* proporciona herramientas para la configuración, monitoreo y administración de dispositivos IoT. Facilita la administración remota del firmware de los dispositivos

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

## Sistema Operativo para redes blockchain

Para las redes blockchain usaremos un modelo de capas de referencia. La organización en capas es bastante diferente que en las redes de computadoras. Ademas la capa de aplicación resuelve problemas adicionales típicos de las redes blockchain

### Capa de infraestructura base:

La capa de infraestructura base proporciona la infraestructura subyacente para la creación y operación de blockchains. INcluye componentes físicos y de red como internet (TCP/IP, HTTP, SSL, etc.) o enrutadores


### Capa de protocolo Base

La capa de protocolo base es la blockchain en si misma. Tiene su propia cadena de bloques con un diseño especifico, incluyendo su propio token nativo. Es responsable de la seguridad y el funcionamiento operativo de la red blockchain. Establece las reglas fundamentales de consenso y la estructura de datos principal. Facilita la comunicación entre nodos y el envío de transacciones. 
Es en esta capa donde se llevan a cabo las transacciones.

Un **mecanismo de consenso** establece las reglas y mecanismos mediante los cuales los nodos llegan a un acuerdo sobre el estado del libro mayor. Sus beneficios son:
- Usar mecanismo de consenso previene problemas como el doble gasto al garantizar que solo una versión del libro mayor sea aceptada por todos los nodos
- Usar mecanismos de consenso aumenta la resistencia a ataques maliciosos al requerir que un número significativo de nodos coincida en el estado del sistema. Algunos ejemplos de protocolos en esta capa son:
	- Bitcoin
	- Ethereum
	- Cardano
	- Solana

Las blockchains en esta capa suelen enfrentar limitaciones en su capacidad para procesar un gran número de transacciones por segundo, lo cual puede resultar en tiempos de espera prolongados y tarifas elevadas, especialmente en períodos de alta demanda. Para resolver esto se definen soluciones de escalabilidad

### Capa de Comunicación entre Redes Blockchain

En esta capa se usan protocolos que facilitan la interoperabilidad y la comunicación entre diferentes redes blockchain. Facilita la creaciónd e redes interconectadas y aborda problemas como la escalabilidad y la dicha interoperabilidad. Algunos ejemplos son *Polkadot* o *Cosmos*

### Capa de Soluciones de Escalabilidad

Esta capa mejora el rendimiento y la capacidad de procesamiento de transacciones al construirse sobre una blockchain existente. Permiten realizar un mayor número de transacciones fuera de la cadena principal, lo cual reduce la carga sobre la blockchain y disminuye los costos asociados, aunque se procura no comprometer la seguridad proporcionada por la blockchain. Sus protocolos son:
- *Rollups:* agrupan varias transacciones en un paquete: este paquetes se valida en una red secundaria y luego registran solo los resultados finales en la blockchain del protocolo base
- *Cadenas laterales:* blockchains independientes que están conectadas a una blockchain principal donde las cadenas laterales pueden procesar transacciones y ejecutar aplicaciones de manera independiente guardando los resultados en sus propios libros mayores, ademas pueden tener sus propios protocolos diferentes de la cadena principal
- *Canales de estado:* permiten transacciones rápidas y privadas entre dos partes sin necesidad de registrar cada transacción en la blockchain principal. Un canal de estado es un entorno temporal donde dos o mas partes pueden ejecutar varias transacciones directamente entre ellas sin involucrar a las blockchains principales. Al finalizar las interacciones el estado final del canal se registra en la blockchain principal, solo se pagan tarifas por abrir y cerrar el canal

### Capa de Aplicaciones

Permite la ejecución y acceso a las aplicaciones que interactúan con la blockchain. Aquí se encuentran las aplicaciones descentralizadas (dApps) que operan sobre la blockchain, así como aplicaciones no descentralizadas

Los contratos inteligentes permiten la ejecución automática de acuerdos cuando se cumples ciertas condiciones predefinidas, estos están registrados en la blockchain por lo que son inmutables y transparentes. Estos pueden gestionar transacciones complejas que involucran múltiples partes y condiciones, pudiendo hasta interactuar con otros contratos y dApps en la blockchain. Los contratos inteligentes minimizan el riesgo humano. Algunos ejemplos de dApps:
- *Finanzas descentralizadas (DeFi):* aquí los contratos inteligentes son fundamentales para gestionar préstamos, intercambios y otros servicios financieros sin intermediarios
- *Gestión de cadenas de suministro:* pueden rastrear productos a lo largo de la cadena de suministro, registrando cada paso en la blockchain para garantizar autenticidad y trazabilidad. Es una dApp siempre que use contratos inteligentes
- *Redes sociales:* ofrecen mayor privacidad y control sobre los datos personales, a menudo recompensando a los usuarios con criptomonedas por su participación
- *Votación:* redes que usan blockchains para mejorar la transparencia y la seguridad en los procesos de votación
- *Almacenamiento descentralizado:* permiten el almacenamiento y distribución de datos de manera descentralizada aumentando la seguridad y resistencia frente a fallos
- *Mercados NFTs*
- *Juegos*

Ejemplos de aplicaciones no descentralizadas:
- *Interfaces de usuarios*
- *Wallets*

### Capa de Desarrollo

Proporciona las herramientas necesarias para desarrollar y desplegar aplicaciones sobre blockchain. Las tecnologías específicas usadas son:
- Apis: permiten a los desarrolladores construir aplicaciones que se comunican con la blockchain sin necesidad de entender completamente su funcionamiento interno
- Bibliotecas: Facilitan el desarrollo de aplicaciones descentralizadas
- Plataformas de desarrollo: Entornos que permiten a los desarrolladores crear y desplegar dApps
- Frameworks para dApps: estructura que proporciona un conjunto de herramientas y bibliotecas par facilitar el desarrollo de dApps

Y los lenguajes suelen ser:
- Solidity
- JavaScript
- Python
- C++
- Go



# Sistemas Operativos de Redes 

Para manejar los tipos de redes a estudiar hacen falta *sistemas operativos de redes (SOR)*. En cada tipo de red hay un problema a ser resuelto si queremos que no tenga un mal desempeño, siendo la SOR quien se encarga de resolver estos problemas. Para que las máquinas en un tipo de red se puedan comunicar hacen falta *protocolos de comunicación*. Los SOR contienen estos protocolos.

Los SOR están organizadas como una pila de capas o niveles, donde la cantidad de capas, los nombres de estas, sus contenidos y su función difieren de un tipo de red a otro. El motivo de esta organización es lograr que cada capa le ofrezca ciertos servicios a las capas superiores ocultando su implementación. De esta forma una capa superior puede acceder a las operaciones y servicios primitivos ofrecidos por una capa inferior mediante le *Interfaz entre dichas capas* la cual es el conjunto de lo que puede ofrecer la capa inferior a la superior.
Además como el SOR se ocupa de la comunicación de información siempre debemos pensar como se comunica una capa $n$ de un dispositivos con la capa $n$ de otro dispositivo sin darle importancia a los problemas de capas inferiores a la $n$.

El *Protocolo de capa $n$* es el conjunto de reglas y convenciones usadas en la conversación entre la capa $n$ de una maquina y la capa $n$ de otra maquina.
Las comunicaciones entre capas consecutivas ocurren:
- **Durante el envío de mensaje:** cada capa pasa los datos y la información de control a la capa inmediatamente inferior, hasta que se alcanza la capa mas baja
- **Durante la recepción de mensaje:** cada capa pasa cierta información conteniendo los datos a la capa inmediatamente superior hasta que alcanza la capa mas alta   

Debajo de la capa 1 está el *medio físico*. Al conjunto de capas y protocolos se la llama *arquitectura de red* o pila de protocolos

# Sistemas operativos para redes de computadoras 

En una red de computadoras la red se usa para la comunicación entre estas. Para ello se pueden usar nodos intermediarios como conmutadores, enrutadores y puertas de enlace, un claro ejemplo es la *internet* 

Primero veremos cómo sería una jerarquía de protocolos para una red de computadoras.
- *Procesos de aplicación* (capa 5 o **capa de aplicación**): Produce un mensaje y lo pasa a la capa 4 para su transmisión 
- La capa 4 (**capa de transporte**): Pone un encabezado en el mensaje para identificarlo y pasa el resultado a la capa 3. Este encabezado contiene *números de secuencia* para que la capa 4 de la máquina destino entregue los mensajes en el orden correcto 
- La capa 3 (**capa de red**): Debido a que hay limitaciones en el tamaño de los mensajes de esta capa, divide en *paquetes* los mensajes entrantes colocándole un encabezado a cada paquete. Además, si la maquina es un enrutador, decide cuál de las lineas de salida existentes usar. Luego pasa los paquetes a la capa 2
- La capa 2 (**capa de enlace de datos**):Agrega un encabeza y un terminador a cada pieza, luego pasa las unidades resultantes a la capa 1 para su transmisión
- Luego en la máquina receptora el mensaje pasa de abajo hacia arriba de capa en capa, perdiendo los encabezados conforme avanza 

En las redes de computadoras hay varios problemas a resolver:
- **Como identificar las máquinas de una red?:**
	- *Solución:* Se usan direcciones para las máquinas
- **Control de flujo:** un emisor rápido satura de datos al receptor hasta que este ya no puede almacenar más datos que le llegan y comienza a perder datos 
	- *Solución:* Uso de retroalimentación al emisor, es decir, indicarle cuándo y cuánto puede enviar
- **Los mensajes que llegan no pueden ser aceptados por un protocolo de capa por ser demasiado grandes:** el mensaje grande llega de una red diferente que tiene un tamaño máximo de mensaje mayor al de la red actual, o hay capas consecutivas que aceptan distintos tamaños de mensajes 
	- *Solución:* fragmentar los mensajes, transmitir fragmentos y reensamblar los mensajes. Hay 2 tipos de soluciones, la *fragmentación transparente* y la *fragmentación no transparente*. En la primera los paquetes se van fragmentando y reensamblando luego de cada capa, mientras que en la segunda los paquetes no se vuelven a reensamblar hasta que no lleguen a su destino 
- **Congestión:** a veces en la red hay que enviar demasiados mensajes por la misma línea de salida de un enrutador y esta se pone más lenta o no puede mandarlos a todos(la red no puede manejar la carga de paquetes que recibe)
	- *Solución:* las computadoras emisoras se enteran de la congestión y reducen el tráfico de salida 


# Modelos de Capas para Redes de Computadoras


En nuestro caso veremos un modelo de capas híbrido con las siguientes capas con sus respectivas funciones y problemas:

1. **Capa de aplicación:**
	- *Función:* Aplicaciones de red middleware
	- *Problemas:* ---
2. **Capa de transporte:**
	- *Función:* Comunicación entre procesos
	- *Problemas:* retransmisiones, control de flujo y control de congestión 
3. **Capa de red:**
	- *Función:* Envío de paquetes entre 2 host usando rutas entre ellos
	- *Problemas:* Almacenamiento y reenvío, enrutamiento, control de congestión, fragmentación de mensajes 
4. **Capa de enlace de datos:**
	- *Función:* Comunicación entre máquinas conectadas directamente entre si
	- *Problemas:* Control de flujo, control de acceso a canal compartido, control de errores
5. **Capa física:**
	- *Funcion:* Transporte usando medios físicos de un stream de datos
	- *Problemas:* Medios físicos guiados y no guiados, interconexión de medios físicos de distinto tipo, teoría de señales

### Capa de Aplicación

En la capa de aplicación tenemos las aplicaciones de red. Cada una ofrece un servicio especifico con su propia forma de interfaz de usuario. Hay 2 opciones para desarrollar aplicaciones de red:
1. El programador para especificar la comunicación usa una API; la *socket API* es el estándar en facto para el software que se comunica sobre la internet
2. El programador se apoya en middlewares para construir la aplicación de red, donde el middleware provee servicios al software de la aplicación que hacen mas fácil a los desarrolladores implementar la comunicación y la entrada/salida de modo que se pueden enfocar en el propósito especifico de la aplicación 

#### TCP/IP

La capa de aplicación de TCP/IP contiene varios protocolos de nivel mas alto:
- FTP (transferencia de archivos)
- SMTP (correo electronico)
- DNS (resolucion de nombres de host en sus direcciones de red)
- HTTP (para la web)

En la capa de aplicación de Internet es muy importante *la web* y los protocolos que la soportan: HTTP, HTTPS, DNS.

En la web están los sitios web que son conjuntos de páginas web entrelazadas. Tambien están las aplicaciones web a las que se accede por medio de un navegador y realizan funciones similares a las aplicaciones de escritorio 

### Capa de Transporte

La capa de transporte provee comunicación entre procesos, mejorando los servicios de la capa de red. La capa de transporte se ejecuta por completo en los hosts. El software y hardware de esta capa se denomina **Entidad de transporte (ET)**

La capa de transporte debería solucionar ciertos problemas:
- Uso de *temporizadores* y las *retransmisiones de paquetes*
- Uso de búferes y control de flujo
- Evitar congestionar la red poniendo demasiados paquetes en ella
- El direccionamiento explicito de los destinos(solo si hay procesos cliente y procesos servidor)

#### Capa de transporte de internet

La capa de transporte del internet tiene 2 protocolos:
- **TCP:**  
	- TCP divide el flujo de bytes en mensajes discretos y pasa cada uno de ellos a la capa de interred. 
	- Proporciona una entrega confiable y en orden de los mensajes, es decir que el flujo de bytes se entrega sin errores a la maquina destino
	- TCP se encarga del *Reensamblado* de los mensajes recibidos en el receptor.
	- TCP maneja el *control de flujo* y *control de congestión* 
- **UDP:**
	- Proporciona entrega de mensajes no confiable y desordenada
	- No tiene confirmaciones de recepción de los mensajes, ni control de flujo, control de congestión o retransmisiones cuando se recibe un mensaje erróneo
	- UDP se suele usar para aplicaciones que no usan control de flujo ni la secuenciación de mensajes, aplicaciones que involucran consultas de solicitud-respuesta
	- Aplicaciones de transmisión de voz y vídeo


### Capa de Red

Los objetivos de la capa de red o capa 3 son:
- Algoritmos de almacenamiento y reenvío
- *Control de congestión*
- Resolver problemas que surgen cuando un mensaje tiene que viajar por redes de distinta tecnología para llegar a destino
- *Enrutamiento*


Un problema recurrente es la demora de llegada de un mensaje, el cual ocurre debido a que se toma la ruta mas larga entre la gran cantidad de rutas entre el origen del mensaje y su destino. Para ello existen los 
- *Algoritmos de enrutamiento:* Eligen la mejor/mejores rutas entre el origen y el destino

*Capa de interred:*
- Permite que los host inyecten paquetes dentro de cualquiera de las redes de la interred
- Los paquetes diferentes entre dos host viajan a su destino de manera independiente
- A causa de esto los paquetes pueden llegar en un orden distinto al cual fueron mandados. SI esto pasa, las capas mas altas deberían ordenarlos

##### Capa de red: TCP/IP

Para distinguir entre las diferentes máquinas que tienen una conexión a internet se usan direcciones IP que pueden ser de *IPv4 (32bits)* o *IPv6 (128 bits)* 
Se envían paquetes IP con su propio formato, y se usan protocolos de enrutamiento como *OSPF* y *BGP* para enrutamiento de paquetes

### Capa de enlace de datos:

El objetivo de la capa de enlace de datos es transformar un medio de transmisión puro en una línea de comunicación que aparezca libre de errores de transmisión

*Problemas de diseño que se consideran:*
- Fragmentación de paquetes en tramas, cuando un paquete es demasiado grande para ser aceptado por la CED
- *Tramas de confirmación de recepción* son usadas cuando el servicio es confiable
- *Control de flujo*
- *Control de acceso a un canal compartido:* Se busca manejar y minimizar o evitar colisiones, las cuales ocurren cuando varias maquinas comparten un mismo canal de comunicaciones y envían tramas en simultaneo usando este canal

A la hora de controlar errores en los mensajes debido a imperfecciones en el medio físico, es necesario que los mensajes lleven cierta información extra con el propósito de control de errores. De esta forma se pueden aplicar alguno de los siguientes 2 enfoques:
- Identificación de errores y retransmisión de mensajes erróneos
- Corrección de errores en el mensaje recibido


### Capa física

El propósito de la capa física es transportar un stream de datos de una máquina a otra usando medios físicos. Aun así la CF no existe solo en medios físicos, estos últimos se conectan entre si usando dispositivos como modems, multiplexores, etc.

*Medios físicos:*
- Bit: se propaga entre pares transmisor/receptor
- Enlace físico: lo que yace entre el transmisor y receptor
- Medios guiados: las señales se propagan en medios sólidos: cobre, fibra óptica, coaxial
- Medios no guiados: las señales se propagan libremente: radio
- Par trenzado: 2 cables de cobre aislados
- cable coaxial: 2 conductores concéntricos de cobre, bidireccionales, broadband (múltiples  canales en el cable)
- Cable de fibra óptica: Fibra de vidrio que transporta pulsos de luz, cada pulso es un bit. Operan a alta velocidad y tienen baja tasa de errores
- Radio: señal transportada en el espectro electromagnético, no usa cable físico, es bidireccional. Hay efectos de propagación de entorno: reflexión, obstrucción por objetos,, interferencia


# REORDENAR DESPUES

## Arquitectura de microservicios

Los **requisitos Funcionales** de esta arquitectura son:
- *Provisión de servicios* especializados: proporcionar funciones únicas y biend efinidas
- *Comunicación entre servicios:* para cumplir con tareas más complejas
- *Consumo de servicios:* los clientes o aplicaciones deben poder solicitar y recibir servicios de manera eficiente

**Requisitos no funcionales:**
- *Escalabilidad:* escalamiento independiente de cada servicio según demanda.
- *Flexibilidad:* en el desarrollo y despliegue, los sesrvicios deben adaptarse a los cambios en las necesidades del negocio
- *Mantenibilidad:* fáci implementar nuevas funcionalidades
- *Seguridad:* se pueden implementar politicas de seguridad más centralizadas y consistentes a través de los servicios. Garantizar la seguridad de los datos y las transacciones entre servicios
- *Independencia y autonomía:* cada servicio debe ser capaz de desarrollarse, implementarse y escalarse de manera independiente
- *Resiliencia:* los servicios deben diseñarse para tolerar fallos y mantener la operación continua, incluso si uno de ellos falla

Por la necesidad de abarcar dichos requisitos es que nace la **arquitectura de microservicios** como una evolución de la **SOA**. En esta la aplicación se divide en pequeños servicios independientes que se comunican entre sí a través de APIs que no dependen de un lenguaje especifico. Cada microservicio se especializa en una sola tarea y se encarga de una funcionalidad especifica, además pueden actuar tanto como cliente, como servidor dependiendo del contexto y la tarea que se está realizando. 
Para la comunicación se usa APIs REST, o gRPC 

Los Nodos o roles existentes en esta arquitectura son:
- *Servicios independientes:* componentes funcionales de aplicación que interactuan entre si
- *API gateway:* intermediario que gestiona las solicitudes de clientes y mocroservicios
- *Clientes:* aplicaciones que consumen los servicios

Los **mensajes de comunicación** son:
- Clientes a API gateway: solicitudes de datos, comandos
- API gateway a microservicios: ruteo de solicitudes a los microservicios correspondientes
- Microservicios a API gateway: respuesta a las solicitudes, resultados de las operaciones
- Microservicios entre si: comunicación inter-servicios para operaciones complejas

Junto con esos mensajes los protocolos usados suelen ser SOAP o REST para la comunicación entre servicios

## Protocolos de capa de aplicación

Para hacer un diseño detallado de una aplicación de red sobre internet conviene definir un protocolo de capa de aplicación. Este se suele apoyar o no en un protocolo de base

### FTP: Protocolo de Transferencia de Archivos

Algunas caracteristicas de FTP:
- Usado para transferir archivos hacia/desde un host remoto
- Cada archivo tiene restricciones de acceso y poseción
- FTP permite inspeccionar carpetas
- FTP permite mensajes de control textuales

Usa modelo cliente/servidor y els ervidor se conecta mediante el puerto 21.

Se intercambian 3 tipos de paquetes:
- Uso de *comandos* enviados al servidor FTP que son enviados como texto ASCII sobre un canal de control
- 	*sintaxis:*
- 		User username
- 		PASS password
- 		LISTS return list of file in current directory
- 		RETR filename retrieves giles
- 		STOR filename stores file onto remote host
- *Mensajes de Respuesta:* a comandos del servidor FTP
- 	*sintaxis:*
- 		Código de estatus y frase
- *Mensajes con datos enviados*


Las reglas(o pasos) de FTP son:
1. Cliente FTP contacta servidor FTP en puerto 21 usando TCP
2. El cliente es autorizado en la conexión de control
3. El cliente inspecciona directorio remoto, envía comandos sobre la conexión de control, se comienza con identificación de ususario y password
4. Cuando el servidor recibe un comando de transferencia de archivo, el servidor abre una 2da conexión de datos TCP para el archivo con el cliente
5. Luego de transferir un archivo, el servidor cierra la conexión de datos.

El servidor abre otra conexión TCP de datos apra transferir otro archivo.
El servidor mantiene el "estado:" directorio corriente, autenticación previa 


## La WEB

Para las paginas web suelen ser importantes los datos y la información. En el mundo hay entidades y relaciones entre entidades. Los datos se refieren a los datos de esas entidades y relaciones. Dichos datos suelen estar en bases de datos siendo estas una de las fuentes de datos que usan las páginas web.

Los datos se procesan de determinada manera y se obtiene lo que se llama información. Esta información es la que tienen las paginas web pudiendo ser organizadas de distinta forma en base a los datos extraidos, no necesariamente en formato de texto, pueden ser diagramas, imagenes, figuras, tablas. Aun asi una página web puede ser solo de datos o solo de información

Se pueden utilizar lenguajes de consulta para expresar consultas sobre datos con el posible fin de generar información. Las consutas son procesadas por motores de bases de datos apra retornar los datos deseados. 

Para ver los datos deseados otra alternativa a escribir consultas en lenguaje de consultas es **navegar**. Al navegar uno va viajando por una serie de pantallas que contienen los datos que desea inspeccionar. Llamamos hipertexto a un conjunto de textos donde cada uno de los cuales contiene enlaces a otros textos. Al seleccionar un enlace se muestra el texto deseado enlazado. Por ende recorrer varios hipertextos es navegar.
Además nos vamos a referir con medias a cosas como fotos, videos, audios, gráficos. Con esta idea podemos generalizar el hipertexto a **hipermedia** donde tenemos un conjunto de nodos donde cada nodo puede tener texto y medias Y enlaces a otros nodos

Con estos conceptos ya podemos decir que una Página Web puede contener vinculos a otras páginas web ubicadas en cualquier lugar del mundo y que si bien una página suele contener texto, tambien puede referencias varios objetos

Las **páginas web estaticas** son simplemente documentos en algún tipo de formato usando HTML5.
Como la información cambia frecuentemente estas pueden ser muy ineficientes, ya que deberiamos modificarlas a mano. Para solucionar esto surgen las **Páginas dinamicas** donde las páginas HTML son generadas por medio de programas que se ejecutan del lado del servidor que toman parámetros de entrada que suelen ser ingresados como valores de formularios.

Que el servidor tenga que construir páginas dinamicas puede ser ineficiente támbien por varios motivos:
1. La página nueva que genero el servidor puede tener mucho en comun con la que ya se encontraba en el browser, repitiendo una parte a ser enviada por la red
2. El cliente se queda bloqueado esperando luego de hacer un pedido HTTP al servidor web y recién puede continuar ejecutandose cuando recibe una página. Estos llamados **pedidos sincronicos** pueden ser conflictivos si el procesamiento de un pedido del lado del servidor toma mucho tiempo ya que el no poder usar la aplicación web mientras tanto para otra cosa puede ser bastante desagradable

La solución a estos problemas es usar una **página única**. Cuando se entra en la aplicación web el servidor web manda una página única al browser que contiene una interfaz con el ususario completa con apariencia similar a las interfaces de usuario de aplicaciones de escritorio. Desde esta página única se pueden hacer los pedidos de datos al servidor web, donde este ultimo solo se encarga de obtener los datos, no de computar las páginas de forma tal que luego de hacer el pedido de datos la aplicación puede seguir haciendo otras tareas mientras se procesa el pedido. A esto se lo llama **pedido asincronico**. Luego cuando llegan los datos se actualiza la interfaz del usuario

### URLs

Como todo enlace incrustado en una página web necesita una manera de nombrar a otra página web y similarmente un objeto referenciado por una página web necesita una manera de ser nombrado, las páginas/objetos se nombran usando URLs (Localizadores Uniformes de Recursos) que son conformados por:
- Nombre del protocolo (HTTP)
- Nombre de dominio de host que contiene la página
- El nombre del archivo que contiene la página(camino al archivo)

El problema de este formato es que no es suficiente para especificar la página dinámica deseada o el programa que obtiene los datos deseados. Es necesario tener parámetros para la creación de páginas dinámicas o para el programa que obtiene datos y es necesario poder ingresar los parámetros en el pedido HTTP.

La primera solución es que la URL contenga el nombre de programa y parámetros, donde estos ultimos son ingresados por medio de un formulario HTML. En esta solución los parametros son pares $\text{nomre=valor}$, se separa el nombre del programa con ? y los parametros con &.

Otra solución es que los aprametros se ingresan separados por & en un campo especial del pedido HTTP llamado *cuerpo de la entidad* donde los URL tienen tamaño maximo, cuando los parámeetros exceden ese tamaño máximo no se puede usar la solución 1, ahi es se torna util la 2da solución


### La web

Un **sitio Web** es un conjunto de páginas web relacionadas localizadas bajo un único nombre de dominio y publicadas por al menos un servidor web, tipicamente producida por una organización o persona. Estos sitios se centran en entregar contenido mediante, usualmente, páginas estaticas

Una **Página de inicio** de un sitio wewb es una página de entrada al sitio web que sirve de guia hacia las páginas que contienen la información necesaria, suele ser la página que se carga por default al navegar

### Aplicaciones web

Las **aplicaciones web** retornan y almacenan información usando scripts del lado del servidor y del lado del browser ejecutan también scripts para diversas tareas. Las mismas suelen soportar tareas, funciones o procesos, siendo su objetivo principal que el usuario realice una o más tareas

En una **aplicación web social** los usuarios pueden crear y compartir contenido, además de comunicarse entre si mediante posts, comentarios y mensajes.

La **Web 2.0** son sitios y aplicaciones que hacen uso de contenido generado por usuarios finales y se caracteriza por una mayor interaccion del usuario, una mayor colaboracion de los usuarios y canales de comunicación mejorados.

Actualmente esta en desarrollo la **Web 3.0** caracterizada por:
- Descentralización: los usuarios están en control de sus datos, los usuarios son dueños del valor que generan, conexiones P2P
- Blockchain: permite transacciones más seguras, privacidad de datos y propiedas
- Web semántica: losd atos tienen significado y son legibles por computadoras, considerandose:
- 	Datos enlazados abiertos: se identifican objetos con URLs, al ver una URL se accede a información util. Dentro de la información a un URL puede haber enlaces a otros URL
- 	Metadatos semánticos: etiquetas semánticas agregadas a las páginas web para describir mejor su significado
- Uso de inteligencia artificial: procesamiento de lenguaje natural y aprendizaje automatico


Para ver las páginas web se usa un *navegador*. Este permite pedir mediante el protocolo HTTP una página/objetos a un servidor web. Una página pedida puede ser dinámica, estatica o una página única. El servidor web retorna la página en respuesta al pedido del navegador. Si els ervidor retornó una página, el navegador interpreta el texto y los comandos de formateo que contiene la página y despliega la página adecuadamente formateada en pantalla.

Un problema que surge con esto es que para poder desplegar una página el navegador tiene que entender su formato. Para que los navegadores entiendan las páginas web estas se escriben en un lenguaje llamado HTML

Para realizar la comunicación entre el browser y el servidor web hay un orden que seguir:
1. El cliente inicica una conexión TCP con el servidor web, usando el puerto 80
2. El servidor web acepta la conexión TCP del cliente
3. Mensajes HTTP intercambiados entre el browser y el servidor web
4. La conexión TCP se cierra

Con HTTP el servidor no mantiene información acerca de pedidos del pasado del cliente. Los protocolos que mantienen el "estado" o historial son complejos

Como no todas las páginas contienen solamente HTML, cuando un servidor regresa una página también regresa alguna información adicional acerca de ella llamado tipo MIME. Si este tipo MIME no es uno de los integrados, el navegador consulta una tabla de tipos MIME que asocia un tipo MIME con un visor.



Para desarrollar visores se usan plug-ing y aplicaciones auxiliares.
**Un Plug-in** es un módulo de código que se ejecutan dentro del proceso del navegador. Estos son instalados por el navegador como una extensión de si mismos. Por consecuencia, los plugins tienen acceso a la página actual y pueden modificar su apariencia.
La *interfaz del plugin* es un conjunto de procedimientos que todos los plugins tienen que implementar a fin de que el navegador pueda llamarlos. Mientras que la *interfaz del navegador* es un conjunto de procedimientos del navegador que e plugin puede llamar. Una vez que un plugin completa su trabajo, se lo elimina de la memoria del navegador.

**Las aplicaciones auxiliares** se ejecutan en un proceso separado del browser, no ofrecen interfaz al navegador ni usan servicios de este. Suelen aceptar el nombre de un archivo y lo abren y despliegan

### Servidores Web

A un *servidor web* se le proporcionará el nombre de un archivo correspondiente a una página a buscar y regresar. También se le puede proporcionar el nombre de un programa con parámetros a ejecutar. Un servidor web se lo puede ver como una computadora que almacena *software del servidor web* y archivos como documentos HTML, imágenes, archivos JavaScript, etc.

Para optimizar el acceso a las páginas estaticas en disco se usa la caché de páginas estaticas en la memoria. Para ahcer aún mas rapido el servidor web se opta por una arquitectura con un módulo frontend y k modulos de procesamiento MP (hilos)

Ahora veremos los pasos de un servidor web con múltiples hilos para manejar pedidos de páginas estáticas:
1. Cuando llega una solicitud el frontend la acepta y construye un registro corto que la describe
2. Después entrega el registro a uno de los MP
3. Si se trata de un pedido de página estatica el MP primero verifica la caché para ver si el archivo está allí
4. Si el archivo está en la cache actualiza el registro para incluir un apuntador al archivo
5. Si el archivo no está en caché el MP inicia una operación de disco. Cuando el archivo lelga del disco, se coloca en la caché y se regresa al cliente
6. Mientras uno o mas MP están bloqueados esperando a que termine una operación del disco, otros MP pueden estar trabajando en otras solicitudes
7. Conviene tener además múltiples discos, para que más de un disco pueda estar ocupado al mismo tiempo

Las arquitecturas actuales muestran una división entre frontend y backend donde al frontend se lo llama proxy reverso, porque retorna contenido de otros servidores backend y sirve estos objetos al ciente. También exiten soluciones que ponen en caché páginas creadas dinámicamente


### Cookies

Una cookie es un pequeño archivo o cadena con contenido en forma de nombre=valor que se usa en los pedidos y respuestas HTTP se envía información de estado de sesión.
Los campos de una cookie son:
- *dominio* (nombre del dominio destino de la cookie)
- *ruta* en la estructura del directorio del servidor. Identifica que partes del árbol de archivos del servidor podrían usar el cookie
- El *campo contenido* toma la forma nombre = valor
- El campo *expira* el cual si esta vacio el navegador descarta la cookie cuando sale. Pero si se proporciona una fecha y hora, el navegador mantiene la cookie hasta que expire dicho horario
- El campo *seguro* que se usa para indicar que el navegador solo puede retornar la cookie a un servidor usando un transporte seguro. Estos e usa para aplicaciones seguras como comercios electronicos.

Si se quiere eliminar una cookie del disco duro del cliente lo que se hace es que els ervidor mande la misma cookie nuevamente pero con la fecha caducada.

Para almacenar las cookies se usa un directorio de cookies para que el navegador pueda guardar las cookies en el disco duro de la máquina del cliente con la opcion de guardar la información en una base de datos.

**Comunicación de cookies al cliente:**
-	Cuando un cliente solicita una página web, el servidor puede proporcionar una cookie junto con la página solicitada

**Comunicación de las cookies al servidor web:**
- Antes que un navegador solicite una página a un sitio web, verifica su directorio de cookies para ver si el dominio al que está solicitando la página ya colocó alguna cookie
- De ser así, todas las cookies para ese dominio se incluyen en el mensaje de la solicitud
- Cuando el servidor web las obtiene, puede interpretarlas de la forma que desee


**Necesidades para un protocolo para la web**
*Cosas que se necesita que soporte un protocolo para la web:*
- Pedido de páginas, de objetos o de ejecución de programas que generan páginas
- Manejo del estado de sesión
- Poder mantener el sistema de archivos del servidor web
- Recepción de páginas por un browser
- Seguridad (encriptación de mensajes)
- Feedback adecuado cuando no se puede responder los pedidos
- Comunicación confiable


### HTTP

**HTTP:** *Hyper Text Transfer Protocol*. Transfiere páginas de servidores web a navegadores y manda pedidos de navegadores a servidores web. Soporta 2 tipos de mensaje:
- HTTP-Request(de navegador a servidor web)
- HTTP-Response (de servidor web a navegador web)


#### Conexiones HTTP

Existen 2 formas de HTTP, el persistente y el no persistente.

El *HTTP no persistente:*
- A lo sumo un objeto se manda por conexión TCP para luego cerrar la conexión
- Descargar múltiples objetos requiere de muchas conexiones
- 	En HTTP 1.0 se establece una conexión TCP por cada solicitud y se libera al recibir respuesta

Este modelo de HTTP no es optimo, ya que para descargar una página estática puede ser necesario establecer varias conexiones 

Para eso existe el *HTTP persistente*, en el cual:
- Múltiples objetos pueden ser enviados a través de una única conexión TCP entre el cliente y el servidor
- Bajo una misma conexión TCP los pedidos son procesados en orden y los resultados se mandan en orden
- Soportado por *HTTP 1.1*

**RTT (definición):** tiempo necesario para que un paquete pequeño viaje del cliente al servidor y de regreso.

De esta forma podemos calcular el tiempo de respuesta de HTTP no persistente para recibir un archivo:
- Un RTT para iniciar la conexión TCP
- Un RTT para el pedido HTTP y el regreso de los primeros bytes de la respuesta HTTP
- Tiempo de transmisión del archivo
- Tiempo de respuesta de HTTP no persistente = $2RTT + \text{tiempo de transmisión del archivo}$

Con HTTP 1.1 se pueden hacer varios pedidos bajo una misma conexión, pero van a ser procesados en orden y los resultados van a ser enviados en orden.
Esto trae varios problemas, ya que no se envían documentos al browser aunque se sepa que se los va a necesitar ya que el servidor va a esperar que sean pedidos. Además no permite recibir varios pedidos, priorizarlos y reordenar las respuestas en el orden mas pertinente 

Por ello se creo el protocolo *HTTP 2.0* en el cual:
- Por medio de un mecanismo server push empuja archivos que sabe que van a necesitarse pero que el cliente puede no saber inicialmente
- Las respuestas a los pedidos pueden volver en cualquier orden
- HTTP 2.0 comprime los encabezados y los envía en binario para reducir el uso de banda ancha
- Cada respuesta lleva un identificador de su pedido
 Hoy en dia tanto Apache HTTP como Ngix soportan HTTP 2.0

#### Pedidos HTTP

Un mensaje de pedido deberia tener la siguiente información:
- En caso que se quiera recibir una página:
- 	El URL de un documento
- 	La especificación de programa que genera la página web
- El *tipo de acción* que se quiere hacer en el sistema de archivos del servidor web(meter páginas, borrar páginas, etc.)
- Mandar *información sobre la máquina/software dek cliente* para que el servidor web pueda retornar páginas adecuadas al cliente
- Mandar *información de estado de sesión* para que el servidor se entere
- *Restricciones sobre el tipo de páginas* que el cliente puede aceptar


Para indicar el tipo de acción que se quiere hacer se usa un campo al principio de la linea donde se pone el nombre del *método* que se quiere usar:
- *Método Post:* Se usa cuando las páginas tienen un input de formulario. Este input es subido al servidor en un campo llamado **cuerpo de la entidad**
- *Método que usa URL:* El metodo GET sirve para sacar la información de una URL concreta, de esta forma el input es subido en el campo URL de la línea del pedido
- *Método PUT:* Sube un archivo en el campo cuerpo de la entidad en el camino especificado por el campo URL
- *Método DELETE:* Borra el archivo especificado en el campo URL
- *Método HEAD:* simplemente solicita el encabezado de la respuesta del servidor web, sin la página o datos de la respuesta, o sea, feedback sobre el resultado del pedido, tipo de contenido, etc.
- *Método OPTIONS:* permite que el cliente consulte al servidor por una página y obtenga los métodos y encabezados HTTP que pueden ser usados con esa página. Aunque tambien se puede usar para saber los métodos HTTP soportados por el servidor web en general

Para enviar mas información diversa lo que se hace es indicar el tipo de información de la que se trata y luego la información en si(body{}, params{}, etc)

#### Respuestas HTTP

La información que deberia tener un mensaje de respuesta:
- Feedback adecuado sobre el pedido realizado (como cuando no se puede cumplir el pedido)
- Página o documento solicitado
- En ese caso información sobre el tipo de documento enviado (como el tipo MIME, ultima modificación, etc.)
- Información de estado de sesión para mantener actualizado al cliente

Para poder especificar en la respuesta el feedback sobre el pedido recibido se usa un código y un mensaje. El código de estado es de 3 dígitos y indica si la solicitud fue atendida o no. Mientras que para mandar además de la página solicitada información adicional en una respuesta HTTP se usan *encabezados de respuesta* que son pares de encabezado y valor donde de indica el tipo de información de la que se trata y luego la información en sí.

Es decir que finalmente las respuestas HTTP tienen el siguiente formato:
1. *Línea de estado*
2. *Encabezado de respuesta*
3. Luego viene el cuerpo de la respuesta

#### Encabezados HTTP

Los mensajes HTTP suelen tener *encabezados.* de pedido, respuesta o de ambos tipos.
Estos encabezados se usan para *proveer información* a ser procesada por el receptor del mensaje, también se usan para *fijar restricciones* que deben cumplir mensajes futuros(tipos de páginas que pueden manejar los clientes, conjuntos de caracteres aceptables, etc.), para proveer información sobre *eventos* importantes o para proveer datos de *estado de la sesión*

### HTML

*HTML* es el lenguaje estándar para crear páginas web. Este describe la estructura de una página web e indica al navegador como mostrar el contenido de la página. La sintaxis es muy parecida a XML. Con HTML uno podria representar:
- Páginas que incluyen texto, gráficos, hipervínculos, etc.
- *Tablas* y *formularios*

Un documento HTML es una serie de *elementos*. Pero ¿Que es un elemento? Bueno, un elemento es simplemento contenido cerrado entre *etiquetas* donde cada etiqueta tiene un nombre y esta demarcada entre '<','>'. Estas etiquetas pueden tener o no atributos, los cuales tienen un nombre y un valor separados por '='.

**Pasos para generar páginas diámicas del lado del servidor:**
1. Un usuario llena un formulario y hace click en el botón de envío
2. Se envía un mensaje al servidor web con el contenido del formulario. Se proporciona el mensaje a un programa o una secuencia de comandos. El programa procesa el mensaje
3. El programa solicita información a un servidor de bases de datos
4. El servidor de bases de datos responde con la información requerida
5. El programa genera una página HTML personalizada y la envia al cliente
6. El browser muestra la página recibido al usuario

Recordemos que las páginas dinamicas son páginas web creadas por programas que se ejecutan en el servidor. Suelen hacer las siguientes tareas:
- Procesar parámetros de formularios
- Procesar encabezados de pedido HTTP
- Pedir datos a fuentes de datos
- Generar páginas web con los datos recibidos
- Generar encabezados de respuesta HTTP


#### PHP

**Enfoque PHP (procesador de hipertexto):**
- Se definen páginas dinámicas mediante la inserción de comandos especiales dentro de páginas HTML.

Para utilizar PHP el servidor web tiene que entender PHP. Ya que normalmente el código PHP es interpretado por un servidor web. PHP se diseño para trabajar con el servidor web Apache, aunque hoy en dia puede ser usado en la mayoria de servidores web.
Algunas cosas que puede hacer PHP:
- Generar contenido de página dinpamica
- Operar con archivos en el servidor
- Recolectar datos de formulario
- Enviar y recibir cookies
- Acceder a encabezados de pedido HTTP
- Definir encabezados de respuesta HTTP
- Acceder a base de datos

PHP es gratuito y fácil de aprender y se ejecuta eficientemente.


##### Acceso a campos de formularios
- *$_POST:* usado para recoelctar datos de formulario luego de someter un formulario con método POST
- *$_GET:* usado para recoelctar datos de formularios luego de someter un formulario con método GET.

**Tipos ded atos de PHP:**
- String: secuencia de caracteres entre comillas
- Integer: número entero
- Float: número con punto decimal o número en forma exponencial
- Boolean: valores booleanos TRUE y FALSE
- Array: un arreglo almacena varios valores en una variable
- Object: PHP permite definir clases y objetos

**Operadores:**
- De comparación, de asignación
- Para los distintos tipos de datos

**Acceso a información de encabezados HTTP:**
- $_SERVER: contiene información de encbezados, caminos y localización de scripts
- Para acceder a encabezados poner como agumento alguna de las siguientes:
- 	HTTP_USER_AGENT, SERVER_ADDR, SERVER_NAME, SERVER_SOFTWARE, SERVER_PROTOCOL, REQUEST_METHOD, REQUEST_TIME, QUERY_STRING, HTTP_ACCEPT, HTTP_CHARSET, HTTP_HOST, etc.

**Definición de encabezados de respuesta HTTP:**
- Hay que usar la función header()
- Se deben fijar encabezados antes de la etiqueta <html aparezca


**Definición de Cookies:**
- Setcokkie() define cookie para ser enviada junto con el resto de los encabezados HTTP
- Esta función debe usarce antes de generar cualquier salida, o sea antes que la etiqueta.
- Un cookie se crea con la función setcookie(name, value, expire, path, domain, secure, httponly)

**Acceso al valor de una cookie:**
- $_COOKIE se usa para retornar el valor de una cookie
- htmlspecialchars convierte caracteres especiales en entidades HTML

## Capa de Protocolo Base de Redes Blockchain 

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
- 	*Nonce:* número aleatorio usado durante el rpoceso de minería para encontrar un hash valido
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
- *Delegated Proof of Stake(DPoS):* Los usuarios votan por *delegados* para validar bloques; estos delegados reciben recompensas por su trabajo. Los delegados pueden validat y agregar nuevas transacciones a la blockchain. Esto incluye validación de bloques y confirmación de transacciones. DPoS es rápido y eficiente. Permite votaciones directas por parte del usuario final. DPoS puede ser menos descentralizado si pocos delegados dominan las votaciones.
- *Byzantine Fault Tolerance(BFT):* un *lider* propone nuevos bloques mientras otros nodos verifican su validez antes del consenso generalizado. Luego de la validación, se hace una votación por nodos participantes del consenso para determinar si aceptan o rechazan el bloque propuesto. Para alcanzar el consenso se requiere que mas del 66% de los nodos honestos esten de acuerdo. Existen mecanismos para detectar nodos deshonestos e ignorarlos durante el proceso de consenso. BFT garantiza alta velocidad y tolerancia a fallos bizantinos, incluso con presenciasignificativa de actores maliciosos. BFT requiere confianza inicial en el lider o estructura jerárquica establecida dentro del sistema

### Bitcoin

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

### Ethereum

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
Al calcular el nuevo estado global, guardan también los cambios incrementales(deltas) que se producen en el estado para poder reconstruir cualquier estado hístorico


## Decisiones de Diseño de Aplicaciones Distribuídas para Redes Blockchain

Para desarrollar una aplicación blockchain, hay que decidir en que facilidades se apoya. Las facilidades de la arquitectura de capas son:
- Protocolos basem comunicación entre blockchains y soluciones de escalabilidad
- Infraestructura de desaroollo proporcionada por capa de desarrollo

Otras aplicaciones:
- Almacenamiento descentralizado: IPFS, Filecoin
- Oráculos: ChainLink
- Plataformas de pago: MoonPay

Hay algunas decisiones sobre las capas en las que se apoya la aplicación distribuida:
- Modelo de consenso que conviene usar
- Elección de Plataforma de blockchain(protocolo base)
- Estrategía de escalabilidad
- Si se va a usar o no capa de comunicación entre blockchains

**Decisiones sobre el modelo de datos:**
- Decidir datos a almacenarse en la blockchain, algunos ejemplos incluyen:
- 	*Transacciones:*
- 	*Contratos inteligentes:* código y lógica del contrato, resultados de la ejecución de los contratos
- 	*Hashes de datos:* en lugar de almacenar un archivo se almacena un hash criptográfico del mismo. Esto es para asegurar que el contenido no ha sido alterado
- 	*Identidades y claves:* identificadores únicos o claves públicas. Certificados dígitales para autenticación
- 	*Registros de eventos:* información sobre eventos importantes de la aplicación, como logs de auditoría, cambios de estado o confirmaciones de acciones dentro del sistema
- 	*Votaciones y decisiones:* en aplicaiones de gobernanza se almacenan: votos emitidos por los participantes y resultados de las decisiones tomadas colectivamente
- 	*Propiedad y derechos:* registro de propiedad de activos digitales, derechos de uso o acceso asociados con los activos
- Decidir datos a almacenarse fuera de la blockchain:
- 	*Datos voluminosos:* como imágenes, videos, documentos o bases de datos extensas. Estos datos se mantienen en sistemas externos como:
- 		Almacenamiento descentralizado: que son adecuados para compartir archivos de manera distribuida como IPFS o Storj
- 		Almacenamiento centralizado: algunos proyectos recurren a servidores tradicionales para almacenar datos
- 	*Datos confidenciales:* información privada de los usuarios como direcciones, números de contacto, etc.
- 	*Procesos computacionales intensivos:* aplicaciones que requieren cálculos complejos como aprendizaje automatico o simulaciones suelen hacerlo fuera de la blockchain y solo registran los resultados relevantes en la cadena
- 	*Datos temporales:* como actualizaciones de precios, resultados deportivos, etc. se mantienen fuera

**Decisión sobre aplicaciones externas a usar**
Las dApps suelen apoyarse en herramientas y sistemas externos para complementar sus funcionalidades y superar algunas de las limitaciones inherentes a la blockchain

Principales categorias de aplicaciones externas:
-	*Almacenamiento descentralizado:* para almacenar grandes vólumenes de datos eficientemente mientras amntienen la seguridad y la descentralización: como IPFS y plataformas de almacenamiento en la nube descentralizadas
-	*Oráculos:* para acceso a datos externos del mundo real.
-	*Redes de computación:* para realizar cálculos intensivos o procesar datos grandes. Por ejemplo servicios centralizados en la nube, redes descentralizadas de computación colaborativa
-	*APIs externas:* como los servicios de pago, datos financieros en tiempo real
-	*Gestión de identidad:* para facilitar la autenticación de ususarios y manejo de identidades descentralizadas como: Civic, uPort
-	*Almacenamiento centralizado:* para almacenar archivos
-	*Plataformas de análisis y visualización:* para proporcionar insights a los usuarios

**Decisiones sobre la economía de tokens:**
La economia de tokens refiere a cuando muchas aplicaciones usan sus propios tokens. Por ende interesa definir puntos como:
- *Proposito:* utilidad del token dentro de la app distribuida
- 	Un token de utilidad está diseñado para acceder a ciertos servicios o funciones
- 	Un token de gobernanza permite a los poseedores participar en decisiones sobre el futuro de la aplicación
- 	Un token de inversión el cual representa activos financieros, como acciones o derechos de propiedad
- 	Un token de recompensa que se usa para incentivar a los usuarios por acciones específicas
- Suministro: se refiere a la cantidad total de tokens que existiran o que estaran disponibles en circulación
- 	Un roken puede tener suministro fijo, otros pueden ser inflacionarios, o deflacionarios
- Distribución: se refiere a como se reparten los tokens entre los diversos participantes
- 	distribución inicial: puede incluir eventos como una ICO(oferta inicial de moneda) o Airdrops
- 	Asignación: Una parte del suministro podría destinarse al equipo fundador, desarrolladores, inversores iniciales o comunidades
- 	mecanismo de distribución: a través de minería, staking o recompensas por participar

**Decisiones a tomar debido al uso de contratos inteligentes:**
- Proposito del contrato: objetivo del contrato, problema que resuelve, acciones que automatizara
- Funciones del contrato: Definir parametros para ellas
- Roles que interactuan con el contrato:¿Como los distintos tipos de usuario interactuan con el contrato?¿Quienes acceden a qué funciones?
- Datos del contrato: ¿Que almacenar?, estructuras de datos,¿Que datos almacenar en la blockchain y cuales no?
- Reglas del contrato: las reglas definen el comportamiento del contrato
- 	Tipos de reglas:
- 		condiciones y restricciones
- 		autorización: quien tiene permiso para ejecutar ciertas funciones del contrato
- 		validaciones: controles para garantizar que las transacciones cumplen con las reglas establecidas
- Decidir acciones que se ejecutan automáticamente: los contratos inteligentes son autoejecutables, lo que significa que ciertas acciones se realizan automaticamente cuando se cumplen las condiciones como por ejemplo:
- 	Transferencias automáticas
- 	Gestión de recompensas
- 	Penalizaciones
- Mecanismos de seguridad: medidas para evitar vulnerabilidades y ataques
- Escalabilidad: ¿el contrato puede manejar más usuarios o transacciones en el futuro?
- Interacción con otras herramientas: oráculos para recibir datos externos, aplicaciones de almacenamiento descentralizados, etc.
- Eventos generados por el contrato: los contratos pueden emitir eventos para informar a los usuarios o aplicaciones externas cuando ocurre algo relevante. Por ejemplo:
- 	Registro de una transferencia de tokens
- 	Notificaciones de actualización de estado en el contrato
- 	Eventos útiles para aplicaciones descentralizadas que escuchan estos datos en tiempo real
- Interacción con otros contratos: en muchas aplicaciones distribuidas, los contratos inteligentes interactuan entre si para lograr tareas más complejas como:
- 	*llamada a contratos externos:* por ejemplo usar contrato de oráculo para cceder a datos del mundo real
- 	*Gestión modular:* dividir la lógica en varios contratos para mejorar la organización y la escalabilidad
- 	*Estándares como ERC-20 y ERC-721* los cuales siguen normas para garantizar la interoperabilidad entre contratos y aplicaciones

**Decidir la estructuración de un contrato inteligente:**
Un contrato inteligente puede estructurarse de diferentes maneras según la complejidad, el proposito y los requisitos del proyecto.
La organización del contrato tiene un impacto directo en su funcionalidad, seguridad y facilidad de mantenimiento
Algunas formas de organizar un contrato inteligente:
- *Contratos monolíticos:* toda la lógica del contrato se encuentra en un único contrato. Puede ser dificil de escalar o actualizar puede ser mas vulnerable a errores si el código es extenso
- *Contratos modulares:* se divide la funcionalidad en varios contratos que interactuan entre si. Por ejemplo: un contrato principal para la lógica básica y contratos secundarios para funciones especificas. Suele ser mas sencillo de actualizar, mejora la organización del código. La interacción entre contratos puede aumentar el costo del gas
- *Contratos heredados:* usa la herencia para extender la funcionalidad de un contrato en base a otros contratos. Promueve reutilización de código, reduce errores
- *Contratos basados en bibliotecas:* se usan para funciones comunes

**Decisiones para la gestión de seguridad e integridad**
- Modelo de gestión de identidad: como se manejan las identidades de los usuarios:
- 	*identidad centralizada:* usar servidores externos para autenticar usuarios
- 	*identidad descentralizada:* implementar identidades auto-soberanas donde los usuarios controlan sus datos
- 	*anonimato y pseudonimato:* determinar si los usuarios pueden interactiar sin proporcionar datos personales
- Metodos de autenticación: como los usuarios acceden a la aplicación:
- 	*claves privadas:* controld e claves privadas para firmar transacciones
- 	*autenticación multifuncional:* combinar claves privadas con otras medidas de seguridad como códigos temporales o biometría
- 	*tokens de acceso:* usar tokens temporales para autorizar acciones dentro del sistema
- Privacidad de los datos: garantizar que los datos de los usuarios estén protegidos:
- 	*cifrado:* cifrar los datos sensibles que pueden ser manejados fuera de la blockchain
- 	*off-chain storage:* almacenar información privada fuera de la blockchain y vincularla mediante hases
- 	*privacidad en transacciones:* implementar tecnologías de privacidad para ocultar detalles transaccionales
- Sistemas de recuperación: planificar cómo los usuarios recuperarán acceso en caso de pérdida de credenciales:
- 	*frases de recuperación:* clave maestra para recuperar la cuenta
- 	*recuperación social:* contactos de confianza ayudan al usuario a recuperar su cuenta
- 	*contratos multisig:* exigir firmas multiples para recuperar credenciales
- Registro de actividad y auditoria: decidir qué datos se registraran para monitoreo. Por ejemplo, usar logs de actividad


## Capa de transporte

**Proposito de la capa de transporte**
La *capa de transporte(CT)* provee comunicación lógica entre procesos de aplicación que se ejecutan en diferentes sistemas finales. Esto no lo puede hacer la capa de red. La CT se implementa solo en los sistemas finales.
Se busca una *comunicación Lógica*, como si los hosts ejecutando los procesos estuvieran directamente conectados
La capa de transporte busca mejorar la calidad de los servicios de la CR

La capa de transporte confía en los servicios de la Capa de Red.
Llamamos *Entidad de transporte(ET)* al software/hardware de la capa de transporte

**¿Por qué conviene estudiar la capa de transporte?**
Al desarrollar una aplicación de red, hay que pensar en qué requisitos ella tiene referentes a la capa de transporte
Ayuda a hacer aplicaciones más eficientes y de mejor calidad al conocer cómo funciona la capa de transporte.
Para usar la API de los sockets ahce falta entender cómo funcionan algunos protocolos de capa de transporte
Para mejorar protocolos de capa de transporte o diseñar nuevos protocolos
 

**Problemas que soluciona la capa de transporte**
- Uso de *temporizadores* y las  *retransmisiones de paquetes*
- El direccionamiento explícito de los destinos
- 	¿Cómo hacer para que un proceso adecuado atienda a las necesidades de una máquina cliente?
- 	El proceso podría no estar activo, el cliente podría no saber cuál proceso usar, etc.
- Uso de búferes para lograr comunicación confiable eficiente
- Control de flujo (evitar que los emisores saturen a los receptores)
- Evitar congestionar la red poniendo demasiados paquetes en ella.
- 	Cuando la CR pierde paquetes, la CT puede solucionarlo

*Segmento* es una unidad de datos del protocolo de transporte
*Confirmaciones de recepción* de paquetes enviados
Los tipos de paquetes que deben ser confirmados son:
- paquete de datos
- paquetes con información de control


Un problema que se presenta es que la capa de transporte deberia permitir la entrega de segmentos al host destino, y que la entrega de segmentos sea ordenada (respetando el orden del flujo de datos a enviar recibido de la capa de aplicación).

Una solución para la entrega ordenada de segmentos al host destino puede ser que:
- El emisor numera los segmentos enviados, usando *números de secuencia*, respetando el orden del flujo de datos recibido de la capa de acplicación.
- Para cada número de segmento enviado el emisor dispara un *temporizador de retransmisiones*.
- El receptor manda *confirmaciones de recepción (ACK)* para segmentos recibidos correctamente.
- Si expira el temporizador de un segmento sin recibir el ACK, el emisor retransmite el segmento correspondiente
- El receptor *re-ensambla en orden* los segmentos recibidos y los entrega a la capa de aplicación.

#### TCP

*TCP (protocolo de control de transmisión)* tiene como meta el proporcionar un flujo de bytes confiable de extremo a extremo a través de una interred no confiable. TCP se adapta dinámicamente a las propiedades de la inter-red y se sobrepone a muchos tipos de fallas. Existe tambien la *Entidad de transporte TCP (ETCP)*, por lo que hay veces que diremos TCP para referirnos a la ETCP y a veces al protocolo TCP.

**Problemas que resuelve TCP:**
- Retransmisión de paquetes: uso de números de secuencia, confirmaciones de recepción y temporizadores
- Fijar la duración de temporizadores de retransmisiones(algoritmo complejo)
- Manejo de conexiones entre pares de procesos
- Direccionamiento
- Control de congestión
- Control de flujo

Una ETCP acepta *flujos de datos* a transmitir de procesos locales. Cada flujo de datos se *divide en fragmentos* llamados segmentos que no exceden los 64KB, y se envía cada segmento dentro de un datagrama IP.

El servicio TCP se obtiene al hacer que tanto el servidor como el cliente creen sockets
- Dirección de un socket = IP + Puerto
- Para obtener el servicio TCP se debe *establecer una conexión* explicitamente entre el socket en la maquina emisora y uno en la maquina receptora.

Un socket puede usarse para múltiples conexiones al mismo tiempo:
- dos o más conexiones pueden terminar en el mismo socket
- Las *conexiones se identifican* mediante los identificadores de sockets de los dos extremos (socket1,socket2)

Es importante saber que cada byte de un flujo de datos a enviar en una conexión TCP tiene su propio *número de secuencia* de 32 bits, lo cual impone un límite en el tamaño de un flujo de datos. Este número de secuencia es importante para confirmaciones de recepción y para otros asuntos según veremos.
La ETCP emisora y la receptora intercambian datos en forma de segmentos, donde cada segmento es el *encabezado TCP* ++ (0 o mas bytes) de datos.

Existen **limites que restringen el tamaño de un segmento**, especificamente cada segmento debe caber en la carga útil de 65.515 bytes del IP. Cada red tiene una *unidad máxima de transferencia(MTU)* y cada segmento debe caber en la MTU (en la practica la MTU es usualmente 1500 bytes).

Otro problema que surge en la capa de transporte al confiar en la capa de red es que, la capa de red (que incluye IP) no proporciona ninguna garantía de que los datagramas se entregarán de manera apropiada, tampoco garantiza que se entregarán.
La solución que aplica TCP es:
- Si un datagrama se recibe correctamente se confirma su recepción
- Si no se confirma la recepción de un datagrama luego de un intervalo de tiempo entonces se debe retransmitir
- Corresponde a TCP terminar los temporizadores y retransmitir los datagramas conforme sea necesario

Otro problema es que los datagramas que llegan podrían hacerlo en el orden incorrecto, lo cual para cuando se trabaja con redes de datagramas. Esto es un problema principalmente porque usualmente la capa de aplicación del receptor necesita procesar los mensajes en el orden en que fueron enviados.
Para solucionarlo TCP se encarga de reensamblar los mensajes en la secuencia apropiada.

Cuando un transmisor envía un segmento, también inicia un temporizador. Cuando llega el segmento a destino, la ETCP receptora devuelve un segmento que contiene un *número de confirmación de recepción* igual al siguiente número de secuencia que espera recibir. Si el temporizador expira antes de llegar el ack, el emisor envía de nuevo el segmento

También pueden llegar segmentos fuera de orden, por lo que habrá que esperar antes de entregar segmentos a la capa de aplicación y antes de enviar confirmaciones de recepción.
Tambien pueden retardarse segmentos en tránsito durante tanto tiempo que el temporizador del emisor expira y los segmentos se retransmiten

Además las retransmisiones podrían incluir rangos de bytes a los de la transmisión original. Esto puede suceder porque hay nuevos datos para enviar y se los puede mandar. Por ello se requiere una administración cuidadosa para llevar el control de os bytes que se han recibido correctamente en un momento determinado


#### Segmentos TCP

Los segmentos sin datos se usan para acks y *mensajes de control*. Se componen por:
- *puerto de origen* y *puerto de destino:* ambos de 16 b. La dirección de un puerto más la dirección IP del host forman un punto terminal único de 48 b. Los puntos terminales de origen y destino en conjunto identifican la conexión
- *Número de secuencia:* es número de byte en el flujo de bytes transmitido y corresponde al primer byte den el segmento. Tiene 32 b de lingitud
- *Número de confirmación de recepción:* indica el siguiente byte esperado del flujo de bytes a transmitir. Tiene 32 b de longitud
- *ACK:* se establece en 1 para indicar que el n° de confirmación de recepción es valido. Si el ACK = 0, entonces el segmento no contiene una confirmación de recepción
- *longitud del encabezado:* N° de palabras de 32 bits en el encabezado TCP, suelen ser 20 bytes, que son 5 5 palabras de 32 b
- El campo *opciones* es de longitud variable
- *URG:* indica que el segmento contiene datos urgentes que deben procesarse de inmediato
- *PSH:* sirve para pedir al receptor que procese y entrege los datos inmediatamente al nivel superior, en lugar de esperar a completar el buffer. Esto se usa en escenarios donde la inmediatez es clave
- *RST:* se utiliza para reiniciar una conexión. Se puede enviar por ejemplo cuando hay un error critico en la conexión
- *Urgent pointer:* complementa el indicador URG. Su proposito es especificar la ubicación del último byte de datos urgentes dentro del segmento
- *CWR (congestion window reduced) y ECE (explicit congestion notification):* relacionados con el manejo de congestión en la red. CWR indica que el transmisor ha reducido su ventana de congestión. ECE señala que el receptor ha detectado congestión a través de notificaciones explicitas


#### Transferencia de datos confiable

Actualmente con mecanismos simples como confirmaciones de recepción, temporizadores y retransmisiones quedan lagunas en como se hace la entrega de datos confiables. Y quedan preguntas como: ¿Que se confirma exactamente en un ACK?, ¿Cuantos paquetes se envian antes de recibir un ACK?, ¿Que hace el receptor cuando se pierde o daña un paquete?.

Para responder estas preguntas hay que definir un *protocolo de datos confiable*. Hay varios de estos porque hace falta *optimizar el rendimiento según las características de la red*, como la latencia, proporcion de errores, y capacidad de la red.

La capa de transporte debe soportar al menos un protocolo para *entrega de datos confiable*. Veremos varios de estos protocolos de mas simple a mas complejo. Estos protocolos asumen que el canal puede:
- Corromper paquetes
- Perder paquetes
- La transferencia de datos es en un sentido, o sea hay un emisor y un receptor

El protocolo mas simple es el de *parada y espera*, aunque luego vermos mas complejos como los de *tubería*. Estos protocolos se pueden usar tanto en capa de transporte como en capa de enlace de datos, pues entrega confiable de datos es un problema de esas capas.

Vimos que la Capa de Transporte se ocupa del uso de temporizadores y retransmisiones de paquetes, ya que los paquetes perdidos deben retransmitirse.
Sabemos que un paquete no se perdio porque fue confirmado con un *paquete de confirmación de recepción(ACK)*. Por ello podemos asumir que un paquete se perdio si pasa un cierto tiempo y no fue confirmado, entonces se perdió y hay que retransmitirlo. Para medir este tiempo se usan temporizadores.

Se puede prestar la situación donde el mensaje que se pierde es un ACK, y el paquete fuera retransmitido innecesariamente, por lo que llegaria mas de una vez el mismo paquete para terminar siendo transmitido a la capa de aplicación mas de una vez. Para solucionar esto se le asigna *números de secuencia* a los paquetes que salen con la idea de que dado un número de secuencia de un segmento que acaba de llegar, el receptor puede usar ese número de secuencia para decidir si el segmento es un duplicado y en ese caso descartarlo

#### Protocolo de parada y Espera

Suponemos que la latencia es lo suficientemente baja como para mandar solo un paquete anted de que llegue el ACK. En dicha situación un protocolo óptimo para manejarla se llama protocolo de *parada y espera*

Tambien supondremos que el canal de comunicaciones subyacente puede perder paquetes. Los paquetes tienen números de secuencias, se trabaja con ACKs y se usan retransmisiones de paquetes.

Con estas suposiciones el **comportamiento del emisor sera:**
1. El emisor envía paquete P y *para* de enviar
2. El emisor *espera* una cantidad "razonable" de tiempo para el ACK
3. Si llega el ACK a tiempo, se envía siguiente paquete. GO TO 2
4. Si no, se retransmite paquete P. GO TO 2
Si hay paquete o ACK demorado pero no perdido la retransmisión va a ser un duplicado con igual número de secuencia, luego se descartara en el receptor


Para evaluar un protocolo para comunicación confiable podemos simplificar un poco las cosas y además hacer un análisis de mejor caso. Para ello vamos a asumir que hay un canal de comunicación que une el emisor con el receptor y que la transmisión entre el emisor y el receptor es sin errores(no se ppierden paquetes, no se demoran paquetes, no se alteran paquetes en curso).

Entonces, vamos a denominar como L la longitud de los segmentos, T a la tasa de transmisión del canal, RTT es el tiempo entre la salida del ultimo bit del mensaje y la llegada del primer bit del ack(pudiendose calcular a partir de "D" o *demora de propagación del emisor al receptor*) y $U_{sender}$ sera la utilización del canal

De esta forma nos queda que:
- *Tiempo de transmisión del segmento:* $L/T$
- RTT = 2 * D
- $U_{sender} = {L/R}/{RTT + L/R}$


#### Protocolos de tubería

En esta situación tenemos una latencia alta, el RTT es muy alto comparado con el tiempo de copiar un paquete. Por lo tanto se pueden mandar varios paquetes antes de que llegue el ACK del primer paquete enviado.
Unos protocolos adecuados para dicha situación se los conocen como *protocolos de tubería*. En nuetro caso veremos 2:
- Protocolo Retroseso-N
- Protocolo de Repetición Selectiva

Los protocolos de tubería se caracterizan debido a que el emisor puede enviar múltiples paquetes al vuelo a ser confirmados. Por lo cual hay que usar bufferes en el emisor y tener un número de secuencia de mas de un bit


La ET emisora debe manejar *buferes para los mensajes de salida* porque puede hacer falta retransmitirlos. El emisor almacena en bufér todas los segmentos hasta que se confirma su recepción


#### Protocolo Retroseso-N

Si tenemos una latencia grande, la proporcion de errores o pérdida de paquetes es muy baja y rara vez se demoran paquetes, entonces se puede hacer el código del receptor mas sensillo y eficiente, usando la solución más fácil a estos problemas. Si estos problemas ocurren con cierta frecuencia, será necesario complicar el código del receptor para que se manejen eficientemente esos problemas.

Si un paquete T a la mitad de una serie larga se daña o pierde, como la CT receptora debe entregar los paquetes a la capa de aplicación en secuencia, no puede entregarle los paquetes que llegaron bien despues de T.
En estos casos, con *Retroseso-N* el receptor descarta todos los paquetes subsecuentes al paquete perdido, sin enviar ack para los paquetes descartados

Entonces, el receptor envía *ack acumulativo*, el mayor número de secuencia tal que los segmentos anteriores se recibieron bien.
El emisor tiene un solo temporizador para el paquete mas víejo no confirmado. Al expirar el temporizador retransmite todos los segmentos no confirmados. Si llega ACK nuevo y hay segmentos enviados no confirmados, el temporizador es reiniciado. Si llega ACK nuevo y no hay segmentos sin confirmar, el temporizador es detenido.
Asumimos en el emisor que voy a tener varios bufferes, todos los del mismo tamaño. Como el RTT es fijo, estos representarián la cantidad de segmentos a enviar por ráfaga para aprovechar el canal al maximo. Para referirnos a los números de secuencia de esos búferes usamos el concepto de *ventana del emisor*
Dicha "ventana" permite hasta N paquetes consecutivos sin confirmar. Llamamos *ventana emisora* a las tramas enviadas sin ack positivo o tramas listas para ser enviadas

Si el espacio de secuencia es de MAX_SEQ + 1 números de secuencia no se puede hacer la ventana emisora de tamaño MAX_SEG + 1, como mucho puede ser de MAX_SEQ


Para evitar que haya mas MAX_SEQ paquetes sin ack pendientes la solución es prohíbir a la capa de red que moleste con más trabajo, para ello se usa un "enable_network_layer" y "disable-network_layer"

El principal problema de retroceso N es el uso ineficiente del canal frente a segmentos perdidos o demorados


#### Protocolo de Repetición Selectiva

En la situacion que tengamos latencia grande, proporción de errores o pérdida de paquetes importante y que los paquetes puedan demorar, va a ser necesario hacer que el código del receptor maneje eficientemente los problemas de la red, por más que esto signifiqie complicar el código del receptor. Veremos el protocolo de repetición selectiva que adopta este enfoque

Si ocurre que un paquete T se pierde a mitad de una serie, la capa de transporte receptora debe entregar paquetes a la capa de aplicación en secuencia. Ocurre lo mismo que con el protocolo de repetición-N. En este caso la solución es distinta, los paquetes en buen estado recibidos después de un paquete dañado E se almacenan en un búfer. Cuando el paquete E llega correctamente, el receptor entrega a la capa de aplicación, en secuencia, todos los paquetes posibles que ha almacenado en el búfer. 
Para ello el mecanismo mas común de retransmisiones es esperar a que el temporizador de E termine y el emisor lo mande de nuevo. Aunque, una mejor solución es usar un ack negativo (NAK) por el receptor, estimulando asi la retransmisión de paquetes antes que los temporizadores terminen y así se mejora el rendimiento.

El receptor confirma individualmente todos los paquetes recibidos correctamente. Hay búferes para paquetes según se necesiten para su entrega eventual en orden a la capa de aplicación. El emisor solo reenvía paquetes para los cuales el ACK no fue recibido o se recibió un NAK. Hay un temporizador del emisor para cada paquete no confirmado

La ventana del emisor contiene N números de secuencias consecutivos, además los limita a enviar paquetes no confirmados

**Tipos de paquetes que puede haber en la ventana del emisor:**
- Paquetes enviados y confirmados porque antes hay paquetes no confirmados
- Paquetes enviados y no confirmados
- Paquetes listos para enviarse en búfer

Es necesario almacenar en búfer paquetes porque puede perderse un pquete y llegar otros a continuación del mismo y en repetición selectiva estos se almacenan. Para representar el conjunto de paquetes que puede almacenar en búfer el receptor se usan intervalos de números de secuencia dentro del espacio de npumeros de secuencia. Un intervalo de esos recibe el nombre de *ventana corrediza*

**Tipos de paquetes que puede haber en la ventana del receptor:**
- Paquetes esperados y no recibidos
- Paquetes recibidos fuera de orden
- Paquetes aceptables en la ventana que no han llegado aun

Se mantiene en búfer un paquete aceptado por la ventana receptora hasta que todos los que le preceden hayan sido pasados a la capa de aplicación

**Algunos detalles de la repetición selectiva:**
- tamaño de ventana emisora comienza en 0 y crece hasta MAX_SEQ
- el receptor tiene un búfer para cada número de secuencia en su ventana
- cuando llega un paquete, su número de secuencia es revisado para ver si cae dentro de la ventana, de ser así, y no ha sido recibido aun, se acepta y almacena

El tamaño de la ventana receptora = (MAX_SEQ + 1)/2. Con tamaños mayores no funciona
En el encabezado de paquete hay número de secuencia de k bits
**¿Como transmitir datos entre dos maquinas y en ambas direcciones eficientemente?**
Para ello se "lleva a caballito (piggybacking)". Consiste en que cuando llega un segmento S con datos, el receptor se aguanta y espera hasta que la capa de aplicación le pasa el siguiente paquete P. La confirmación de recepción de S se anexa a P en un segmento de salida (usando el campo ack en el encabezado del segmento de salida).

Sabiendo esto, para extender repetición selectiva para tener flujo de datos entre 2 maquinas en las dos direcciones hay que usar el piggybacking, es decir, la capa de transporte para mandar un ack, debe esperar por un paquete al cual superponer un ack.
Esto nos trae otro problema, ¿Como evitar retrasar demasiado el envío de confirmaciones de recpción por no tener trafico de regreso? Bueno, se usa un temporizador auxiliar de modo que tras llegar un paquete de datos en secuencia, se arranca un temporizador auxiliar mediante start_ack_timer. Si no se ha presentado tráfico de regreso antes de que termine este temporizador, se envía un paquete de ack independiente. Esto siempre con el tiempo de temporizador auxiliar mucho menor a el tiempo de temporizador de retransmisiones, para asegurarse que el ack de un paquete correctamente recibido llegue antes que el emisor termine su temporización y retransmita el paquete


## Control de Flujo en la capa de transporte


**Control de flujo:** Hay que evitar que un host emisor rápido desborde a un host receptor lento.

La capa de enlace de datos se ocupa del control de flujo entre dos máquinas directamente conectadas entre sí(pueden ser enrutador o host)

Podemos asumir que el receptor maneja búferes para los mensajes que llegan. Esto es necesario porque:
- Si la llegada de segmentos del emisor es mucho más rapida que el receptor para procesar los segmentos recibidos, entonces el receptor necesitará poder almacenar segmentos antes de procesarlos.
- El receptor puede acumular una cantidad de segmentos suficientes antes de pasarlos a la capa de aplicación para que loss procese
- Los segmentos pueden llegar desordenados, por lo tanto, si llegan un grupo de segmentos y faltan segmentos previos a ellos, habrá que almacenar los segmentos de ese grupo en buffer.

La capa de aplicación lee los mensajes que llegan, pero no necesariamente al instante en que los datos llegan. En lugar de eso, la aplicación receptora puede estar ocupada con otra tarea y puede no intentar leer los datos hasta bastante después que estos llegaron. Si la aplicación es demasiado lenta en leer los datos, el emisor puede saturar los búferes del receptor.
La capa de red puede tornar al receptor más lento y con menos capacidad de almacenamiento.

Aquí tenemos 2 situaciones:
1. Un enrutador en la rita entre el emisot y receptor daña un paquete; este error se va a detectar por la capa de transporte cuando el paquete dañado llegue al receptor. Si luego de ese paquete dañado llegan varios buenos, la capa de transporte tendrá que almacenarlos y el receptor va a ponerse más lento y con menos capacidad del búfer
2. El algoritmo de enrutamiento hace que cambien las rutas, rutas más lentas son remplazadas por rutas más rápidas; esto puede hacer que paquetes lleguen al receptor fuera de orden. Si esto sucede, entonces va a obligar a la capa de transporte a almacenar paquetes fuera de orden en búfer y el receptor va a ponerse más lento y con menos capacidad de búfer.

La capa de transporte puede tornar al receptor más lento y con menos capacidad de almacenamiento. Por ejemplo, si la cantidad de conexiones abiertas aumenta drasticamente; por ende, la cantidad de b+ufer para cada conexion disminuye y el receptor se pone más lento por la cantidad de aplicaciones aumentada. Esta situación sumada a las anteriores puede producir desbordamiento de búferes.


Si bien la capa de enlace de datos maneja el control de flujo, no maneja ninguna de las situaciones anteriores, por lo tanto necesitan ser tenidas en cuenta por la capa de transporte.

Si nos quedamos solo con los protocolos de comunicación confiable anteriores, estos no son suficientes para evitar desbordamiento de búferes en el receptor. Hace falta definir un protocolo especial para el control de flujo.

Si el receptor tiene varias conexiones, debe usar los búferes a medida que llegan los segmentos. Se dedican conjuntos de búferes especificos a conexiones especificas


**¿Como maneja el receptor el uso de búferes cuando entra un segmento?**
Cuando entra un segmento, el receptor intenta adquirir un búfer nuevo; si hay uno disponible se acepta el segmento, de otro modo se lo descarta.



Hasta ahora sabemos que se pueden dar las situaciones anteriores. El receptor y el emisor deben ajustar dinámicamente sus alojamientos de búferes, es decir, deben tener ventanas de tamaños variables. Ahora el emisor no sabe cúantos datos mandar en un momento dado, pero sí sabe cuántos datos le gustaría mandar.


**Entonces,¿Como se comportaria un protocolo de control de flujo?**
La solución se basa en que el host emisor *solicita espacio en búfer en el otro extremo* para estar seguro de no enviar de más y sobrecargar al receptor, porque solo el receptor sabe cuanto necesita.
El receptor sabe cuál es su situación y cuánto espacio puede otorgar, por ello cuando este recibe el pedido del emisor le reserva una cierta cantidad de búferes al emisor. Estos búferes podrian repetirse por conexión o no.
Si los búferes se reparten por conexión y aumenta la cantidad de conexiones abiertas el receptor necesita ajustar dinámicamente sus reservas de búferes


**Funcionamiento de la comunicación entre host emisor y host receptor usando la solución anterior**
1. Inicialmente el emisor solicita una cierta cantidad de búferes, con base en sus necesidades percibidas
2. El receptor otorga entonces tantos búferes como puede
3. El receptor, sabiendo su capacidad de manejo de búferes podría indicar al emisor "te he reservado X búferes"

Para no generar conflicto con los ACK, el receptor puede incorporar tanto las ack como las reservas de búfer en el mismo segmento.
El emisor lleva la cuenta de su *asignación de búferes* con el receptor; por lo que cada vez que el emisor envía un segmento este ultimo debe disminuir su asignación de buferes disponible. Cuando la asignación de búferes disponibles llega a 0, el emisor debe detenerse por completo

Una situación que puede pasar es que el receptor otorgue una cantidad de bufferes pero este mensaje se pierda terminando asi en un deadlock. ¿Como podemos evitar esto?. Bueno pues cada host puede enviar periódicamente un *segmento de control* con el ack y estado de búferes de cada conexión, de esta forma el estancamiento se romperá tarde o temprano

#### Control de Flujo en TCP

No se requiere:
- que los emisores envíen datos tan pronto como llegan a la aplicación
- que los receptores envíen confirmaciones de recepción tan pronto como sea posible
- que los receptores entreguen datos a la aplicación apenas los reciben

Con TCP no podemos usar el protocolo de control de flujo anteriormente visto, puesto que en TCP los números de secuencia no significan número de paquete. Anted cada búfer ocupado tenía un número de paquete. Ahora los números de secuencia son posiciones en el flujo de datos a enviar. El receptor a lo más ´puede saber qué rangos de números de secuencia de bytes recibidos tiene en búfer


Para acondicionar el protocolo de control de flujo anterior se le pueden hacer algunas mejoras:
- Los encabezados de los segmentos recibidos ocupan espacio y no hace falta almacenarlos en el búfer. En su lugar se pueden almacenar datos recibidos del flujo de datos
- No es necesario que el emisor solicite espacio del búfer al receptor. El receptor sabe de cuanto espacio dispone y cuanto espacio puede otorgar


Como no se almacenan encabezados de segmentos, no hace falta gaurdar segmentos en búferes. En su lugar se necesita guardar datos y no hace falta usar varios búferes para esto. TCP maneja un *búfer de recepción circular* en el receptor para la conexión

Como TCP usa este búfer único no le puede decir al emisor "te he reservado x búferes". Entonces para anunciar al emisor la reserva de espacio en búfer:
- El receptor puede indicar al emisor la cantidad de bytes consecutivos que se pueden enviar, comenzando por el byte cuya recepción se ha confirmado
- A esto se le llama en TCP *tamaño de ventana*
- En el encabezado TCP un *campo de tamaño de ventana* se usa para indicar esta información.

El TCP del emisor también usa un búfer circular.
**La cantidad de bytes que el emisor puede enviar al receptor depende** del tamaño del búfer del emisor y del tamaño de ventana. La cantidad de bytes a enviar no debe superar el mínimo de ambos valores

La formula para calcular el tamaño de ventana del receptor es: 
- Tamaño de ventana = RcvBuffer - [LastByteRcvd - LastByteRead]

**El receptor:**
- Cuando la conexión TCP recibe bytes en el orden correcto y en secuencia, coloca los datos en el buffer de recepción
- El receptor puede confirmar la llegada de datos nuevos y anunciar el nuevo tamaño de ventana al emisor
- Si el búfer de recepción está lleno, avisar tamaño de ventana de cero
- Una vez que el receptor entrega a la capa de aplicación X datos de búfer de recepción lleno, puede avisar al emisor de un tamaño de ventana de X

**El emisor:**
- Si el tamaño de ventana anunciado es cero el emisor no podra enviar datos
- El emisor envía segmentos cumpliendo la siguiente propiedad: LastByteSent - LastByteAcked $\le$ tamaño de ventana


Con este nuevo protocolo ¿Como manejamos las perdidas de segmentos en TCP?

Para esto hay varias soluciones. En la primera el receptor solicita segmentos especificos mediante  un segmento especial llamado NAK.
Tras recibir segmentos faltantes, el receptor puede enviar una confirmación de recepción de todos los datos que tiene un búfer. Cuando el receptor nota una brecha entre el número de secuencia esperado y el número de secuencia del paquete recibido, el receptor envía un NAK en un campo de opciones.


En la otra solución (ack selectivos) el receptor le dice al emisor que piezas recibio.
El emisor puede así reenviar los datos no confirmados que ya envío. Se usan dos campos de opciones:
- *Sack permited option:* se envía en segmento SYN para indicar que se usarán acks selectivos
- *Sack option:* con lista de rangos de números de secuencia recibidos

Cuando la ventana es de 0, el emisor no puede enviar segmentos, salvo en dos situaciones:
1. pueden enviarse *datos urgentes*
2. el emisor puede enviar un segmento de 1B para hacer que el receptor re-anuncie el siguiente byte esperado y el tamaño de la ventana. TCP proporciona esta opción para evitar un bloqueo irreversible si llega a perderse un anuncio de ventana


En las líneas con alto ancho de banda, alto retardo o ambas cosas, la ventana de 64KB con frecuencia es un problema. El problema viene cuando si bien un tamaño de ventana más grande permitira al emisor continuar enviando datos, pero como el campo de tamaño de ventana es de 16 bits, es imposible expresar tal tamaño.

La solución a esto es permitir al emisor y al receptor negociar un factor de escala de ventana.
Ambos lados pueden desplazar el tamaño del campo de ventana hasta 14 bits a la izquierda, permitiendo por lo tanto ventanas de hasta 2^30 bytes. La myoria de las implementaciones actuales de TCP manejan esta opción


## Control de Congestión Capa de Transporte

Si un emisor manda a un receptor más información que la capacidad de carga de la subred, esta ultima se congestionará, pues será incapaz de entregar los segmentos a la velocidad con que llegan

Para solucionar esto necesitaremos un mecanismo de control de congestión basado en la capacidad de carga de la subred, el cual debe aplicarse al emisor.
Entonces para controlar la congestión en TCP algunos hosts dismunuiran la tasa de datos.

Para llevar la cuenta de cúantos datos un host puede enviar por la red TCP maneja una *ventana para la congestión (VC)* cuyo tamaño es el número de bytes que el emisor puede tener en la red en un momento dado. En TCP el host tiene una forma de detectar congestión, y al hacerlo el host ajusta el tamaño de la VC


**La expiración de un temporizador causada por un paquete perdido se puede deber a:**
1. ruido en la linea de transmisión
2. el descarte de paquetes en el enrutador congestionado

Hoy la p+erdida de paquetes por errores de transmisión es rara debido a que las troncales de larga distancia son de fibra óptica. Luego, la mayoría de las expiraciones de tiempo en internet se deben a la congestión
En TCP todos los algoritmos de congestión suponen que las expiraciones de tiempo son causados por congestión


¿Como calcular un tamaño para ña ventana de congestión?
Una idea seria probar con un mínimo de datos e ir duplicando gradualmente hasta que no se pueda más. Un algoritmo basado en esta idea se le llama *"arranque lento"*

**Algoritmo de arranque lento (Jacobson 1988):**
- El emisor asigna a la VC el segmento de tamaño maximo (STM) usado por la conexión: entonces envía 1 STM. Emisor y receptor se ponen de acuerdo en el tamaño del STM.
- Si se recibe el ack de este segmento antes que expire el temporizador, el emisor agrega el equivalente en bytes de un segmento a la VC para hacerla de 2 STM y envía dos segmentos
- Cuando la VC es de n segmentos, si de todos los n se reciben acks a tiempo, se aumenta la VC en la cuenta de bytes correspondiente a n segmentos
- La VC sigue creciendo exponencialmente hasta expiración del temporizador o hasta alcanzar el tamaño de la ventana receptora
- Si ocurre un timeout se recorta la VC a tamaño VC/2, o sea no se enviarán rafagas de segmentos mayores a VC/2


Este algoritmo no es perfecto y tiene varios problemas:
- *Critica 1:* Recortar la ventana de congestión a la mitad porque hubo una expiración de temporizador y quedarse ahí, puede ser demasiado, porque puede ser que la red tenga una capacidad mayor a esa mitad y así se desaprovecharia esa capacidad de la subred
- *Critica 2:* con la retransmisión disparada por expiración de temporizador el tiempo de espera puede ser relativamente grande. Cuando se pierde un paquete el emisor se demora en reenviar el paquete perdido.


Para que el emisor reconozca rapidamente que uno de sus paquetes se perdió vamos a asumir que cada paquete que llega al receptor dispara un paquete ack. De esta forma si se pierde un paquete pero los siguientes llegan bien, el emisor recibira acks duplicados.
Igualmente esto podria significar 1 de 2 cosas:
- Como los segmentos pueden tomar distintos caminos, pueden llegar fuera de orden y esto va a disparar acks duplicados incluso cuando no se ha perdido ningún segmento
- Si se pierde un segmento, habrá probablemente varios acks duplicados.

Para solucionar esto TCP asume que 3 acks duplicados implican que el paquete se perdio. Luego ese paquete retransmite inmediatamente y antes de que expire el temporizador.
Esta heuristica se llama *retransmisión rápida*


Otra solución es el **Algoritmo de control de congestión de internet (TCP Tahoe):**
- Usa un *umbral* además de las ventanas de recepción y congestión
- Al ocurrir una expiración del temporizador o detectarse 3 acks duplicados, se fija el umbral en la mitad de la ventana de congestión actual, y la ventana de congestión se restablece a un segmento máximo
- Luego se usa el arranque lento para determinar lo que puede manejar la red, excepto que el crecimiento exponencial termina al alcanzar el umbral
- A partir del punto en el que se alcanza el umbral las transmisiones exitosas aumentan linealmente la ventana de congestión (en un segmento máximo por ráfaga)
- Recomenzar con una ventana de congestión de un paquete toma un RTT (para todos los datos previamente transmitidos que dejen la red y para ser confirmados, incluyendo el paquete retransmitido)
- Si no ocurren más expiraciones de temporizador/3 acks duplicados, la ventana de congestión continuará creciendo hasta el tamaño de la ventana del receptor. En ese punto dejará de crecer y permanecera constante mientras no ocurran más expiraciones de temporizador y la ventana del receptor no cambie de tamaño

Aunque esto mejore un poco la congestión, aun se puede criticar que comenzar con arranque lento cada vez que se pierde un paquete puede ser demasiado. Ya que por ahora el algoritmo TCP Tahoe se basa en:
- *invariante:* tamaño ventana de congestión $\le$ tamaño ventana receptor
1. Se usa arranque lento hasta alcanzar el umbral
2. Luego vienen incrementos aditivos hasta alcanzar timeout o 3 ack duplicados
3. Luego el umbral se fija a la mitad del tamaño de la ventana de congestión
4. Goto 1

Para solucionar el arranque lento del principio existe el *Algoritmo de TCP Reno (1990)*
Cuya idea es evitar el arranque lento (exceptuando cuando la conexión es comenzada) cuando expira el temporizador de re-envios.
Su funcionamiento es:
1. Luego de iniciada la conexión se comienza con arranque lento
2. A continuación la ventana de congestión crece linealmente hasta que se detecta una pérdida de paquete. Se cuentan acks duplicados y se considera perdida de paquete el recibir 3 acks duplicados
3. El paquete perdido es retransmitido (usando retransmisión rápida)
4. *Recuperación rapida:* Se manda un paquete por cada ack duplicado recibido. Un RTT luego de la retransmisión rápida el paquete perdido es confirmado. La recuperación rápida termina con esa confirmación de recepción
5. Luego de recibir el nuevo ack: la ventana de congestión de una conexión se achica a la mitad de lo que era cuando se encontraron 3 duplicados (decrecimiento multiplicativo). El conteo de ack duplicados se pone en 0
6. Luego la ventana de congestión va incrementando de a un segmento por cada RTT (crecimiento aditivo)
7. Este comportamiento continua indefinidamente

Luego se hicieron ajustes menores a TCP Reno que no veremos.

En resumen **TCP Reno:**
- Invariante: tamaño v¿de la ventana de congestión $\le$ tamaño de la ventana de receptor
1. Luego de iniciada la conexión viene arranque lento hasta alcanzar umbral
2. Luego vienen incrementos aditivos de hasta 3 ack duplicados
3. Luego viene recuperación rapida
4. Luego se reduce la ventana de congestión a la mitad
5. GOTO 2



## Evitando segmentos duplicados retrasados

Hay 2 razones por las que pueden llegar segmentos duplicados a un host receptor:
1. Si se pierde un ack y el segmento se retransmite
2. Si el segmento se demora debido a la congestión y su temporizador expira, el emisor lo retransmitira

Como no se puede entregar segmentos duplicados a la capa de aplicación, es necesario saber si un segmento que llega al host receptor es duplicado o no.

¿Como hacer para saber eficientemente si doss egmentos son diferentes o no?
La solución inviable es comparar ambos segmentos bit a bit ya que esto requeriria almacenar todos los segmentos que llegaron previamente, y eso es muy ineficiente.

Una mejor solución es numerar los segmentos con números de secuencia. Entonces los paquetes con n° de secuencia diferentes son distintos. Esta idea funcionaria bien si tenemos un n° de secuencia de tamaño arbitrario O números de secuencia lo suficientemente largos como para estar seguros de que no se van a reutilizar

Aun así los npumeros de secuencia no pueden ser de tamaño arbitrario porque queremos que los segmentos tengan longitud máxima. Por lo tanto el espacio de números de secuencia es finito; porque queremos que el número de secuencia sea un campo del encabezado de longitud fija

Esta idea de solo usar un espacio de secuencia finito y numerar los segmentos con n° de secuencia no siempre funciona bien
Por ejemplo, en la situación que pasa cuando un segmento S con n° de secuencia X queda demorado debido a que la red esta congestionada. El temporizador de retransmisiones asociado a S expira y se retransmite S. El protocolo de enrutamiento cambia las rutas y la retransmisión de S llega rápido a destino. Pero aun quedo en la red un *duplicado retrasado* de S (el que tiene número de secuencia X). Este duplicado retrasado de S más adelante llega a destino generando problemas.
Este tipo de problemas son tan serios que deben ser evitados


Entonces ¿Como encaramos los problemas de duplicados retrasados?
La idea es asegurar que ningun paquete viva más allá de T sec (tiempo de vida de paquete).
Esto se refiere a paquetes de datos, retransmisiones de ellos y a confirmaciones de recepción. Eliminar paquetes viejos que andan dando vueltas por ahí.
Veremos que esta idea hace que la solución de los problemas de duplicados retrasados sea manejable


**Para resolver el problema de duplicados retrasados dentro de una conexión:**
Asumiendo que T es el tiempo de vida de paquete, el origen etiqueta los segmentos con n° de secuencia que no van a reutilizarse dentro de T sec.
Para lograr que al regresar al principio de los n° de secuencia, los segmentos viejos con el mismo n° de secuencia hayan desaparecido hace mucho tiempo, el espacio de secuencia debe ser lo suficientemente grande para garantizar eso

Normalmente la cantidad de números de secuencia debe ser mayor a la cantidad de segmentos que puedo enviar en el tiempo de vida de cada segmento. Tendrá que ser potencia de 2 porque el número de secuencia es un campo del encabezado del segmento

**¿Como evitar que un duplicado retrasado que pasa de una conexión a otra genere problemas?**
Como al establecer una conexión se usan segmentos, una conexión debería tener un *N° inicial de secuencia* con el que comienza a operar

Una idea de solución seria escoger como número inicial de secuencia de la conexión nueva un n° de secuencia que haga imposible o improbable que el duplicado retrasado de n° de secuencia X genere problemas. Además se mantiene dentro de una conexión que el origen etiqueta los segmentos con n° de secuencia que no van a reutilizarse dentro de T sec (tiempo de vida del paquete).

Una implementación dada en el libro de Comer dice que:
Al crear una nueva conexión cada extremo genera un número de secuencia de 32 bits aleatorio que pasa a ser el npumero inicial de secuencia para todos los datos enviados. Alguna implementación de TCP usa esta solución.
Esta implementación tiende a funcionar debido a que la probabilidad de que un paquete duplicado retrasado genere problemas en una conexión siguiente es baja debido a la elección aleatoria del número inicial de secuencia de la conexión siguiente


Otra implementación diferente es dada en el libro de Tanembaum, donde:
Vincular el número de secuencia de algún modo al tiempo y para medir el tiempo usar un reloj de modo que:
- Cada host tiene un *reloj de hora del dia*
- Los relojes de los host no necesitan ser sincronizados, pues se supone que cada reloj es un contador binario que se incrementa a si mismo en intervalos uniformes.
- El reloj continua operando aun ante la caída del host
Cuando se establece una conexión los k bits de orden mayor del reloj = *Número inicial de secuencia*

Esto funciona debido a que si el reloj se mueve más rapido que la asignación de npumeros de secuencia a los paquetes que se envían, entonces el número inicial de secuencia de una nueva conexión va a ser mayor al número de secuencia de cualquier duplicado retrasado de la conexión previa


## Estableciendo conexiones

Como al establecer una conexión se usan segmentos, una conexión debería tener un número de secuencia con el que comienza a operar.
La idea sigue siendo la misma, vincular el número inicial de secuencia de algún modo al tiempo y para medir el tiempo usar un reloj

La implementación de la idea de Tomlinson dice que:
- Cada host tiene un reloj de hora del dia. Los relojes de los host no necesitan ser sincronizados, se supone que cada reloj es un contador binario que se incrementa a si mismo en intervalos uniformes. El reloj continua operando aun ante la caída del host
- Cuando se establece una conexíon los k bits de orden mayor del reloj = *número inicial de secuencia*


Cuando un host se cae, al reactivarse sus ET no saben dónde estaban en el espacio de secuencia. Este es un problema porque para el siguiente segmento a enviar no se sabe qué números de secuencia generar; si se genera mal, entonces el nuevo segmento podría tener el mismo número de secuencia que otro segmento distinto circulando por la red.
Para solucionar esto vamos a requerir que las ET estén inactivas durante T segundos tras una recuperación para permitir que todos los segmentos viejos expiren (entonces no vamos a tener dos segmentos diferentes con el mismo número de secuencia)

**¿Cómo hacer para establecer una conexión entre dos host?**
Para establecer conexión el host de origen envía un segmento *CONNECTION REQUEST* al destino y espera una respuesta *CONNECTION ACCEPTED*.
Supongamos que se establecen conexiones haciendo que un host 1 envía segmento S = CR N, P a host 2 donde N es el número de secuencia y P es el número de puerto. Host 2 confirma ese pedido con segmento CA N

En este contexto puede pasar que S se demora demasiado en llegar a host 2, vence el timer en host 1 y host 1 manda un duplicado S'. Luego puede psar que host 2 reciba S' y un buen tiempo despues S
El problema con esto es que no tenemos forma de saber si un segmento CR que contiene un número de secuencia inicial es un duplicado de una conexión reciente o una conexión nueva, por ende el host no sabe si mandar un segmento CA o no.
La solución a esto es el *Acuerdo de las 3 vias* de Tomlinson de 1975 donde:
- En un caso de operación normal solo hay que fijarse en el número de secuencia del segmento de datos enviado
- En un caso de segmento CR duplicado con retraso. El host 1 rechaza el primer CA del host 2, al rechazar el host 1 del intento de establecimiento de conexión del host 2, el host 2 se da cuenta de que fue engañado por un duplicado con retardo y *abandona la conexión*; de esta forma un duplicado con retardo no causa daño


#### Establecimiento de una conexión TCP

El número de secuencia inicial de una conexión no es 0, se usa un *esquema basado en reloj* con un pulso de reloj cada 4 usec. Al caerse un host, no podra reiniciarse durante el tiempo máximo de paquete, para asegurar que no haya paquetes de conexiones previas vagando por internet.

El campo *SYN* en el encabezado TCP se usa para establecer conexiones.
La solicitud de conexión es con SYN = 1, y ACK = 0.
La respuesta de conexión si lleva una confirmación de recepción, por lo que tiene SYN = 1 y ACK = 1. Recordar además que hay un campo con número de secuencia confirmado.

En TCP las conexiones usan el *acuerdo de 3 vias*:
1. Para establecer una conexión, el servidor, espera pasivamente una conexión entrante ejecutando LISTEN y ACCEPT y especificando cierto origen o bien nadie en particular
2. En el lado del cliente ejecuta CONNECT, la cual envía un segmento TCP con el bit SYN encendido y el bit ACK apagado, y espera una respuesta
3. Al llegar el segmento al destino, la ETCP allí revisa si hay un proceso que haya ejecutado un LISTEN en el puerto indicado en el campo puerto de destino
4. Si no lo hay, envía una respuesta con el bit RST encendido para rechazar la conexión
5. Si algún proceso está escuchando en el puerto ese proceso recibe el segmento TCP entrante y puede entonces aceptar o rechazar la conexión; si la acepta se envía un segmento de ack


## Liberación de conexiones

**¿Como hacer un protocolo para liberación de conexiones?**

La primera idea seria hacer un protocolo en el que:
- el host 1 dice "ya termine¿terminaste también?"
- Si el host 2 responde "Ya termine también. Adios", la conexipon puede liberarse con seguridad.
En la practica un protocolo asi no siempre funciona, porque existe el *problema de los dos ejércitos*

Hay 2 ejercitos azules rodeando a un ejercito blanco. Si los dos ejércitos azules atacan simultaneamente van a ganar. Por eso quieren sincronizar su ataque. Supongamos que el comandante del ejercito azul 1 manda un mensaje  "¿que le parece que ataquemos en el horario X?", el mensaje llega y el comandante del ejercito azul 2 contesta que está de acuerdo. Aun así el ataque no va a ocurrir puesto que el comandante del ejercito azul 2 no sabe si el mensaje fu recibido por el ejercito azul 1.

**SPOILER:** No existe un protocolo que resuelva el problema de los 2 ejercitos 

Para el caso de liberación de conexiones "atacar" equivale a "desconectar". Si ninguna de las aprtes está preparada para desconectarse hasta estar convencida que la otra está preparada para desconectarse también, nunca ocurrira la desconexión

Otra idea seria permitir que cada parte decida cuando la conexión está terminada. Este es un problema mas sencillo. Veremos cuatro escenarios de liberación de conexión usando un acuerdo de 3 vias. Aunque este protocolo no es infalible, generalmente es adecuado

**La liberación de conexión en un host significa** que la ET remueve la información sobre la conexión de su tabla de conexiones abiertas y avisa de alguna manera al dueño de la conexión


El caso normal:
1. Host 1 envía un segmento DISCONNECTION REQUEST e inicia un temporizador para el caso que no llegue DR de host 2
2. Al llegar DR al host 2, éste emite un segmento DR e inicia un temporizador para el caso de que no llegue respuesta de host 1
3. Al llegar esta DR el host 1 envía de regreso un segmento ACK y libera la conexión
4. Cuando el segmento ACK llega el host 2 tambien libera la conexión

Caso 2 Si se pierde el último segmento ACK:
- Al expirar el temporizador la conexión se libera de todos modos

Caso 3 Si se pierde el segundo DR:
- El host 1 no recibira la respuesta esperada, su temporizador expirará y todo comenzará de nuevo

Caso 4, Respuesta perdida y DRs subsiguientes perdidos:
Supongamos que todos los intentos repetidos de retransmitis la DR también fallan debido a la pérdida de segmentos:
- Tras N reintentos el emisor se da por vencido y libera la conexión
- Mientras tanto tambíen termina el temporizador del receptor y también se sale

El protocolo anterior falla si se pierde la DR inicial y N retransmisiones. El emisor se dará por vencido y liberará la conexión, pero el otro lado no sabrá nada sobre los intentos de desconexión y seguirá plenamente activo. Esta situación origina una *conexión abierta a medias*

Para evitar estas *conexiones abiertas a medias* hay varias soluciones. Una es evitar que el emisor se diera por vencido tras N reintentos, sino obligandolo a seguir insistiendo hasta recibir una respuesta. 
El problema de esta solución es que si se permite que expire el temporizador en el otro lado, entonces el emisor continuará eternamente, pues nunca aparecerá una respuesta

Otra manera de matar conexiones abiertas a medias es:
- Si no ha llegado ningún segmento durante una cierta cantidad de segundos al host 2, se libera automaticamente la conexión en el host 2
- Luego el host 1 detectará la falta de actividad y también se desconectara
- Esta solución también resuelve el caso que la red "se rompio" y los host ya no pueden conectarse

Para implementar esta idea es necesario que cada ET tenga un temporizador que se detenga y se reinicie con cada envío de un segmento.
Por esto mismo no se puede garantizar absolutamente que cuando se libera una conexión no occure pérdida de datos. Pero si se puede limitar mucho que esto suceda


#### Liberación de Conexiones

La *liberación simétrica:*
- Cada parte se cierra por separado, independientemente de la otra
- Una de las partes emite un DISCONNECT porque ya no tiene más datos por enviar y aun está dispuesta a recibir datos de la otra parte
- Una conexión se libera cuando ambas partes han emitido una primitiva DISCONNECT


La liberación simetrica es ideal cuando cada proceso tiene una cantidad fija de datos por enviar y sabe con certidumbre cuándo los ha enviado
En otras situaciones la determinación de si se ha efectuado o no todo el trabajo o si debe terminarse o no la conexión no es tan obvia
TCP trabaja con liberación simetrica


#### Liberación de una conexión TCP

En TCP los encabezados tienen un campo dedicado a la liberación de conexiones.
El campo *FIN* especifica que el emisor no tiene más datos que transmitir.
Tras cerrar una conexión, un proceso puede continuar recibiendo datos indefinidamente
Ambos segmentos, SYN y FIN, tienen número de secuencia y por tanto, tienen la garantía de procesarse en el orden correcto

**Resumen:**
- Para liberar una conexión cualquiera de las partes puede enviar un segmento TCP con el bit FIN establecido, lo que significa que no tiene más datos por transmitir, pero todavía puede recibir datos del otro lado
- Al confirmarse la recepción del FIN, ese sentido se apaga. Sin embargo puede continuar un flujo de datos indefinidos en el otro sentido
- Cuando ambos sentidos se han apagado, se libera la conexión
- Normalmente se requieren 4 segmentos TCP para liberar una conexión: un FIN y un ACK para cada sentido. Sin embargo es posible que el primer ACK y el segundo FIN estén contenidos en el mismo segmento, reduciendo la cuenta total a 3
- Una vez que el cliente manda el ACK al servidor, entra en un estado de espera llamado TIMED-WAIT
- El tiempo gastado en TIMED_WAIT es de dos tiempos de vida de paquete. TCP espera esta cantidad para garantizar que todos los paquetes de la conexión han muerto, en el caso que el ACK final se haya perdido
- Luego de la espera la conexión se cierra formalmente y todos los recursos del lado del cliente son liberados.
- Ambos extremos de una conexión TCP pueden enviar segmentos FIN al mismo tiempo. La recepción de ambos se confirma de la manera normal y se apaga la conexión. No hay diferencia entre la liberación secuencial o simultanea por parte de los hosts


## La Capa de Red

La capa de red tiene como proposito el llevar paquetes de un host de origen a uno de destino siguiendo una ruta conveniente.
Los asuntos de los que se encarga esta capa son:
- Almacenamiento y reencío
- Enrutamiento
- Control de Congestión
- Conectar redes de distintas tecnologías
- Fragmentación

**¿Por que estudiamos la capa de red?**
- Para entender cómo están organizadas las redes
- Para entender cómo se intercoenctan redes de distintas recnologías
- Para aprender algunos conceptos fundamentales como proveedores de servicios de red, enrutadores, etc.
- Para entender la necesidad de los enrutadores y cómo funcionan
- Para entender cómo se hacen asignaciones de direcciones de red a máquinas en una red local, a instituciones varias. El por qué y cómo se lo hace
- Para entender algunos problemas fundamentales y algoritmos alternativos para su solución. Enrutamiento, control de congestión, fragmentación

El hardware subyacente de la capa de red se compone de varias subredes de distinta tecnología unidas entre sí usando puertas de enlace.
Recordemos que un paquete no puede pasar tal cual de una red a otra porque los formatos de paquete difieren de una red a otra, y porque los tamaños maximos de paquetes difieren de una red a otra


**Enfoques para mandar un conjunto de paquetes desde un host de origen a un host de destino**

Hay dos bandos en relación a cómo se debe hacer esto:
- Usar una ruta fija para mandar todos los paquetes (*servicio orientado a la conexión*)
- La ruta puede cambiar, por lo que distintos paquetes pueden seguir distintos caminos (*servicio no orientado a la conexión*)

*Servicio no orientado a la conexión:*
- Alentado por la comunidad de internet
- Los paquetes se enrutan de manera independiente. La ruta a usar entre los host va a cambiar cada cierto tiempo. Cada paquete debe llevar una dirección de destino completa
- La nomenclatura usada es: Paquetes = *datagramas*, Subredes = *subredes de datagramas*
-  Para ver el **Diseño de la tabla de un enrutador** vamos a suponer que: Existe un procedimiento que dada la dirección del host de destino me retorna dirección del enrutador destino, y que el enrutador de destino sabe cómo entregar el paquete a host de destino (por mas que el host de destino esté en una LAN)
-  *Tabla del enrutador:* La tabla del enrutador solo necesita entradas para los enrutadores de la subred. cada entrada de la tabla de enrutador esta formada por filas "<enrutador de destino, línea de salida>" donde la linea de salida es la dirección de un enrutador

Cuando lelga un paquete a un enrutador:
1. Se lo almacena y se comprueba que llegó bien
2. Se determina el enrutador de destino asociado al host de destino
3. Se usa fila de ese enrutador de destino para reenviar el paquete por linea de salida de esa fila

Podemos pensar que *dirección de un host* es un número con dos partes, <dirección de red, número de máquina>, donde:
- La *dirección de red* sirve para identificar una red
- El *número de máquina* sirve para identificar una máquina dentro de la red
- Por ejemplo direcciones de 8 bits, red de 4 máquinas viene dada por las direcciones: 11010000, 11010001m 11010010 y 11010011 (dirección de red es 110100)
- IP respeta esta convención pero con direcciones de 32 bits

Podemos pensar que los enrutadores que están conectados a hosts de una misma red tambien forman parte de esa red. O sea que tienen el mismo valor en la parte de dirección de red (cuentan como máquinas tambien).
Todo host de destino va a tener un enrutador con igual dirección de red y hay que usar ese enrutador de destino para llegar al host de destino

Dada la dirección de host de destino, para encontrar enrutador de destino apropiado se debe buscar el enrutador de destino cuya dirección concuerde con la mayor cantidad de bits desde la izquierda con la dirección de host de destino.

Por ejemplo, en el ejemplo anterior suponemos que tenemos enrutadores de destino de direcciones: 10010000, 110000001, 11110010 y 11010011. Suponemos que nos llega un paquete dirigido al host de destino 11010010. El enrutador de destino que concuerda en más bits con ese host de destino es 11010011 y ese es el que se va a considerar para llegar al host de destino

**Servicio orientado a la conexión:**
- Alentado por las compañias telefonicas
- Todos los paquetes se mandan por la misma ruta
- *Trabajo a realizar antes de mandar paquetes:*
- 	Hay que configurar una ruta del host de origen al de destino
- 	Esto se llama crear una conexión
- 	*circuito virtual (CV)* = conexión
- Cada paquete lleva un *identificador* que indica a cual CV pertenece
- Cuando no se necesita enviar más paquetes se *libera la conexión*. Al hacer eo, también se termina el CV

Se elige una ruta de la máquina de origen a la de destino. Esta ruta se almacena en tablas dentro de los enrutadores

#### Enrutamiento jerárquico

Cuando crece mucho el tamaño de las subredes, también lo hacen las tablas de enrutamiento.
Estas tablas consumen memoria del enrutador, necesitan más tiempo de CPU para examinarlas en base a que tan grandes son


¿Cómo hacer para que las tablas de enrutamiento no crecan demasiado cuando crece mucho el tamaño de la subred?
La solución a esto se llama *enrutamiento jerárquico:*
- Los enrutadores se dividen en *regiones*
- Un enrutador sabe cómo enrutar paquetes a destinos de su región
- Tambien sabe cómo enrutar a otras regiones
- Pero no sabe nada de la estructura interna de las regiones en las que no está

El precio a pagar del enrutamiento jerárquico es una longitud de ruta mayor, de esta forma no podemos aspirar a encontrar la mejor ruta

Las tablas de enrutamiento jerárquico se presentan por tener una columna para el host destino, una para la linea por la que se va a enviar el paquete y una para la cantidad de "hops" que se necesitan para llegar. De esta forma tenemos entradas para todos los enrutadores locales, y entradas para las demás regiones en las que no está el enrutador

Aun asi en las redes enormes, una jerarquía de dos niveles es insuficiente; la solución para esto es agrupar las regiones en clústeres, los clústeres en zonas, las zonas en grupos, etc.

#### Arquitectura de un enrutador

**Las funciones claves de un enrutador son:**
- Ejecutar algoritmos de enrutamiento/protocolos (RIP, OSPF, BGP)
- Enviar paquetes de enlaces de ingreso a enlaces de salida

<img width="683" height="324" alt="imagen" src="https://github.com/user-attachments/assets/205551e7-6e38-4587-a2da-b10c7446d40c" />

<img width="703" height="435" alt="imagen" src="https://github.com/user-attachments/assets/8cc7a9df-74d5-4916-a32a-7cbb0175eaf5" />

<img width="689" height="519" alt="imagen" src="https://github.com/user-attachments/assets/10385b1c-b3a6-42ee-b05c-5a4dbb23297c" />


#### Algoritmos de enrutamiento

Queremos evitar los siguintes efectos indeseados:
- Algoritmos enrutadores que puedan quedar inactivos
- Los caminos pueden ser innecesariamente largos
- Se pueden sobrecargar algunas de las líneas de comunicación y los enrutadores asociados a ellas

  La causa de dichos problemas es que la capa de red elige mal las rutas para enviar paquetes.
  Para escoger bien las rutas para enviar los paquetes se deben usar *algoritmos de enrutamiento* eficientes. Estos algoritmos se ejecutan en los enrutadores de la subder, son responsables de llenar y actualizar las tablas de enrutamiento

Antes de ver los algoritmos de enrutamiento vamos a ver como representar una subred como un grafo:
- Vamos a tener el Grafo G = (N,E) donde N = conjunto de enrutadores y E = conjunto de enlaces. Los arcos tienen etiquetas para el costo de atravesarlos
- Los costos de los arcos podrian calcularse como función de varios parámetros como la distancia, ancho de banda, tráfico medio, costo de comunicación, longitud media de las colas, retardo medio y otros factores. Para calcular el costo de un camino (x1 , x2, x3 , ... , xn) simplemente debemos sumar los costos de los caminos intermedios, en este caso costo(x1,x2,..,xn) = costo(x1,x2) + costo(x2,x3) + ... + costo (xn-1,xn)

**Algoritmo de enrutamiento de caminos más cortos:**
Para elegir una ruta entre un par de enrutadores, encontrar en el grafo una de las *rutas mas cortas* entre ellos. Algoritmos de cálculo de la ruta mas corta entre dos nodos como el de *Dijkstra* (1959), donde:
- Dado ung rafo conexo con costos en los enlaces, y nodo n en el grafo, obtiene *árbol de caminos más cortos* desde n hacia todos los demás nodos
- El árbol de caminos más cortos se representa como un *mapeo* donde para cada nodo del grafo de la subred asigna a su padre (en el árbol de caminos más cortos)
- Repasar los detalles del algoritmo de Dijkstra visto en algoritmos 2

**Procedimiento para calcular tablas de reenvío en redes de datagramas usando algoritmo de Dijtstra:**
1. Construir grafo de la subred con costos
2. Ingresar grafo de la subred con costos en los enrutadores
3. En cada enrutador construir tabla de enrutamiento, para lo cual:
- 	Ejecutar algoritmo Dijkstra en el enrutador
- 	A partir del árbol de caminos más cortos con raíz en el enrutador obtenido generar la tabla de reenvío del enrutador

#### Algoritmo de Inundación

La idea de inundación dice que para enviar un paquete de un origen $u$ a un destino $v$ los caminos usados son aquellos que respetan las siguientes reglas:
- $u$ manda el mensaje por todas las líneas de salida
- Cada paquete que llega a un enrutador distinto de $v$ se reenvpia por cada una de las lpineas excepto aquella por la que llegó

Hay algunos problemas con la idea anterior:
- La inundación genera grandes cantidades de paquetes duplicados, a menos que se tomen algunas medidas para limitar el proceso
- Árbol de envío de paquetes. Cada arco representa un paquete que se envia
- Árbol de envío de paquetes es infinito con infinitos duplicados. O sea, se generan infinitas rutas. La causa es la presencia de ciclos en el grafo de la subred

Por eso, ahce falta limitar un poco el proceso de inundación dado en la idea anterior para resolver el problema. La solución es que cada enrutador recuerda *los paquetes difundidos* previamente por 'el para decidir si acepta un paquete
  

**Refinamiento de la solución de registro de paquetes difundidos:**
- El enrutador de origen pone *número de secuencia en cada paquete que recibe de sus host (así se distingue entre paquetes distintos del mismo enrutador de origen)*
- Un enrutador recuerda para cada enrutador de origen los números de secuencia recibidos
- Si llega un paquete a un enrutador con par <enrutador de origen, número de secuencia> recibido antes, no se lo reenvía

En la implementación para cada enrutador se usa una *tabla de registro de paquetes difundidos*.
Con esto podemos limitar que las listas enlazadas crezcan sin limites. ¿Como? Bueno vamos a agregar una columna llamada contador que indica el mayor número de secuencia tal que llegaron paquetes con todos los números de secuencia anteriores desde ese enrutador de origen.

Tambien existe **inundación con contador de saltos:** el cual integra un contador de saltos en el encabezado de cada paquete, que disminuye con cada salto y el paquete se descarta cuando el contador llega a 0.
**¿Como se determina el contador de saltos?**
Lo dieal es inicializar el contador de saltos a la *longitud de la ruta entre el origen y el destino*. Si el emisor desconoce el tamaño de la ruta, puede inicializar el contador en el peor caso, es decir, el *diametro total de la subred*

Y por ultimo **Inundación selectiva:** Es una idea para la inundación bastante práctica en donde:
- Los enrutadores no envían cada paquete de entrada por todas las lineas, sino solo por aquellas que van aproximadamente en la dirección correcta.
- El enrutador necesita almacenar información para poder aplicar inundación selectiva, especificamente:
- 	Se necesita saber en que dirección va cada linea
- 	Se necesita saber en qué dirección está el destino


## Protocolo de Enrutamiento de Estado de Enlace

Requerimos un algoritmo de enrutammiento que se adapte a cambios en la topología y el trafico de la red.

La idea es que al usar el algoritmo de Dijkstra periódicamente y cada vez que cambia la topología en la red, se va a tener en cuenta la topología y el tra¿áfico. En cada una de esas veces se necesita conocer la topología de la subred y los retardos de las líneas.
El algoritmo de enrutamiento de estado de enlace implementa esta idea

**Enrutamiento de estado de enlace (Link state routing-LSR):**
- En cada enrutador usar *algoritmo de Dijkstra* para encontrar la ruta más corta de un enrutador a los demás enrutadores
- La topología y retardos en las líneas se distribuyen a cada enrutador.
- Este algoritmo es valioso porque responde rapido frente a cambios en la topología de la red y es amplicamente usado en internet (como parte del protcolo OSPF)
- **¿Que tareas debe hacer un enrutador LSR?**
1. Descubrir sus vecinos
2. Medir el costo a cada uno de sus vecinos
3. Construir un paquete diciendo lo que ha aprendido
4. Enviar este paquete a todos los demás enrutadores
5. Computar el camino más corto a cada uno de los otros enrutadores

Para averiguar quiénes son los vecinos de un enrutador se envía un *paquete hello* a cada línea punto a punto. Se espera que el enrutador del otro extremo regrese una respuesta indicando quién es


Para que un enrutador conozca el retardo hasta sus vecinos se puede enviar un paquete ECHO especial a través de la linea. Una vez que llegue al otro extremo, éste debe regresarlo inmediatamente. Se usan temporizadores para medir el tiempo, normalmente midiendo el tiempo de ida y vuelta y se divide por 2.
El único problema de este metodo es que asume implícitamente que los retardos son simétricos

Cada enrutador construye un *paquete de estado de enlace (LSP)* que contiene:
- Identidad del emisor (para saber de quien se trata)
- Número de secuencia (para distinguir entre distintos LSP de un enrutador)
- Edad
- Lista de <vecino, retardo al vecino>

Los LSP se contruyen a intervalos irregulares. Normalmente construirlos cuando ocurra un evento significativo, como la caída o la reactivación de la línea o de un vecino, o el cambio apreciable de sus propiedades

Para la **Distribución confiable de los LSP** se utiliza inundación, pero se lleva *registro de los paquetes difundidos*.
- Cada paquete contiene un *Número de secuencia* que se incrementa con cada paquete nuevo enviado. Los enrutadores llevan el registro de todos los pares <enrutador de origen, secuencia> que ven.

Cuando llega un LSP a un enrutador, si es nuevo (nuevo número de secuencia mayor que los anteriores) se reenvia a través de todas las líneas, excepto aquella por la que llegó.
Si es un duplicado (número de secuencia mayor visto, pero repetido) se descarta.
Si llega un paquete con número de secuencia menor que el mayor visto hasta el momento, se rechaza como obsoleto debido a que el enrutador tiene datos más recientes.

Se puede construir la tabla de enrutamiento de un enrutador una vez que el enrutador ha acumulado un grupo completo de paquetes de estado del enlace.
Primero usando los LSP construir el grafo de la subred completa. Cada enlace se representa dos veces, una para cada dirección. Los dos valores pueden promediarse o usarse por separado.
Se ejecuta el algoritmo de Dijkstra para construir la ruta mas corta a todos los destinos posibles.
Con los resultados del mismo se actualiza la tabla de enrutamiento

El algoritmo de inundación de paquetes de estado de enlace tiene algunos problemas que mencionamos a continuación:

**Primer problema:** Si los números de secuencia vuelven a comenzar, reinará la confusión. La solución es usar un número de secuencia de longitud suficiente para que el problema anterior no suceda. Por ejemplo 32 bits

**Problema 2:** Si llega a corromperse un número se secuencia y se escribe 65540 en lugar de 4 (un error de un bit), los paquetes 5 a 65540 serán rechazados como obsoletos, dado que se piensa que el número de secuencia actual es 65540. Para solucionar esto, como protección contra los errores en las líneas enrutador-enrutador, se confirma la recepción de todos los paquetes de estado del enlace. Antes de actualizarse el número de secuencia más grande, el enrutador manda una confirmación de recepción al transmisor y luego espera una respuesta afirmativa o negativa del transmisor. En el primer caso se actualiza el número de secuencia mas grande, en el segundo caso se descarta el paquete que se recibió por estar errado

**Problema 3:** Si llega a caerse un enrutador (de origen), perderá el registro de su número de secuencia. Si comienza nuevamente en 0, se rechazará el siguiente paquete.
Para solucionarlo, la información de los enrutadores sólo expira (a lo largo de la red) cuando el enrutador está caido

**¿Cuando se puede detectar que un enrutador está caído?**
Cuando se actualicen las tablas de enrutamiento y se manden los paquetes Hello.

Una vez identificado que enrutador está caído se hace lo siguiente:
- Se propaga la información de este hecho por toda la red.
- Se hace que la información asociada al enrutador caído expire (paquetes pendientes a enviar, número de secuencia más grande recibido, etc.)
- Así que cuando ese enrutador vuelva a la vida, puede comenzar con número de secuencia 0

**Problema 4:** ¿Cómo hacer para asegurar que no pueda perderse ningún paquete y sobrevivir durante un período indefinido?
Para ello se debe incluir un campo de *edad en cada paquete* tal que:
- Se disminuye la edad una vez cada segundo
- Los enrutadores también decrementan el campo edad durante el proceso inicial de inundación
- Se descarta el paquete cuya edad sea 0

Para hacer el algoritmo de inundación de paquetes más eficiente:
- Una vez que un paquete de estado del enlace llega a un enrutador para ser inundado, no se encola para transmisión inmediata. En vez de ello, entra en un *búfer de almacenamiento* donde espera un tiempo breve.
Sia ntes de transmitirlo, llega otro paquete de estado del enlace proveniente del mismo origen, se comparan sus números de secuencia. Si son iguales se decarta el duplicado, si son diferentes se desecha el más viejo


El *buffer de paquetes para un enrutador* contiene una celda por cada paquete de estado de enlace recién llegado, pero aún no procesado por completo.
Una fila de la tabla del búfer de paquetes de un enrutador contiene:
- Origen del paquete, número de secuencia, edad, datos de los estados de enlaces.
- Puede tener ciertas *Flags* o *banderas* como:
- 	Banderas de confirmación de recepción: indica a dónde tiene que enviarse la confirmación de recepción del paquete
- 	Banderas de envío: significan que el paquete debe enviarse a través de las líneas indicadas.
- 	Si llega un duplicado mientras el original aún está en el bufer, los bits de las banderas tienen que cambiar

El número de secuencia y edad son usados para inundación confiable.
Los paquetes LSP nuevos son confirmados en las líneas que son recibidos y enviados por todas las demás lineas

## Protocolo de vector de distancia

Cada enrutador mantiene una *tabla de enrutamiento (o de reenvío)* indizada por cada enrutador en la subred. Cada entrada comprende la línea preferida de salida hacia ese destino y una estimación del tiempo o distancia a ese destino.
A partir de su tabla de enrutamiento un enrutador E puede obtener *unv ector de distancia* que contiene una lista de pares <destino, retardo estimado>.
El retardo de un enrutador a un vecino suyo, puede medirlo con *paquetes de ECO* que el receptor simplemente marca con la hora y los regresa tan rápido como puede.

Cada $t$ mseg, cada enrutador envía a todos sus vecinos un vector de distancia y también recibe un vector de distancia de cada vecino.

**NOTACIÓN:**
- El vector de distancia del enrutador X se denota con $VD_X$.
- $VD_X$ es una función: $VC_X(i)$ que es la "distancia estimada" para llegar al enrutador i desde X
- Si X vecino de E, el retardo de E a X se denota con $R_{E,X}$ y se obtiene mediante un paquete ECO
- Entonces la distancia estimada desde E enrutador a i a traves de X es $R_{E,X} + VD_X(I)$

Si tengo muchas estimaciones del camino mas corto de E hasta i pasando por $X_n$, claramente la mejor va a ser la menor de todas ellas, siendo entonces el vecino de E con mejor estimación quien conviene que sea la línea de salida a usar desde E para ir a i

El enrutador E estima la *distancia* desde E al enrutador de destino i de la siguiente manera: 
$d(E, i) = \min (\{ R_{E,X} + VD_X(i) | X vecino de E  \})$

El mejor vecino para ir desde E a I se define como: 
$MV(E,i) = \text{elegir} \{ V:R_{E,V} + VD_V(i) = d(E,i)\}$

Entonces para actualizar la tabla de enrutamiento de E se va a seguir la secuencia:
- E recibió de todo vecino X suyo: $VD_X$ y $R_{E,X}$
- La tabla de enrutamiento de E en la fila del enrutador de destino i va a tener los valores: $d(E,i)$ y $MV(E,i)$
- Observar que la vieja tabla de enrutamiento no se usa en este cálculo


Lo malo del Algoritmo de Enrutamiento de Vector de Distancia, es que reacciona con rapidez a las buenas noticias, pero con lentitud ante las malas

Esto se debe a que si tengo por ejemplo N nodos, y todos los estan operativos y **ALCANZABLES** entonces como en cada paso todos comparten información, en a lo sumo N saltos todos sabran la topologia de la red y los caminos. El problema viene cuando hay un nodo inalcanzable o inoperativo, ya que como los nodos solo hablan con los vecinos directos (a distancia de 1 salto) siempre pretenderan que hay algun vecino lejano que sabra como llegar al nodo inalcanzable, haciendo que nunca se detecte el error


## Control de Congestión en la capa de red


La cola en un búfer que precede a un enlace tiene capacidad finita.
¿Que pasa con un paquete cuando llega a una línea de salida con buffer lleno?
El paquete que llega a un búfer lleno se pierde. Los paquetes perdidos deben ser retransmitidos por el enrutador previo o el host emisor.

Si comienzan a llegar muchos paquetes por algunas líneas de entrada y todas necesitan la misma línea de salida, se irán acumulando los paquetes en una cola. Si no hay suficiente memoria para almacenar todos los paquetes, muchos de ellos se perderán


Si bien vimos control de congestión en TCP, estos algoritmos tienen problemas:
- El host destino demora demasiado en enterarse de la congestión (solo por expiración de temporizador de retransmisiones o 3 ack duplicados)
- Los hosts solo se enteran de pérdidas de paquetes, no pueden controlar qué paquetes perder y cuáles no

Tenemos varias razones para estudiar el control de congestión en la capa de red:
- Para resolver los problemas de los protocolos de control de congestión de TCP mencionados
- Para entender las medidas que pueden tomar los enrutadores para detectar la congestión y colaborar con la capa de transporte para ayudar a controlar mejor la congestión

Hay 2 tipos de soluciones que son las primeras que se nos ocurren:
- Aumentar los recursos
- Disminuir la carga en la subred (nos concentramos en esto)

Formas de disminuir la carga en la subred:
- **Regulación del tráfico:** hacer que hosts responsables de la congestión se enteren más rápido (que con protocolos de TCP) de la congestión y reduzcan su tasa de transferencia
- **Desprendimiento de carga:** enrutadores descartan paquetes inteligentemente antes que se saturen los buferes


#### Identificación de la Congestión

¿Como puede hacer un enrutador para darse cuenta si tiene algún puerto de salida congestionado?
Para ello cada enrutador monitorea la demora de la cola de línea de salida.
Se asocia a cada línea d = *demora reciente de cola de esta línea*
Tomar periodicamente una muestra de la *longitud de cola instantanea de la línea*
Actualizar d periodicamente usando: $d_{nvo} = a \space d_{ant} + (1-a) * s$ donde $a$ determina la rapidez con que el enrutador olvida la historia reciente

Siempre que $d$ rebasa un umbral, la línea de salida entra en un *estado de advertencia*.
Cada paquete nuevo que llega se revisa para ver si su línea de salida está en estado de advertencia. Si es así, se realiza alguna acción


#### Regulación de Tráfico

La **regulación de tráfico** es cuando los emisores ajustan sus transmisiones para enviar un tráfico que la red pueda soportar.
La congestión se da en los enrutadores (y no en los hosts).
¿Como se puede enterar un host de que hay congestión?
Bueno pues, se le avisa de la congestión
Una vez que un enrutador tiene una línea de salida en estadod e advertencia puede avisar a los hosts responsables de los paquetes que llegan a esa línea congestionada

**Método de paquetes reguladores:**
1. Usar *paquetes reguladores* si la línea de salida esta en estado de advertencia. El enrutador regresa un *paquete regulador (PR)* al host de origen, proporcionándole el destino encontrado en el paquete
2. Para que el paquete original no genere más PR más adelante en la ruta, en el paquete original se activa un bit del encabezado y despúes se reenvía
3. El PR le pide al host de origen que reduzca en un porcentaje X el tráfico enviado al destino especificado
4. El host ignora los PR que se refieran a ese destino por un intervalo fijo
5. Una vez que haya expirado ese tiempo, el host escucha más PR durante un intervalo I. Si llega alguno, el host reduce el flujo aún más y comienza a ignorar nuevamente los PR. Si no llega ningun PR durante I, el host incrementa el flujo

Lo malo del método de paquetes reguladores es que a altas velocidades o distancias grandes, el envío de un paquete regulador a los hosts de origen no funciona bien porque la reacción es muy lenta

La solución es el *Método de paquetes reguladores de salto por salto*. Hacer que el paquete regulador ejerza su efecto en cada salto que da, de modo que:
- Cuando el paquete regulador llega a un enrutador F, se le obliga a F a reducir el flujo al siguiente enrutador D (F deberá destinar más buferes al flujo)
- Luego el paquete regulador llega al enrutador E anterior a F e indica a E que reduzca el flujo a F. Esto impone una mayor carga a los buferes de E, pero da un alivio inmediato a F. Y se sigue así sucesivamente


**Método de bit de advertencia**. Señalar el estado de advertencia activando un bit especial en el encabezado del paquete. Cuando el paquete llega a su destino, la entidad transportadora copia el bit en la siguiente confirmación de recepción que se regresa al origen. A continuación el origen reduce el trafico. Mientras el enrutador está en estadod e advertencia, continua activando el bit de advertencia, lo que significa que el origen continua obteniendo confirmaciones de reepción con dicho bit activado.
El origen monitorea la fracción de confirmacipnes de recepción con el bit activado y ajusta su tasa de transmisión de manera acorde. En tanto los bits de advertencia continuan fluyendo, el origen continua disminuyendo su tasa de transmisión.
Cuando la tasa de transmisión disminuye lo suficiente, el origen incrementa su tasa de transmisión. Debido a que cada enrutador a lo largo de la ruta puede activar el bit de advertencia, el tráfico se incrementa solo cuando no había enrutadores con problemas

Una implementación de bit de advertencia usada por TCP es *ECN (Explicit Congestion Notification):*
- Se usa en TCP/IP
- Se marcan 2 bits en el encabezado IP con distintos fines
- 	00: transporte no capaz en ECN
- 	10: transporte capaz de ECN, ECT(0)
- 	01: transporte capaz de ECN, ECT(1)
- 	11: congestión encontrada, CE
- Si ambos extremos soportan ECN mandan sus paquetes con ECT(0) y ECT(1) respectivamente
- Si el paquete atraviesa una cola congestionada y el enrutador soporta ECN, se cambia código en el paquete CE para avisar al receptor de la congestión
- El uso de ECN en conexión TCP es opcional
- Para usar ECN, debe ser negociado al establecer la conexión TCP incluyendo opciones adecuadas en segmentos SYN y SYN-ACK
- Se usan dos banderas en encabezado TCP para soportar ECN:
- 	ECE(ECN echo): se usa para mandar indicación de congestión al emisor
- 	CWR (ventana de congestión reducida): es usada para confirmar que la indicación ECE fue recibida

**Secuencia de ejecución de ECN típica:**
1. Se negocia ECN en conexión TCP
2. Emisor manda paquete IP P con ECT(0)
3. P llega a enrutador congestionado que soporta ECN y enrutador marca P con CE
4. Receptor recibe P con CE y manda segmento Q(con ACK P) de vuelta usando bandera ECE prendida
5. Emisor recibe Q con ECE prendido, entonces emisor reduce la ventana de congestión
6. Emisor manda siguiente segmento al otro extremo usando la bandera CWR prendida para confirmar recepción de aviso de congestión
Se continúa transmitiendo segmentos con ECE prendido hasta recibirse un segmento con CWR prendido

#### Desprendimiento de Carga

En el esquema anterior cuando se satura una línea de salida de un enrutador, se pierden paquetes indiscriminadamente. Esto claramente es un problema a solucionar ya que no todos los paquetes tienen la misma importancia.

Una solución seria descartar los paquetes inteligentemente antes de que se ocupe todo el espacio del búfer cuando hay estado de advertencia en una línea de salida

Algunos criterios para escoger qué paquetes descartar:
- **Según el tipo de aplicación que se está usando:**
- 	Estrategia Vino: descartar primero los paquetes más nuevos
- 	Estrategia Leche: descartar primero los paquetes mas viejos
- **Según la importancia de los paquetes:**
- 	Marcar los paquetes con clases de prioridades
- 	Los enrutadores primero se desprenden de paquetes de la clase más baja, luego los de la siguiente clase, etc.

Se suele usar desprendimiento de carga junto con reducción de tráfico. La respuesta a paquetes perdidos por desprendimiento de carga es que el origen disminuya su tasa de transferencia.
Si expira el temporizador de retransmisiones, el emisor lo toma como pérdida de paquete. Vemos ahora una implementación de esta solución

**Implementación del Algoritmo de detección temprana aleatoria (RED)** para detectar cuándo comenzar a descartar paquetes, los enrutadores mantienen un *promedio móvil de sus longitudes de cola*. Cuando este promedio de una cola C sobrepasa el umbral, una pequeña fracción de los paquetes son descartados al azar. Con cada uno de esos paquetes:
1. El enrutador *elige un paquete al azar* de C
2. Se descarta el paquete seleccionado
3. El origen notará falta de ACK y la capa de transporte disminuirá la velocidad de transmisión.

El elegir paquetes al azar hace más probable que los host emisores más rápidos pierdan un paquete, lo noten, y reduzcan su tasa de transferencia.

El método RED se usa en internet cuando los hosts no pueden recibir señales explicitas de congestión. Tanenbaum dice que la mayoría de los host de internet no reciben mensajes explicitos de congestión de los enrutadores


## La capa de Red IP y NAT

Protocolo de CR *IP (protocolo de internet)*
Su propósito:
- Explicar formato de datagramas
- Definición de direcciones IP
- Definición de redes
- Definición y uso de tablas de reenvío
- Manejo de fragmentación de paquetes

**Razones para estudiar IP:**
1. Para entender cómo se hacen asignaciones de direcciones de red a máquinas en una red local, a instituciones varias. Para entender cómo designar o identificar a las redes
2. Para comprender cómo se hace el renvío de paquetes en internet
3. Para comprender cómo se hace la fragmentación y reensamblado de paquetes
4. IP da la base conceptual para entender otros protocolos de capa de red en internet

IP tiene dos versiones:
- IPv4: trabaja con direcciones IP de 32 bits
- IPv6: trabaja con direcciones IP de 128 bits
- Los formatos de datagrama de la dos versiones son diferentes

La capa de red del internet tiene las siguientes metas:
1. *Datagramas IPv4* para poder comprender cómo los enrutadores/hosts hacen el procesamiento de paquetes
2. Direcciones IPv4
3. Conceptos fundamentales en los que nos basamos
4. Asignación de redes a organizaciones
5. Tablas de enrutamiento. Uso de enfoque CIDR
6. Control de tamaño de tablas de enrutamiento. Uso de enfoque de agregación de prefijos
7. Racionamiento de uso de direcciones IPv4. Uso del enfoque NAT

#### Datagramas IP

*datagrama IP* = encabezdo + texto
*encabezado* = parte fija de 20 bytes + parte opcional
Un encabezado tiene varios campos. Cada tipo de información que necesito va en uno o más campos. La parte opcional tiene longitud variable

Entre las partes obligatorias estan:
- Campo *IHL* (4b). Se maneja igual que el mismo campo en TCP, longitud del encabezado en palabras de 32b o 5 cuando no hay opciones.
- Campo *longitud total:* 2B de encabezado + datps $\le$ 65535 B
- Campo *tipo de servicio:* Los ultimos 2 bits se usan para información de notificación de congestión. Los 6 primeros bits se usan para indicar la clase de servicio
- Campo *protocolo* (8b): dice a cuál proceso de transporte entregar el paquete
- Campo *identificación:* se usa para que el host de destino determine a qué paquete un fragmento pertenece
- Campo *tiempo de vida:* se usa para limitar el tiempo de vida de un paquete. Debe decrementarse en cada salto. Cuando llega a cero el paquete es descartado y se manda un paquete de advertencia al host de origen. Esto evita que los paquetes anden dando vueltas demasiado tiempo
- Campo *suma de verificación:* se usa para detectar errores en el encabezado cuando el paquete viaja a lo largo de la red. Deve recalcularse en cada salto, porque el campo tiempo de vida siempre cambia. Es solo sobre el encabezado porque en capa de transporte se chequea el segmento entero con otro campo checksum.
- En un datagrama IP tambien estan los campos *direcciones de origen y de destino*, cada una tiene 32 b e indican el número de red y el número de máquina. Como consecuencia de esto se usan npumeros IP diferentes para distinguir las máquinas de una red, además las direcciones IP son jerárquicas

#### Direcciones IP

Cada host y enrutador en la internet tienen una *dirección IP* tal que la dirección mas baja es 0.0.0.0 y la mas alta 255.255.255.255.
**Una máquina puede tener más de una IP**, ya que cada máquina tiene una IP por cada red a la que está conectada

Una *interfaz* es la conexión entre el host/enrutador y el enlace físico. Un enrutador tiene muchas interfaces, una por cada línea de salida. Un host tiene una o dos interfaces:
- con Ethernet cableada
- Con red inalambrica 802.11 (Wi-Fi)
Cada interfaz tiene asociada una dirección IP

Las inteerfaces están conectadas entre sí por medio de **conmutadores y estaciones base**


#### Conceptos fundamentales en los que nos basamos

Una red corresponde a un bloque contiguo del espacio de direcciones IP llamado *prefijo*.
Los prefijos se escriben dando la dirección IP más baja en el bloque y la cantidad de bits usadas para la dirección de la red.
Por ejemplo en el prefijo 128.208.0.0/24 la dirección IP más baja en el bloque es 128.208.0.0, la porción de la red es de 24 bits y hay 2^8 máquinas en la red

En el libro de *Kurose* se define una subred como un conjunto de interfaces de dispositivos con la misma parte de red de la dirección IP.
Otra definición seria máquinas que se pueden alcanzar físicamente entre sí *sin la necesidad de un enrutador interviniente*

La **"Receta"** para determinar las subredes es:
Desacoplar cada interfaz de su host o enrutador, creando islas de redes aisladas. Cada red aislada se llama una *subred*. Las subredes se indican usando prefijos


#### Asignación de redes a prganizaciones

**Efecto sobre el reenvío de paquetes de tener una tabla de reenvío grande:**
- Los enrutadores deben buscar en la tabla de reenvío grande para enviar cada paquete, la eficiencia de esta búsqueda es afectada
- Los enrutadores en un proveedor de servicios de internet (PSI) grande pueden tener que enviar millones de paquetes por segundo. Este gran volumen de paquetes a enviar empeora más las cosas. Para esto hace falta hardware especial y una computadora de propósito general no alcanza.

**Efecto sobre el algoritmo de enrutamiento de tener una tabla grande:**
El costo de actualizar las tablas de enrutamiento es grande
En **CONCLUSIÓN:** hay que evitar tablas de reenvío demasiado grandes.

Se nos genera un nuevo problema, ¿Cómo asignar una red a una organización sin que se desperdicien demasiadas direcciones y sin que las tablas de enrutamiento crezcan demasiado?
- Si se le da una red demasiado chica a una organización, esta puede expandirse y terminar con más de un prefijo, lo cual qumentará el tamaño de algunas tablas de reenvío. Por lo tanto, cada organización debe tener un solo prefijo de red
- Si se le da una red demasiado grande a una organización, entonces se pueden desperdiciar muchas direcciones IP.
- Colocar todas las subredes del mundo en una tabla de reenvío hace que las tabla sea demasiado grande. Esto no es necesario, porque veremos que un enrutador en una región no necesita saber de subredes en regiones muy alejadas de ella

Esto nos genera un **subproblema:** ¿Cómo asignar una red a una organización sin que se desperdicien demasiadas direcciones?.
La idea de la solución es alojar las direcciones IP de una red en un bloque contiguo que permite 2^k máquinas. Por ejemplo, si un sitio necesita 2000 direcciones, se le da un bloque de 2048 direcciones

**Implementación de la solución: CIDR (Classles Inter Domain Routing):**
En todas las máquinas de la red, la parte de la dirección IP para identificar la red es la misma. Se presenta la red asignada con un *único prefijo*

#### Tablas de enrutamiento

Una máscara de una red está formada por 1s para identificar la red seguido de 0s para identificar las máquinas. ¿Cual es la máscara de la red de prefijo 128.208.0.0/24?
La máscara seria 11111111 11111111 11111111 00000000, otra forma de expresarla es 255.255.255.0

¿Como podría definirse la tabla de enrutamiento?
Para ello el enrutamiento es jerárquico y solo se representan redes de organismos- las llamadas subredes.
Cada entrada de la tabla de enrutamiento se extiende para darle una máscara de 32 bits. *Tabla de enrutamiento* para todas las redes tiene entradas: (dirección IP inicio subred, máscara, línea de salida)






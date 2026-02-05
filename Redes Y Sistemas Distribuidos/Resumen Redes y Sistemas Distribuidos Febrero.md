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



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





# La Internet de las cosas(IOT)



> #### La internet de las cosas (IoT) es un sistema interconectado que
permite que dispositivos físicos , conocidos como dispositivos
IoT se conecten a internet y compartan datos entre sí y con
sistemas en la nube.

- Los dispositivos IoT se conectan a [[La Internet]] a través de diferentes tecnologías para enviar y recibir datos

- Estos datos recopilados pueden enviarse a plataformas en [[La nube]] donde se almacenan, procesan y analizan

- Las computadoras se usan para gestionar la red de los IoT, analizar los datos recopilados y el control y monitoreo de esta red



Algunos ejemplos pueden ser, sensores, actuadores, wearables, electrodomésticos inteligentes, cámaras de seguridad interconectadas, etc.



El propósito de la IOT es actuar en base a la información recopilada para (luego de un análisis de esta información) simplificar tareas cotidianas, reducir el esfuerzo humano y hacer que la tecnología sea mas accesible y mas user friendly. Aumentando así la eficiencia en diversos contextos como hogares, industrias, ciudades, la salud, etc.



### Las metas de la IoT son:

- Automatizacion de tareas humanas

- Proporcionar datos en tiempo real sobre condiciones específicas

- Optimizar recursos

- Mejorar la vida cotidiana

- Analizar los datos apra tomar decisiones 

- Mejorar la seguridad física




# Estructura de la IoT

## Las redes de IoT pueden clasificarse segun diferentes criterios:

### Por tipo de conectividad:

- **Redes de celulares**

    - Usan tecnologías como 4G y 5G para proporcionar alta
    velocidad y cobertura amplia. 

- **Redes de medio alcance**

    - Como WIFI

- **Redes de corto alcance**

    - Incluyen tecnologías como Bluetooth y Zigbee, que son
    adecuadas para entornos pequeños como hogares y oficinas.

- **Redes de área amplia de baja potencia(LPWAN)**

    - Estas redes están diseñadas para dispositivos que requieren largas distancias de comunicación con bajo consumo energético.

### Por proposito o aplicacion

- **Redes de salud**

    - Se usan en aplicaciones de telemedicina y monitoreo de pacientes, permitiendo la recopilación y transmisión de datos médicos en
    tiempo real. Suelen usar dispositivos wearables que envían datos a
    profesionales médicos.

- **Redes industriales**

    - Diseñadas para el monitoreo y control de maquinaria en fábricas. Usan redes celulares o Ethernet industrial.

- **Redes de agricultura inteligentes**

    - Usadas para la monitorización de cultivos y ganado, aprovechando la tecnología LPWAN. Suelen usar sensores para recopilar datos.

- **Redes de hogar inteligente**

    - Integran dispositivos domésticos conectados como termostatos, cámaras de seguridad. Usan Zigbee o Zwave.

- **Redes para ciudades inteligentes**

    - Usadas para gestionar servicios urbanos como el tráfico, la iluminación pública y la gestión de residuos. Suelen usar sensores para recolectar datos. Pueden incluir redes de celulares o LPWAN.

- **Redes de transporte y logística**

    - se usan para optimizar el transporte y la gestión de la cadena de suministro. Por ejemplo:seguimiento de vehículos y flotas, monitoreo de condiciones descarga, sistemas de gestión de almacenes.

- **Redes IoT de retail**

    - Se usan para mejorar la experiencia del cliente y la eficiencia operativa en el comercio minorista. Por ejemplo: beacons para marketing de proximidad, sistemas de inventario inteligentes, análisis de comportamiento de clientes.

### Por consumo energético

- **Bajo consumo**

    - Redes que priorizan la eficiencia energética

- **Muy Bajo consumo**

    - Como RFID (para rastrear ubicación y movimiento de productos en tiendas; para permitir acceso a áreas restringidas en edificios de oficinas, para rastreo de ganado) y NFC (para pagos móviles, compartir información entre celulares, llaves electrónicas, usados en productos o tarjetas personales para proporcionar información).

- **Alto consumo**

    - Redes que pueden soportar dispositivos con mayor demanda energética. Suelen usar WiFi o redes de celulares



## Redes IoT de sensores

Una red de sensores normalmente incluye diversos dispositivos para recopilar, analizar y transmitir datos

Normalmente están compuestas por:

- **Sensores:** Dispositivos que recopilan datos especificos

- **Gateways IoT:** Dispositivos que hacen de intermediarios entre los sensores y la nube, transmiten data

- **Servidores en la nube:**  almacenamiento y procesamiento e datos, análisis y ejecución de algoritmos

- **Dispositivos de usuario:**  dispositivos usados para monitoreo y controlar la red de sensores

## Conectores entre dispositivos

- **Sensores a Gateways Iot:** usualmente conectados mediante redes inalambricas de corto o mediano alcance o redes de largo alcance y baja potencia

- **Gateways Iot a Servidores en la nube:** Conectados a traves de internet usando TCP/IP normamente mediante wifi, ethernet o redes moviles

- **Servidores en la nube a dispositivos del usuario:** Conecion a traves de internet usandi TCP/IP permitiendo el acceso remoto

## SIstemas CPS(Cyber-physical Sistems)



Estos sistemas están diseñados para interactuar con el mundo físico a través de sensores y actuadores y están controlados por algoritmos computacionales. **Caracteristicas:**

- Capacidad para interactaur y controlar procesos físicos

- Alta fiabilidad y seguridad

- Procesamiento distribuido y en tiempo real



## Dispositivos invilucrados en una CPS

- **Sensores:** lo mismo que en la red de sensores

- **Actuadores:**  Dispositivos que realizan acciones en base a los datos

- **Controladores:** Dispositivos que procesan los datos de los sensores y envian mensajes a los actuadores. Es el cerebro del sistema

- **Sistemas en la nube:** lo mismo q antes

- **Dispositivos de usuario:**  lo mismo que antes



## Conexiones entre dispositivos

- **Sensores a controladores:** Conexion por cable o inalambrica

- **Controladores a actuadores:** conexion por cables o inalambricas

- **Controladores a servicios en la nube:** Conexion por ethernet o redes celulares

- **Conexiones entre servidores en la nube y dispositivos de usuario**



# Funciones de un controlador

- **Recopilacion y procesamiento de datos** provenientes de sensores

- **Control y ejecucion de acciones** basados en los datos de sensores y las cordinaciones programadas el controlador envía comandos a los
actuadores para realizar acciones específicas.

- **Monitoreo y supervicion:** mantiene un monitoreo constante del estado
de los dispositivos conectados incluyendo sensores y actuadores.

- **Comunicacion y coordinacion:** facilita la comunicación entre diferentes
dispositivos y sistemas en la red, actuando como intermediario para la
transmisión de datos. Se coordina con Gateways IoT y servidores en la
nube para el análisis y almacenamiento de datos.

- **Gestor de alarmas y eventos:** detecta condiciones anómalas o
situaciones de fallo y genera alarmas para notificar al personal de
mantenimiento o a los sistemas de supervisión. Registra eventos
importantes para el diagnóstico y el análisis posterior.

- **Retroalimentacion de Gateways y sistemas en la nube:** transmite datos
recopilados y procesados a los servidores en la nube para análisis
adicional y almacenamiento. Puede sincronizar datos con otros sistemas
de control y monitoreo remoto.



# Sistema operativo para la Nube



# ***Sistemas operativos para la Nube***



#### Conocimiento previo:

- **Infraestructura como servicio(laaS):**

    Ambiente formado por recursos informaticos basicos que pueden ser accedidos via interfaces basadas en servicios en la nube y herramientas. Los usuarios pueden aprovisionar,configurar y gestionar sus propios recursos informaticos. Los proveedores son responsables del mantenimiento

- **Plataforma como servicio(PaaS):**

    Plataforma completa para que los desarrolladores creen,desplieguen y gestionen aplicaciones sin preocuparse por la infraestructura subyecente. Proporciona herramientas y servicios para el desarrollo de aplicaciones como base de dats, middleware y entornos de ejecucion, tambien el proveedor esta a cargo del mantenimiento

- **Software como servicio**

    Permite a los usuarios acceder a aplicaciones completas alojadas en la nube mediante una suscripcion, sin necesidad de instalacion o mantenimiento local. Se puede acceder als ervicio mediante cualquier aparato tecnologico con conexion a internet

- **Virtualización:**

    Permite dividir un servidor fisico en varias amquinas virtuales, donde cada una es capaz de ejecutar su propio sistema operativo y aplicaciones. El **Hipervisor** es el software que se encarga de permitir que varias instancias se ejecuten en un solo servidor fisico. SI una maquina virtual falla no afecta a las demas, y se pueden agregar segun se necesite



- **Containerizacion:**

    Se empaqueta el codigo de la aplicacion junto con los archivos de configuracion relacionados requeridas para ejecutar el codigo. Las aplicaciones son desplegadas en contenedores donde cada contenedor ejecuta un proceso, permitiendo asi ejecutar varios servicios en la nube ejecutarse como un servidor, si un container falla no afecta al resto. AL compartir nucleo de sistema operativo, reqeuieren menos recursos que las VM



### Capa de red:

Esta formada por protocolos que facilitan la conectividad y el enrutamiento dentro de la infrestructura de red de cada proveedor

**Tipos de protocolos usados:**

- Protocolos de internet: para que losd atos puedan moverse entre redes. Se usan **IP** y **BGP**

- **VPN:** Permiten establecer conexiones seguras entre las redes del cliente y la nube por internet

- **Protocolos para conexiones privadas entre cliente y proveedor de la nube:** Cuando las empresas necesitan conexiones mas rapidas y seguras

### Capa de infraestructura:

Protocolos basicos que permiten la comunicacion y transferencia de datos entre servidores y clientes.



Incluye los tipos de protocolos:

- Protocolos de capa de aplicacion internet como **HTTP, HTPPS, FTP**

- Protocolos de capa de trasnporte de internet como **TCP,UDP**

### Capa de almacenamiento

Consiste de protocolos usados para acceder y gestionar datos almacenados en la nube. Se utilizan diferentes protocolos para este almacenamiento:

- **En bloque:** se almacenan datos en bloques individuales

- **De archivo:** permite accesoa  sistema de archivo

- **De objetos:** para grandes cantidades de datos no estructurados como **Archivos multimedia, copias de seguridad o datos IoT**



### Capa de Plataforma 

Es un conjunto de herramientas y servicios que los desarrolladores pueden usar para construir y ejecutar aplicaciones

Esta capa permite que las aplicaciones se conecten y trabajen con servicios en la nube utilizando APIs

**Facilidades:**

- Esta capa da todo lo necesario para que se pueda **Escribir codigo, probarlo y desplegarlo**

De esta forma los desarrolladores no tienen que preocuparse en configuraciones o gestiones.

En esta capa se usan los protocolos:

- **REST**

- **gRPC**



### Capa de Funciones sin Servidor

Involucra protocolos que permiten ejecutar codigo en respuesta a eventos sin necesidad de gestionar servidores ni la infraestructura.

**Tipos de evento mas comunes:**

- **Eventos HTTP**

- **Cambios en la base de datos**

- **Eventos de almacenamiento en la nube**

- **Eventos de ensajeria**

- **Eventos de la IoT**

- **Eventos** **a intervalos regulares**

- **Eventos de aplicaciones externas**



### Capa de contenedores:

protocolos y tecnologias usadas para la gestion y orquestacion de contenedores en al nube usando tecnologias como Kubernetes y Docker



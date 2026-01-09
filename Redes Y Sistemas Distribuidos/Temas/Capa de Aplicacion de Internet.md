
# Capa de Aplicacion de Internet



Para desarrollar aplicaciones de red para internet hay 2 enfoques:

- EL programador para especificar la comunicacion usa una interfaz para programar programar de aplicacion(API)

- **La Web**, el programador se apoya en la tecnologia de la web para contruir una aplicacion de red



## Arquitectura de Aplicaciones

Las aplicaciones de red de internet suelen usar uno de los siguientes estilos de arquitectura:

- Cliente-Servidor

- Peer-to-peer(P2P)

- Arquitectura orientada a servicios

- Microservicios



## Arquitectura CLiente-Servidor:

EN el modelo cliente-servidor hay 2 procesos que se comunican, uno en la maquina del cliente y otro en la maquina servidor

#### Forma de la comunicación:

1. El proceso cliente manda solicitud al proceso servidor

2. El proceso cliente espera un mensaje de respuesta

3. Luego el proceso servidor recibe y procesa la solicitud

4. El proceso servidor manda mensaje de respuesta al proceso cliente

#### Caracteristicas de los servidores:

- Siempren estan en un host

- Con direccion IP permanente

- Se pueden usar centros de datos para escalabilidad

#### Caracteristicas de los clientes:

- Pueden estar conectados **intermitentemente**

- Usando direcciones IP dinamicas

- Los clientes no se comunican directamente entre si



#### Pasos de una aplicacion cliente-servidor usando UDP:

1. Cliente crea datagrama con IP y puerto del servidor y envía datagrama

2. Si llega,servidor lee datagrama

3. Servidor envia respuesta especificando direccion y puerto de cliente

4. Si lega, cliente lee datagrama

5. Cliente finaliza



#### Evaluación

- No se dice que se hace si al respuesta no llega al cliente

- Es responsabilidad de la aplicacion de red manejar esto



#### Pasos de una aplicacion cliente-servidor usando TCP

1. Se ejecuta del servidor

2. Servidor espera por pedido de conexion entrante

3. El cliente requiere pedido de conexion al servidor

4. El servidor acepta la conexion con el cliente

5. El cliente envía pedido al servidor

6. El servidor lee el pedido

7. El servidor envía la respuesta

8. El cliente lee la respuesta

9. Si hay mas pedidos al servidor: Goto 5

10. El cliente cierra la conexion

11. El servidor cierra la conexion



## Arquitectura P2P

#### Ejemplos de aplicaciones P2P:

- **Distribución de archivos:** La aplicacion distribuye un archivo de una única fuente a un gran numero de compañeros

- **Bases de datos distribuidas:** Sobre una gran comunidad de compañeros

- **Streaming:** Video on demand

- **VoIP:** voz sobre IP

## Distribucion de archivos P2P vs Cliente-Servidor

#### Parametros a considerar:

- Tasa de subida del enlace de acceso al compañero i

- Tasa de subida del enlace de acceso al servidor

- Tasa de descarga del enlace de acceso al compañero i

- Tamaño del archivo a ser distribuido

- Numero de compañero que quieren adquirir una copia del archivo

El **Tiempo de distribución** es el tiempo que toma obtener una copia del archivo por los N compañeros. Tiempo para distribuir F a N clentes usando enfoque cliente-servidor



$D_{C-S} >= max({NF/u_S},F/d_{min}) $



Al comienzo de la distribucion solo el servidor tiene el archivo. Para que la comunidad de compañeros reciba este archivo, el servidor debe enviar cada bir del archivo al menos una vez en su enlade de acceso. EN P2P cada compañero puede ayudar al servidor a distribuir el archivo. Entonces la capacidad total de subida del sistema es:

$u_{Total}=u_s+\sum{u_i}$

Por lo tanto el **tiempo minimo de distribución es:**

$NF/u_{total}
$

Por lo cual tenemos que la distribucion de archivos de:

- **Cliente-Servidor es:**

    - $D_{C-S}>= max(NF/u_s,F/d_{min})
    $

- **P2P:**

    $D_{P2P}>= max(F/u_s , F/d_{min},NF/(u_s+ \sum{u_i}))
    $



### Bit Torrent:

Tracker: Listado de compañeros participando en el torrent

Torrent: Grupo de compañeros intercambiando trozos de un archivo



CUando un compañero se une a torrentno tiene trozos. Se registra en el tracker para obtener la lista de compañeros, se conecta a un subconjunto de estos y avisa al tracker que esta en BitTorrent. Mientras descarga un compaero sube trozos a otros compañeros. Se puede cambiar de compañeros y una vez alguno tiene un archivo completo puede quedarse o irse del torrent



## Arquitectura orientada a servicios

#### Requisitos funcionales:

- Provision de servicios

- Consumo de servicios

#### Requisitos no funcionales:

- Interoperabilidad

- Reusabilidad

- Escalabilidad

- Flexibilidad

- Seguridad

Organiza las aplicaciones en servicios reutilizables que se comunican entre si a través de un bus de servicios. Cada servicio realiza una función especifica y puede ser usado por diferentes aplicaciones. En SOA se usan patrones como solicitud-respuesta,publicar-suscribir o enviar-olvidar. Estos servicios pueden actuar tanto como servidores o clientes

**Nodos:**

- **Servicios independientes:** Cada uno tiene un rol definido

- **Bus de servicios empresarial(ESB):** Infraestructura de software que facilita la integración y la comunicación entre los servicios

- **Clientes:** Consumen los servicios ofrecidos




## Arquitectura de microservicios

#### Requisitos funcionales:

- **Provisión de servicios especializados:** proporcionar funciones únicas y bien definidas

- **Comunicación entre servicios:** Para cumplir con tareas más complejas

- **Consumo de servicios:** Los clientes o aplicaciones deben poder solicitar y recibir servicios de manera eficiente

#### Requisitos no Funcionales:

- **Escalabilidad:** Escalamiento independiente de cada servicio según demanda

- **Flexibilidad:** En el desarrollo y depliegue, los servicios deben adaptarce a las necesidades

- **Mantenibilidad:** Facil implementar nuevas funcionalidades

- **Seguridad:** Garantizar la seguridad de los datos y las transacciones entre servicios

- **Independencia y autonomia:** Cada servicio debe ser capaz de desarrollarse,implementarse y escalarse de manera independiente

- **Resiliencia:** Los servicios deben diseñarse para tolerar fallos y mantener operación continua, incluso si uno de ellos falla

Para esto se utiliza la **Arquitectura de microservicios** siendo esta una evolucion de la SOA.

En esta arquitectura la aplicacion se divide en pequeños **Servicios independientes** que se comunican entre sí a través de APIs REST o gRPC que no dependen de un lenguaje específico

- Cada microservicio se especializa en una tarea



#### Nodos:

- **Servicios independientes:** COmponentes funcionales de aplicacion que interactuan entre si

- **API Gateway:** Intermediario que gestiona las solicitudes entre clientes y microservicios

- **Clientes:** Aplicaciones que consumen los servicios

#### Mensajes de comunicación:

- **Clientes a API Gateway:** solicitudes de datos,comandos

- **API Gateway a Microservicios:** Ruteo de solicitudes a los microservicios correspondientes

- **Microservicios a API Gateway:** respuesta a las solicitudes, resultados de las operaciones

- **Microservicios entre si:** Conmunicacion inter-servicios para operaciones complejas

#### Protocolos:

se suele usar SOAP o REST para la comunicación entre servicios



## Protocolos de Capa de Aplicación

#### Cosas a definir en un protocolo de capa de aplicación:

- Tipos de mensajes intercambiados

- Sintaxis del mensaje

- Semantica del mensaje

- Reglas

- Estado

#### Tipos de protocolos

- Protocolos abiertos:

    - permiten interoperabiidad

    - son definidos en RFCs

- Protocolos propietarios

    por ejemplo: Skype



Para hacer un diseño detallado de una aplicacion de res sobre internet conviene definir un **Protocolo de capa de aplicacion,** el cual puede apoyarse o no en un protocolo base




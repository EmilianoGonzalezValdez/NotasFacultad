
# Sistema Operativo para IoT



Muchos dispositivos IoT sond e baja potencia y tienen recursos limitados. Por lo cual los protocolos para IoT están diseñados para ser ligeros y eficientes. La IoT se enfoca en la comunicación entre dispositivos IoT heterogéneos. A causa de esto se necesitan ciertos protocolos para escalar una gran cantidad de dispositivos IoT gestionando transmisiones de datos frecuentes y a menudo en tiempo real

Para IoT usaremos un modelo de capas por referencia con las mismas capas que para las redes de computadoras. La principal diferencia es que las capas en IoT tambiens e encargan de solucionar unos problemas mas especificos de IoT y que se agregan 2 capas mas. A continuacion veremos cada capa



## Capa fisica:

Se encarga de la transmision de bits a partir de medios fisicos(sensores y actuadores)

#### Problemas:

- **Consumo energetico:** Mejorar la eficiencia en uso de bateria

- **Interferencias y ruido:** Las comunicaciones inalambricas se pueden ver afectadas por interferencias o ruido

- **Conectividad:** Garantizar la conexione ntre dispositivos en entornos dificiles

#### Protocolos:

- **Zigbee:** Eficiente en consumo de bateria

- **LoRaWAN:** Permite la  eficiente comunicacion a larga distancia

- **NB-IoT:** Permite baja potencia y larga duracion de la bateria



## Capa de Enlace de Datos:

Responsable de la transmision de datos entre dispositivos dentro de la misma red local

#### Problemas:

- **Control de errores:** Igual que antes

- **Control de acceso al medio:** Igual que antes

- **Retrasos y variaciones en el tiempo de transmision** 

- **Desconexiones frecuentes:** Debido a que los dispositivos IoT suelen ser moviles y pueden llegar a lugares con mala cobertura

- **Seguridad de la comunicación:** Los datos enviados no deben ser interceptados

#### Protocolos:

- **Wi-Fi**

- **Ethernet**

- **Bluethooth**

- **Zigbee**

- **LoRaWan**

- **BLE:** Muy ideal al consumo de bateria

- **6LoWPAN:** permite encapsular y enviar paquetes IPV6 sobre redes de baja potencia

## Capa de Red:

Gestiona el direccionamiento y el enrutamiento de los datos entre diferentes redes

#### Problemas:

- **Enrutamiento:** En redes con dispositivos moviles y topologias cambiantes

- **Escalabilidad:** Gestio eficiente de un gran numero de dispositivos

- **Movilidad en redes inalambricas:** Soporte para dispositivos que se mueven fuera y dentro de la red

#### Protocolos:

- **IPV4,IPV6**

- **6LoWPAN:** permite que dispositivos de baja potencia usen IPV6

- **RPL:** Adapta las rutas de transmision en funcion de las condiciones de la red, optimizando el uso de los recursos y reduciendo el consumo de energía

## Capa de Transporte:

Asegura la transmision de datos confiable y ordenada entre dispositivos

#### Problemas:

- **Fiabilidad de la transmision:** asegurar que los datos lleguen de manera confiable

- **Control de flujo y gestion de congestion**

- **Compatibilidad de protocolo:** Integracion con protocolos especificos de IoT

#### Protocolos:

- **TCP, UDP**

- **MQTT:** Diseñado para minimizar el consumo de energia durante la transmision de datos

- **CoAP:** proporciona confirmaciones de entrega y retransmision de mensajes perdidos

## Capa de aplicación

Define protocolos de comunicación usados por las aplicaciones de la IoT(Facilita la comunicacion entre el usuario y el ssitema IoT)

#### Problemas:

- **Interoperabilidad:** Asegurar que los dispositivos y aplicaciones de diferentes fabricantes puedan comunicarse entre si

- **Seguridad y privacidad:** Garantizar que los datos sean transmitidos y almacenados de manera segura

- **Gestion de Dispositivos:** Administracion eficiente de un gran numero de dispositivos

- **Eficiencia Energetica**

- **Fiabilidad y calidad de servicio:** Entrega de mensajes confiables

- **Escalabilidad y ancho de banda:** Poder manejar la demanda al aumentar la cantidad de dispositivos

- **Simplicidad:** Simples de implementar

- **Complejidad:** Suficientemente complejos como para manejar las necesidades de las aplicaciones

#### Protocolos:

- **HTTP,HTTPS**

- **MQTT:** facilita la comunicacion entre dispositivos y servidores, entre distintos fabricantes, y soporta grandes cantidades de nodos y transmisiones de datos frecuentes. Utiliza un modelo de **Publicacion/uscriptor** es decir, manda datos solo cuando es necesario. Utiliza **Topicos** para direccionar mensajes y el **Broker** es un servidor que actua de itnermediario entre dispositivos IoT

- **CoAP:** proporciona un enfoque ligero para la comunicacion entre dispositivos y servidores. Ligero y facil de implementar. Ideal para dispositivos con baterias

- **WebSocket:** Se basa en TCP y permite streams de mensajes enviados en ambas direcciones entre cliente y servidor

- **DDS:** middleware centrado en datos para la comunicacion de maquina-maquina

- **XMPP:** comunicacion de tiempo real y streaming de datos XML

## Capa de procesamiento y Almacenamiento:

Responsable de procesar, almacenar y analizar losd atos recopilados por los dispositivos IoT

#### Problemas:

- **Procesamient en tiempo real:** Capacidad de procesar y analizar datos rapidamente

- **Almacenamiento Masivo:** Manejoeficiente de grandes volumenes de data

#### Componentes:

- Servidores locales

- edge computing

- las nubes

#### Tecnologias:

- Basees de datos

- sistemas de procesamiento de datos en tiempo real

- analisis de grandes cantidades de datos

## Capa de gestion y orquestacion

🤪 Se encarga de la gestion y orquestacion de la red IoT 

Proporciona herramientas para la configuracion,monitoreo,actualizacion y administracion de disositivos y aplicaciones IoT

#### Funciones:

- Gestion de dispositivos

- seguridad

- actualizaciones de firmware

- monitoreo de rendimiento

#### Plataformas IoT:

proveen herramientas para la gestion centralizada de dispositivos

#### Problemas:

- **Configracion y monitoreo:**

- **Actualizacion de Firmware**

#### Protocolos de gestion de dispositivos:

- **LwM2M:** Facilita la dministracion remota del firmware de los dispositivos, asi como su configuracion, monitoreo y administracion


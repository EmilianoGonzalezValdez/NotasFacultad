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
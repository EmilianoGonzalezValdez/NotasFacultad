*Requisitos funcionales:* 
- Provisión de servicios: los servicios deben ser capaces de proporcionar funcionalidades especificas 
- Consumo de servicios: los clientes deben poder solicitar y recibir servicios

*Requisitos no funcionales:*
- Interoperabilidad: entre servicios. Es decir, comunicación entre servicios de manera efectiva independientemente de la plataforma o lenguaje de programación usado
- Reusabilidad: los servicios deben diseñarse para reutilizarse en diferentes contextos
- Escalabilidad: los servicios deben escalar según sea necesario
- Flexibilidad: los servicios deben ser capaces de adaptarse a cambios en las necesidades del negocio
- Seguridad: garantizar la seguridad de los datos y transacciones entre servicios

Para lograr todos estos requisitos la solución es organizar las aplicaciones en *servicios reutilizables* que se comunican entre sí a través de un bus de servicios.
Cada servicio realiza una función específica y puede ser usado por diferentes aplicaciones. En arquitectura SOA, los servicios se comunican entre si usando patrones como: solicitud-respuesta, publicar-suscribir, o enviar-olvidar. Los servicios son modulares y pueden actuar tanto como clientes como servidores dependiendo del contexto.

En este sentido podemos organizar la arquitectura en 2 componentes:
- **Nodos o  roles:**
	- *Servicios independientes:* cada servicio tiene un rol definido
	- *Bus de servicios empresarial:* infraestructura de software que facilita la integración y comunicación entre los servicios 
	- *Clientes:* consumen los servicios ofrecidos
- **Mensajes de comunicación:**
	- *Clientes a ESB:* solicitudes de servicios, datos a procesar
	- *ESB a servicios:* enrutamiento de solicitudes a los servicios adecuados
	- *Servicios a ESB:* respuestas a las solicitudes, datos procesados
	- *Servicios entre sí:* comunicación para coordinar acciones y compartir datos
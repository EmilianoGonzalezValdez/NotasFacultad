Los **requisitos Funcionales** de esta arquitectura son:
- *Provisión de servicios* especializados: proporcionar funciones únicas y bien definidas
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
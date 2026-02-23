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
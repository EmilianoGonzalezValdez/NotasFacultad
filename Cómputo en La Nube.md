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
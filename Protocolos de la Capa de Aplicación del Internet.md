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
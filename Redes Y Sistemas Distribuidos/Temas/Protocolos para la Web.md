
# Protocolos para la Web



## ***Necesidades para un Protocolo para la Web***

- Pedido de páginas, de objetos, o de ejecución de programas que generan páginas

- Manejo del estado de la sesión

- Poder mantener el sistema de archivos del servidor web

- Recepción de páginas por un browser

- Seguridad(encriptación de mensajes)

- Feedback adecuado cuando no se puede responder los pedidos

- Comunicación confiable



## ***HTTP***

El protocolo HTTP (hyper text transfer protocol) transfiere páginas de servidores web a navegadores y manda pedidos de navegadores a servidores web. Sus mensajes soportados son:

- HTTP-Request (de navegador a servidor)

- HTTP-Response (de servidor a navegador)



#### Conexiones HTTP 

- **HTTP no persistente:** Se manda como maximo un objeto por conexion TCP. Por lo cual descargar múltiples objetos requiere varias conexiones. Lo cual puede llegar a ser extremadamente ineficiente. Soportado por HTTP 1.0. Su tiempo de respuesta para recibir un archivo es de:

$2*RTT + \text{Tiempo de transmisión de archivo}$

- **HTTP persistente:** Multiples objetos pueden ser enviados a través de una única conexion TCP entre cliente y servidor. Los pedidos y resultados se mandan en orden. Soportado por HTTP 1.1



**RTT(definición):** Tiempo necesario para que un paquete pequeño viaje del cliente al servidor y de regreso



### ***HTTP2***

Por medio de un mecanismo de server push empuja archivos que sabe que se van a necesitar antes de que el cliente sepa de su necesidad. Las respuestas a los pedidos pueden volver en cualquier orden. HTTP 2.0 comprime los encabezados y los envía en binario para reducir su uso de ancho de banda. Cada respuesta lleva un identificador de su pedido



#### Informaciones que debería tener un mensaje de pedido:

- En caso que se quiera recibir una página el mensaje de pedido debería tener: el **URL** de un documento y la **especificación de programa que genera página web**

- El **tipo de acción** que se quiere hacer en e sistema de archivos del servidor web. Se escribe en la primera palabra de la primera linea 

- Mandar **información sobre la maquina/software del cliente** para que servidor web pueda retornar páginas adecuadas al cliente

- Mandar **información de estado de sesión** para que el servidor se entere

- **Restricciones sobre el tipo de páginas** que el cliente puede aceptar



### Métodos de pedido HTTP

**Metodo Post:** La pagina web a menudo contiene input de formulario. El inut es subido al servidor en un campo llamado **cuerpo de la entidad**

**Método Get:** El input es subido en el campo URL de la línea del pedido

**Método PUT:** Sube un archivo en el campo **cuerpo de la entidad** en el camino especificado por el campo URL

**Método DELETE:** Borra el archivo especificado en el campo URL

**Metodo HEAD:** Simplemente solicita el encabezado de la respuesta del servidor web, sin la pagina o datos de la respuesta, o sea, feedback sobre el resultado del pedido, tipo de contenido, etc

**Método OPTIONS:** Permite que el cliente consulte al servidor por una página y obtenga los métodos y encabezados http que pueden ser usados con esa página


![alt text](image(2).png)



#### Informaciones que debería tener un mensaje de respuesta:

- Feedback adecuado sobre el pedido realizado. Para ello se usa un código y un mensaje a traves de una **Línea de estado** la cual contiene un codigo de 3 digitos que dice si la solictud fue atendida y si no, el porque

- Página o documento solicitado

- En ese caso información sobre el tipo de documento enviado. Para ello se indica el tipo de informacion de que se trata y luego la informacion en si. En esto se usan encabezados de respuesta que son pares, nombre de encabezado y su valor

- Información de estado de sesión para mantener actualizado al cliente

#### Partes de una respuesta HTTP:

- **Linea de estado**

- **Encabezados de respuesta**(opcional)

- Luego vienen el cuerpo de la respuesta



#### Encabezados HTTP

Los mensajes HTTP suelen tener **encabezados**, estos pueden ser de pedido, de respuesta o de ambos tipos. Se usan para **preever información** a ser procesada por el receptor del mensaje(info de la maquina del cliente, la maquina del servidor, sobre la pagina retornada, etc.). Ademas se usan para **fijar restricciones** que deben cumplir mensajes futuros, para proveer información sobre **eventos** importantes y tambien para proveer datos de**l** **estado de la sesión**



## ***HTML***

HTML (Lenguaje de marcado de hipertexto) es el lenguaje estándar para crear páginas web. Describe la estructura de una pagina web y indica al navegador como mostrar el contenido de la página. Su **sintaxis** es muy parecida a la de **XML**

Un documento HTML es una serie de **elementos**, donde **elementos** es el nombre que le damos a cierto contenido encerrado entre etiquetas. Una etiqueta tiene un nombre, esta enmarcada entre < >, pueden tener o no **atributos.** Un atributo puede tener nombre y un valor separados por =



#### Pasos para generar una página dinamica

1. Un usuario llena un formulario y hace click en el botón de envio

2. Se envia un ensaje al servidor web con el contenido del formulario

3. El programa solicita información a un servidor de bases de datos

4. El servidor de bases de datos responde con la información requerida

5. El programa genera una página HTML personalizada y la envía al cliente

6. El browser muestra la página recibida al usuario



**Paginas dinamicas:** Son páginas web generadas por programas que se ejecutan en el servidor

**Tareas que suelen hacer las páginas dinamicas:**

- Procesar parámetros de formularios

- Procesar encabezados de pedido HTTP

- Pedir datos a fuentes de datos

- Generar página web con los datos recibidos

- Generar encabezados de respeusta HTTP



## ***PHP***



PHP (procesador de hipertexto) se utiliza para definir páginas dinamicas mediante la inserción de comandos especiales dentro de páginas HTML



**Algunas cosas que puede hacer PHP:**

- Puede generar contenido de página dinámica

- Puede operar con archivos en el servidor

- Puede recolectar datos de formulario

- Puede enviar y recibir cookies

- Puede acceder a encabezados de pedido HTTP

- Permite definir encabezados de pedido HTTP

- Permite acceder a base de datos

- Es gratis


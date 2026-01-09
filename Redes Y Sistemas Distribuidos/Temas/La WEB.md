
# La WEB



Para las paginas web suelen ser importantes los datos y la informacion. Los datos refieren a los datos de las entidades y relaciones del mundo, los cuales suelen estar en una base de datos.

Estos datos se procesan de determinada manera y obtiene informacion. Las paginas web muchas veces contienen informacion. Esa informacion puede obtenerse de distintas fuentes de datos, estos son extraidos y organizados de determinada forma dando lugar a la informacion. Esta informacion puede ser alguna estadística sobre los datos y no necesariamente tiene que ser texto

Los datos pueden ser consultados. Una consulta suele describir, usando un lenguaje de consulta , los datos deseados. Estos lenguajes de consulta sirven para expresar dichas consultas. Estas son procesadas por motores de bases de datos para retornas los datos deseados

Para ver los datos deseados tambien podemos **navegar** entre una serie de pantallas que contienen los datos que deseamos o informacion. Llamamos **hypertexto**  a un conjunto de textos los cuales contienen enlaces a otros textos. Nos referimos con **medias** a cosas como fotos,videos,audios,graficos,etc. Podemos generalizar hipertexto a hipermedia donde cada nodo puede tener texto, medias y enlaces a otros nodos

#### Paginas web:

cada pagina web puede contener vinculos a otras paginas web ubicadas en cualquier lugar del mundo. Una pagina web suele contener texto y referencias a varios objetos

 **Las paginas web estaticas** son documentos en algun formato. Lo malo es que trabajar con estas paginas se vuelve muy ineficiente cuando la informacion cambia frecuentemente o cuando la informacion de la pagina varia de acuerdo a parametros. Claramente queremos evitar el modificar a mano las paginas estaticas a cada rato.

Por ello usamos las denominadas **Paginas dinámicas**, las cuales son generadas ppor medio de programas, que toman parametros de entrada, que se ejecutan del lado del servidor. Sus parametros suelen ser ingresados como valores de campos de formularios HTML

Cuando la pagina nueva a generarse dinámicamente en el servidor ya tiene una parte importante en común con la pagina del browser, este proceso de crear paginas dinámicas se vuelve ineficiente. Ya que el browser deberá volver a interpretar la parte en común de la nueva pagina

**Pedidos sincrónicos:** Al hacer un pedido HTTP al servidor web, el cliente se queda bloqueado esperando a recibir la pagina. Si el procesamiento de un pedido tarda mucho, esto se vuelve un problema para el usuario

**Solución:** Usar una **Página Única.** ¿De que se trata esto?.

Bueno pues cuando se entra en la aplicación web el servidor manda una **página única** que contiene una interfaz con el usuario completa. Desde esta página única se pueden hacer pedidos de datos al servidor web, el cual solo obtiene los datos, no computa páginas. Luego de hacer un pedido la aplicación puede seguir ahciendo otras tareas mientras se procesa el pedido. A esto se le llama **pedido asincronico**. Cuando llegan los datos se actualiza la interfaz del usuario de la pagina del browser

Para referencias paginas web usamos [[URLs]]



#### Sitio web:

Un sitio web es un conjunto de páginas web relacionadas localizadas bajo un único nombre de dominio y publicadas por al menos un servidor web, tipicamente producida por una organización o persona. Estos se encargan de entregar contenido, normalmente, mediante paginas estaticas. Utilizan una **pagina de inicio**, siendo esta una pagina de entrada al sitio web que sirve como guia hacia las demas paginas del sitio



#### Web 2.0

Son sitios y [[Aplicaciones Web]] que hacen uso de contenido generado por usuarios finales. Se caracteriza por una mayor interacción del usuario, una mayor colaboración de los usuarios y canales de comunicación mejorados

#### Web 3.0

Esta web es caracterizada por:

- **Descentralización:** Los usuarios están en control de sus datos, siendo dueños del valor que generan. 

- **Blockchain:** Permite transacciones más seguras, privacidad de datos y propiedad

- **Web semantica:** Los datos tienen significado y son legibles por computadoras. Los objetos se identifican con URLs pudiendo estar anidadas, y existen **metadatos semánticos**, los cuales son etiquetas semánticas agregadas a las paginas web para describir su signifiaco mejor

- **Uso de inteligencia artificial:** Procesamiento de lenguaje natural y aprendizaje automático



#### Browser:

Para ver las paginas web se usa un **Navegador(Browser)**

EL **Navegador** permite pedir una pagina/objetos a un servidor web, mediante protocolo HTTP. Una página pedida puede ser estatica o dinamica o página única. El servidor web retorna la pagina en respuesta al pedido del navegador. SI el servidor retornó una pagina, el navegador interpreta el texto y los comandos de formateo que contiene la página y despliega la página adecuadamete formateada en pantalla

Para que los navegadores entiendan las páginas web, estas se escriben en un lenguaje llamado HTML



#### Resumen de comunicación entre browser y servidor web

#### Orden seguido:

1. EL cliente inicia una conexion TCP(crea socket) con el servidor web, usando el puerto 80

2. El servidor web acepta la conexion TCP del cliente

3. Mensajes HTTP(mensajes de protocolo de capa de aplicación) intercambiados entre el browser(cliente HTTP) y el servidor web

4. La conexion TCP se cierra

#### Con HTTP:

El servidor web no mantiene la información acerca de pedidos del pasado del cliente. Los protocolos que mantienen el **estado** son complejos ya que si el cliente/servidor se cae, sus visiones del "estado" pueden ser inconsistentes y deben ser reconciliadas 



#### Problema:

**No todas las páginas contienen solamente HTML:**

¿Como sabe el navegador de que tipo de página se trata?

**Solución:** Cuando un servidor regresa una pagina tambien regresa el tipo MIME de la página. Si el tipo MIME de la pagina no es de los integrados el navegador consulta una tabla de tipos MIME que asocia a cada tipo MIME con un visor. Ademas las páginas de tipo text/html se despliegan de manera directa




Para las paginas web suelen ser importantes los datos y la información. En el mundo hay entidades y relaciones entre entidades. Los datos se refieren a los datos de esas entidades y relaciones. Dichos datos suelen estar en bases de datos siendo estas una de las fuentes de datos que usan las páginas web.

Los datos se procesan de determinada manera y se obtiene lo que se llama información. Esta información es la que tienen las paginas web pudiendo ser organizadas de distinta forma en base a los datos extraidos, no necesariamente en formato de texto, pueden ser diagramas, imagenes, figuras, tablas. Aun asi una página web puede ser solo de datos o solo de información

Se pueden utilizar lenguajes de consulta para expresar consultas sobre datos con el posible fin de generar información. Las consutas son procesadas por motores de bases de datos apra retornar los datos deseados. 

Para ver los datos deseados otra alternativa a escribir consultas en lenguaje de consultas es **navegar**. Al navegar uno va viajando por una serie de pantallas que contienen los datos que desea inspeccionar. Llamamos hipertexto a un conjunto de textos donde cada uno de los cuales contiene enlaces a otros textos. Al seleccionar un enlace se muestra el texto deseado enlazado. Por ende recorrer varios hipertextos es navegar.
Además nos vamos a referir con medias a cosas como fotos, videos, audios, gráficos. Con esta idea podemos generalizar el hipertexto a **hipermedia** donde tenemos un conjunto de nodos donde cada nodo puede tener texto y medias Y enlaces a otros nodos

Con estos conceptos ya podemos decir que una Página Web puede contener vinculos a otras páginas web ubicadas en cualquier lugar del mundo y que si bien una página suele contener texto, tambien puede referencias varios objetos

Las **páginas web estaticas** son simplemente documentos en algún tipo de formato usando HTML5.
Como la información cambia frecuentemente estas pueden ser muy ineficientes, ya que deberiamos modificarlas a mano. Para solucionar esto surgen las **Páginas dinamicas** donde las páginas HTML son generadas por medio de programas que se ejecutan del lado del servidor que toman parámetros de entrada que suelen ser ingresados como valores de formularios.

Que el servidor tenga que construir páginas dinamicas puede ser ineficiente támbien por varios motivos:
1. La página nueva que genero el servidor puede tener mucho en comun con la que ya se encontraba en el browser, repitiendo una parte a ser enviada por la red
2. El cliente se queda bloqueado esperando luego de hacer un pedido HTTP al servidor web y recién puede continuar ejecutandose cuando recibe una página. Estos llamados **pedidos sincronicos** pueden ser conflictivos si el procesamiento de un pedido del lado del servidor toma mucho tiempo ya que el no poder usar la aplicación web mientras tanto para otra cosa puede ser bastante desagradable

La solución a estos problemas es usar una **página única**. Cuando se entra en la aplicación web el servidor web manda una página única al browser que contiene una interfaz con el ususario completa con apariencia similar a las interfaces de usuario de aplicaciones de escritorio. Desde esta página única se pueden hacer los pedidos de datos al servidor web, donde este ultimo solo se encarga de obtener los datos, no de computar las páginas de forma tal que luego de hacer el pedido de datos la aplicación puede seguir haciendo otras tareas mientras se procesa el pedido. A esto se lo llama **pedido asincronico**. Luego cuando llegan los datos se actualiza la interfaz del usuario
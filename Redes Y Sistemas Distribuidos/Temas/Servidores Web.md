
# Servidores Web



## ¿Que es?

A un servidor web se lo puede ver como una computadora que almacena **software del wervidor web y archivos** como documentos HTML, imágenes, archivos JavaScript, etc. A un servidor web se le proporcionará el nombre de un archivo correspondiente a una página a buscar y regresar. Tambíen se le puede proporcionar el nombre de un programa con parámetros a ejecutar

El **problema** con este diseño de servidor web es que cada solicitud de pagina estática requiere un acceso al disco para obtener el archivo, lo cual es muy ineficiente para n paginas estáticas. La **solución** para esto es usar un **caché** de paginas estáticas en la memoria por lo cual esto agilizaría el proceso de buscar numerosas veces una página estática. 

Otro **problema** es que hasta ahora un servidor web es un proceso con un solo hilo de ejecución. La **solución** es implementar una arquitectura con un **módulo front end** y k **módulos de procesamiento-MP-**(hilos) donde todos los MP tienen acceso al caché y a uno o mas discos

#### Pasos de un servidor web con múltiples hilos para manejar pedidos de páginas estáticas:

1. Cuando llega una solicitud el front end la acepta y construye un registro que la describe

2. Despúes entrega el registro a uno de los MP

3. Si se trata de pedido de página estática el MP primero verifica el caché para ver si es archivo esta allí

4. Si el archivo está en caché, actualiza el registro para incluir un apuntador al archivo

5. Si el archivo no está en el caché, el MP inicia una operación de disco(cuando el archivo llega a disco se coloca en el caché y se regresa al cliente)

6. Mientras uno o más MP están bloqueados esperando a que termine una operación de disco, otros MP pueden estar trabajando en otras solicitudes

7. Conviene tener además múltiples discos, para que más de un disco pueda estar ocupado al mismo tiempo



Las **Arquitecturas actuales** muestran una división entre **front end** y **back end**. Al **front end server** se lo llama **proxy reverso**, porque retorna contenido de otros **servidores back-end** y sirve estos objetos al cliente. Hay soluciones que ponen en caché también páginas creadas dinámicamente



Tiene 2 elementos principales, los componentes y conectores. Esta vista describe que componentes existen y como interactúan entre ellos en tiempo de ejecución. Prácticamente es un grafo donde los componentes son nodos y los conectores aristas 

**Componentes:** Son unidades de computo y almacenamiento de datos, cada una tiene nombre y tipo
**Conectores:** Describen el medio en el cual la interacción entre componentes toma lugar, estos también tienen nombre y tipo, muchas veces, representando protocolos 

Distintos sistemas tienen distintas estructuras de **CYC**, algunas de estas siendo generales y útiles para una clase de problema en especifico, estos son llamados estilos arquitectónicos. Es decir, un *Estilo Arquitectónico* define una familia de arquitecturas que satisfacen restricciones de ese estilo en especifico. Para **CYC** existen:
- **Tubos y Filtros:** Adecuado para sistemas que fundamentalmente realizan *transformaciones de datos*, ya que se compone de una red de transformadores para realizar el resultado deseado. Esta compuesto por un solo tipo de componente: El Filtro, y un tipo de conector: El Tubo de forma que el filtro realiza transformaciones y se la pasa a los demás filtros por un tubo 
	- ***Restricciones:***
		- Un filtro es una entidad independiente y asíncrona
		- Un filtro no necesita saber la identidad de los filtros que envían o reciben datos
		- Un tubo es un canal unidireccional que transporta flujo de un filtro a otro
		- Un tubo solo conecta 2 Filtros
		- Los filtros deben hacer Buffering y sincronización para asegurar el correcto funcionamiento como productor y consumidor
		- Un sistema puro de filtros y tubos requiere usualmente que cada filtro tenga su propio hilo de control
- **Estilo de datos compartidos:** Hay 2 tipos de componentes, el repositorio de datos y el usuario de datos. El primero provee almacenamiento permanente confiable, mientras que los segundos acceden a los datos almacenados en este, realizan cálculos y luego guardan esos resultados en el repositorio. De esta forma solo hay 1 conector de escritura/lectura. Tiene 2 variantes
	- ***Estilo Pizarra***: Donde al haber un cambio el repositorio avisa a los usuarios
	- ***Estilo Repositorio***: Donde el repositorio es pasivo 
- **Estilo Cliente Servidor:** Estilo normalmente multinivel donde hay 2 tipos de componentes, los clientes y los servidores, los primeros solo se comunican con el servidor de forma asíncrona; siendo estos también quienes deben iniciar la comunicación. El único tipo de conector que hay es request/reply 
- **Estilo Publicar-Suscribir:** Hay 2 componentes, los publicadores y los suscriptores, de modo que cada vez que se publica algo, se invoca a las componentes suscriptas
- **Estilo Peer To Peer:** Un único componente donde cada uno puede pedirle servicios a otro
- **Estilo de Procesos Que Se Comunican:** Procesos que se comunican entre si
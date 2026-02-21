*Grafo de la interred:*
- Los nodos son enrutadores multiprotocolo; un lado entre dos enrutadores multiprotocolo significa que esos enrutadores están conectados vía una subred.
Una vez construido el grafo de la interred, pueden aplicarse algoritmos de enrutamiento al grupo de enrutadores multiprotocolo.


**Organización del enrutamiento en 2 niveles:**
- En cada red se utiliza un *protocolo de puerta de enlace interior (IGP)*
- Entre las redes se usa un *protocolo de puerta de enlace exterior (EGP)*
La red puede usar diferentes protocolos IGP, pero debe usarse el mismo protocolo EGP.

En internet el EGP se llama BGP (Border Gateway Protocol). Porque cada red es operada independientemente de las otras se le llama *Sistema autonomo* donde un provedor de internet puede tener uno o más SA.
La internet con BGP busca caminos formados por la lista de nombres de sistemas autonómos y destino que es prefijo.
Por eso la internet con BGP no trabaja con un grafo de la interred como los anteriores, ya que en ese grafo no se nombran SA , o prefijos y solo se nombran puertas de enlace.
Pero pensar en términos de grafos sirve para teorizar o formalizar y se puede acomodar la estructura de acuerdo a las necesidades
La forma de estructurar un área es considerando los tipos de redes soportadas por OSPF. Se puede decir que un área permite acceder a un conjunto de LANs, cada una de ellas dada por un prefijo



Una red de multi acceso se representa como un nodo para la red en sí. Los arcos desde ese nodo de la red a los enrutadores tienen peso 0

**Tipos de conexiones y redes que soporta OSPF:**
1. Las líneas punto a punto entre dos enrutadores
2. Redes de multiacceso con difusión
3. Redes de multiacceso con muchos enrutadores, cada uno de los cuales se puede comunicar directamente con los otros


Para reflejar la red de arriba por medio de un grafo dirigido:
- Los enrutadores se representan con nodos
- A cada arco se le asigna un costo o retardo
- Una conexión punto-punto entre dos enrutadores se representa por un par de arcos, uno en cada dirección. Sus pesos pueden ser diferentes

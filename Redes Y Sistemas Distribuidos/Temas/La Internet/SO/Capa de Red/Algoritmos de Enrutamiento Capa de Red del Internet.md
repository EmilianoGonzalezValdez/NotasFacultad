Queremos evitar los siguintes efectos indeseados:
- Algoritmos enrutadores que puedan quedar inactivos
- Los caminos pueden ser innecesariamente largos
- Se pueden sobrecargar algunas de las líneas de comunicación y los enrutadores asociados a ellas

  La causa de dichos problemas es que la capa de red elige mal las rutas para enviar paquetes.
  Para escoger bien las rutas para enviar los paquetes se deben usar *algoritmos de enrutamiento* eficientes. Estos algoritmos se ejecutan en los enrutadores de la subder, son responsables de llenar y actualizar las tablas de enrutamiento

Antes de ver los algoritmos de enrutamiento vamos a ver como representar una subred como un grafo:
- Vamos a tener el Grafo G = (N,E) donde N = conjunto de enrutadores y E = conjunto de enlaces. Los arcos tienen etiquetas para el costo de atravesarlos
- Los costos de los arcos podrian calcularse como función de varios parámetros como la distancia, ancho de banda, tráfico medio, costo de comunicación, longitud media de las colas, retardo medio y otros factores. Para calcular el costo de un camino (x1 , x2, x3 , ... , xn) simplemente debemos sumar los costos de los caminos intermedios, en este caso costo(x1,x2,..,xn) = costo(x1,x2) + costo(x2,x3) + ... + costo (xn-1,xn)

**Algoritmo de enrutamiento de caminos más cortos:**
Para elegir una ruta entre un par de enrutadores, encontrar en el grafo una de las *rutas mas cortas* entre ellos. Algoritmos de cálculo de la ruta mas corta entre dos nodos como el de *Dijkstra* (1959), donde:
- Dado ung rafo conexo con costos en los enlaces, y nodo n en el grafo, obtiene *árbol de caminos más cortos* desde n hacia todos los demás nodos
- El árbol de caminos más cortos se representa como un *mapeo* donde para cada nodo del grafo de la subred asigna a su padre (en el árbol de caminos más cortos)
- Repasar los detalles del algoritmo de Dijkstra visto en algoritmos 2

**Procedimiento para calcular tablas de reenvío en redes de datagramas usando algoritmo de Dijtstra:**
1. Construir grafo de la subred con costos
2. Ingresar grafo de la subred con costos en los enrutadores
3. En cada enrutador construir tabla de enrutamiento, para lo cual:
- 	Ejecutar algoritmo Dijkstra en el enrutador
- 	A partir del árbol de caminos más cortos con raíz en el enrutador obtenido generar la tabla de reenvío del enrutador
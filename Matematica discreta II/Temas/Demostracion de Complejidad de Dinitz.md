La complejidad del algoritmo de Dinitz, tanto en su versión original como en la occidental, es **𝑂(𝑛²𝑚)**.

La demostración de esta complejidad se basa en las siguientes observaciones:

1. **Número de redes auxiliares:** El nivel (o distancia) de 𝑡 en las redes auxiliares sucesivas siempre aumenta. Dado que la distancia entre dos vértices en un grafo con 𝑛 vértices puede variar entre 1 y 𝑛-1, solo puede haber **𝑂(𝑛)** redes auxiliares distintas que se construyan durante la ejecución del algoritmo.
    
2. **Complejidad de construcción de una red auxiliar:** Cada red auxiliar se construye utilizando una Búsqueda en Amplitud (BFS), que tiene una complejidad de **𝑂(𝑚)**.
    
3. **Complejidad de encontrar un flujo bloqueante en una red auxiliar:** Este es el componente más complejo, y su análisis difiere ligeramente entre la versión original de Dinitz y la occidental. En ambos casos, se busca demostrar que esta complejidad es **𝑂(𝑛𝑚)**.
    
    - **Versión Original de Dinitz:** En esta versión, se asume que la red auxiliar se construye de tal manera que no hay vértices sin un lado de salida (es decir, todos los caminos llegan a _t_ o a un sumidero). Esto permite que una Búsqueda en Profundidad (DFS) siempre llegue a _t_ sin necesidad de retroceder (backtracking) en un camino que no conduce al sumidero.
        
        - Cada camino aumentante se encuentra con DFS, lo cual toma **𝑂(𝑛)** tiempo (ya que no hay backtracking y la longitud del camino es a lo sumo _n_).
        - Cada camino que se encuentra y se utiliza satura al menos un lado en la red auxiliar.
        - Como hay _m_ lados en total, esto implica que se encuentran a lo sumo **𝑂(𝑚)** caminos aumentantes.
        - Por lo tanto, la complejidad de encontrar todos los caminos aumentantes y actualizar el flujo es **𝑂(𝑛𝑚)**.
        - Para mantener la propiedad de que no hay vértices sin lados de salida después de cada flujo aumentante, el algoritmo realiza una operación de "podado" (pruning). Esta operación consiste en recorrer los vértices desde los niveles más altos a los más bajos, eliminando aquellos que ya no tienen lados de salida.
        - El podado se realiza después de cada camino aumentante. Cada operación de podado implica recorrer 𝑂(𝑛) vértices y cada verificación de si un vértice tiene lados de salida es 𝑂(1). Por lo tanto, el costo de las operaciones de podado acumuladas a lo largo de todos los 𝑂(𝑚) caminos es **𝑂(𝑛𝑚)**.
        - Además, la eliminación física de los vértices y sus lados (que ocurre a lo sumo una vez por vértice) tiene una complejidad total de **𝑂(𝑚)** (debido a la propiedad del apretón de manos: la suma de los grados es el doble del número de lados).
        - Sumando las complejidades, la de encontrar un flujo bloqueante en la versión original es **𝑂(𝑛𝑚) + 𝑂(𝑛𝑚) + 𝑂(𝑚) = 𝑂(𝑛𝑚)**.
    - **Versión Occidental de Dinitz (Dinic-Even):** Esta versión también utiliza DFS para encontrar caminos aumentantes en la red auxiliar. El proceso se describe mediante una secuencia de operaciones: 'A' (avanzar), 'R' (retroceder) e 'I' (incrementar).
        
        - Las operaciones 'A' y 'R' tienen una complejidad de **𝑂(1)**.
        - Una operación 'I' (incrementar flujo a lo largo de un camino) implica recorrer el camino dos veces (una para incrementar y otra para borrar los lados saturados), lo que toma **𝑂(𝑛)** tiempo (siendo _n_ la longitud máxima de un camino).
        - La cantidad de operaciones 'A' en una "corrida" (secuencia de operaciones para encontrar y usar un camino) es **𝑂(𝑛)**, ya que cada avance mueve el puntero de un nivel al siguiente.
        - Cada operación 'R' (retroceder) y cada operación 'I' (incrementar) eliminan al menos un lado del grafo auxiliar. Dado que hay _m_ lados en total, esto significa que hay a lo sumo **𝑂(𝑚)** "palabras" o ciclos de operaciones 'A...AX' (donde X es 'I' o 'R').
        - Cada una de estas "palabras" tiene una complejidad de **𝑂(𝑛)** (que incluye las operaciones 'A', 'R' y la potencial 'I' que es 𝑂(𝑛)).
        - Multiplicando la complejidad por palabra por el número total de palabras, la complejidad de encontrar un flujo bloqueante en la versión occidental es **𝑂(𝑛𝑚)**.

**Complejidad total:** Sumando los componentes:

Complejidad total = (Complejidad de hallar un flujo bloqueante + Complejidad de construir una red auxiliar) × Número de redes auxiliares Complejidad total = (𝑂(𝑛𝑚) + 𝑂(𝑚)) × 𝑂(𝑛) Complejidad total = 𝑂(𝑛²𝑚) + 𝑂(𝑛𝑚) Complejidad total = **𝑂(𝑛²𝑚)**
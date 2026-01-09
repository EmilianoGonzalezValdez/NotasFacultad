
### Complejidad del algoritmo de Edmonds-Karp

El algoritmo de Edmonds-Karp siempre termina y opera con una complejidad de **O(nm²)**.

### Prueba de la complejidad

La prueba de la complejidad de Edmonds-Karp se basa en dos aspectos clave: el costo de encontrar un camino aumentante y el número máximo de veces que se pueden encontrar dichos caminos.

1. **Costo de cada iteración:** Edmonds-Karp selecciona el camino aumentante con la menor longitud utilizando un algoritmo de búsqueda en anchura (BFS). La complejidad de BFS es O(m), donde 'm' es el número de lados en la red.
    
2. **Número de caminos aumentantes (Z):** Para demostrar la complejidad de O(nm²), es necesario establecer que el número de caminos aumentantes que encuentra el algoritmo es O(nm). Esto se logra demostrando que la "distancia" de un vértice desde la fuente 's' en la red residual, relativa al flujo actual, nunca decrece con cada iteración del algoritmo. Más precisamente, si $d_k(x)$ es la distancia del vértice $x$ desde $s$ en la red residual después de $k$ iteraciones, entonces $d_k(x) \le d_{k+1}(x)$ para todo $x \in V$. Esta propiedad, que no requiere ser probada aquí, es crucial.
    
    Consideremos un lado $\vec{xy}$ que se vuelve "crítico" en el paso $k$ del algoritmo. Un lado se vuelve crítico si se utiliza para actualizar el flujo y se satura (si se usa en dirección hacia adelante) o se vacía (si se usa en dirección hacia atrás).
    
    - **Caso 1: $\vec{xy}$ se satura (se usa hacia adelante).** Esto significa que el flujo en $\vec{xy}$ alcanza su capacidad, $f_k(\vec{xy}) = c(\vec{xy})$. Para que $\vec{xy}$ vuelva a ser crítico en un paso posterior $j > k$, debe ser vaciado, es decir, utilizado en dirección hacia atrás en algún paso $i$ donde $k < i \le j$. Cuando $\vec{yx}$ se usa en dirección hacia atrás, significa que $d_i(x) = d_i(y) + 1$ (porque Edmonds-Karp usa caminos de longitud mínima). Debido a la propiedad de que las distancias no disminuyen, $d_i(y) \ge d_k(y)$, y sabemos que $d_k(y) = d_k(x) + 1$ (ya que $\vec{xy}$ fue usado hacia adelante en un camino de longitud mínima en el paso $k$). Combinando esto, se obtiene que la distancia de $s$ a $t$ ($d_j(t)$) en el paso $j$ será al menos $d_k(t) + 2$.
        
    - **Caso 2: $\vec{xy}$ se vacía (se usa hacia atrás).** Esto significa que el flujo en $\vec{yx}$ se reduce a cero, $f_k(\vec{yx}) = 0$. Para que $\vec{xy}$ vuelva a ser crítico, debe saturarse, es decir, utilizarse en dirección hacia adelante en algún paso posterior $i$. Similar al caso anterior, esto implicará que la distancia de $s$ a $t$ aumenta al menos en 2.
        
    
    En ambos escenarios, cada vez que un lado se vuelve crítico y luego vuelve a ser crítico en la dirección opuesta, la distancia mínima de $s$ a $t$ aumenta al menos en 2. Dado que la distancia entre $s$ y $t$ puede variar entre 1 y $n-1$ (donde 'n' es el número de vértices), un lado particular puede volverse crítico en la misma dirección como máximo O(n) veces.
    
    Como cada camino aumentante que se encuentra vuelve crítico al menos un lado, y hay 'm' lados en total, el número total de caminos aumentantes ($Z$) es $O(m \times n)$.
    

**Conclusión:** Multiplicando la complejidad de cada iteración por el número total de iteraciones, obtenemos la complejidad total de Edmonds-Karp: $O(m) \times O(nm) = O(nm^2)$.
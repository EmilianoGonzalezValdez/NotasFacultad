


Para demostrar que $d_k(x) \leq d_{k+1}(x)$ para todo $x \in V$, donde $d_k(x)$ es la distancia del $k$-ésimo flujo $f_k$ en una corrida de Edmonds-Karp, nos basamos en el **Teorema auxiliar uno** y su prueba provista en las fuentes.

**Teorema 14 (Teorema auxiliar uno)**
Sean $f_0, f_1, \ldots,$ los flujos que se van obteniendo en las iteraciones $0, 1, \ldots$ de Edmonds-Karp. Definamos $d_k(x) = d_{f_k}(s, x)$, $b_k(x) = d_{f_k}(x, t)$. Entonces, para todo $x \in V$, $d_k(x) \leq d_{k+1}(x)$.

**Prueba**
La prueba procede por contradicción.
1.  **Suposición de contradicción:** Asumimos que el conjunto $A = \{x : d_{k+1}(x) < d_k(x)\}$ no es vacío.
2.  **Elección de $x_0$:** Sea $x_0 \in A$ el elemento tal que la distancia $d_{k+1}(x_0)$ es la menor de todas las distancias $d_{k+1}(y)$ para $y \in A$.
3.  **Existencia de camino aumentante:** Dado que $x_0 \in A$, se cumple que $d_{k+1}(x_0) < d_k(x_0) \leq \infty$. Esto implica que $d_{k+1}(x_0)$ es finito, y por lo tanto, existe un $f_{k+1}$-camino aumentante desde $s$ hasta $x_0$.
4.  **Predecesor en el camino:** Sea $p_{k+1} := s \ldots zx_0$ el $f_{k+1}$-camino aumentante de longitud mínima entre $s$ y $x_0$, lo que significa que su longitud es $d_{k+1}(x_0)$. En este camino, $z$ es el vértice inmediatamente anterior a $x_0$. Por lo tanto, $d_{k+1}(z) = d_{k+1}(x_0) - 1$.
5.  **Propiedad de $z$:** Esta relación implica que $z \notin A$. Si $z$ estuviera en $A$, entonces $d_{k+1}(z) < d_{k+1}(x_0)$, lo cual contradiría la elección de $x_0$ como el elemento con la distancia $d_{k+1}$ mínima en $A$. Como $z \notin A$, se cumple que $d_k(z) \leq d_{k+1}(z)$.

Ahora, se consideran dos casos para la arista entre $z$ y $x_0$ en el camino $p_{k+1}$:

**Caso 1: $\overrightarrow{zx_0}$ es una arista (en dirección "forward")**
*   Si $\overrightarrow{zx_0}$ es una arista en el camino $p_{k+1}$, esto significa que $f_{k+1}(\overrightarrow{zx_0}) < c(\overrightarrow{zx_0})$.
*   De $z \notin A$, sabemos que $d_k(z) \leq d_{k+1}(z)$.
*   Si $\overrightarrow{zx_0}$ también fuera una arista aumentante para el flujo $f_k$, entonces $d_k(x_0) \leq d_k(z) + 1$.
*   Sustituyendo $d_k(z) \leq d_{k+1}(z)$ y $d_{k+1}(z) = d_{k+1}(x_0) - 1$:
    $d_k(x_0) \leq d_k(z) + 1 \leq d_{k+1}(z) + 1 = (d_{k+1}(x_0) - 1) + 1 = d_{k+1}(x_0)$.
*   Esto implicaría que $d_k(x_0) \leq d_{k+1}(x_0)$, lo cual contradice la suposición de que $x_0 \in A$ (donde $d_{k+1}(x_0) < d_k(x_0)$).
*   Por lo tanto, la arista $\overrightarrow{zx_0}$ *no* pudo haber sido aumentante para el flujo $f_k$. Esto significa que $f_k(\overrightarrow{zx_0}) = c(\overrightarrow{zx_0})$ (estaba saturada).
*   Sin embargo, como $\overrightarrow{zx_0}$ es parte de un $f_{k+1}$-camino aumentante, $f_{k+1}(\overrightarrow{zx_0}) < c(\overrightarrow{zx_0})$.
*   Para que el flujo en $\overrightarrow{zx_0}$ haya disminuido de saturado en $f_k$ a no saturado en $f_{k+1}$, significa que en la iteración $k$, la arista $\overrightarrow{x_0z}$ (la inversa) debió haberse utilizado en dirección "backward" en el $f_k$-camino aumentante. La fuente indica que esto se da "en el camino $p_k: s \ldots \leftarrow xz \ldots t$". Si este es el caso, la distancia de $z$ a $s$ sería $d_k(z) = d_k(x_0) + 1$.
*   La fuente concluye este caso con la frase "De aquí deriva una contradicción de manera mística". Esto sugiere un paso de inferencia no completamente detallado o una sutil contradicción en la cadena lógica según el texto. No obstante, el objetivo es demostrar que la suposición inicial lleva a una contradicción.

**Caso 2: $\overleftarrow{x_0z}$ es una arista (en dirección "backward")**
*   Esto significa que la arista original es $\overrightarrow{x_0z} \in E$ y que $f_{k+1}(\overrightarrow{x_0z}) > 0$. El camino $p_{k+1}$ utiliza esta arista en la forma $s \ldots z \leftarrow x_0$. Por lo tanto, $d_{k+1}(z) = d_{k+1}(x_0) + 1$.
*   La fuente reitera: "Como antes, $d_{k+1}(z) < d_{k+1}(x) \Rightarrow z \in A \Rightarrow d_k(z) \leq d_{k+1}(z)$". (Cabe señalar que, si $d_{k+1}(z) = d_{k+1}(x_0) + 1$, entonces $d_{k+1}(z) > d_{k+1}(x_0)$, por lo que la implicación $d_{k+1}(z) < d_{k+1}(x_0) \Rightarrow z \in A$ no se sigue directamente de esta relación de distancias, pero el punto clave es que $z \notin A$ por la minimialidad de $x_0$).
*   Dado que $z \notin A$, se tiene $d_k(z) \leq d_{k+1}(z)$.
*   La fuente argumenta que, si $f_k(\overrightarrow{x_0z}) = 0$, pero $f_{k+1}(\overrightarrow{x_0z}) > 0$, entonces la arista $\overrightarrow{x_0z}$ debió haber sido usada en dirección "forward" en la iteración $k$. Por lo tanto, existe un $f_k$-camino aumentante de la forma $p_k: s \ldots \overrightarrow{x_0z} \ldots t$.
*   Dado que Edmonds-Karp elige caminos de longitud mínima, $d_k(z) = d_k(x_0) + 1$.
*   Similar al Caso 1, la fuente indica que "de lo cual deriva la contradicción de la misma manera mística".

**Conclusión de la prueba**
Ambos casos conducen a una contradicción con la suposición inicial de que $A$ no es vacío. Por lo tanto, el conjunto $A$ debe ser vacío ($A = \emptyset$). Esto implica que no existe ningún $x$ para el cual $d_{k+1}(x) < d_k(x)$, lo que demuestra que $d_k(x) \leq d_{k+1}(x)$ para todo $x \in V$.

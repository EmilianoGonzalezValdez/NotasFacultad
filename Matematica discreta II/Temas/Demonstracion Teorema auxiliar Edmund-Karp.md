La fuente proporcionada aborda directamente el teorema que usted menciona en el Teorema 14, titulado "Teorema auxiliar uno". Este teorema establece que, para los flujos $f_0, f_1, \dots$ obtenidos en las iteraciones del algoritmo de Edmonds-Karp, si se definen $d_k(x) = d_{f_k}(s, x)$ y $b_k(x) = d_{f_k}(x, t)$, entonces para todo $x \in V$:

1. $d_k(x) \le d_{k+1}(x)$
2. $b_k(x) \le b_{k+1}(x)$

Esto significa que la longitud de los $f$-caminos aumentantes nunca decrece con cada iteración de Edmonds-Karp.

Sin embargo, la fuente indica que la demostración completa para $b_k(x) \le b_{k+1}(x)$ no se proporciona explícitamente, sino que se deja como ejercicio, señalando que es análoga a la prueba para $d_k(x) \le d_{k+1}(x)$.

A continuación, se presenta la demostración para $d_k(x) \le d_{k+1}(x)$ tal como aparece en la fuente, la cual es relevante para entender la lógica subyacente para $b_k(x) \le b_{k+1}(x)$:

**Demostración de $d_k(x) \le d_{k+1}(x)$:** La prueba se realiza por contradicción.

1. **Asunción por contradicción:** Se asume que el conjunto $A = {x : d_{k+1}(x) < d_k(x)}$ no es vacío ($A \ne \emptyset$).
    
2. **Elección de $x_0$:** Se elige un elemento $x_0 \in A$ tal que su distancia $d_{k+1}(x_0)$ es la menor de todas las distancias $d_{k+1}(y)$ para $y \in A$. Dado que $x_0 \in A$, se cumple que $d_{k+1}(x_0) < d_k(x_0) \le \infty$, lo que implica que $d_{k+1}(x_0) < \infty$. Por lo tanto, existe un $f_{k+1}$-camino aumentante entre $s$ y $x_0$.
    
3. **Análisis del camino:** Sea $p_{k+1} := s \dots zx_0$ el $f_{k+1}$-camino aumentante de longitud mínima entre $s$ y $x_0$, donde $z$ es el vértice inmediatamente anterior a $x_0$. Como este camino es de longitud mínima, la distancia a $z$ es $d_{k+1}(z) = d_{k+1}(x_0) - 1$. Esto implica que $z \notin A$ (ya que si $z \in A$, $d_{k+1}(z)$ sería menor que $d_{k+1}(x_0)$, contradiciendo la elección de $x_0$).
    
4. **Casos para el lado $zx_0$:** Se analizan dos casos posibles para el lado que conecta $z$ y $x_0$ en el $f_{k+1}$-camino aumentante:
    
    - **Caso 1: $z \to x_0$ es un lado directo ($\overrightarrow{zx_0} \in E$)**: En este caso, $d_{k+1}(z) < d_{k+1}(x_0)$. Dado que $z \notin A$, se tiene $d_k(z) \le d_{k+1}(z)$. Combinando esto, se obtiene $d_k(z) \le d_{k+1}(z) < d_{k+1}(x_0) < \infty$. Como $d_k(z) < \infty$, existe un $f_k$-camino aumentante entre $s$ y $z$, denotado $p_k$. Si el lado $\overrightarrow{zx_0}$ pudiera agregarse al final de $p_k$ para formar un $f_k$-camino aumentante entre $s$ y $x_0$, se tendría $d_k(x_0) \le d_k(z) + 1$. Sustituyendo, $d_k(x_0) \le d_{k+1}(z) + 1 = (d_{k+1}(x_0) - 1) + 1 = d_{k+1}(x_0)$. Pero esto implicaría $x_0 \notin A$, lo cual es una contradicción con la suposición inicial de que $x_0 \in A$. Por lo tanto, no se puede agregar $x_0$ al final de $p_k$. Esto significa que el lado $\overrightarrow{zx_0}$ debe estar saturado en el paso $k$, es decir, $f_k(\overrightarrow{zx_0}) = c(\overrightarrow{zx_0})$. Sin embargo, $p_{k+1}$ es un camino aumentante, lo que implica que $f_{k+1}(\overrightarrow{zx_0}) < c(\overrightarrow{zx_0})$ en el paso $k+1$. Esto solo es posible si, para pasar de $f_k$ a $f_{k+1}$, se utilizó el lado $x_0 \to z$ de forma inversa ($\overleftarrow{x_0z}$) en el camino aumentante $p_k'$ (es decir, $s \dots \overleftarrow{x_0z} \dots t$). Dado que Edmonds-Karp elige el camino de longitud mínima, se tendría $d_k(z) = d_k(x_0) + 1$. A partir de aquí, la fuente indica que se deriva una contradicción de manera "mística".
        
    - **Caso 2: $x_0 \to z$ es un lado inverso ($\overleftarrow{x_0z} \in E$)**: Esto significa que $p_{k+1}$ es de la forma $s \dots \overleftarrow{x_0z}$. De forma análoga, $d_{k+1}(z) < d_{k+1}(x_0)$, lo que implica $z \notin A$ (si $z$ estuviera en $A$, su distancia $d_{k+1}(z)$ sería menor que la de $x_0$, contradiciendo la minimidad de $x_0$). Así, $d_k(z) \le d_{k+1}(z)$. Existe un $f_k$-camino aumentante $p_k: s \dots z$. Si el lado $\overleftarrow{x_0z}$ no puede usarse para extender este camino (es decir, si $f_k(\overleftarrow{x_0z}) = 0$), pero $p_{k+1}$ es $f_{k+1}$-aumentante (implicando $f_{k+1}(\overleftarrow{x_0z}) > 0$), entonces $\overrightarrow{x_0z}$ debe haber sido usado en modo directo para pasar de $f_k$ a $f_{k+1}$. Por Edmonds-Karp, este camino $s \dots \overrightarrow{x_0z} \dots t$ sería de longitud mínima, por lo que $d_k(z) = d_k(x_0) + 1$. De nuevo, la fuente afirma que esto lleva a una contradicción "de la misma manera mística".
        
5. **Conclusión:** Dado que ambos casos llevan a una contradicción, la asunción inicial de que $A \ne \emptyset$ debe ser falsa. Por lo tanto, $A = \emptyset$, lo que implica que $d_k(x) \le d_{k+1}(x)$ para todo $x \in V$.
    

La fuente concluye la prueba para $d_k(x) \le d_{k+1}(x)$ y reitera que la demostración para $b_k(x) \le b_{k+1}(x)$ "queda como ejercicio", sugiriendo que la misma lógica y pasos se aplicarían de manera análoga al considerar los caminos desde $x$ hasta $t$.
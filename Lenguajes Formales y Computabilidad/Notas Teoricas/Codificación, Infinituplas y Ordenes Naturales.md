
---
### Codificación de Infinituplas y el Teorema Fundamental de la Aritmética

Para que los modelos de computabilidad puedan procesar secuencias de datos, necesitamos una forma de "empaquetar" una lista de números en un único natural. Usamos una versión "cheta" del _Teorema Fundamental de la Aritmética_ basada en la descomposición en primos.

- **El conjunto $\omega^{[N]}$**: Representa todas las infinituplas de números naturales donde solo una cantidad finita de sus coordenadas son distintas de cero.
- **La función de codificación $\langle \dots \rangle$**: Dada una infinitupla $(s_1, s_2, \dots) \in \omega^{[N]}$, le asignamos un único número natural $x$ mediante el producto de potencias de primos: $$x = \langle s_1, s_2, \dots \rangle = \prod_{i=1}^{\infty} pr(i)^{s_i}$$ donde $pr(i)$ es el $i$-ésimo número primo ($pr(1)=2, pr(2)=3, pr(3)=5, \dots$).

> [!success] Teorema de Biyección El Teorema 2 garantiza que esta forma de codificar es una **biyección** entre las infinituplas con soporte finito y los números naturales positivos ($N$). Esto significa que a cada lista le toca un número único y viceversa.

#### Procedimiento de Descodificación: Bajada $i$-ésima y Longitud

Para recuperar los datos guardados en un número $x$, usamos dos herramientas fundamentales que "desarman" el paquete:

- **Bajada $i$-ésima $(x)_i$**: Es el exponente que tiene el primo $pr(i)$ en la factorización de $x$. Para calcularlo en un ejercicio, buscamos la mayor potencia de ese primo que divide al número: $$(x)_i = \max { t \in \omega : pr(i)^t \text{ divide a } x }$$
- **Función Longitud ($Lt$)**: Nos dice cuántos elementos relevantes hay en la lista codificada (es decir, cuál es el índice del último primo con exponente no nulo). $$Lt(x) = \begin{cases} \max { i : (x)_i \neq 0 } & \text{si } x \neq 1 \ 0 & \text{si } x = 1 \end{cases}$$

> [!note] Reconstrucción Cualquier número natural $x$ se puede expresar unívocamente como $x = \prod_{i=1}^{Lt(x)} pr(i)^{(x)_i}$.

### Órdenes Naturales sobre $\Sigma^*$

Para que una máquina que solo entiende números pueda procesar palabras (y viceversa), establecemos biyecciones entre $\Sigma^*$ y $\omega$. Estas biyecciones dependen de un **orden total** $\le$ fijado sobre el alfabeto $\Sigma = {a_1, \dots, a_n}$.

- **La función $\#_\le$ (Palabra a Número)**: Dada una palabra $\alpha = a_{i_k} a_{i_{k-1}} \dots a_{i_0}$, su código numérico se calcula como una suma de potencias de $n$ (donde $n$ es el tamaño del alfabeto): $$\#_\le(\alpha) = i_k n^k + i_{k-1} n^{k-1} + \dots + i_0 n^0$$ donde $\#_\le(\epsilon) = 0$.
- __La función $*_\le$ (Número a Palabra)_*: Es la inversa exacta de $\#_\le$. Dado un número $j$, nos devuelve la palabra que ocupa la posición $(j+1)$ en la lista ordenada.

#### El Orden Lexicográfico

Es el criterio algorítmico para ordenar las palabras en la lista infinita. Para comparar dos palabras $\alpha$ y $\beta$, seguimos estas reglas:

1. **Comparar longitudes**: Si $|\alpha| \neq |\beta|$, la palabra más corta es menor.
2. **Comparar símbolos**: Si tienen la misma longitud, buscamos el primer símbolo (de izquierda a derecha) en el que difieren. La palabra que tenga el símbolo "menor" según el orden del alfabeto es la palabra menor.

> [!warning] Ojo con el diccionario Este orden **no es igual** al del diccionario común. En el diccionario, "b" es mayor que "aa", pero en nuestro orden lexicográfico "b" es **menor** que "aa" porque es más corta.

---

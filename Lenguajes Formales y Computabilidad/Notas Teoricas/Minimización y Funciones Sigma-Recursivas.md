
---
### El Operador de Minimización ($M(P)$)

La **minimizacion de variable numérica** es el constructor que formaliza la búsqueda ciega de un resultado. Si tenemos un predicado $P(t, \vec{x}, \vec{\alpha})$, la expresión $min_t P(t, \vec{x}, \vec{\alpha})$ denota al menor número natural $t$ tal que el predicado se hace verdadero ($P=1$).

Definimos la función de minimización como: $$M(P) = \lambda \vec{x} \vec{\alpha} [min_t P(t, \vec{x}, \vec{\alpha})]$$

- **Dominio de $M(P)$:** Está formado solo por las entradas $(\vec{x}, \vec{\alpha})$ para las cuales **existe al menos un** $t \in \omega$ tal que $P(t, \vec{x}, \vec{\alpha}) = 1$.
- **Parcialidad:** Si para una entrada no existe ningún $t$ que cumpla la condición, la función $M(P)$ queda **indefinida** para ese dato. Esto es lo que permite modelar algoritmos que "se cuelgan" o entran en bucles infinitos.

> [!tip] Regla U: Diseño de Predicados Para encontrar un predicado $P$ tal que $M(P) = f$, lo más fácil es diseñar $P$ de modo que para cada dato en el dominio de $f$, el valor $f(\vec{x}, \vec{\alpha})$ sea el **único** $t$ que cumple $P(t, \vec{x}, \vec{\alpha}) = 1$.

#### Uso Práctico: Raíz Cuadrada Exacta

Para definir $f(x) = \sqrt{x}$ (solo para cuadrados perfectos):

1. Usamos el predicado $P = \lambda tx [t^2 = x]$.
2. $M(P)$ buscará el primer $t$ cuyo cuadrado sea $x$.
3. Si $x=5$, como no hay ningún natural que al cuadrado de 5, la función se colgará, lo cual es correcto ya que 5 no está en el dominio de la raíz exacta.

### Definición de la Clase $R^\Sigma$

Las funciones **$\Sigma$-recursivas** ($R^\Sigma$) son la clausura inductiva de las funciones iniciales bajo composición, recursión primitiva y **minimizacion de predicados $\Sigma$-totales**.

- **Inclusión:** Como $R^\Sigma$ usa los mismos constructores que $PR^\Sigma$ y le suma uno nuevo, se cumple que $PR_\Sigma \subseteq R_\Sigma$.
- **Jerarquía:** Existen funciones que son $\Sigma$-recursivas pero **no** son primitivas recursivas, como la famosa _Función de Ackermann_.
- **Totalidad vs. Parcialidad:** Mientras que todas las funciones en $PR^\Sigma$ son totales (siempre terminan), las funciones en $R^\Sigma$ pueden ser parciales debido a la minimización.

> [!warning] La restricción de totalidad En la definición formal de $R^\Sigma$, el constructor $M(P)$ solo se permite si el predicado $P$ es **total**. Esto garantiza que la búsqueda sea "limpia": en cada paso $t$, sabemos con seguridad si la respuesta es 0 o 1, y no nos quedamos trabados esperando la respuesta del predicado.

### Robustez del Paradigma de Gödel

El modelo funcional es extremadamente sólido y no depende de elecciones arbitrarias:

1. **Leibniz vence a Gödel:** Toda función $\Sigma$-recursiva es $\Sigma$-efectivamente computable. Esto se prueba viendo que un humano puede simular la composición, la inducción y la búsqueda del mínimo paso a paso.
2. **Independencia del Alfabeto:** Si una función $f$ es mixta para dos alfabetos distintos ($\Sigma$ y $\Gamma$), ser recursiva en uno es equivalente a serlo en el otro. La computabilidad es una propiedad de la lógica de la función, no de los símbolos que usemos para escribirla.
3. **Conjuntos Σ-recursivos:** Un conjunto $S$ se dice $\Sigma$-recursivo si su función característica $\chi_S$ es una función $\Sigma$-recursiva.

> [!info] Operaciones Lógicas La clase de los predicados $\Sigma$-recursivos es cerrada bajo $\vee, \wedge, \neg$. Esto implica que si operamos conjuntos decidibles (recursivos), el resultado sigue siendo decidible.

---

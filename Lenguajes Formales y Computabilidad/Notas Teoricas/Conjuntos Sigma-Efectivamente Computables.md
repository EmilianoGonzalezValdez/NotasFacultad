
---

### La Decidibilidad y la Función Característica

Un conjunto $S \subseteq \omega^n \times \Sigma^{*m}$ se dice **$\Sigma$-efectivamente computable** (o decidible) si existe un procedimiento efectivo capaz de determinar, para cualquier entrada posible, si esta pertenece o no al conjunto.

La herramienta matemática para formalizar esto es la **función característica** $\chi_S$, definida como: $$\chi_S(x) = \begin{cases} 1 & \text{si } x \in S \ 0 & \text{si } x \notin S \end{cases}$$

Decimos que un conjunto $S$ es $\Sigma$-efectivamente computable si su función característica $\chi_S$ es $\Sigma$-efectivamente computable.

#### El Procedimiento para Decidir

Para que un procedimiento efectivo $P$ **decida** la pertenencia a $S$, debe cumplir condiciones más estrictas que las de un procedimiento que simplemente computa una función:

1. **Entrada:** Acepta cualquier $n$-upla de naturales y $m$-upla de palabras del alfabeto de entrada.
2. **Detención Obligatoria:** A diferencia de las funciones generales, el procedimiento **debe terminar siempre**, sin importar si el dato está en $S$ o no.
3. **Resultado Binario:** Si el dato pertenece a $S$, debe devolver $1$; si no pertenece, debe devolver $0$.

> [!info] El "Oráculo" del Sí o No Cuando un procedimiento cumple estas reglas, decimos que **decide** la pertenencia a $S$. Es como tener un juez que nunca se queda callado y siempre tiene una sentencia final.

#### Propiedades y Operaciones Lógicas

La decidibilidad se preserva bajo las operaciones lógicas usuales de la teoría de conjuntos:

- **Conjuntos Finitos:** Todo conjunto finito es automáticamente $\Sigma$-efectivamente computable. El procedimiento simplemente compara la entrada con cada elemento de la lista finita; si termina la lista y no hubo coincidencia, devuelve 0.
- **Complemento:** Si $S$ es decidible, su complemento $(\omega^n \times \Sigma^{*m}) - S$ también lo es (basta con intercambiar los resultados 1 y 0 del procedimiento).
- **Unión e Intersección:** Si $S_1$ y $S_2$ son decidibles, entonces $S_1 \cup S_2$ y $S_1 \cap S_2$ también lo son.
- **El conjunto vacío:** $\emptyset$ es siempre $\Sigma$-efectivamente computable para cualquier alfabeto. El procedimiento simplemente devuelve 0 para cualquier entrada.

> [!tip] Diferencia Crucial No confundas "computar el dominio de una función" con "decidir un conjunto". En la decidibilidad, **no existe la colgada legal**. Si el procedimiento se cuelga para un dato que no está en el conjunto, entonces el conjunto **no es decidible** mediante ese método.

> [!example] Ejemplos de Conjuntos Decidibles
> 
> - El conjunto de los números pares.
> - El conjunto de palabras que tienen longitud igual a un número $x$ determinado.
> - Cualquier producto cartesiano de conjuntos decidibles, como $\omega^3 \times \Sigma^{*2}$.

---

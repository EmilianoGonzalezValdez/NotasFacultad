
---

### La Convergencia de los Modelos

A lo largo del estudio de la computabilidad, vimos tres formalizaciones matemáticas distintas para capturar la noción intuitiva de _procedimiento efectivo_ (el paradigma de Leibniz). Aunque arrancan de bases totalmente diferentes, se demostró que todas tienen exactamente la misma potencia de cómputo:

1. **Paradigma de Turing:** Basado en una máquina mecánica con cinta y cabezal.
2. **Paradigma de Gödel:** Basado en funciones recursivas construidas por composición, recursión y minimización.
3. **Paradigma de Neumann:** Basado en un lenguaje de programación imperativo ($S_\Sigma$) con variables y comandos.

La relación entre estos modelos y la intuición se resume en la idea de que **Turing, Gödel y Neumann intentan vencer a Leibniz**, es decir, intentan dar una definición matemática precisa de lo que un humano puede calcular con lápiz y papel.

> [!success] Resultados de Robustez Se demostró formalmente que:
> 
> - Toda función _Turing-computable_ es efectivamente computable (Leibniz vence a Turing).
> - Toda función _recursiva_ ($\Sigma$-recursiva) es efectivamente computable (Leibniz vence a Gödel).
> - Toda función _computable en $S_\Sigma$_ es efectivamente computable (Leibniz vence a Neumann).
> - Los tres modelos son equivalentes entre sí: una función es recursiva si y solo si es Turing-computable, y si y solo si es computable en el lenguaje imperativo.

### La Tesis de Church-Turing

La **Tesis de Church-Turing** (o Tesis de Church) es un postulado fundamental que establece que el límite de lo que es "calculable" por cualquier medio físico o mecánico coincide exactamente con las funciones definidas en estos modelos.

A diferencia de los teoremas de equivalencia entre modelos, esta tesis **no es un teorema demostrable**, sino una afirmación sobre la naturaleza de la realidad: postula que no existe (ni existirá) ningún modelo de computación que pueda resolver algo que no sea resoluble por una Máquina de Turing o una función recursiva.

> [!info] Independencia del Alfabeto La computabilidad es una propiedad intrínseca de las funciones y no depende de los símbolos que usemos. El _Teorema de Independencia del Alfabeto_ asegura que si una función es recursiva respecto a un alfabeto $\Sigma$, también lo será respecto a cualquier otro alfabeto $\Gamma$ suficientemente grande.

#### Uso Práctico en la Materia

Gracias a esta equivalencia, cuando queremos probar que una función es computable, podemos elegir el camino más fácil:

- Si parece un algoritmo de pasos, usamos **Neumann** ($S_\Sigma$).
- Si parece una construcción matemática, usamos **Gödel** ($PR_\Sigma$ o $R_\Sigma$).
- Si involucra manipulación física de símbolos, usamos **Turing**.

Cualquier resultado obtenido en un paradigma se traslada automáticamente a los otros.

---

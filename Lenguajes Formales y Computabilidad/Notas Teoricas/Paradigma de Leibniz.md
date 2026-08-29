
---

# Paradigma de Leibniz (El Mundo Intuitivo)

Este tema, también llamado _Paradigma Filosófico_, representa la noción de computabilidad previa al formalismo matemático. En honor a Gottfried Leibniz, llamamos así al conjunto de conceptos intuitivos que Turing, Gödel y Neumann intentarán "vencer" (capturar matemáticamente).

### [[Procedimiento Efectivo|El Concepto de Procedimiento Efectivo]]

Es la base de todo. Se define como un método mecánico, preciso e inambiguo para realizar una tarea.

- **El Operador Humano:** Una persona con lápiz y papel (recursos ilimitados) que sigue instrucciones simples.
- **Repetibilidad:** Ante el mismo dato de entrada, la ejecución debe ser idéntica.
- **Resultado o Colgada:** El procedimiento termina con un dato o continúa para siempre.

### [[Funciones Sigma-Efectivamente Computables|Funciones Σ-efectivamente computables]]

Una función mixta es **$\Sigma$-efectivamente computable** si existe un procedimiento efectivo que la resuelva.

- **Criterio de Detención:** Si la entrada está en el dominio ($Df$), el procedimiento **debe** detenerse y dar el resultado. Si no está, **no debe** detenerse nunca.
- **Independencia del Alfabeto:** La noción de "computar" intuitivamente no depende de qué símbolos usemos en el papel.

### [[Conjuntos Sigma-Efectivamente Computables|Conjuntos Σ-efectivamente computables (Decidibilidad)]]

Un conjunto es **$\Sigma$-efectivamente computable** (o decidible) si su **función característica** ($\chi_S$) es $\Sigma$**-efectivamente computable**.

- **El Oráculo del "Sí o No":** Existe un procedimiento que, para cualquier entrada, **siempre termina** devolviendo 1 (si pertenece al conjunto) o 0 (si no pertenece).
- **Propiedad de los Finitos:** Todo conjunto finito es, por definición, efectivamente computable.

### [[Conjuntos Sigma-Efectivamente Enumerables|Conjuntos Σ-efectivamente enumerables]]

Un conjunto es **$\Sigma$-efectivamente enumerable** si puede ser "listado" por un procedimiento efectivo.

- **El Listador:** Existe un procedimiento que toma los naturales $0, 1, 2, \dots$ como entrada y va "escupiendo" todos los elementos del conjunto, posiblemente con repeticiones.
- **Relación con el Dominio:** El dominio de cualquier función efectivamente computable es siempre un conjunto efectivamente enumerable.

> [!success] Teorema de la Doble Enumerabilidad (Teorema 3) Un conjunto $S$ es decidible (computable) si y solo si tanto $S$ como su complemento ($S^c$) son efectivamente enumerables.

---


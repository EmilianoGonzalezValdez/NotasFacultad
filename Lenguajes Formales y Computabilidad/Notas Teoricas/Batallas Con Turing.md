
---

### Integración del Hardware al Mapa Teórico

Para que la teoría de la computabilidad sea realmente sólida, no alcanza con que el software (Neumann) y la matemática (Gödel) coincidan. El modelo de Turing, que representa la ejecución física en una máquina de cinta, también debe ser equivalente. Esto se cierra con dos teoremas fundamentales que completan el círculo de "batallas".

#### Teorema 12: Gödel vence a Turing

Este resultado establece que **toda función $\Sigma$-Turing computable es $\Sigma$-recursiva**.

- **La idea de la prueba:** Dado que el funcionamiento de una Máquina de Turing es mecánico y finito (estados, movimientos de cabezal, lectura/escritura), se pueden definir funciones recursivas que "fotografíen" la configuración de la cinta y el estado en cada paso $t$. Es un proceso muy similar a las funciones universales $i_{n,m}$ y $E_{n,m}$ que usamos para Neumann.

#### Teorema 13: Turing vence a Neumann

Este resultado establece que **toda función $\Sigma$-computable (programas de $S_\Sigma$) es $\Sigma$-Turing computable**.

- **La idea de la prueba:** Se demuestra que es posible construir una Máquina de Turing que funcione como un _emulador_. Esta máquina usa su cinta para representar las variables $Nk$ y $Pk$ de un programa y sus estados internos para simular el flujo de las instrucciones (incluidos los saltos `GOTO`).

### El Teorema de Equivalencia Final (Teorema 14)

Este es el resultado más importante de toda la primera parte de la materia. Declara el **empate técnico** y la **robustez** del concepto de computabilidad.

> [!success] Teorema 14 (Equivalencia de Modelos) Para cualquier alfabeto $\Sigma$ finito, las siguientes afirmaciones son equivalentes:
> 
> 1. $f$ es **$\Sigma$-Turing computable** (Hardware/Cinta).
> 2. $f$ es **$\Sigma$-recursiva** (Funciones matemáticas/Gödel).
> 3. $f$ es **$\Sigma$-computable** (Programas imperativos/Neumann).

#### Extensión a Conjuntos

La equivalencia no se queda solo en las funciones; se hereda directamente a la clasificación de los conjuntos de datos:

- **Enumerabilidad:** Ser un conjunto $\Sigma$-enumerable (Neumann), $\Sigma$-recursivamente enumerable (Gödel) o $\Sigma$-Turing enumerable es exactamente lo mismo.
- **Decidibilidad:** Ser un conjunto $\Sigma$-computable (Neumann), $\Sigma$-recursivo (Gödel) o $\Sigma$-Turing computable también es equivalente.

> [!info] ¿Por qué esto es "informático"? Este resultado nos asegura que la computabilidad es una **propiedad intrínseca** de los problemas y no depende del lenguaje de programación o de la arquitectura de la computadora que elijas. Si un problema es indecidible en uno de estos modelos, lo es en todos los demás.

---


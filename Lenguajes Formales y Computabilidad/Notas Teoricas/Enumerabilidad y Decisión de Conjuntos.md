
En esta última parte del paradigma de Neumann, aplicamos los conceptos de computabilidad de funciones para clasificar los conjuntos de tuplas mixtas (números y palabras). Al igual que en los modelos anteriores, la distinción fundamental reside en si un programa puede **decidir** la pertenencia a un conjunto o simplemente **listar** (generar) sus elementos.

### Conjuntos $\Sigma$-enumerables

Un conjunto $S \subseteq \omega^n \times \Sigma^{*m}$ es llamado **$\Sigma$-enumerable** bajo el paradigma de Neumann cuando es vacío o existe una función $F$ tal que su imagen es exactamente $S$ ($IF = S$) y cada una de sus funciones componentes es $\Sigma$-computable. Intuitivamente, esto significa que existe un procedimiento (un programa) capaz de generar todos los elementos del conjunto, uno tras otro, a partir de una entrada natural.

Para facilitar la resolución de ejercicios, contamos con la **Proposición 6 (Caracterización de $\Sigma$-enumerabilidad)**, que establece que un conjunto no vacío $S$ es enumerable si y solo si existe un único programa $P$ tal que:

- Para cada número natural $x$ de entrada, el programa $P$ se detiene y deja en las variables protagonistas ($N1, \dots, Nn, P1, \dots, Pm$) una tupla que pertenece a $S$.
- Para cualquier elemento del conjunto $S$, existe al menos un valor de entrada $x$ que hace que el programa $P$ genere dicha tupla.

> [!tip] Uso de Macros en Enumeración Gracias al **Primer Manantial de Macros**, para probar que un conjunto es enumerable podemos construir un programa "maestro" que use macros de las funciones componentes $F_i$. Si las funciones que generan las coordenadas son computables, el conjunto es automáticamente enumerable.

### Conjuntos $\Sigma$-computables (Decidibles)

Un conjunto $S \subseteq \omega^n \times \Sigma^{*m}$ se define como **$\Sigma$-computable** (o decidible) si su **función característica** $\chi_S$ es una función $\Sigma$-computable. En términos prácticos, esto implica que existe un programa $P$ que actúa como un "juez":

- Si la entrada $(x, \alpha)$ pertenece a $S$, el programa se detiene y deja un **1** en la variable $N1$.
- Si la entrada no pertenece a $S$, el programa se detiene y deja un **0** en la variable $N1$.

Dicho programa debe detenerse **siempre** (es decir, para todas las entradas posibles del universo $\omega^n \times \Sigma^{*m}$), ya que la función característica es, por definición, total.

#### Macro de Pertenencia a Conjuntos

Una aplicación directa de este concepto en la ingeniería de programas es la existencia del macro de salto condicional basado en conjuntos. Si $S$ es un conjunto $\Sigma$-computable, el **Primer Manantial de Macros** garantiza que podemos usar la instrucción: $$[IF \ (V1, \dots, Vn, W1, \dots, Wm) \in S \ GOTO \ A1]$$ Este macro evaluará la pertenencia de los contenidos de las variables actuales al conjunto $S$ y diseccionará el flujo del programa al label $A1$ si la respuesta es afirmativa.

> [!danger] Error común: Dominio vs. Computabilidad Es fundamental no confundir un conjunto que es el **dominio** de una función computable con un conjunto **computable**. Un conjunto puede ser el dominio de un programa (el programa se detiene solo si el elemento está en el conjunto), pero si para los elementos de afuera el programa entra en bucle infinito en lugar de devolver "0", el conjunto **no es computable**, sino meramente enumerable.

#### Operaciones que preservan la computabilidad

Al igual que en el paradigma de Gödel, la clase de los conjuntos $\Sigma$-computables es cerrada bajo las operaciones lógicas usuales. Si tenemos dos conjuntos decidibles $S_1$ y $S_2$, entonces su unión ($S_1 \cup S_2$), intersección ($S_1 \cap S_2$) y resta ($S_1 - S_2$) también son conjuntos $\Sigma$-computables. Esto se debe a que podemos combinar los programas que deciden cada conjunto mediante macros de tipo `IF` y operadores lógicos para formar un nuevo "decididor".

---

**Glosario de Conjuntos en Neumann**

- **$\Sigma$-enumerable:** Conjunto cuyos elementos pueden ser listados por un programa.
- **$\Sigma$-computable:** Conjunto para el cual existe un programa que decide la pertenencia en tiempo finito.
- **Decidir:** Acción de un programa de devolver 1 o 0 de forma total según la entrada.

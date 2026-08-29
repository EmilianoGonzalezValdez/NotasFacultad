
---
### Definición Formal: La 7-upla

La **Máquina de Turing (MT)** es la formalización matemática del concepto de "máquina" que manipula símbolos en una cinta. Se define formalmente como una **7-upla** $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$, donde cada componente cumple un rol específico en el sistema:

- **$Q$:** Es un conjunto finito cuyos elementos llamamos _estados_. Representan la "memoria interna" o el momento concreto de la máquina durante su funcionamiento.
- **$\Sigma$:** Es el _alfabeto de entrada_. Contiene los símbolos que se usan para formar la palabra inicial en la cinta.
- **$\Gamma$:** Es el _alfabeto de cinta_. Es un conjunto finito de símbolos que incluye obligatoriamente al alfabeto de entrada ($\Sigma \subseteq \Gamma$).
- **$B$:** Es el símbolo **blanco** (_blank symbol_). Cumple que $B \in \Gamma - \Sigma$ (está en la cinta pero no en la entrada). Se usa para representar que un cuadro de la cinta está vacío.
- **$\delta$:** Es la **función de transición**, el "cerebro" o personalidad de la máquina. Se define como: $$\delta: D_\delta \subseteq Q \times \Gamma \to Q \times \Gamma \times {L, R, K}$$
- **$q_0$:** Es el _estado inicial_ ($q_0 \in Q$) donde arranca la computación.
- **$F$:** Es el conjunto de _estados finales_ ($F \subseteq Q$). Si la máquina alcanza un estado de $F$, decimos que la palabra es aceptada.

> [!info] Asunción Inocua de Disyunción Para evitar errores de tipo y facilitar el análisis matemático, asumimos que el conjunto de estados $Q$ y el alfabeto de cinta $\Gamma$ son **disjuntos** ($Q \cap \Gamma = \emptyset$).

#### La Función de Transición ($\delta$): El Alma de la Máquina

La función $\delta$ determina qué tarea realiza la máquina y a qué estado pasa según lo que lea su cabezal. Una instrucción $\delta(p, \sigma) = (q, \gamma, m)$ se interpreta así:

1. **Borrra** el símbolo $\sigma$ y **escribe** $\gamma$ en su lugar.
2. **Mueve** el cabezal según $m \in {L, R, K}$ ($L$: izquierda, $R$: derecha, $K$: quieto).
3. **Cambia** el estado interno de $p$ a $q$.

> [!warning] Límites de Movimiento y Detención Si la máquina intenta moverse a la izquierda ($L$) estando en el primer cuadro de la cinta, no puede hacer nada y se detiene, ya que la cinta solo es infinita hacia la derecha. También se detiene si el par (estado, símbolo) no pertenece al dominio de $\delta$.

#### Componentes de la Cinta y el Cabezal

El modelo de Turing se apoya en una infraestructura física abstracta:

- **Cinta de papel:** Dividida en cuadros, con un primer cuadro a la izquierda y extensible infinitamente hacia la derecha.
- **Cabeza lectora (Cabezal):** Lee un cuadro a la vez, puede borrar, escribir y moverse.
- **Determinismo:** La máquina es determinística; ante un mismo estado y símbolo, siempre realiza la misma tarea y pasa al mismo estado.

> [!example] Ejemplo de Comportamiento Si tenemos $\delta(q_0, a) = (q_1, @, L)$, la máquina estando en $q_0$ y viendo una 'a', escribirá un '@', se moverá un lugar a la izquierda y pasará al estado $q_1$.

---

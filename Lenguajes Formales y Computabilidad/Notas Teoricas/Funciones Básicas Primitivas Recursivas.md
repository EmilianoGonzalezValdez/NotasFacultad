
---

### La Intuición del Ladrillo Básico

El **Paradigma de Gödel** (o paradigma funcional/recursivo) postula que cualquier función efectivamente computable puede ser expresada como una combinación finita de funciones ultra simples. En este modelo, no hay cintas ni cabezales; hay **Funciones Iniciales** que aceptamos como "obviamente computables" por un humano con papel y lápiz, y **constructores** que nos permiten crear funciones complejas a partir de ellas.

> [!info] El conjunto inicial de funciones La base de todo el edificio funcional ($PR_\Sigma^0$) está compuesta por: $${Suc, Pred, C_{0,0}^0, C_{0,0}^\epsilon} \cup {d_a : a \in \Sigma} \cup {p_{n,m}^j : 1 \le j \le n+m}$$

#### Detalle de las Funciones Iniciales

Para resolver ejercicios y combos de teoría, es vital manejar la definición exacta y el **tipo** de cada ladrillo:

- **Sucesor ($Suc$):** Incrementa un número natural en uno.
    - Tipo: $(1, 0, \#)$.
    - Definición: $Suc(n) = n + 1$.
- **Predecesor ($Pred$):** Resta uno a un natural, pero ojo que solo está definida para $n > 0$.
    - Tipo: $(1, 0, \#)$.
    - Definición: $Pred(n) = n - 1$. Su dominio es $\mathbb{N}$ (naturales sin el cero).
- **Funciones Derecha ($d_a$):** Agregan el símbolo $a \in \Sigma$ al final de una palabra. Hay una función $d_a$ por cada símbolo del alfabeto.
    - Tipo: $(0, 1, *)$.
    - Definición: $d_a(\alpha) = \alpha a$.
- **Proyecciones ($p_{n,m}^i$):** "Extraen" un dato de una entrada mixta. El índice $i$ indica qué posición devolver.
    - **Numérica:** Si $1 \le i \le n$, devuelve el natural en esa posición: $p_{n,m}^i(\vec{x}, \vec{\alpha}) = x_i$.
    - **Alfabética:** Si $n+1 \le i \le n+m$, devuelve la palabra: $p_{n,m}^i(\vec{x}, \vec{\alpha}) = \alpha_{i-n}$.
- **Constantes ($C_{n,m}^k$ o $C_{n,m}^\alpha$):** Ignoran la entrada y devuelven siempre el mismo número $k$ o palabra $\alpha$.
    - Ejemplo numérico: $C_{1,3}^3(x, \alpha_1, \alpha_2, \alpha_3) = 3$.
    - Ejemplo alfabético: $C_{1,3}^\epsilon(x, \alpha_1, \alpha_2, \alpha_3) = \epsilon$.

> [!tip] Uso Práctico: Justificación de Macros En la práctica, estas funciones son el paso final de cualquier demostración de que algo es $\Sigma$-recursivo primitivo ($PR_\Sigma$). Si lográs descomponer tu función hasta que solo queden estas piezas y los constructores legales, ganaste.

#### El concepto de Σ-totalidad en Funciones Iniciales

Casi todas las funciones iniciales son **$\Sigma$-totales**, es decir, están definidas para cualquier combinación de entradas del tipo correcto. La gran excepción es **$Pred$**, cuyo dominio no incluye al cero, lo que la hace una función parcial sobre $\omega$.

---

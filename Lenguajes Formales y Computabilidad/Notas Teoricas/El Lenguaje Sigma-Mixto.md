
---
### El Corazón del Lenguaje: Funciones Mixtas

Una función es **$\Sigma$-mixta** si está diseñada para operar simultáneamente con números naturales y palabras de un alfabeto $\Sigma$ fijo. Esto evita la ambigüedad de tipos en las definiciones de computabilidad.

Para que una función $f$ sea considerada $\Sigma$-mixta, debe cumplir dos condiciones:

1. **Dominio restringido**: Deben existir $n, m \ge 0$ tales que $Df \subseteq \omega^n \times \Sigma^{*m}$. Es decir, recibe $n$ números y $m$ palabras.
2. **Imagen homogénea**: El resultado debe ser siempre un número ($If \subseteq \omega$) o siempre una palabra ($If \subseteq \Sigma^*$).

> [!note] El concepto de Σ-total Una función es **$\Sigma$-total** si su dominio es exactamente el conjunto de todas las combinaciones posibles de sus entradas, es decir, $Df = \omega^n \times \Sigma^{*m}$.

#### Clasificación por Tipo (n, m, s)

Cada función mixta tiene una "firma" o tipo que la identifica unívocamente (siempre que no sea la función vacía $\emptyset$). El tipo se escribe como una terna $(n, m, s)$:

- **$n$**: Cantidad de argumentos numéricos ($\omega$).
- **$m$**: Cantidad de argumentos alfabéticos ($\Sigma^*$).
- **$s$**: Tipo de salida. Usamos **#** para una salida numérica y $*$ para una salida alfabética.

> [!example] Ejemplos de tipos
> 
> - $Suc$: Tipo $(1, 0, \#)$.
> - $d_a$ (función derecha): Tipo $(0, 1, *)$.
> - $\lambda \alpha [ |\alpha| ]$: Tipo $(0, 1, \#)$.

### Predicados Σ-mixtos y Operaciones Lógicas

Un **predicado** es simplemente una función mixta cuyo resultado está restringido al conjunto ${0, 1}$, donde $1$ representa "Verdadero" y $0$ representa "Falso".

Si tenemos dos predicados $P$ y $Q$ con el mismo dominio $S$, podemos construir nuevos predicados mediante operaciones lógicas:

- **Disyunción ($P \vee Q$)**: Vale 1 si alguno de los dos es 1.
- **Conjunción ($P \wedge Q$)**: Vale 1 solo si ambos son 1.
- **Negación ($\neg P$)**: Intercambia 1 por 0 y viceversa.

> [!tip] Función Característica ($\chi_S$) Es el predicado que "identifica" a un conjunto $S$. Devuelve $1$ si el elemento pertenece a $S$ y $0$ si no. Decimos que un conjunto es **$\Sigma$-computable** si su función característica lo es.

### Composición y Funciones Iniciales

La computabilidad se construye combinando bloques básicos. El método principal es la **composición**.

#### La n-upla de funciones $[f_1, \dots, f_r]$

Para componer funciones que reciben varios argumentos, definimos una función especial $f_1, \dots, f_r = (f_1(e), \dots, f_r(e))$. Su dominio es la intersección de los dominios de todas las funciones que la componen.

#### Funciones Iniciales (Los Ladrillos)

Estas funciones son la base del Paradigma de Gödel (recursividad) y se consideran "obviamente computables":

- **Sucesor ($Suc$):** $n \to n+1$.
- **Predecesor ($Pred$):** $n \to n-1$ (y $Pred(0)$ queda indefinido).
- **Constantes ($C_{n,m}^k$ o $C_{n,m}^\alpha$):** Devuelven siempre el mismo valor $k$ o $\alpha$.
- **Proyecciones ($p_{n,m}^i$):** Devuelven el contenido de la coordenada $i$-ésima de la entrada.
- **Funciones Derecha ($d_a$):** Agregan el símbolo $a$ al final de una palabra.

> [!important] Preservación de la Naturaleza Mixta La composición de funciones $\Sigma$-mixtas siempre da como resultado otra función $\Sigma$-mixta. Esto garantiza que nunca nos salgamos del universo de objetos definido.

---

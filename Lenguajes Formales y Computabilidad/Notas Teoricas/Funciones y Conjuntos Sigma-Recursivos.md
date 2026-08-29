
---
### Definición de la Clase $PR^Σ$

La clase de las funciones **$\Sigma$-recursivas primitivas** ($PR^\Sigma$) se define como la _clausura inductiva_ del conjunto de funciones iniciales bajo los constructores de composición y recursión primitiva. Esto significa que una función $f$ pertenece a $PR^\Sigma$ si puede obtenerse a partir de las funciones iniciales aplicando una cantidad finita de veces esos dos constructores.

> [!info] El "ADN" de $PR^Σ$
> 
> 1. **Base:** Todas las funciones iniciales ($Suc, Pred, C, p, d_a$) están en $PR^\Sigma$.
> 2. **Paso:** Si $f, g, h, G_a$ están en $PR^\Sigma$, entonces las funciones obtenidas por composición y por cualquiera de los cuatro casos de recursión primitiva también están en $PR^\Sigma$.
> 3. **Conclusión:** Solo las funciones obtenidas por estas reglas pertenecen al club.

#### Propiedad de Computabilidad (Leibniz vence a Gödel)

Toda función $f \in PR^\Sigma$ es **$\Sigma$-efectivamente computable**. Esto es así porque partimos de funciones que un humano puede calcular fácilmente y usamos reglas (composición e inducción) que preservan esa capacidad.

### Conjuntos y Predicados $PR^Σ$

Para Gödel, no hay distinción entre "decidir" un conjunto y calcular una función.

- **Conjunto $PR^\Sigma$**: Un conjunto $S$ es $\Sigma$-primitivo recursivo si su **función característica** $\chi_S$ es una función en $PR^\Sigma$.
- **Predicado $PR^\Sigma$**: Es una función cuya imagen está contenida en ${0, 1}$ y pertenece a $PR^\Sigma$.

> [!success] Operaciones Lógicas Si tenés dos predicados $P$ y $Q$ que son $PR^\Sigma$, entonces los predicados formados por las conectivas lógicas también lo son:
> 
> - **Negación ($\neg P$):** $1 \dot{-} P$.
> - **Conjunción ($P \wedge Q$):** $P \cdot Q$.
> - **Disyunción ($P \vee Q$):** $\neg(\neg P \wedge \neg Q)$. Esto implica que si dos conjuntos son $PR^\Sigma$, su unión, intersección y diferencia también lo son.

#### Caracterización por Dominio

Un resultado clave (que es un **Combo de Teorema**) es que un conjunto $S$ es $PR^\Sigma$ **si y solo si** es el dominio de alguna función que pertenece a $PR^\Sigma$.

### Lema de División por Casos

Este es el "destornillador" principal para resolver ejercicios. Nos permite definir una función "por tramos" y asegurar que el resultado sigue siendo $PR^\Sigma$.

Dadas funciones $f_1, \dots, f_k$ en $PR^\Sigma$ con dominios $Df_1, \dots, Df_k$ disjuntos de a pares    ($Df_i \cap Df_j = \emptyset$), la función $f = f_1 \cup \dots \cup f_k$ es **$PR^\Sigma$**.

#### Procedimiento Práctico para Ejercicios

Para probar que una función $f$ definida por casos es $PR^\Sigma$, tenés que:

1. **Identificar los casos:** Ver cuántas condiciones tiene la función (por ejemplo, "si $x$ es par", "si $x$ es impar").
2. **Definir los conjuntos:** Llamar $S_1, S_2, \dots$ a los subconjuntos del dominio que disparan cada caso.
3. **Probar que los conjuntos son $PR^\Sigma$:** Generalmente usando funciones características de predicados simples ($x=y$, $x \le y$, etc.).
4. **Probar que las funciones de cada tramo son $PR^\Sigma$:** Mostrar que en ese tramo la función se comporta como una composición de iniciales.
5. **Cerrar:** Invocar el _Lema de División por Casos_ para concluir que la unión de esos tramos es $PR^\Sigma$.

> [!example] Ejemplo: Función Identidad Condicionada Si $f(x) = x$ si $x$ es par, y $f(x) = 0$ si $x$ es impar.
> 
> 1. $S_1 = {x : x \text{ es par}}$ es $PR^\Sigma$.
> 2. $f_1 = p_{1,0}^1 | S_1$ es $PR^\Sigma$ (proyección restringida a conjunto $PR^\Sigma$).
> 3. $S_2 = {x : x \text{ es impar}}$ es $PR^\Sigma$.
> 4. $f_2 = C_{1,0}^0 | S_2$ es $PR^\Sigma$ (constante restringida).
> 5. Por Lema de División por Casos, $f = f_1 \cup f_2$ es $PR^\Sigma$.

---

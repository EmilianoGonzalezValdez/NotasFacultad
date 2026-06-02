
El lenguaje $S_\Sigma$ es un modelo formal de programación imperativa diseñado para modelizar el concepto de computación efectiva. La sintaxis define qué combinaciones de símbolos son válidas para ser interpretadas por la "máquina" de Neumann.

### Alfabeto y Componentes Fundamentales

Toda palabra en $S_\Sigma$ se construye sobre el alfabeto $\Sigma \cup \Sigma_p$. El **alfabeto de programa** $\Sigma_p$ contiene los símbolos necesarios para definir operaciones y control de flujo: $$\Sigma_p = Num \cup {\leftarrow, +, \dot{-}, ., \neq, \curvearrowright, \epsilon, N, K, P, L, I, F, G, O, T, B, E, S}$$ Donde $Num = {0, 1, \dots, 9}$. A partir de estos símbolos se definen los tres elementos básicos:

- **Variables Numéricas ($Nk$):** Almacenan naturales. Se escriben como la letra $N$ seguida del índice en notación decimal (ej. $N0, N1, N14$).
- **Variables Alfabéticas ($Pk$):** Almacenan palabras de $\Sigma^*$. Se escriben como la letra $P$ seguida del índice (ej. $P0, P1, P22$).
- **Labels (Etiquetas $Lk$):** Identificadores de destino para saltos. Se forman con la letra $L$ seguida del índice (ej. $L0, L1$).

> [!info] Notación de índices En el formalismo, el índice $k$ se escribe como $\bar{k}$ (la palabra decimal). Así, la variable $N5$ es la palabra de longitud 2 formada por los símbolos $N$ y $5$. Por convención, las entradas de una función se ubican en $N1 \dots Nn$ y $P1 \dots Pm$, y el resultado debe devolverse en $N1$ o $P1$.

### Instrucciones: Definición y Tipos

Una **instrucción básica** es una palabra que indica una transformación de estado o una alteración del flujo. Existen exactamente **11 formas básicas** agrupadas por su función:

#### Asignaciones y Operaciones

- **Incremento:** $Nk \leftarrow Nk + 1$ (Suma 1 al contenido de $Nk$).
- **Decremento:** $Nk \leftarrow Nk \dot{-} 1$ (Resta 1; si es 0, permanece en 0).
- **Copia Numérica:** $Nk \leftarrow Nn$ (Copia el contenido de $Nn$ en $Nk$).
- **Limpieza Numérica:** $Nk \leftarrow 0$ (Asigna el valor 0).
- **Extensión Alfabética:** $Pk \leftarrow Pk.a$ (Agrega el símbolo $a \in \Sigma$ al final de la palabra en $Pk$).
- **Reducción Alfabética:** $Pk \leftarrow \curvearrowright Pk$ (Elimina el primer símbolo de la izquierda; si es $\epsilon$, no hace nada).
- **Copia Alfabética:** $Pk \leftarrow Pn$ (Copia el contenido de $Pn$ en $Pk$).
- **Limpieza Alfabética:** $Pk \leftarrow \epsilon$ (Asigna la palabra vacía).

#### Control de Flujo

- **Salto Condicional (Num):** `IF` $Nk \neq 0$ `GOTO` $Ln$ (Salta a la instrucción con etiqueta $Ln$ si $Nk$ no es 0).
- **Salto Condicional (Alpha):** `IF` $Pk$ `BEGINS` $a$ `GOTO` $Ln$ (Salta si la palabra en $Pk$ comienza con el símbolo $a \in \Sigma$).
- **Salto Incondicional:** `GOTO` $Ln$ (Equivalente a una transferencia directa a $Ln$).
- **Instrucción Neutra:** `SKIP` (No modifica variables ni flujo; se usa para labels de cierre o estructuras de macros).

> [!note] Instrucciones Etiquetadas Una instrucción puede estar precedida por un label para permitir que sea destino de un salto: $Lk I$ (donde $I$ es básica). El label $Lk$ se considera el identificador de esa línea.

### Estructura de Programa y la Ley de los GOTO

Un **programa** $P$ es una palabra formada por la concatenación de instrucciones $I_1 I_2 \dots I_n$ ($n \ge 1$). La validez de un programa depende de la **Propiedad G** o **Ley de los GOTO**:

> [!danger] Ley de los GOTO Si en cualquier instrucción $I_i$ del programa aparece un salto `GOTO` $Lm$, **debe existir** al menos una instrucción $I_j$ en ese mismo programa que posea el label $Lm$.

#### Propiedades del Análisis Sintáctico

1. **Parseo Único (Lema 1):** Debido a la estructura del alfabeto, cualquier programa $P$ tiene una **única descomposición** en instrucciones. No hay ambigüedad al separar las líneas de código.
2. **Longitud y Puntero:** Se define $n(P)$ como la cantidad de instrucciones. La ejecución es secuencial ($1, 2, \dots$). Si el puntero de instrucción intenta acceder a $n(P)+1$, el programa se detiene.

> [!tip] Uso en Ejercicios Al diseñar programas, es vital asegurar que el dominio se respete. Si una función es parcial, el programa no debe detenerse (entrar en bucle infinito) para entradas fuera del dominio. Esto se logra con saltos del tipo `L1 GOTO L1`.

---

**Glosario de Sintaxis**

- **$\Sigma_p$:** Alfabeto de símbolos de programa exclusivos de $S_\Sigma$.
- **Variable Auxiliar:** Variable con índice alto usada para no alterar las entradas (ej. $N100$).
- **Instrucción Básica:** La acción mínima realizable sobre una variable o el flujo.


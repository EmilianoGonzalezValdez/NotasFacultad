
En el paradigma de Neumann, una función se considera computable si existe un programa en el lenguaje $S_\Sigma$ capaz de transformar un estado inicial con los datos de entrada en un estado final que contenga el resultado. Este enfoque formaliza la idea de "procedimiento efectivo" mediante la ejecución secuencial de instrucciones que modifican variables.

### Configuración Inicial y Estado Estándar

Para que la computación sea consistente, debemos definir cómo se cargan los datos en la memoria antes de que el programa $P$ empiece a correr. Se utiliza la notación de **estado inicial estándar** para representar una memoria donde casi todas las variables son 0 o $\epsilon$, excepto las que contienen los argumentos.

- **Notación:** $|x_1, \dots, x_n, \alpha_1, \dots, \alpha_m|$ representa el estado donde las primeras $n$ variables numéricas ($N1, \dots, Nn$) contienen los números de entrada, y las primeras $m$ variables alfabéticas ($P1, \dots, Pm$) contienen las palabras de entrada.
- **Resto de las variables:** Automáticamente, todas las variables $Nk$ para $k > n$ se inicializan en 0, y todas las $Pk$ para $k > m$ se inicializan en $\epsilon$.

> [!info] Casos Límite Si la función no tiene entradas numéricas ($n=0$), el estado se denota $|\alpha_1, \dots, \alpha_m|$. Si no tiene entradas alfabéticas ($m=0$), se denota $|x_1, \dots, x_n|$. Si no tiene ninguna entrada, se usa el símbolo $| \diamond |$, que representa un estado donde todo es 0 o vacio.

### Operadores de Salida $\Psi$

Dado que un programa modifica muchas variables a la vez, necesitamos una regla para saber **dónde leer el resultado** una vez que el programa se detiene. Para esto se definen los operadores $\Psi$.

#### El Operador Numérico ($\Psi_{n,m,#}$)

Se utiliza cuando la función que queremos computar devuelve un número natural ($f: \dots \to \omega$).

- **Definición:** $f = \Psi_{n,m,#} P$.
- **Resultado:** El valor de la función es el contenido final de la variable **$N1$** cuando el programa $P$ se detiene.
- **Dominio:** La función está definida para una entrada solo si el programa $P$ **termina** partiendo del estado inicial correspondiente.

#### El Operador Alfabético ($\Psi_{n,m,*}$)

Se utiliza cuando la función devuelve una palabra ($f: \dots \to \Sigma^*$).

- **Definición:** $f = \Psi_{n,m,*} P$.
- **Resultado:** El valor de la función es el contenido final de la variable **$P1$** al momento de la detención.

> [!danger] Importancia de la Detención Si el programa $P$ no se detiene para una entrada $(\vec{x}, \vec{\alpha})$, entonces ese punto **no pertenece al dominio** de la función computada ($\Psi P$ es indefinido en ese punto).

### Definición Formal de Computabilidad

Una función mixta $f: Df \subseteq \omega^n \times \Sigma^{_m} \to O$ (donde $O$ es $\omega$ o $\Sigma^_$) es **$\Sigma$-computable** si existe un programa $P$ de $S_\Sigma$ tal que $f = \Psi_{n,m,s} P$, siendo $s$ el tipo de salida (# o *).

#### Relación con el Paradigma de Leibniz

Se cumple que toda función $\Sigma$-computable es también $\Sigma$-efectivamente computable. Esto significa que el modelo de Neumann es una formalización válida (fiel) del concepto intuitivo de procedimiento efectivo.

#### Uso práctico en ejercicios

Para probar que una función es computable, el procedimiento suele ser:

1. **Diseñar el programa $P$**: Asegurarse de que use las variables $N1 \dots Nn$ y $P1 \dots Pm$ como entrada.
2. **Gestionar el resultado**: El algoritmo debe asegurar que, al finalizar, el valor buscado esté en $N1$ (si es número) o $P1$ (si es palabra).
3. **Asegurar la no-detención**: Si la función es parcial, el programa debe entrar en un bucle infinito (usando etiquetas y `GOTO`) para las entradas que no están en el dominio.

> [!example] Ejemplo: Función Sucesor El programa `N1 ← N1 + 1` computa la función $Suc: \omega \to \omega$. Al terminar, el resultado de incrementar la entrada $N1$ queda en la misma variable $N1$, que es donde $\Psi_{1,0,#}$ busca el resultado.

---

**Glosario de Computabilidad**

- **$\Psi_{n,m,s} P$:** Función matemática que representa el "comportamiento de caja negra" del programa $P$.
- **Estado Inicial Estándar:** Configuración de memoria donde las entradas ocupan las primeras posiciones de las variables.
- **Variable Protagonista:** Variable que contiene una entrada o el resultado final ($N1, P1$).


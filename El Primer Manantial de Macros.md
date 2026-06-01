
El _Primer Manantial de Macros_ es un resultado fundamental del paradigma imperativo que garantiza que cualquier función o predicado que sea **$\Sigma$-computable** puede ser utilizado como una instrucción simple (macro) dentro de un programa de $S_\Sigma$.

### Definición y Alcance

El teorema (Proposición 5 de la Guía 7) establece que si tenemos funciones o predicados que ya sabemos que se pueden computar (ya sea porque hicimos el programa o por los paradigmas de Turing/Gödel), el lenguaje $S_\Sigma$ automáticamente "gana" la capacidad de usarlos como bloques de construcción.

#### Tipos de macros garantizados

El manantial asegura la existencia de tres tipos de estructuras fundamentales para la programación en $S_\Sigma$:

- **Macros de Asignación Numérica:** Para cualquier función $f: Df \subseteq \omega^n \times \Sigma^{*m} \to \omega$ que sea computable, existe el macro: $$[V_{n+1} \leftarrow f(V_1, \dots, V_n, W_1, \dots, W_m)]$$
- **Macros de Asignación Alfabética:** Para cualquier función $g: Dg \subseteq \omega^n \times \Sigma^{_m} \to \Sigma^_$ que sea computable, existe el macro: $$[W_{m+1} \leftarrow g(V_1, \dots, V_n, W_1, \dots, W_m)]$$
- **Macros de tipo IF (Saltos):** Para cualquier predicado $P: DP \subseteq \omega^n \times \Sigma^{*m} \to {0, 1}$ que sea computable, existe el macro: $$[IF \ P(V_1, \dots, V_n, W_1, \dots, W_m) \ GOTO \ A_1]$$

> [!success] Importancia Teórica Este manantial es el que permite que Neumann "venga a vencer a Leibniz". Nos dice que el lenguaje $S_\Sigma$ es lo suficientemente potente como para absorber cualquier procedimiento efectivo que hayamos definido antes.

### Uso Práctico en Ejercicios

Para resolver ejercicios de la Guía 7 o de parcial, el Manantial de Macros funciona como una **justificación legal**. Si necesitás usar una función compleja (como el resto de una división o el máximo de una palabra), el procedimiento es:

1. Mencionar que la función $f$ es $\Sigma$-computable (generalmente porque es $\Sigma$-p.r. y ya lo probaste en Guías anteriores).
2. Invocar el **Primer Manantial de Macros** para asegurar que el macro existe en $S_\Sigma$.
3. Escribir el macro en tu programa con las variables protagonistas adecuadas, por ejemplo: $[N3 \leftarrow SUMA(N3, N1)]$.

> [!warning] Ojo con el Dominio Recordá que si la función $f$ es parcial (no está definida para todas las entradas), el macro expandido **no debe detenerse** cuando recibe una entrada fuera de $Df$. Esto es vital para que la simulación sea fiel a la función original.

### Relación con otros Manantiales

Existe un **Segundo Manantial de Macros**, pero este depende de resultados que se ven recién en la Guía 8, relacionados con la equivalencia total entre el paradigma de Gödel y el de Neumann. El _Primer Manantial_ se limita a lo que ya demostramos que es computable mediante programas concretos o funciones recursivas básicas.

---

**Mini-glosario de la nota**

- **Manantial:** Fuente de recursos (macros) que potencia el lenguaje básico.
- **$\Sigma$-computable:** Función que puede ser calculada por un programa en $S_\Sigma$.
- **Justificación:** Argumento teórico necesario para usar macros en un examen.
}
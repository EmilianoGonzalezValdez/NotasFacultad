
---

### El Teorema de Godelización de Programas

Este teorema completa la equivalencia entre paradigmas demostrando que **toda función $\Sigma$-computable es $\Sigma$-recursiva**. En términos prácticos, esto significa que cualquier cosa que haga un programa de Neumann ($S_\Sigma$) puede ser descrita y calculada mediante una función matemática de Gödel utilizando los constructores de recursión y minimización.

La clave de la demostración es que la ejecución de un programa es un proceso mecánico que puede ser "fotografiado" paso a paso. Para probarlo, usamos las funciones universales de simulación ($i, E, Halt, T$) definidas previamente.

#### Representación Matemática de un Programa

Si una función $f$ es computada por un programa $P_0$, podemos expresar el resultado de $f$ para una entrada $(\vec{x}, \vec{\alpha})$ mediante la composición de funciones recursivas.

Para una función con salida numérica (tipo $\#$), la fórmula es: $$f(\vec{x}, \vec{\alpha}) = E_{n,m,1}^{\#} (T_{n,m}(\vec{x}, \vec{\alpha}, P_0), \vec{x}, \vec{\alpha}, P_0)$$

Donde:

1. **$T_{n,m}(\vec{x}, \vec{\alpha}, P_0)$:** Es el tiempo de detención (minimización del predicado $Halt$). Nos dice cuántos pasos tarda el programa en parar.
2. **$E_{n,m,1}^{\#}(\dots)$:** Es la función de estado que extrae el contenido de la variable $N1$ en ese tiempo exacto.

> [!info] La lógica de la prueba Como $Halt$ es recursiva primitiva, su minimización $T$ es **$\Sigma$-recursiva**. Como $E$ también es recursiva primitiva, la composición de ambas resulta en una función **$\Sigma$-recursiva**. Así, cualquier programa $P$ queda "atrapado" dentro del mundo funcional de Gödel.

#### El rol de la Función Universal $\Psi$

Este resultado demuestra que la función universal $\Psi_{n,m,s}^P$ es, por definición, una función recursiva. Esto tiene una consecuencia fundamental: la computabilidad no depende de la "magia" del hardware o de los cables de una computadora, sino que es una propiedad puramente aritmética de las funciones.

> [!warning] Parcialidad Heredada Es fundamental recordar que aunque $E$ y $Halt$ son totales, la función $T$ (tiempo de parada) puede ser parcial si el programa no termina. Por eso, el resultado final $f$ puede ser una función parcial, lo que encaja perfectamente con la definición de las funciones en $R_\Sigma$.

### Uso Práctico: ¿Por qué es importante para el final?

En los exámenes, este resultado (junto con el de Neumann vence a Gödel) te permite moverte entre paradigmas con total libertad.

- Si tenés un conjunto definido por un programa (Neumann), sabés que es un conjunto $\Sigma$-recursivo o $r.e.$ (Gödel).
- Te permite justificar que cualquier operación de "bajo nivel" (como el manejo de variables) tiene un respaldo matemático sólido.

> [!tip] La "Batalla" en los Combos Si en el final te toca el **Combo 3 o 9**, te van a pedir esta demostración. Lo más importante es que escribas la composición de $f$ en función de $E$ y $T$, aclarando que $E$ es $p.r.$ y $T$ es $M(Halt)$, por lo tanto recursiva.

---

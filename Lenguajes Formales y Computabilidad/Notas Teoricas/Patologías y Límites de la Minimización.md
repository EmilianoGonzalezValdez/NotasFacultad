
---

### El Límite del Constructor $M(P)$

A diferencia de la composición y la recursión primitiva, que siempre preservan la computabilidad, el constructor de **minimizacion** es el único que puede sacarnos del universo de lo computable. Si bien en la Guía 6 vimos que $M(P)$ funciona bárbaro para predicados totales y acotados, en el terreno de los predicados parciales o con búsquedas infinitas, surgen "patologías" matemáticas.

#### Predicados Recursivos con Minimización no Computable

Existe un resultado contundente: hay predicados $P$ que son **$\Sigma$-recursivos** (es decir, que podemos decidir), pero cuya minimización $M(P)$ **no es $\Sigma$-recursiva** (ni siquiera efectivamente computable).

**El ejemplo patológico:** Se define un predicado $P$ basado en el conjunto $A$ (Aceptación). Se puede demostrar que existe un $P \in R_\Sigma$ tal que:

1. Su dominio $DM(P)$ es todo el conjunto de programas $Pro_\Sigma$.
2. El valor de la minimización $M(P)$ en un programa $P_0$ está directamente vinculado a si ese programa para o no ($AutoHalt_\Sigma$).
3. **Conclusión:** Como $AutoHalt_\Sigma$ no es recursivo, la función $M(P)$ tampoco puede serlo.

> [!danger] La trampa de la búsqueda infinita Esto demuestra que, aunque el predicado sea "lindo" (recursivo), el acto de buscar el _menor t_ que lo cumple puede ser una tarea imposible de automatizar si la respuesta depende de problemas indecidibles como la parada.

### Funciones Recursivas con Dominios "Feos"

Otra patología común es que una función sea $\Sigma$-recursiva pero su **dominio** no sea un conjunto recursivo (decidible).

- **Ejemplo:** La función constante $C_{0,1}^1|_A$ (la función que siempre devuelve 1, pero restringida solo a los programas que paran con su propio código).
- **Análisis:** La función es recursiva (por el _Lema de restricción_), pero su dominio es el conjunto $A$. Como ya probamos que $A$ es enumerable pero **no** decidible, tenemos una función legal cuyo dominio es un conjunto "rebelde".

> [!warning] Error Común en el Final Es tentador pensar que si $f$ es una función "calculable", su dominio $Df$ también debe serlo. ¡Error! El dominio de una función recursiva es siempre $\Sigma-r.e.$, pero no necesariamente $\Sigma$-recursivo.

### Cuantificación No Acotada: El Salto al Vacío

La patología final radica en el uso de los cuantificadores $\exists t$ y $\forall t$ sin un límite superior.

- **Cuantificación Acotada:** $(\exists t \le x) P(t)$ preserva la recursividad primitiva.
- **Cuantificación No Acotada:** $(\exists t) P(t)$ puede dar como resultado algo no computable.

El ejemplo máximo es $AutoHalt_\Sigma$: se define cuantificando el predicado $Halt$ (que es $p.r.$), pero como la búsqueda del tiempo $t$ no tiene techo, el resultado es un predicado que escapa de la matemática funcional.

> [!tip] Resumen para Ejercicios Siempre que veas una minimización o una búsqueda existencial **sin cota**, tené cuidado: ahí es donde suelen esconderse los problemas indecidibles y las funciones que no son recursivas.

---


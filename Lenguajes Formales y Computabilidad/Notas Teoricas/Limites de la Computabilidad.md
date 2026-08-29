
---

Este bloque se centra en las propiedades de las funciones recursivas y la clasificación de los conjuntos. Aquí es donde el paradigma de Gödel (funcional) se encuentra con su frontera final: el **Problema de la Parada** y los conjuntos que ninguna máquina puede decidir.

### [[Clausura y Herramientas del Paradigma Recursivo]]

En esta nota agrupamos los resultados que nos permiten "manipular" funciones recursivas con la misma facilidad que las primitivas recursivas, justificando legalmente los saltos entre paradigmas.

- **Lema de división por casos para funciones Σ-recursivas:** Demostración de que si definimos una función por tramos con dominios disjuntos y recursivos, el resultado sigue siendo una función $\Sigma$-recursiva.
- **Lema de restricción de funciones Σ-recursivas:** Prueba de que restringir una función recursiva a un subconjunto $\Sigma-r.e.$ preserva la recursividad.
- **Propiedades de clausura de conjuntos:** La unión e intersección de conjuntos $\Sigma-r.e.$ es $\Sigma-r.e.$, y la unión, intersección y resta de conjuntos $\Sigma-recursivos$ es $\Sigma-recursiva$.

### [[Caracterización de Conjuntos Σ-r.e. (Recursivamente Enumerables)]]

Esta nota es el corazón teórico para clasificar dominios e imágenes. Es fundamental para el **Combo 6** de teoremas.

- **Teorema 5 (Las 4 caras de la enumerabilidad):** Demostración de la equivalencia entre ser $\Sigma-r.e.$, ser la imagen de una función recursiva, ser el dominio de una función recursiva ($S = Df$) y ser la imagen de una función $\Sigma-p.r.$.
- **Relación con la Decidibilidad (Lema 4):** Demostración de que un conjunto es $\Sigma-recursivo$ si y solo si él y su complemento son $\Sigma-r.e.$.

> [!tip] Clave de Examen: El "Paralelismo" La prueba de que $S$ y $\bar{S}$ enumerables implican $S$ computable es la famosa técnica de correr dos listas en paralelo hasta que el dato aparezca en una de las dos.

### [[El Problema de la Parada (AutoHaltΣ)]]

Aquí es donde la computabilidad choca contra la pared. Esta nota contiene la demostración por contradicción (diagonalización) más famosa de la materia.

- **Definición de AutoHaltΣ:** El predicado que determina si un programa para cuando recibe su propio código como entrada.
- **Indecidibilidad de AutoHaltΣ (Lema 6):** Prueba matemática de que $AutoHalt_\Sigma$ no es una función $\Sigma-recursiva$.
- **Imposibilidad Efectiva (Teorema 7):** Aplicación de la **Tesis de Church** para concluir que no existe ningún procedimiento efectivo (ni humano ni de máquina) para decidir la parada.

### [[Los Conjuntos A y N]]

La clasificación definitiva de los problemas según su dificultad de cómputo. Fundamental para el **Combo 8**.

- **El Conjunto A (Aceptación):** Definición de $A = {P \in Pro_\Sigma : AutoHalt_\Sigma(P) = 1}$. Prueba de que $A$ es $\Sigma-r.e.$ pero no $\Sigma-recursivo$.
- **El Conjunto N (No-Aceptación):** Definición de $N = {P \in Pro_\Sigma : AutoHalt_\Sigma(P) = 0}$. Prueba de que $N$ **ni siquiera es Σ-r.e.** (no se puede listar).

> [!danger] ¡Cuidado con el Vacío! El conjunto $N$ es el ejemplo de que hay problemas que están totalmente fuera del alcance de la computabilidad: no solo no podemos decidir si un dato está ahí, sino que ni siquiera existe un programa que pueda empezar a listarlos sin colgarse para siempre.

### [[Patologías y Límites de la Minimización]]

Resultados avanzados sobre cuándo la minimización de Gödel "se rompe" o deja de ser computable.

- **Predicados recursivos con minimización no computable:** Existencia de predicados $P$ recursivos tales que $M(P)$ no es efectivamente computable.
- **Dominios no recursivos:** Ejemplo de funciones recursivas cuyo dominio no es un conjunto recursivo (como la restricción al conjunto $A$).

---



---

En esta nota clasificamos los conjuntos de programas según la posibilidad de decidir o listar su comportamiento. Esta es la aplicación directa de la indecidibilidad del _Problema de la Parada_ y marca el límite último de lo que podemos computar con cualquier modelo. Suponemos para estas definiciones que $\Sigma \supseteq \Sigma_p$ para que los programas puedan procesarse a sí mismos.

### Definición y Naturaleza de los Conjuntos

Dividimos al universo de los programas de Neumann ($Pro_\Sigma$) en dos grandes grupos basados en el predicado $AutoHalt_\Sigma$:

- **El Conjunto A (Aceptación):** Es el conjunto de programas que se detienen cuando reciben su propio código como entrada. $$A = { P \in Pro_\Sigma : AutoHalt_\Sigma(P) = 1 }$$
- **El Conjunto N (No-Aceptación):** Es el conjunto de programas que entran en un bucle infinito (se "cuelgan") al procesarse a sí mismos. $$N = { P \in Pro_\Sigma : AutoHalt_\Sigma(P) = 0 }$$

> [!success] Propiedad de A: Es $\Sigma-r.e.$ El conjunto $A$ es **recursivamente enumerable**. **Sustento:** Podemos definir una función recursiva $f = M(\lambda tP [Halt_{0,1}(t,P,P)])$. Como $Halt$ es $\Sigma-p.r.$, su minimización es una función recursiva cuyo dominio es exactamente $A$. Por el Teorema 5, ser el dominio de una función recursiva equivale a ser $\Sigma-r.e.$.

> [!danger] Propiedad de N: No es $\Sigma-r.e.$ El conjunto $N$ es el ejemplo máximo de la limitación computacional: **ni siquiera se puede listar**. **Demostración:** Si $N$ fuera enumerable, podríamos definir $AutoHalt_\Sigma$ mediante una unión de funciones por casos: usaríamos la función característica 1 sobre $A$ y la función característica 0 sobre $N$. Como ambos serían r.e., el _Lema de división por casos_ nos diría que $AutoHalt_\Sigma$ es recursivo, lo cual ya probamos que es falso.

#### Diferencias entre A y N para el Final

Es vital no confundir estos conjuntos en las preguntas teóricas del **Combo 8**:

1. **A es "listable" pero no "decidible"**: Existe un programa que puede listar todos los elementos de $A$ (si un programa para, eventualmente lo sabremos), pero no existe un programa que pueda decir "no" si un programa se cuelga.
2. **N no es nada**: No hay forma de listar programas que se cuelgan porque para saber que uno está en $N$, tendríamos que esperar tiempo infinito para estar seguros de que nunca va a parar.

> [!warning] El Dominio no garantiza Decidibilidad Estos conjuntos prueban que el dominio de una función recursiva (como $C_{0,1}^1|_A$) no siempre es un conjunto recursivo. Esto rompe la intuición de que "si hay una función, el conjunto es lindo".

### Aplicación en Ejercicios de Clasificación

Para resolver ejercicios donde te piden clasificar un conjunto $S$ de programas:

- Si podés probar que $S = A$, entonces declarás que es **$\Sigma-r.e.$ pero no recursivo**.
- Si podés probar que $S = N$, declarás que **no es ni r.e. ni recursivo**.
- Cualquier conjunto que contenga a $N$ o cuyo complemento sea $A$ suele caer en la categoría de no-enumerable.

> [!example] Ejemplo: programas que se autopropagandean El conjunto $L = {P \in Pro_\Sigma : \Psi_P(\diamond) = P}$ es no vacío por el Teorema de Recursión de Kleene, y se puede demostrar que es $\Sigma-r.e.$ usando técnicas de simulación con $Halt$ y $E$.

---


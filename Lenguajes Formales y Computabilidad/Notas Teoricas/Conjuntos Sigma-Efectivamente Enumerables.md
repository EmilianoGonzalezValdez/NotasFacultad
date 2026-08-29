
---

### La Intuición del Listador y Definición Formal

Un conjunto $S \subseteq \omega^n \times \Sigma^{*m}$ se dice **$\Sigma$-efectivamente enumerable** si existe un procedimiento efectivo capaz de "listar" o "anunciar" todos sus elementos, sin omitir ninguno. A diferencia de la decidibilidad, aquí no se exige que podamos saber en tiempo finito si un elemento _no_ está en el conjunto.

Matemáticamente, un conjunto $S$ es $\Sigma$-efectivamente enumerable si:

1. Es el conjunto vacío ($\emptyset$).
2. Existe una función $F: \omega \to \omega^n \times \Sigma^{*m}$ tal que la imagen de $F$ es exactamente $S$ ($IF = S$), y cada una de sus funciones componentes $F_{(i)}$ es **$\Sigma$-efectivamente computable**.

> [!info] El Procedimiento de Enumeración Decimos que un procedimiento $P$ **enumera** a $S$ si, partiendo de los datos de entrada $0, 1, 2, 3, \dots$, el procedimiento se detiene siempre y va devolviendo elementos $e_0, e_1, e_2, \dots$ de modo que el conjunto de todas esas salidas sea exactamente $S$. Notá que un elemento puede aparecer repetido en la lista, no hay drama con eso.

### Propiedades y Relación con la Computabilidad

La enumerabilidad es una propiedad más "débil" que la computabilidad, pero están íntimamente relacionadas por estos resultados clave:

- **Computable implica Enumerable:** Si un conjunto $S$ es $\Sigma$-efectivamente computable, entonces es $\Sigma$-efectivamente enumerable. El procedimiento es fácil: listamos todos los elementos del universo y, para cada uno, usamos el "decididor" de $S$; si dice que sí, lo sacamos por pantalla.
- **Dominios de Funciones:** El dominio de **toda** función $\Sigma$-efectivamente computable es un conjunto $\Sigma$-efectivamente enumerable. Esta es la base de por qué existen conjuntos que podés listar pero no decidir: podés listar las entradas donde la función para, pero no podés saber si en las otras se va a colgar o simplemente está tardando mucho.
- **Operaciones:** La unión y la intersección de conjuntos $\Sigma$-efectivamente enumerables producen conjuntos que también son $\Sigma$-efectivamente enumerables.

#### El Teorema de la Doble Enumerabilidad (Teorema 3)

Este es el resultado estrella del pilar y un **Combo de Teorema**. Establece el puente definitivo entre enumerar y decidir: Un conjunto $S$ es **decidible** (computable) si y solo si tanto $S$ como su complemento ($S^c$) son **efectivamente enumerables**.

> [!success] ¿Por qué funciona el Teorema 3? Si tenés un listador para los que están en $S$ y otro para los que no están ($S^c$), para saber si un dato $x$ está en $S$, ponés a correr ambos listadores en paralelo. Tarde o temprano, $x$ va a aparecer en una de las dos listas. Cuando aparezca, ya tenés la respuesta definitiva (1 o 0) y podés frenar.

#### Uso Práctico: Cómo probar que un conjunto es enumerable

Para demostrar que un conjunto $S$ es enumerable en un ejercicio, tenés que describir el "listador":

1. Tomar una entrada $x \in \omega$.
2. Usar la **codificación de infinituplas** para "desarmar" a $x$ en varios números (por ejemplo, $x_1 = (x)_1, x_2 = (x)_2$).
3. Si es necesario, transformar números a palabras usando $*_\le$.
4. Mostrar que combinando esos datos podés generar cualquier elemento de $S$.

> [!example] Ejemplo: Enumerar $\omega \times \omega$ El procedimiento recibe $x$, calcula $x_1 = (x)_1$ y $x_2 = (x)_2$, y devuelve el par $(x_1, x_2)$. Como la función de codificación es suryectiva sobre los pares, este procedimiento pasará eventualmente por todos los pares posibles de naturales.

---


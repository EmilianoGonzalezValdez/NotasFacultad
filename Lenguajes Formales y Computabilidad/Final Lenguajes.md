
---

### Combo 1: Los Cimientos de la Recursividad y el Poder de Neumann

En este combo sentamos las bases: cómo se relacionan los conjuntos con las funciones y cómo un lenguaje imperativo ($S_\Sigma$) puede "imitar" a la matemática funcional (Gödel).

#### Caracterización de conjuntos $\Sigma-p.r.$

- **Idea central**: Queremos probar que un conjunto es "lindo" ($\Sigma-p.r.$) si y solo si es el dominio de una función que también es "linda".
- **A qué apuntar**:
    - En la ida ($\implies$), simplemente definís una función característica y le aplicás el predecesor; si la función para, el elemento estaba en el conjunto.
    - En la vuelta ($\impliedby$), usás **inducción**. El caso de la composición es clave: necesitás las **extensiones totales** ($\bar{g}_i$) para asegurar que la función característica no se "cuelgue" antes de tiempo si una de las partes de la composición no está definida.

#### Neumann vence a Gödel (Caso Recursión Primitiva)

- **Idea central**: Probar que si una función se define por recursión sobre una palabra, existe un programa de Neumann que la calcula.
- **A qué apuntar**: El programa es un "comedor de palabras". Usás un bucle que mira el primer símbolo, lo borra con la **bajada** ($\text{↷}$) y aplica la macro de la función $G_a$ correspondiente. Es vital reconstruir la palabra en una variable auxiliar ($P_{m+2}$) porque $G_a$ la necesita como parámetro.

---

### Combo 2: Unificación y Enumeración

Acá el foco es cómo pegar funciones por pedazos y cómo un programa puede "escupir" todos los elementos de un conjunto.

#### Lema de división por casos ($\Sigma-p.r.$)

- **Idea central**: Si tenés varias funciones $\Sigma-p.r.$ con dominios que no se pisan (disjuntos), podés unirlas en una sola gran función $\Sigma-p.r.$.
- **A qué apuntar**: Usás el truco de la **potencia alfabética** ($\alpha^x$). Extendés las funciones a todo el universo ($\bar{f}_i$) y las multiplicás por sus funciones características. Como los dominios son disjuntos, solo una parte de la fórmula "sobrevive" (da la palabra original) y las demás se vuelven vacías ($\epsilon$).

#### Caracterización básica de conjuntos $\Sigma$-enumerables

- **Idea central**: Un conjunto se puede listar (enumerable) si y solo si hay un programa que, dándole números naturales como "índices", te devuelve todos sus elementos.
- **A qué apuntar**: En la demostración, usás el **Primer Manantial de Macros** para construir un programa que cargue los resultados de las funciones componentes en las variables de salida ($N_i, P_i$). La clave es que el programa debe cubrir todas las combinaciones posibles de la imagen.

---

### Combo 3: Gödel vence a Neumann y la Decidibilidad

Este es el "corazón" de la materia: cómo la matemática (Gödel) puede describir perfectamente lo que hace una computadora (Neumann).

#### Gödel vence a Neumann (Computable $\implies$ Recursiva)

- **Idea central**: Si un programa de Neumann puede calcular algo, existe una fórmula matemática (función recursiva) que hace lo mismo.
- **A qué apuntar**: La demostración es una construcción gigante por composición. Usás la **Función de Tiempo** ($T_{n,m}$) para saber cuándo para el programa y luego le aplicás la **Función de Estado** ($E$) para extraer el resultado de la variable $P_1$ o $N_1$. Es como sacar una foto al estado final de la memoria de la máquina.

#### Caracterización de conjuntos $\Sigma-efectivamente$ computables

- **Idea central**: Un conjunto es decidible (computable) si y solo si podés enumerar tanto al conjunto como a su complemento.
- **A qué apuntar**: Si tenés dos enumeradores (uno para el "SÍ" y otro para el "NO"), el procedimiento para decidir es poner a los dos a laburar en paralelo (usando un tiempo $T$ que aumenta) hasta que el dato aparezca en una de las dos listas.

---

### Combo 4: Operaciones y Listas

Repite la enumeración del Combo 2 y agrega la sumatoria.

#### Lema de la sumatoria

- **Idea central**: Demostrar que sumar los resultados de una función $p.r.$ en un rango acotado sigue siendo $p.r.$.
- **A qué apuntar**: Se prueba por **recursión primitiva** sobre el límite superior de la suma. Definís una función base para el caso 0 y una función de paso que agarra el acumulado y le suma el siguiente término.

---

### Combo 5: Efectividad y Cuantificación

Se centra en demostrar que nuestras herramientas lógicas no rompen la computabilidad.

#### Recursión alfabética preserva computabilidad efectiva

- **Idea central**: Si tenés procedimientos manuales (lápiz y papel) para las funciones base, podés armar un manual de instrucciones para la recursión alfabética.
- **A qué apuntar**: El procedimiento es un bucle que analiza el primer símbolo de la palabra de entrada, llama al procedimiento de la función $G$ correspondiente y repite hasta que la palabra se agota ($\epsilon$).

#### Lema de cuantificación acotada

- **Idea central**: Si un predicado es $p.r.$, entonces preguntar "¿se cumple para todos los elementos menores a $x$?" también es $p.r.$.
- **A qué apuntar**: Transformás el "para todo" ($\forall$) en una **productoria acotada** de funciones características. Si todos dan 1 (verdadero), el producto es 1. Si uno falla y da 0, todo el producto se hace 0.

---

### Combo 6: El Puente entre Dominio e Imagen

Este combo es fundamental para entender los conjuntos R.E. (recursivamente enumerables).

#### $\Sigma-efectivamente$ computable $\implies$ enumerable

- **Idea central**: Si sabés decidir si algo está en un conjunto, podés armar una lista de ese conjunto.
- **A qué apuntar**: Generás todos los elementos posibles del universo (que sabemos que es enumerable) y, para cada uno, usás el "decididor". Si te dice que está, lo ponés en la lista; si no, ponés un elemento fijo del conjunto para no dejar huecos en la secuencia.

#### Caracterización de conjuntos $\Sigma-r.e.$ (Caso $I_F \implies D_f$)

- **Idea central**: Si un conjunto es la imagen de una función, entonces es el dominio de otra.
- **A qué apuntar**: Esta es la famosa búsqueda de la **"semilla"** ($N_{20}$). El programa recibe una entrada y se queda buscando infinitamente en el espacio de todas las combinaciones posibles (tiempo $t$ e índice $k$) hasta encontrar una que, al aplicarle $F$, dé la entrada original. Si la encuentra, para (por eso es el dominio); si no, se cuelga para siempre.

---

### Combo 7: Límites y Recortes

Cómo manejar la minimización y las restricciones de dominio.

#### Lema de minimización acotada

- **Idea central**: Buscar el primer número que cumple algo es $p.r.$ **siempre que sepas que hay un techo** ($f$) donde dejar de buscar.
- **A qué apuntar**: Usás una productoria acotada para chequear todos los casos hasta el techo. Definís un predicado auxiliar $P_1$ que vale 1 solo para el primer $t$ que cumple la propiedad, asegurando que encontrás el mínimo.

#### Lema de restricción de funciones

- **Idea central**: Si una función es recursiva y le achicás el dominio a un conjunto R.E., el resultado sigue siendo recursivo.
- **A qué apuntar**: Usás el enumerador del conjunto $S$ para filtrar. El programa se queda buscando qué índice del enumerador produce la entrada actual; cuando lo encuentra, aplica la función original.

---

### Combo 8: El Caos y el Orden (Halting y Minimización)

El combo más dramático: la prueba de que hay cosas que las computadoras no pueden hacer, y cómo programar la búsqueda de un mínimo.

#### Undecidibilidad de AutoHalt

- **Idea central**: No existe un programa que pueda decir si **cualquier** programa (incluido él mismo) va a parar o no.
- **A qué apuntar**: Se prueba por **contradicción (diagonalización)**. Suponés que existe el macro `AutoHalt`. Construís un programa "rebelde" que, si el macro dice que para, él entra en un bucle infinito; y si el macro dice que no para, él se detiene. Al correr este programa con su propio código, el macro miente sí o sí.

#### Neumann vence a Gödel (Caso Minimización)

- **Idea central**: El constructor de minimización de Gödel equivale a un bucle `while` en Neumann.
- **A qué apuntar**: El programa es un contador que empieza en 0 y va subiendo de a uno, chequeando el predicado $P$ con una macro en cada paso. El primer valor que hace que el macro salte al label de salida es el mínimo.

---

### Combo 9: El Cierre de los Paradigmas

Repite la división por casos (pero para funciones recursivas) y Gödel vence a Neumann.

#### Lema de división por casos ($\Sigma-recursivas$)

- **Idea central**: Similar al de $p.r.$, pero ahora la construcción es imperativa porque las funciones recursivas pueden ser parciales.
- **A qué apuntar**: Usás un **reloj global** ($N_{20}$) que va aumentando. En cada paso, simulás ambas funciones por esa cantidad de tiempo. La primera que termine "gana" y da el resultado. Esto maneja el problema de que una de las funciones podría no parar nunca.

---


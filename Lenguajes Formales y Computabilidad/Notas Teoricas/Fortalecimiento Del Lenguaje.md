
---

### Simulación Controlada y Enumeración de Dominios

Gracias al **Segundo Manantial de Macros**, podemos usar el predicado $Halt_{n,m}$ (que es $\Sigma$-recursivo primitivo) dentro de cualquier programa de $S_\Sigma$. Esto permite resolver el problema de la "parcialidad": si intentamos correr un programa que no sabemos si termina, nuestro propio programa podría colgarse. El uso de $Halt$ nos permite "testear" la ejecución durante un tiempo $t$ finito sin riesgo de quedar atrapados en un bucle infinito.

#### Procedimiento para Enumerar Dominios ($Df$)

Para enumerar el dominio de una función computable $f$ (computada por un programa $P_0$), aplicamos la técnica de **búsqueda en espacio y tiempo**:

1. Recibimos un dato $x \in \omega$ como "semilla".
2. Descomponemos $x$ usando macros de **bajadas de primos**: $x_1 = (x)_1$ (el candidato a estar en el dominio) y $t = (x)_2$ (el tiempo de prueba).
3. Usamos el macro `[IF Halt(t, x1, P0) GOTO L1]`.
    - Si el macro dice **SÍ**: El programa $P_0$ termina con la entrada $x_1$ en $t$ pasos. Entonces $x_1$ pertenece a $Df$. El programa devuelve $x_1$ como salida válida.
    - Si el macro dice **NO**: No podemos asegurar nada. Para que el enumerador sea total (y cumpla la definición), devolvemos un elemento fijo que sepamos que está en el dominio (ej. 0 si $0 \in Df$).

> [!tip] Clave para la práctica En los ejercicios de enumeración de dominios o imágenes, siempre usás la variable de entrada como un "índice" que contiene tanto el dato como el tiempo. Así te asegurás de recorrer todos los pares posibles $(dato, tiempo)$ y no colgarte nunca.

### Enumeración de Conjuntos de Programas

Los programas de $S_\Sigma$ son palabras del alfabeto $\Sigma \cup \Sigma_p$. Esto nos permite tratarlos como datos de entrada para _otros_ programas escritos en un lenguaje con un alfabeto un poco más grande: $S_{\Sigma \cup \Sigma_p}$.

#### Análisis de Propiedades de Programas

Podemos construir programas que decidan o enumeren subconjuntos de $Pro_\Sigma$ basándose en su comportamiento.

- **Procedimiento:** Se utiliza un orden total $\le$ sobre $\Sigma \cup \Sigma_p$ y la función $*_\le$ para generar sistemáticamente todas las palabras posibles.
- **Filtro:** Para cada palabra generada, se chequea con un macro `[IF P ∈ ProΣ GOTO ...]` (que es p.r.) si es un programa válido. Luego se testea su comportamiento con $Halt$ y $E$.

> [!example] Ejemplo: Conjunto de programas que dan 10 Para enumerar ${P \in Pro_\Sigma : \Psi_P(10) = 10}$, el programa genera un candidato $P$, prueba si termina con entrada 10 en $t$ pasos, y si termina, chequea si la variable de salida $N1$ vale 10 usando el macro del extractor de estado $E_{1,0,1}^{\#}$.

### Autorreferencia y Teoremas de Recursión

Cuando el alfabeto $\Sigma$ es lo suficientemente grande ($\Sigma \supseteq \Sigma_p$), un programa puede recibir su propio código como entrada alfabetica. Esto da lugar a comportamientos "reflexivos".

#### Programas que se Autopropagandean

Existen programas que, sin recibir datos de entrada (desde el estado $| \diamond |$), terminan devolviendo su propio código fuente como salida.

- **Teorema de la Recursión de Kleene:** Garantiza la existencia de un programa $P$ tal que $\Psi_P(\diamond) = P$.
- **Teorema de la Recursión Doble (Smullyan):** Garantiza que existen pares de programas $(P_1, P_2)$ que pueden "hablar" entre sí, por ejemplo, que ambos devuelvan la concatenación $P_1 P_2$.

> [!danger] El Conjunto A Se define $A = {P \in Pro_\Sigma : \text{P para con la entrada } |P| }$. Este conjunto es el corazón de la limitación de la computabilidad. Es **enumerable** (podemos usar la técnica de $Halt$ para listarlos), pero no es **computable** (no hay un programa que diga "no" con seguridad si un programa se va a colgar).

---


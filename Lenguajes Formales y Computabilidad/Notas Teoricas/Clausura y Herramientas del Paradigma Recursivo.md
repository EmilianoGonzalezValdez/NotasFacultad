
---
### División por Casos para Funciones $\Sigma$-recursivas

Este resultado establece que si una función se define "por tramos" donde cada tramo es una función $\Sigma$-recursiva y los dominios son conjuntos recursivos disjuntos, el resultado final sigue siendo una función **$\Sigma$-recursiva**.

**Teoría y Procedimiento:** Sean $f_1, \dots, f_k$ funciones $\Sigma$-recursivas con dominios $Df_1, \dots, Df_k$ disjuntos de a pares ($Df_i \cap Df_j = \emptyset$). La función unión $f = f_1 \cup \dots \cup f_k$ definida como: $$f(e) = \begin{cases} f_1(e) & \text{si } e \in Df_1 \ \vdots & \ f_k(e) & \text{si } e \in Df_k \end{cases}$$ es $\Sigma$-recursiva.

Para demostrarlo (y resolver ejercicios), se utiliza un **programa de Neumann** que implementa una búsqueda sistemática en el tiempo. El procedimiento es:

1. Se inicializa una variable de tiempo $T = 0$.
2. En un bucle, se incrementa $T$ y se testea mediante el macro del predicado de parada acotada $Halt_{n,m}$ si alguno de los programas $P_i$ (que computan las funciones $f_i$) termina en exactamente $T$ pasos.
3. Como los dominios son disjuntos, a lo sumo uno de los programas terminará.
4. Si el macro de $Halt$ para un $P_i$ da 1, se invoca el macro de la función $f_i$ y se devuelve el resultado.

> [!info] Importancia de la Disjuntez La condición de que los dominios sean disjuntos es vital para que la función esté bien definida. El uso de la variable de tiempo $T$ asegura que el programa no se "cuelgue" testeando una función que no termina, ya que $Halt$ (con tiempo acotado) siempre es recursivo primitivo.

### Restricción de Funciones $\Sigma$-recursivas a Conjuntos $\Sigma$-r.e.

Este lema permite "filtrar" el dominio de una función recursiva manteniendo su carácter recursivo, siempre que el nuevo dominio sea, al menos, enumerable.

**Teoría y Procedimiento:** Si $f: Df \to O$ es $\Sigma$-recursiva y $S \subseteq Df$ es un conjunto $\Sigma-r.e.$, entonces la restricción $f|_S$ es una función **$\Sigma$-recursiva**.

Para resolver ejercicios o realizar la prueba, se asume que $S$ es la imagen de una función recursiva $F$ (por definición de $\Sigma-r.e.$). El programa que computa $f|_S$ sigue estos pasos:

1. Recibe la entrada $e$.
2. Inicia un bucle sobre una variable $x = 0, 1, 2, \dots$ buscando si existe un índice tal que $F(x) = e$.
3. Como $F$ es recursiva, se utilizan macros para calcular sus valores.
4. Si el programa encuentra que $e$ es efectivamente un elemento de la imagen de $F$ (y por ende $e \in S$), entonces procede a aplicar el macro de la función original $f$ sobre $e$ y devuelve el resultado.

> [!warning] El riesgo del bucle Si $e \notin S$, el programa se quedará buscando en el bucle de la imagen de $F$ para siempre. Esto es correcto, ya que el dominio de la función restringida $f|_S$ debe ser precisamente $S$.

### Propiedades de Clausura de Conjuntos $\Sigma$-recursivos y $\Sigma$-r.e.

Los conjuntos recursivos (decidibles) y los recursivamente enumerables (listables) presentan propiedades de clausura bajo operaciones de conjuntos.

- **Conjuntos $\Sigma$-recursivos:** Son cerrados bajo **unión, intersección y complemento** (o resta de conjuntos). Esto se debe a que las operaciones lógicas ($\vee, \wedge, \neg$) sobre sus funciones características (que son $\Sigma$-recursivas totales) preservan la recursividad.
- **Conjuntos $\Sigma$-r.e.:** Son cerrados bajo **unión e intersección**.
    - _Unión:_ Se prueba corriendo los dos enumeradores y alternando sus salidas.
    - _Intersección:_ Se prueba mediante un programa que filtra elementos que aparecen en ambas listas.

> [!tip] Relación entre tipos de conjuntos Todo conjunto $\Sigma-recursivo$ es automáticamente $\Sigma-r.e.$, pero la recíproca no es cierta (lo veremos con el conjunto $A$).

---

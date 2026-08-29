
---
### Los Ladrillos de la Materia: Alfabetos y Palabras

Para empezar a formalizar la computabilidad, primero tenemos que definir sobre qué "suelo" nos paramos. En esta materia, todo proceso ocurre sobre un alfabeto y genera palabras.

- **Alfabeto ($\Sigma$):** Es un conjunto finito de símbolos. Por ejemplo, $\Sigma = {0, 1}$ o $\Sigma = {a, b, c}$. Incluso el conjunto vacío $\emptyset$ puede ser un alfabeto.2
- **Palabras ($\Sigma^*$):** Es el conjunto de todas las sucesiones finitas de símbolos tomados de $\Sigma$.
    - **Palabra vacía ($\epsilon$):** Es la única palabra que no tiene símbolos, por lo tanto su longitud es cero ($|\epsilon| = 0$).
    - **Longitud ($|\alpha|$):** Es la cantidad de símbolos que componen la palabra $\alpha$.
    - **Ocurrencias ($|\alpha|_\sigma$):** Cantidad de veces que aparece el símbolo $\sigma$ en la palabra $\alpha$.

> [!success] Propiedad de Inclusión Como las palabras de longitud 1 son exactamente los símbolos del alfabeto, se cumple que $\Sigma \subseteq \Sigma^*$. Además, $\epsilon \in \Sigma^*$ siempre, incluso si el alfabeto es vacío ($\emptyset^* = {\epsilon}$).

#### Operaciones y Estructura de Palabras

- **Concatenación:** Si tenemos $\alpha_1, ..., \alpha_n \in \Sigma^*$, su "unión" se escribe $\alpha_1...\alpha_n$. Si todas son la misma palabra $\alpha$, usamos la potencia $\alpha^n$ (donde $\alpha^0 = \epsilon$).
- **Tramo Inicial y Final:** $\beta$ es un tramo inicial de $\alpha$ si hay una palabra $\gamma$ tal que $\alpha = \beta\gamma$.
- **Subpalabra:** $\alpha$ es subpalabra de $\beta$ si existen palabras $\delta, \gamma$ tales que $\beta = \delta\alpha\gamma$.
- **Recíproca ($\gamma^R$):** Es la palabra escrita al revés.

> [!note] Notación de posición $[\alpha]_i$ Usamos $[\alpha]_i$ para el $i$-ésimo símbolo de $\alpha$. Si $1 \le i \le |\alpha|$, devuelve el símbolo; en cualquier otro caso, devuelve $\epsilon$.

### El Universo Matemático Orientado a Objetos

En esta materia somos muy estrictos con los "tipos" de datos. Para evitar errores en las demostraciones de los combos y en la programación, dividimos todo lo que existe en categorías **disjuntas**.

Para identificar a qué categoría pertenece algo, usamos la función **Tipo ($Ti$)**:

1. **NUMERO ($\omega$):** Los naturales y el cero.
2. **CONJUNTO:** Como $\mathbb{N}, \omega, \emptyset$ o $\mathcal{P}(\mathbb{N})$.
3. **PALABRA:** Incluye a $\epsilon$, símbolos y cadenas de $\Sigma^*$.
4. **0-UPLA ($\diamond$):** Objeto único que representa una secuencia vacía de elementos.
5. **n-UPLA:** Pares ordenados $(a, b)$, ternas, etc., para $n \ge 2$.
6. **INFINITUPLA:** Sucesiones infinitas $(a_1, a_2, \dots)$.

> [!danger] ¡Prohibido Mezclar! Como estas categorías son disjuntas, **nunca** un número es una palabra, ni una palabra es un conjunto. Por lo tanto, se cumplen estas desigualdades fundamentales: $$0 \neq \emptyset \neq \epsilon \neq \diamond$$ Aunque todos representen una idea de "nada", son objetos de distinta naturaleza técnica.

> [!example] Ejemplos de la función Ti
> 
> - $Ti(\pi) = \text{NUMERO}$.
> - $Ti(\emptyset) = \text{CONJUNTO}$.
> - $Ti(\epsilon) = \text{PALABRA}$.
> - $Ti(\diamond) = \text{0-UPLA}$.

#### Numerales vs. Números

Es vital no confundir el **concepto matemático** de un número con el **símbolo** que usamos para escribirlo.

- **Números:** Son entes abstractos (el número diez).
- **Numerales ($Num$):** Son los símbolos ${0, 1, 2, 3, 4, 5, 6, 7, 8, 9}$.
- **Importancia:** El numeral `5` es una **palabra** de longitud 1, mientras que el número $5$ es un **número**. Por definición, $Num \cap \omega = \emptyset$.

> [!info] Notación Visual En los textos podemos ver numerales comunes ($5$), numerales **bold** ($\mathbf{5}$) o numerales _itálicos_ ($5$). Son todos símbolos (palabras) distintos entre sí.

---

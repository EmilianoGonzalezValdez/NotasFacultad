 
## Estados y Descripciones Instantáneas

La semántica de $S_\Sigma$ formaliza el comportamiento de un programa durante su ejecución. Mientras que la sintaxis nos dice cómo escribir instrucciones, la semántica describe cómo esas instrucciones modifican la "memoria" (el **Estado**) y cómo evoluciona el control del programa (la **Descripción Instantánea**).

### El Estado y la Representación de Memoria

En el paradigma de Neumann, el **Estado** representa el contenido de todas las variables en un momento preciso de la computación. Matemáticamente, un estado es un par de infinituplas $(s⃗, σ⃗) = ((s_1, s_2, \dots), (\sigma_1, \sigma_2, \dots))$ que pertenecen a los conjuntos $\omega[N]$ y $\Sigma^*[N]$.

- **Variables Numéricas:** $s_i$ representa el contenido de la variable $N\bar{i}$. Casi todas las variables tienen valor 0, excepto una cantidad finita.
- **Variables Alfabéticas:** $\sigma_i$ representa el contenido de la variable $P\bar{i}$. Casi todas las variables contienen la palabra vacía $\epsilon$, excepto una cantidad finita.

> [!note] Propiedad de Finitud Aunque el modelo usa infinituplas para simplificar el formalismo matemático, en la práctica cualquier programa solo involucra una cantidad finita de variables.

### Descripciones Instantáneas (DI) y Dinámica de Cómputo

Una **Descripción Instantánea (DI)** es una "foto" completa del sistema en un instante de tiempo $t$. Se representa como una terna $(i, s⃗, σ⃗) \in \omega \times \omega[N] \times \Sigma^*[N]$.

- **Puntero de Instrucción ($i$):** El primer componente indica qué instrucción del programa $P$ se debe realizar a continuación (la instrucción $I_P^i$).
- **Estado Actual ($s⃗, σ⃗$):** Los otros dos componentes representan los valores almacenados en la memoria en ese instante.

La **computación** de un programa $P$ partiendo de un estado $(s⃗, σ⃗)$ es la sucesión infinita de DIs generada a partir de $(1, s⃗, σ⃗)$. Cada paso de esta sucesión representa la ejecución de una instrucción.

### Función Sucesora $S_P$ y el Verbo "Realizarp"

La evolución de una DI a la siguiente está regida por la **Función Sucesora $S_P$**. Esta función toma una DI y devuelve la DI resultante de ejecutar la instrucción correspondiente. Para definirla, se utiliza el concepto técnico de **realizarp** (realizar si se puede).

La definición matemática de $S_P(i, s⃗, σ⃗)$ se divide en dos grandes escenarios:

1. **Instrucción Válida ($i \in {1, \dots, n(P)}$):** La función aplica el efecto de la instrucción $I_P^i$ sobre el estado y actualiza el puntero $i$. Por ejemplo:
    - Si es una **asignación** ($Nk \leftarrow Nk+1$), el puntero pasa a $i+1$ y se modifica la celda $s_k$ del estado.
    - Si es un **salto condicional efectivo**, el puntero $i$ cambia al menor label $l$ que coincida con el destino del salto.
2. **Puntero fuera de rango ($i \notin {1, \dots, n(P)}$):** Si el puntero señala una instrucción que no existe (como 0 o un valor mayor a la longitud del programa), la función sucesora devuelve la misma DI: $S_P(i, s⃗, σ⃗) = (i, s⃗, σ⃗)$. En este caso, la máquina "se queda patinando" en el mismo lugar.

#### Detención del Programa

Un programa $P$ **se detiene** partiendo de un estado inicial si, en algún paso $t$ de la computación, la primera coordenada de la DI (el puntero de instrucción) alcanza exactamente el valor $n(P) + 1$.

- Esto significa que el programa ha terminado de ejecutar su última instrucción de forma secuencial y "cae" fuera del código.
- Si el programa entra en un bucle infinito (por ejemplo, con un `GOTO` que vuelve atrás constantemente), nunca alcanzará el valor $n(P)+1$ y se dice que **no se detiene**.

> [!tip] Visualización de Trazas Para resolver ejercicios de ejecución, se recomienda escribir la DI inicial y aplicar $S_P$ paso a paso, anotando cómo cambia la variable afectada y el índice de la próxima instrucción. Si el índice llega a ser la cantidad de líneas + 1, el programa terminó.

---

**Glosario de Semántica**

- **Estado:** Par de infinituplas con los datos de la memoria.
- **DI:** Terna que une el puntero de instrucción con el estado actual.
- **$S_P$:** Función que computa el siguiente paso de ejecución.
- **Realizarp:** Ejecutar una instrucción solo si es sintácticamente posible.


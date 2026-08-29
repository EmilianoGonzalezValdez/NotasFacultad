
---
### Neumann vence a Gödel (RΣ ⊆ Computables)

Este teorema es el primer gran paso para unificar los modelos. Establece que **toda función $\Sigma$-recursiva es $\Sigma$-computable**. En criollo: si Gödel puede definir una función con sus constructores, Neumann puede escribir un programa en $S_\Sigma$ que la calcule.

La demostración se hace por **inducción** sobre la complejidad de la función $h$ (basada en el conjunto $R_{\Sigma, k}$). El caso base ($k=0$) son las funciones iniciales, que ya sabemos que son computables. Para el paso inductivo, tenemos que ver cómo Neumann simula los constructores de Gödel.

#### Simulación de la Minimización (Caso h = M(P))

Si tenemos una función definida por minimización $h = M(P)$, y por hipótesis inductiva el predicado $P$ es computable, Neumann lo resuelve con un **bucle de búsqueda**.

- **Procedimiento:** Se usa una variable (por ejemplo $N_{n+1}$) que arranque en 0 y se va testeando el predicado $P$ mediante un macro. Si el macro dice que no se cumple, se aumenta la variable y se vuelve a probar.
- **Programa en $S_\Sigma$:**
    
    ```
    L2 [ IF P(Nn+1, N1, ..., Nn, P1, ..., Pm) GOTO L1 ]
       Nn+1 ← Nn+1 + 1
       GOTO L2
    L1 N1 ← Nn+1
    ```
    

> [!info] Lógica del Bucle Este programa se queda "colgado" si el predicado nunca vale 1, lo cual es perfecto porque en ese caso el dominio de la minimización de Gödel también es indefinido.

#### Simulación de la Recursión (Caso h = R(f, G))

Para funciones definidas por recursión (por ejemplo, sobre variable alfabética), Neumann usa un programa que **descompone el dato** y va aplicando las funciones de paso.

- **Procedimiento:** El programa primero calcula el caso base con $f$ y guarda el resultado. Luego, mediante un bucle, va analizando los símbolos de la palabra que comanda la inducción (usando `IF BEGINS a`). Por cada símbolo, aplica el macro de la función de paso $G_a$ correspondiente y actualiza el resultado acumulado.

> [!example] Ejemplo de Simulación Si la función es $h(t, x) = t+x$, el programa de Neumann simularía la inducción sumando de a uno ($Suc$) una cantidad $t$ de veces sobre el valor inicial $x$.

#### El Segundo Manantial de Macros

Como consecuencia directa de que Neumann vence a Gödel, surge una herramienta práctica fundamental: el **Segundo Manantial de Macros**.

- **Teoría:** Si una función $f$ (o predicado $P$) es **$\Sigma$-recursiva**, entonces existe legalmente un macro en $S_\Sigma$ para usarla como si fuera una instrucción básica.
- **Uso en ejercicios:** Esto te permite meter en tus programas cualquier cosa que ya hayas probado que es recursiva (como la suma, el producto, el factorial, la bajada de un número primo $(x)_i$, etc.) sin tener que escribir todo el código de nuevo.

> [!tip] Diferencia entre Manantiales
> 
> - **Primer Manantial:** Macros para funciones que sabés que son _computables_ (vía programas).
> - **Segundo Manantial:** Macros para funciones que sabés que son _recursivas_ (vía Gödel). Gracias a las batallas, ¡ahora podés usar los dos!

---

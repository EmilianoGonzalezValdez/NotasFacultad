
---
### De Reconocedor a Calculadora: La MT con Unit

Para que una Máquina de Turing pueda procesar funciones $\Sigma$-mixtas (que involucran números naturales $\omega$), necesitamos una forma de representar esos números en la cinta, ya que originalmente la cinta solo entiende símbolos de un alfabeto.

Para esto introducimos el **Símbolo Unit ($p$)**. Una _Máquina de Turing con unit_ se define formalmente como una 8-upla $M = (Q, \Sigma, \Gamma, \delta, q_0, B, p, F)$, donde sumamos este símbolo especial $p \in \Gamma - ({B} \cup \Sigma)$.

> [!note] Representación de Números En este modelo, el número natural $x$ se representa en la cinta mediante el símbolo $p$ repetido $x$ veces. Si $x = 0$, se representa con la palabra vacía $\epsilon$. Esto permite que la máquina "cuente" posiciones o cantidades de forma mecánica.

### Definición de Función Σ-Turing computable

Decimos que una función mixta $f$ es **$\Sigma$-Turing computable** si existe una MT con unit que sea capaz de transformar una configuración inicial con los datos de entrada en una configuración final que contenga el resultado.

#### Configuración Inicial Estándar

Para que el cómputo sea válido, la máquina debe arrancar siempre de la misma forma. Si la función recibe $n$ números y $m$ palabras, la cinta debe empezar así: $$\lfloor q_0 B \text{ } p^{x_1} B \dots B p^{x_n} B \alpha_1 B \dots B \alpha_m \rfloor$$ Esto significa que el cabezal ($q_0$) empieza leyendo un blanco ($B$), y luego vienen todos los argumentos separados por blancos.

#### El Resultado según el Tipo de Salida

Dependiendo de qué devuelva la función ($s$), la máquina debe terminar de una forma específica:

- *_Salida Alfabética ($s = *$):__ La máquina debe detenerse alcanzando una DI final de la forma $\lfloor p B f(\vec{x}, \vec{\alpha}) \rfloor$.
- **Salida Numérica ($s = \#$):** La máquina debe detenerse alcanzando una DI final de la forma $\lfloor p B p^{f(\vec{x}, \vec{\alpha})} \rfloor$.

> [!important] Requisitos de Éxito y Fracaso
> 
> 1. **Convergencia:** Si la entrada está en el dominio ($Df$), la máquina **debe detenerse** en un estado $p \in Q$ con el formato de salida correcto.
> 2. **Divergencia:** Si la entrada **no** está en el dominio, la máquina **no debe detenerse nunca**.
> 3. **Detención Final:** Se considera que la máquina terminó de calcular cuando llega a la DI final y ya no hay más transiciones posibles (el par $(p, B)$ no está en el dominio de $\delta$ o pide un movimiento $L$ imposible).

### Procedimiento Práctico para Ejercicios

Cuando tengas que diseñar una MT que compute una función (como $Suc$ o $Sum$):

1. **Limpieza:** Lo primero que suele hacer la máquina es moverse hacia la derecha para encontrar los datos.
2. **Procesamiento:** Manipular los símbolos $p$ y los símbolos de $\Sigma$ según la lógica de la función.
3. **Formateo de Salida:** Al terminar, la máquina debe "borrar" los datos sobrantes y dejar solo el resultado precedido por un blanco y un estado de detención, respetando los formatos $\lfloor p B f \dots \rfloor$ o $\lfloor p B p^f \dots \rfloor$.

> [!example] Ejemplo: Función Sucesor ($Suc$) Para computar $Suc(x) = x+1$:
> 
> 1. Arranca en $q_0 B p^x$.
> 2. La máquina viaja hasta el final de la secuencia de $p$'s.
> 3. Agrega un símbolo $p$ adicional.
> 4. Vuelve al principio, se posiciona antes del primer blanco y se detiene.
> 5. Resultado final en cinta: $B p^{x+1}$ (con el estado correspondiente).

---

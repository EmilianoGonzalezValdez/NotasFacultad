
---

### El Criterio de Aceptación: Alcance de Estado Final

En el paradigma de Turing, una palabra se considera "aceptada" si la máquina, partiendo de una configuración inicial estándar, logra entrar en un **estado final** ($q \in F$). No importa qué símbolos queden en la cinta ni dónde esté el cabezal al terminar; lo único que cuenta es haber "pisado" un estado del conjunto $F$.

#### Definición Matemática de Aceptación

Dada una MT $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$, decimos que una palabra $\alpha \in \Sigma^*$ es **aceptada** por $M$ si existe una descripción instantánea $d \in Des$ tal que:

1. **Configuración Inicial:** El cómputo arranca desde $\lfloor q_0 B \alpha \rfloor$.
2. **Procesamiento:** Se llega a $d$ tras una cantidad finita de pasos ($\lfloor q_0 B \alpha \rfloor \vdash^* d$).
3. **Estado de Éxito:** El estado contenido en esa DI final pertenece a los estados finales ($St(d) \in F$).

> [!info] ¿Qué es St(d)? La función **Estado ($St$)** devuelve el único símbolo del conjunto de estados $Q$ que ocurre en la palabra que forma la descripción instantánea $d$.

### El Lenguaje aceptado L(M)

El conjunto de todas las palabras que cumplen el criterio anterior se denomina **Lenguaje aceptado por $M$** y se denota como $L(M)$: $$L(M) = { \alpha \in \Sigma^* : \alpha \text{ es aceptada por } M \text{ por alcance de estado final} }$$

#### Comportamiento ante palabras NO aceptadas

Si una palabra $\alpha$ no pertenece a $L(M)$, pueden pasar dos cosas:

- **Detención en estado no final:** La máquina llega a una configuración de la cual no puede salir (se detiene), pero el estado actual $q \notin F$.
- **Cómputo infinito:** La máquina entra en un bucle y nunca se detiene. En este caso, como nunca alcanza un estado final, la palabra tampoco es aceptada.

> [!tip] La configuración inicial estándar Notá que la definición matemática exige que la cinta arranque con un blanco ($B$) seguido de la palabra de entrada: $\lfloor q_0 B \alpha \rfloor$. Esto garantiza que el cabezal siempre empiece leyendo el primer símbolo de la palabra (o un blanco si la palabra es $\epsilon$).

> [!example] Ejemplo de Aceptación Si tenemos $F = {q_f}$ y la máquina realiza el cómputo $q_0 B ab \vdash a q_1 b \vdash a b q_f$, la palabra $ab$ pertenece a $L(M)$ porque el estado final de la última DI es $q_f \in F$.

---

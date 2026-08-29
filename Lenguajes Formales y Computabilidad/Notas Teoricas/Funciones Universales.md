
---
### La Foto de la Computación en el Tiempo $t$

Para que el paradigma de Gödel pueda demostrar que es tan potente como el de Neumann, necesita herramientas para describir el estado de un programa en cualquier momento. Definimos funciones que actúan como una "cámara de fotos" que captura la _Descripción Instantánea_ (DI) luego de que el programa $P$ haya ejecutado exactamente $t$ pasos.

Estas funciones reciben como entrada el tiempo $t$, los datos de entrada $(\vec{x}, \vec{\alpha})$ y el código del programa $P$.

- **Función de Instrucción ($i_{n,m}$):** $i_{n,m}(t, \vec{x}, \vec{\alpha}, P)$ devuelve el número de la instrucción que toca ejecutar después del paso $t$. Si el programa ya terminó, devuelve $n(P)+1$.
- **Funciones de Estado ($E_{n,m,j}^{#}$ y $E_{n,m,j}^{*}$):** Devuelven el contenido de la variable número $j$ (ya sea numérica o alfabética) tras $t$ pasos.

> [!success] Propiedad de Recursividad Primitiva Las funciones $i_{n,m}$ y $E_{n,m,j}$ son **$(\Sigma \cup \Sigma_p)$-recursivas primitivas** ($p.r.$). **¿Por qué?** Porque simular un único paso de un programa es una tarea mecánica simple que no tiene riesgo de bucle infinito; simplemente es aplicar la función $S_P$ una cantidad finita de veces.

### El Predicado de Parada Acotada ($Halt_{n,m}$)

Es el predicado más importante para las demostraciones de este pilar. Determina si un programa $P$ se ha detenido en **exactamente** $t$ pasos partiendo de una entrada dada.

$$Halt_{n,m} = \lambda t \vec{x} \vec{\alpha} P [i_{n,m}(t, \vec{x}, \vec{\alpha}, P) = n(P) + 1]$$

- **Propiedad:** Es un predicado **$(\Sigma \cup \Sigma_p)-p.r.$**.
- **Uso Práctico:** Al ser recursivo primitivo, siempre nos da una respuesta (1 o 0) en tiempo finito. Es la herramienta que usamos en los ejercicios de "Enumerar conjuntos" para preguntar: "¿Este programa ya terminó en este tiempo $t$?".

### El Tiempo de Detención ($T_{n,m}$)

Si queremos saber _cuánto_ tarda un programa en terminar (sin fijar un tiempo $t$ de antemano), usamos el operador de minimización sobre el predicado $Halt$.

$$T_{n,m} = M(Halt_{n,m}) = \lambda \vec{x} \vec{\alpha} P [min_t Halt_{n,m}(t, \vec{x}, \vec{\alpha}, P)]$$

> [!danger] La Diferencia Crucial A diferencia de $Halt$, la función $T_{n,m}$ **no es recursiva primitiva**, pero sí es **$\Sigma$-recursiva**. **Procedimiento en Ejercicios:** Si un programa nunca termina, $T_{n,m}$ se queda buscando el tiempo $t$ para siempre y queda indefinida. Esto es lo que permite que las funciones recursivas capturen la "parcialidad" de los programas que se cuelgan.

#### Aplicación: La Función Universal $\Psi$

Gracias a estas funciones, podemos expresar el resultado de cualquier programa $P$ como una simple composición de funciones recursivas:

1. Buscamos el tiempo de parada: $t = T_{n,m}(\vec{x}, \vec{\alpha}, P)$.
2. Sacamos la foto de la variable de salida en ese tiempo: $E_{n,m,1}(t, \vec{x}, \vec{\alpha}, P)$.

Esta construcción es la base de la prueba del **Combo 3 y 9**: "Gödel vence a Neumann".

---


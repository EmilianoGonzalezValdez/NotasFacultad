
# Método de aceptación y rechazo

El **método de aceptación y rechazo** es una de las herramientas más potentes y universales en simulación. Funciona como una "red de seguridad" cuando el método de la transformada inversa falla porque la función de distribución acumulada es imposible o muy costosa de invertir analíticamente. Su lógica se basa en un esquema de **ensayo y error** controlado: generamos un valor de una variable "fácil" y decidimos si nos sirve para nuestra variable "difícil" mediante un segundo sorteo aleatorio.

### Aceptación y rechazo en el caso discreto

Para generar una variable aleatoria $X$ con probabilidades $p_j$, necesitamos una variable de **soporte** $Y$ con probabilidades $q_j$ que ya sepamos simular. La condición fundamental es que exista una constante $c \geq 1$ tal que cubra a nuestra variable objetivo: $$\frac{p_j}{q_j} \leq c \text{ para todo } j \text{ donde } p_j > 0$$.

El algoritmo funciona de la siguiente manera:

1. **Simular** un valor de la variable de soporte $Y$.
2. **Generar** una uniforme $U \sim U(0,1)$ independiente.
3. **Evaluar la condición:** Si $U < \frac{p_Y}{c \cdot q_Y}$, aceptamos el valor y devolvemos $X = Y$.
4. Si no se cumple, **rechazamos** y volvemos al paso 1.

> [!NOTE] La eficiencia del método es clave: el número de intentos hasta obtener una aceptación sigue una **distribución geométrica** con media $c$. Por eso, en los ejercicios siempre buscamos la cota $c$ más pequeña posible para minimizar los rechazos.

> [!TIP] Si tenés una variable con muchos valores y probabilidades parecidas, usar una **uniforme discreta** como soporte suele ser mucho más eficiente que una búsqueda lineal en tablas de probabilidad acumulada.

### Aceptación y rechazo en el caso continuo

En el mundo continuo, el razonamiento es idéntico pero trabajando con funciones de densidad $f(x)$ (objetivo) y $g(y)$ (soporte). Buscamos una constante $c$ tal que $\frac{f(y)}{g(y)} \leq c$ para todo el dominio.

Para resolver ejercicios de este tipo, el paso más difícil suele ser encontrar la **cota mínima $c$**. El procedimiento recomendado es:

1. Definir la función de cociente $h(x) = \frac{f(x)}{g(x)}$.
2. Hallar los **puntos críticos** calculando la derivada $h'(x) = 0$.
3. Evaluar $h(x)$ en esos puntos y en los extremos del dominio para encontrar el valor máximo absoluto, que será nuestra $c$.

#### La Normal Estándar por rechazo

Como la acumulada de la Normal ($\Phi$) no se puede invertir, un método clásico es generar $|Z|$ usando una **exponencial** $E(1)$ como soporte.

- Se calcula la cota óptima $c = \sqrt{2e/\pi} \approx 1.32$.
- El algoritmo acepta $Y \sim E(1)$ si $U \leq \exp(-(Y-1)^2/2)$.
- Finalmente, se le asigna un signo aleatorio $(\pm)$ con probabilidad $0.5$ para obtener la $Z \sim N(0,1)$ completa.

#### Optimización por compresión (Squeezing)

Cuando las funciones $f(x)$ son muy complejas de calcular (muchos logaritmos o potencias), se usa el **squeezing**. Consiste en definir un **rectángulo de aceptación segura** $[u_1, u_2] \times [0, v_1]$ que esté por debajo de la curva de densidad.

- **Vía rápida:** Si el punto generado cae dentro del rectángulo, aceptamos el valor **instantáneamente** sin hacer cuentas difíciles.
- Si cae fuera pero bajo la curva, hacemos el cálculo completo.

> [!EXAMPLE] En la simulación de una $Gamma(3/2, 1)$, el uso de un rectángulo de compresión permite que en casi la mitad de las iteraciones la computadora se ahorre el cálculo de raíces y exponenciales.

---

#### Mini-glosario

- **Soporte ($g$):** Distribución conocida y fácil de simular que usamos como "molde".
- **Cota $c$:** Factor que escala al soporte para que siempre esté por encima de la función objetivo; representa el promedio de intentos por éxito.
- **Squeezing:** Técnica de optimización geométrica para evitar cálculos matemáticos pesados en la CPU.

Espero que este resumen te sirva para encarar los problemas de la guía. La clave siempre está en elegir un buen soporte para que esa $c$ sea lo más cercana a 1 posible; así no perdés tiempo rechazando valores. ¡Cualquier duda con una derivada o un despeje, me avisás!
### ¿Por qué estudiar este tema? / ¿Para qué sirve?

El estudio de la **generación de variables aleatorias continuas** es la pieza clave para que una simulación pueda representar la realidad de forma fluida. En los sistemas reales, el tiempo, el peso, la distancia o el dinero no suelen cambiar en saltos discretos, sino que pueden tomar cualquier valor en un rango continuo. Aprender estos métodos nos permite "traducir" el azar básico de la computadora (que solo nos da números entre 0 y 1) a comportamientos complejos como el tiempo que tarda una máquina en romperse o la llegada de clientes a un banco. Sin estas herramientas, no podríamos aplicar el **Método de Monte Carlo** para resolver problemas que no tienen solución matemática exacta.

---

### Resumen del tema

La generación de variables aleatorias (v.a.) continuas consiste en transformar números pseudoaleatorios provenientes de una distribución uniforme $U \sim U(0,1)$ en valores que sigan una función de densidad $f(x)$ específica. Según las **Notas de Cátedra**, existen dos enfoques principales: el **Método de la Transformada Inversa**, que es el más rápido si conocemos la fórmula de la probabilidad acumulada, y el **Método de Aceptación y Rechazo**, que funciona como un sistema de "ensayo y error" para casos más difíciles. El tema también cubre algoritmos optimizados para la distribución **Normal** (que es fundamental en estadística) y para los **Procesos de Poisson**, que modelan eventos a lo largo del tiempo.

---

### Método de la Transformada Inversa

Este subtema se conecta con el tema general porque constituye el procedimiento fundamental y más directo de transformación, basándose en la relación matemática exacta entre la probabilidad acumulada y el intervalo $(0,1)$.

La teoría indica que si $U$ es una v.a. uniforme, entonces $X = F^{-1}(U)$ tiene la distribución deseada. El procedimiento requiere integrar la función de densidad para obtener la acumulada $F(x)$, igualarla a $U$ y despejar la $x$.

#### Aplicaciones y optimizaciones en modelos estándar

- **Distribución Exponencial:** Es el caso más común, donde $X = -\frac{1}{\lambda} \ln(U)$.
- **Distribución Gamma:** Al ser la suma de $n$ exponenciales, se puede optimizar multiplicando las uniformes antes de aplicar un único logaritmo: $X = -\frac{1}{\lambda} \ln\left(\prod_{i=1}^{n} U_i\right)$.
- **Máximos de uniformes:** Para simular variables con acumulada $F(x) = x^{n}$, basta con generar $n$ uniformes y elegir el valor más grande.

> [!NOTE] Este método es el preferido por su eficiencia, pero solo se puede usar si la función de distribución tiene una inversa que podamos calcular analíticamente.

### Método de Aceptación y Rechazo

Este subtema se conecta con el tema general porque ofrece una alternativa universal para generar cualquier distribución de la que conozcamos su densidad, incluso cuando no podemos invertir su acumulada.

El algoritmo utiliza una **densidad de soporte** $g(y)$ (que sea fácil de generar) y una constante $c$ que actúe como cota superior para el cociente entre la densidad objetivo y la de soporte. Se genera un candidato $Y$ y se acepta solo si una nueva uniforme $U$ cumple que $U < f(Y)/(c \cdot g(Y))$.

#### Eficiencia y optimización por compresión

- **Costo de iteración:** El número de intentos sigue una distribución _geométrica_ con media $c$, por lo que el éxito del método depende de elegir una $c$ lo más pequeña posible.
- **Rechazo Transformado con Compresión:** Es una mejora avanzada que define un "rectángulo de aceptación segura" bajo la curva para evitar el cálculo de funciones costosas como logaritmos en cada intento.

>[!abstract] [[Método de Aceptación y Rechazo]]

### Simulación de la Distribución Normal

Este subtema se conecta con el tema general porque resuelve el reto técnico de simular la distribución más importante de la ciencia, la cual carece de una función acumulada cerrada para invertir.

Para generar una **Normal Estándar** $Z \sim N(0,1)$, se utilizan transformaciones que aprovechan propiedades geométricas en dos dimensiones.

#### Box-Muller, Método Polar y Razón entre Uniformes

- **Box-Muller:** Usa funciones trigonométricas para convertir dos uniformes en dos normales: $X = \sqrt{-2 \ln(U_1)} \cos(2\pi U_2)$.
- **Método Polar:** Optimiza a Box-Muller eliminando el uso de senos y cosenos mediante un método de aceptación y rechazo sobre un círculo unitario.
- **Razón entre Uniformes:** Un método moderno que genera la normal como el cociente $Z = V/U$, donde el par $(U, V)$ pertenece a una región específica $C_f$ definida por la densidad normal.

### Generación de Procesos de Poisson

Este subtema se conecta con el tema general porque aplica la simulación de v.a. continuas (específicamente tiempos de espera) para construir modelos dinámicos que cuentan eventos en el tiempo.

Un proceso de Poisson puede ser **homogéneo** (tasa $\lambda$ constante) o **no homogéneo** (tasa $\lambda(t)$ variable).

#### Algoritmo de Adelgazamiento (Thinning)

- **Caso Homogéneo:** Se simula generando tiempos entre arribos como variables _exponenciales_ independientes.
- **Caso No Homogéneo:** Se utiliza el **adelgazamiento**, donde se genera un proceso con una tasa máxima $\lambda_{max}$ y cada evento se acepta con probabilidad $p = \lambda(t)/\lambda_{max}$, filtrando los puntos para que sigan la intensidad variable deseada.

---

### Conclusión breve

En fin, generar variables continuas es como tener un manual de instrucciones para moldear el azar. Si la matemática es amigable, usamos la **Transformada Inversa** por su rapidez; si el modelo se pone difícil, aplicamos **Aceptación y Rechazo**; y para pesos pesados como la **Normal** o el tráfico de eventos (**Poisson**), usamos trucos geométricos y filtros. Con estas bases, ya podés programar simulaciones que imiten casi cualquier fenómeno real.

---

### Mini-glosario opcional

- **Función de Densidad ($f(x)$):** La curva que indica qué tan probable es que la variable tome valores en un punto dado.
- **Jacobiano:** Factor de ajuste necesario cuando cambiamos de coordenadas (como de $x,y$ a polares) para que la probabilidad total siga siendo 1.
- **Adelgazamiento:** Técnica de "colador" estadístico para simular tasas de llegada que cambian con el tiempo.
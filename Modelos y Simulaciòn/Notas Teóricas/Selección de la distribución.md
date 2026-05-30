
Para que los resultados de una simulación sean válidos, el modelo debe representar fielmente las fuentes de incertidumbre del sistema real (como tiempos de servicio, arribos o fallas). Este proceso consiste en transformar datos observados en una estructura matemática que la computadora pueda procesar para generar escenarios futuros.

---
### Estrategias de modelado de datos

Existen tres enfoques principales para decidir qué "números" inyectar en el simulador según la calidad y cantidad de datos disponibles:

- **Uso directo de datos históricos:** Consiste en tomar los registros tal cual ocurrieron en el pasado. Su utilidad es limitada: sirve para **validar el modelo** (ver si el simulador se comporta como la realidad conocida), pero no permite explorar escenarios que no hayan ocurrido antes.
- **Distribución empírica:** Se construye una función de probabilidad basada directamente en la frecuencia de los datos observados.
    - **Distribución empírica lineal (Suavizado):** Si los datos son continuos, se ordenan las observaciones $X_{(1)} < X_{(2)} < ... < X_{(n)}$ y se unen los puntos con una poligonal. Esto permite simular valores intermedios que no estaban en la muestra original pero que se encuentran dentro del rango observado. La fórmula para la probabilidad acumulada entre dos puntos es: $$Fel(x) = \frac{i-1}{n-1} + \frac{x - X_{(i)}}{(n-1)(X_{(i+1)} - X_{(i)})} \quad \text{para } X_{(i)} \leq x \leq X_{(i+1)}$$
- **Inferencia estadística (Distribuciones teóricas):** Es el enfoque más robusto. Se ajustan los datos a una familia conocida (Normal, Exponencial, etc.). Sus ventajas son que suaviza irregularidades, permite generar valores fuera del rango observado y facilita cambiar escenarios simplemente modificando parámetros (como aumentar la tasa de arribos $\lambda$).
---
### Medidas estadísticas y diagnóstico para ejercicios

Para elegir una distribución teórica en la práctica, se debe calcular los _estadísticos muestrales_ de tu muestra de tamaño $n$ y compararlos con las propiedades de las familias de distribuciones conocidas.

#### Fórmulas de cálculo fundamentales

- **Media muestral ($\bar{X}(n)$):** Indica la tendencia central. $$\bar{X}(n) = \frac{1}{n} \sum_{i=1}^{n} X_i$$.
- **Varianza muestral ($S^2(n)$):** Mide la dispersión. Es un estimador no sesgado de la varianza poblacional $\sigma^2$. $$S^2(n) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X}(n))^2$$.
- **Coeficiente de variación ($\widehat{cv}$):** Relación entre el desvío y la media. $$\widehat{cv}(n) = \frac{\sqrt{S^2(n)}}{\bar{X}(n)}$$

> [!tip] Reglas de oro para identificar distribuciones en la práctica Al resolver ejercicios, compará tus resultados con estos criterios:
> 
> 1. **Distribución Exponencial:** El indicio más fuerte es que el **coeficiente de variación es aproximadamente 1** ($\widehat{cv} \approx 1$).
> 2. **Distribución Normal:** La distribución es simétrica. Debés verificar que la **media muestral sea similar a la mediana muestral**.
> 3. **Distribución de Poisson:** El valor esperado y la varianza teóricos son iguales. Buscá que $\bar{X}(n) \approx S^2(n)$.

---
#### Herramientas visuales de apoyo

Antes de realizar tests formales, se usan gráficos para descartar opciones:

- **Histogramas:** Permiten comparar visualmente la forma de la muestra con la función de densidad teórica superpuesta. Se recomienda usar el _histograma normalizado_ (dividiendo la frecuencia por la amplitud del intervalo $\Delta$) para que el área total sea 1 y sea comparable con una densidad.
- **Diagramas de caja (Box-Plots):** Ayudan a visualizar los cuartiles (25%, 50%, 75%) y detectar **outliers** (valores extremos) o asimetrías que descartarían una distribución normal.
- **q-cuantiles:** Se usan para comparar percentiles de la muestra contra los teóricos.

---

**Mini-glosario:**

- **Estadı́stico muestral:** Variable aleatoria definida a partir de los datos de una muestra que se usa para estimar una propiedad de la población.
- **Outlier:** Observación extrema que se aleja del grueso de los datos y puede distorsionar la elección de la distribución.
- **Distribución Empı́rica:** Modelo basado puramente en lo observado, sin asumir una forma matemática predefinida.

---

# La técnica de Bootstrap

La técnica de **Bootstrap** es un método de inferencia estadística que permite recuperar información valiosa (como la varianza o el error de un estimador) a partir de los datos observados, sin necesidad de asumir ninguna hipótesis previa sobre la distribución original de la que provienen. Es especialmente útil cuando la distribución es desconocida o muy compleja para calcular sus propiedades de forma analítica.

### Funcionamiento y muestras bootstrap

Este método se basa en el concepto de **muestra bootstrap**, que es una muestra aleatoria de tamaño $n$ tomada **con reposición** a partir de un conjunto original de $n$ observaciones.

Si tenemos los datos $x_1, x_2, \dots, x_n$, la distribución empírica $F_e$ les asigna a todos la misma probabilidad $1/n$. Al tomar una muestra con reposición, algunos valores originales pueden repetirse y otros pueden no aparecer en la nueva muestra.

#### Procedimiento para replicaciones

Para cada muestra bootstrap generada, evaluamos el estimador de interés $\hat{\theta}$. Este valor calculado se denomina **replicación bootstrap** de $\hat{\theta}$. Por ejemplo, si nuestro estimador es la media muestral $\bar{X}$, calculamos el promedio de cada una de las muestras bootstrap obtenidas.

> [!NOTE] La cantidad total de muestras bootstrap posibles es $n^n$. Si $n$ es pequeño (ej. $n=3$), hay pocas combinaciones ($3^3 = 27$) y podemos calcularlas todas; esto se conoce como **estimación bootstrap ideal**.

#### Variación: Aproximación por Monte Carlo

Cuando el tamaño de la muestra $n$ es grande, calcular las $n^n$ combinaciones es imposible (ej. para $n=20$, $20^{20}$ es un número astronómico). En estos casos, aplicamos el **método de Monte Carlo**: seleccionamos aleatoriamente un número $N$ de muestras bootstrap (donde $N$ es mucho menor que $n^n$) y estimamos los valores esperados promediando los resultados de esas $N$ muestras.

### Estimación bootstrap de parámetros (ECM y Varianza)

El objetivo principal es usar las replicaciones para medir qué tan bueno es nuestro estimador original con respecto al parámetro real de la población.

#### Error Cuadrático Medio (ECM)

El ECM mide la dispersión del estimador respecto al parámetro. En bootstrap, se estima calculando la esperanza sobre la distribución empírica: $$ECM(\hat{\theta}, \theta) \approx \frac{1}{N} \sum_{j=1}^{N} (\hat{\theta}(b^{(j)}) - \theta(F_e))^2$$ Donde:

- $\theta(F_e)$ es el parámetro calculado con los datos originales (ej. la varianza de la muestra original).
- $\hat{\theta}(b^{(j)})$ es el estimador evaluado en la $j$-ésima muestra bootstrap.

#### Estimación de la Varianza

Para estimar la varianza de un estimador $\hat{\theta}$, generamos $N$ muestras bootstrap, calculamos sus replicaciones $\hat{\theta}(b_1), \dots, \hat{\theta}(b_N)$ y luego calculamos la **varianza muestral** de esos resultados: $$V\hat{a}r_{F_e}(\hat{\theta}) = \frac{1}{N-1} \sum_{j=1}^{N} (\hat{\theta}(b_j) - \hat{\theta}_m)^2$$ Donde $\hat{\theta}_m$ es el promedio de las $N$ replicaciones bootstrap.

#### Variación: Estimación de una proporción

También podemos estimar la probabilidad de que un estimador caiga en un rango, como $P(a < \hat{\theta} < b)$. Esto se trata como el valor esperado de una variable Bernoulli que vale 1 si la replicación cae en el intervalo y 0 si no. La estimación será simplemente la proporción de muestras bootstrap que cumplieron la condición.

> [!TIP] Bootstrap es una herramienta de "fuerza bruta" computacional. No requiere saber si los datos son Normales o Exponenciales; la computadora "re-muestrea" los datos una y otra vez para entender su variabilidad.

---

### Mini-glosario

- **Distribución empírica ($F_e$):** Distribución que asigna probabilidad $1/n$ a cada dato observado en la muestra.
- **Muestreo con reposición:** Técnica de extracción donde cada elemento seleccionado vuelve al conjunto antes de la siguiente extracción, permitiendo que se repita.
- **Replicación bootstrap:** El valor que toma un estimador cuando se aplica sobre una muestra generada por bootstrap.

En resumen, Bootstrap es como "crear universos paralelos" a partir de tus propios datos para ver cuánto cambian tus resultados. Es la solución ideal cuando no tenés fórmulas teóricas para la varianza de lo que estás queriendo medir. ¡Espero que este resumen te sirva para el repaso!
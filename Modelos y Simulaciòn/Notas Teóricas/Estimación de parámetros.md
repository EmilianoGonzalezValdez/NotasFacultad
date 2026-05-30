
En simulación, un **estimador** $\hat{\theta}$ es cualquier función de los datos observados en una muestra ($X_1, X_2, \dots, X_n$) que se utiliza para inferir el valor de un parámetro desconocido $\theta$ de la población.

### Propiedades de un buen estimador

Para decidir si un estimador es confiable para nuestra simulación, evaluamos cuatro propiedades teóricas fundamentales:

- **Insesgabilidad:** El estimador es _insesgado_ si su valor esperado es igual al parámetro real ($E[\hat{\theta}] = \theta$). Si existe una diferencia, se denomina **sesgo**.
- **Consistencia:** A medida que el tamaño de la muestra $n$ aumenta, el estimador debe aproximarse cada vez más al parámetro real.
- **Eficiencia:** Entre dos estimadores insesgados, el más eficiente es el que tiene la **menor varianza**.
- **Suficiencia:** El estimador debe utilizar toda la información relevante contenida en la muestra.

#### Error Cuadrático Medio (ECM)

Es la medida estándar para conocer la precisión total de un estimador. Combina la variabilidad con el sesgo: $$ECM(\hat{\theta}, \theta) = Var(\hat{\theta}) + (E[\hat{\theta}] - \theta)^2$$

> [!note] Si el estimador es insesgado, el sesgo es cero y el ECM coincide exactamente con la varianza del estimador ($ECM = Var(\hat{\theta})$).

### Método de Máxima Verosimilitud (MLE)

Es la técnica más utilizada para construir estimadores. Parte de la premisa de que el mejor valor para un parámetro es aquel que maximiza la probabilidad (o densidad) de haber obtenido la muestra que realmente observamos.

#### Procedimiento práctico para resolver ejercicios

1. **Definir la función de verosimilitud $L(\theta)$:** Es el producto de las funciones de probabilidad (o densidad) de cada dato de la muestra: $$L(\theta) = f_\theta(X_1) \cdot f_\theta(X_2) \cdot \dots \cdot f_\theta(X_n)$$
2. **Aplicar logaritmo (Log-Verosimilitud):** Se suele trabajar con $\ln(L(\theta))$ porque transforma los productos en sumas, facilitando la derivada.
3. **Maximizar:** Se deriva respecto a $\theta$, se iguala a cero y se despeja el parámetro.

#### Aplicaciones comunes de MLE

- **Para una Exponencial ($E(\lambda)$):** El estimador de máxima verosimilitud para $\lambda$ es la inversa de la media muestral: $$\hat{\lambda} = \frac{1}{\bar{X}(n)}$$
- **Para una Geométrica ($Geom(p)$):** El estimador para la probabilidad de éxito $p$ es: $$\hat{p} = \frac{1}{\bar{X}(n)}$$

### Estimadores universales: Media y Varianza Muestral

Independientemente de la distribución, estos dos estadísticos son los pilares para parametrizar modelos:

- **Media Muestral ($\bar{X}(n)$):** Es un estimador insesgado para la esperanza $E[X]$. Su varianza es $\sigma^2/n$, lo que significa que es consistente (a mayor $n$, mayor precisión). $$\bar{X}(n) = \frac{1}{n} \sum_{i=1}^{n} X_i$$
- **Varianza Muestral ($S^2(n)$):** Se usa para estimar la dispersión $\sigma^2$. Es un estimador insesgado porque se divide por $n-1$ (corrigiendo el sesgo que tendría si se dividiera por $n$). $$S^2(n) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X}(n))^2$$

> [!tip] Uso en simulaciones Si tu simulación requiere una distribución Normal $N(\mu, \sigma^2)$ y solo tenés una muestra de datos reales, lo más razonable es parametrizar tu modelo usando $\hat{\mu} = \bar{X}(n)$ y $\hat{\sigma}^2 = S^2(n)$.

---

**Mini-glosario:**

- **$\hat{\theta}$ (Theta sombrero):** Notación estándar para un estimador.
- **Sesgo:** La diferencia entre lo que el estimador espera obtener y la realidad.
- **Consistencia:** Propiedad de "mejorar" la puntería al aumentar los datos.

---

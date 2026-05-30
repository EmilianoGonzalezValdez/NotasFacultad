
Este capítulo aborda la necesidad de transformar los datos brutos generados por una computadora en información estadística válida. Dado que cada corrida de un modelo es una observación de una variable aleatoria, el análisis permite medir la precisión de los resultados y asegurar que el modelo represente fielmente la aleatoriedad del sistema real.

---
### Ejes temáticos principales

1. ***[[Selección de la distribución]]:*** Trata sobre cómo modelar las fuentes de incertidumbre (como tiempos de falla o arribos) a partir de datos reales:
	- **Uso de datos:** Se explica la diferencia entre usar datos históricos directamente, construir una _distribución empírica_ (basada en la muestra observada) o aplicar _inferencia estadística_ para ajustar los datos a una distribución teórica (Normal, Exponencial, etc.).
	- **Medidas de apoyo:** Se utilizan medidas como la media muestral $X(n)$, varianza muestral $S^2(n)$ y el coeficiente de variación para decidir qué familia de distribución se ajusta mejor.

2. ***[[Estimación de parámetros]]:*** Una vez elegida una familia de distribución, el foco se pone en hallar los valores específicos (parámetros como $\lambda, \mu, p$) que la definen para nuestro caso:
	- **Propiedades de los estimadores:** Define qué hace "bueno" a un estimador $\hat{\theta}$ (insesgabilidad, consistencia, eficiencia y suficiencia).
	- **Máxima Verosimilitud (MLE):** Es el método principal para encontrar los parámetros que maximizan la probabilidad de que la muestra observada ocurra realmente.

3. ***[[Gestión del tamaño de la muestra y algoritmos recursivos]]:*** Este eje resuelve la pregunta técnica de cuántas simulaciones son necesarias para que el resultado sea confiable.
	- **Criterio de parada:** Utiliza el _Teorema Central del Límite_ para determinar un número $n$ de simulaciones tal que el desvío estándar del estimador sea menor a una precisión $d$ deseada.
	- **Algoritmo recursivo:** Introduce fórmulas para actualizar la media y la varianza en cada paso del programa sin tener que guardar todos los datos previos, optimizando la memoria y el tiempo de cómputo.

4. ***[[Estimación por intervalos de confianza]]:*** En lugar de obtener un solo número, este eje enseña a calcular un rango de valores donde se encuentra el parámetro real con una probabilidad determinada:
	- **Nivel de confianza ($1-\alpha$):** Se explica cómo construir intervalos para la media $E(X)$ o para proporciones $p$ (como la probabilidad de que un evento ocurra), garantizando que el parámetro real esté allí el, por ejemplo, 95% de las veces.

5. ***[[Técnica de Bootstrap]]:*** Es un método de remuestreo moderno que se aplica cuando no conocemos la distribución teórica de los datos y no queremos asumir normalidad.
	- **Procedimiento:** Consiste en generar nuevas muestras (muestras bootstrap) tomando elementos con reposición de los datos originales.
	- **Utilidad práctica:** Permite estimar el Error Cuadrático Medio (ECM) y la varianza de estimadores complejos cuya fórmula matemática sería imposible de hallar de otra manera.

---

**Mini-glosario:**

- **Distribución Empírica:** Distribución construida directamente a partir de las frecuencias de los datos observados.
- **MLE (Máxima Verosimilitud):** Método para estimar parámetros que mejor "explican" los datos obtenidos.
- **Remuestreo:** Técnica de generar nuevas muestras a partir de una muestra original para realizar inferencias.

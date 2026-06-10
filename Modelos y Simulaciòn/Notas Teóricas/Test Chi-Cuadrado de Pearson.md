
El **test chi-cuadrado de Pearson** es una prueba de bondad de ajuste utilizada para determinar si una muestra de $n$ observaciones independientes proviene de una distribución de probabilidad específica $F$. Este método es la herramienta estándar para **datos discretos** (que toman valores en un conjunto ${1, 2, ..., k}$) o para datos continuos que han sido agrupados en clases o intervalos [97, 454; 98, 474].

### Procedimiento y Estadístico de Prueba

Para aplicar el test, comparamos las **frecuencias observadas** en la muestra contra las **frecuencias esperadas** que predice la teoría si la hipótesis nula $H_0$ fuera cierta.

Sean:

- $N_i$: Frecuencia observada (cantidad de veces que aparece el valor $i$ en la muestra).
- $p_i$: Probabilidad teórica de que una variable con distribución $F$ tome el valor $i$.
- $n p_i$: Frecuencia esperada (cuántas veces debería haber aparecido el valor $i$ según la teoría).

El estadístico de prueba $T$ se define como: $$T = \sum_{i=1}^{k} \frac{(N_i - n p_i)^2}{n p_i}$$ Este valor mide la "distancia" global entre nuestra muestra y la distribución ideal; un valor de $T$ excesivamente grande sugiere que la discrepancia no es producto del azar y, por lo tanto, se debe rechazar $H_0$ [97, 455; 456].

#### Grados de Libertad y Distribución de Referencia

Bajo la hipótesis nula y para una muestra $n$ suficientemente grande, el estadístico $T$ se distribuye aproximadamente como una variable aleatoria **Chi-cuadrado** ($\chi^2$). Los grados de libertad ($gl$) dependen de la información previa de los parámetros:

- **Parámetros especificados:** Si conocemos todos los parámetros de la distribución de antemano, $gl = k - 1$.
- **Parámetros estimados:** Si debemos estimar $m$ parámetros a partir de la muestra (por ejemplo, estimar $\lambda$ de una Poisson usando la media muestral), entonces $gl = k - 1 - m$.

#### Variación: Estimación del p-valor por Simulación

Cuando el $p$-valor obtenido mediante la tabla $\chi^2$ es muy cercano al nivel de significación $\alpha$ (ej: 0.05), se puede recurrir a la simulación para obtener mayor precisión. El procedimiento consiste en:

1. Simular $M$ muestras de tamaño $n$ a partir de la distribución teórica $F$.
2. Para cada muestra simulada, calcular su propio estadístico $T_{sim}$.
3. El $p$-valor estimado es la proporción de veces que $T_{sim} \geq t_{observado}$ [97, 461; 97, 464].

En el caso de parámetros no especificados, por cada simulación se deben **re-estimar** los parámetros a partir de la muestra simulada para recalcular las probabilidades $p_i(sim)$ y obtener un $T_{sim}$ válido.

#### Aplicación Práctica: Agrupamiento de Clases

Si se trabaja con variables discretas que tienen infinitos valores (como Poisson) o variables continuas, es necesario agrupar los datos en $k$ grupos o intervalos [97, 469; 98, 475].

> [!warning] Requisito de Frecuencia Esperada Para que la aproximación a la distribución $\chi^2$ sea confiable, se suele requerir que cada frecuencia esperada $n p_i$ sea al menos igual a 5. Si alguna clase tiene una frecuencia menor, se recomienda agruparla con una clase adyacente.

> [!example] Ejemplo de cálculo de p-valor Si obtenemos un estadístico $T = 14.59$ con $gl = 7$, y el $p$-valor es $P(\chi_7^2 \geq 14.59) \approx 0.04$, rechazamos $H_0$ con un nivel de significación del 5% porque $0.04 < 0.05$.

---

**Mini‑glosario:**

- **Frecuencia Observada ($N_i$):** Conteo real de datos en una categoría dentro de la muestra.
- **Frecuencia Esperada ($n p_i$):** Cantidad de datos que deberían caer en esa categoría según el modelo teórico.
- **Grados de Libertad ($gl$):** Número de categorías independientes menos la cantidad de parámetros estimados y uno adicional por la suma de probabilidades.

---


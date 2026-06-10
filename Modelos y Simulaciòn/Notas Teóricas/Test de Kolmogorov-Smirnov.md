# Test de Kolmogorov-Smirnov

El **test de Kolmogorov-Smirnov (K-S)** es una prueba de bondad de ajuste diseñada específicamente para variables aleatorias con **distribuciones continuas**. A diferencia del test de Pearson, este método no requiere agrupar los datos en clases o intervalos, lo que evita la pérdida de información y lo hace mucho más potente para muestras pequeñas [97, 474; 97, 475].

### Procedimiento y Estadístico de Prueba

La lógica del test consiste en comparar la **Función de Distribución Acumulada Empírica** ($F_e(x)$) de la muestra con la **Función de Distribución Teórica** ($F(x)$) que se desea validar. El estadístico $D$ representa la mayor discrepancia (distancia máxima) entre ambas curvas.

Dada una muestra de tamaño $n$ de observaciones independientes $Y_1, Y_2, \dots, Y_n$:

1. **Ordenar la muestra:** Se ordenan los datos de menor a mayor para obtener los estadísticos de orden $Y_{(1)} < Y_{(2)} < \dots < Y_{(n)}$.
2. **Definir la distribución empírica:** $F_e(x)$ se define como la proporción de datos menores o iguales a $x$: $$F_e(x) = \frac{\#{j : Y_j \leq x}}{n}$$

3. **Calcular el estadístico $D$:** Debido a que $F(x)$ es creciente y $F_e(x)$ es una función escalonada, la distancia máxima debe buscarse en los puntos de salto (en cada dato $Y_{(j)}$). El estadístico se calcula evaluando la distancia "justo antes" del salto y "en" el salto: $$D = \max_{1 \leq j \leq n}\left\{\frac{j}{n} - F(Y_{(j)}), F(Y_{(j)}) - \frac{j-1}{n} \right\}$$

> [!info] Propiedad de independencia de la distribución Un resultado fundamental (Teorema 8.1) indica que la distribución del estadístico $D$ **es independiente de la distribución $F$** que se está testeando, siempre que sea continua. Esto significa que el p-valor para una Exponencial o una Normal es el mismo que si estuviéramos probando contra una **Uniforme(0,1)**.

4. **Cálculo del p-valor por simulación:** Gracias a la propiedad anterior, si los parámetros están especificados, podemos estimar el p-valor generando muestras de una $U(0,1)$:
    - Generar $k$ muestras de tamaño $n$ de variables $U \sim U(0,1)$.
    - Para cada muestra, calcular su propio estadístico $d_i$ usando $F(u) = u$.
    - $p\text{-valor} \approx \frac{\#{i : d_i \geq d_{\text{observado}}}}{k}$.

> [!tip] Regla de decisión Si el $p\text{-valor} \leq \alpha$ (ej. 0.05), se rechaza la hipótesis nula $H_0$ de que los datos provienen de la distribución $F$.

#### Variación: Parámetros no especificados

Si los parámetros de la distribución $F$ deben estimarse a partir de la muestra (ej. estimar $\lambda$ usando $\bar{Y}$), el estadístico $D$ ya no es independiente de la distribución.

En este caso, para que el test sea válido, **no se deben usar uniformes** para el p-valor. Se debe:

1. Simular muestras de la distribución específica ($F$) con los parámetros estimados.
2. En cada simulación, **re-estimar** los parámetros a partir de la muestra simulada.
3. Calcular el estadístico de esa simulación comparando la muestra simulada contra la distribución con los parámetros re-estimados.
4. El p-valor será la proporción de estos estadísticos simulados que superen al original.

> [!warning] Error común Usar el p-valor de la distribución uniforme cuando los parámetros fueron estimados puede llevar a conclusiones erróneas (generalmente a no rechazar $H_0$ cuando se debería) [98, 492; 99, 494].

---

**Mini‑glosario:**

- **Estadísticos de orden ($Y_{(j)}$):** Valores de la muestra organizados de forma creciente.
- **Distribución Empírica ($F_e$):** Función escalonada que acumula $1/n$ de probabilidad en cada dato observado.
- **Supremo (sup):** La menor de las cotas superiores; en este contexto, el valor máximo de la diferencia entre curvas.

---


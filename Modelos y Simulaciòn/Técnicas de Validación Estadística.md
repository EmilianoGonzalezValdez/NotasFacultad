
Este mapa de contenido organiza los métodos necesarios para determinar si un conjunto de observaciones (reales o simuladas) proviene de una distribución específica o si distintas muestras son coherentes entre sí. El objetivo es validar que el modelo matemático representa fielmente la realidad antes de realizar inferencias.

### Conceptos fundamentales de la validación

Esta sección introduce la lógica detrás de cada test de hipótesis utilizado en simulación.

- **Hipótesis Nula ($H_0$):** Afirmación de que los datos siguen la distribución esperada.
- **Estadístico de prueba ($T$):** Variable aleatoria que mide la discrepancia entre la muestra y la teoría.
- **p-valor:** Indicador probabilístico para decidir el rechazo; un valor pequeño sugiere que la muestra es improbable bajo $H_0$.

> [!info] Regla de Decisión Si el $p-valor \leq \alpha$ (nivel de significación), se rechaza la hipótesis nula.

### Pruebas de Bondad de Ajuste

Se utilizan para comparar una muestra contra una distribución teórica $F$.

- [[Test Chi-Cuadrado de Pearson]]: Ideal para **datos discretos** o continuos agrupados en intervalos.
- [[Test de Kolmogorov-Smirnov]]: El método predilecto para **datos continuos**, basado en la distancia máxima entre distribuciones.

### Inferencia sobre muestras independientes

Métodos para validar si diferentes conjuntos de datos provienen de la misma población, incluso sin conocer la distribución subyacente.

- #### El problema de las dos muestras (Wilcoxon/Mann-Whitney)
    
    Test basado en la **suma de rangos** para determinar si dos muestras provienen de la misma distribución.
- #### Test de rangos para varias muestras (Kruskal-Wallis)
    
    Extensión del test anterior para validar la independencia e igualdad de distribución entre $m$ muestras distintas.

### Validación de Procesos de Poisson

Técnicas específicas para testear si un proceso de arribos se comporta como un proceso de Poisson (homogéneo o no).

- [[Validación del número de arribos]]: Testeo de la cantidad total de eventos como v.a. Poisson.
- [[Validación de la función de intensidad]]: Métodos para verificar si la tasa $\lambda(t)$ es la misma en diferentes jornadas.

> [!tip] Nota Práctica Para procesos de Poisson homogéneos, se puede usar KS para verificar si los tiempos de arribo están **uniformemente distribuidos** en el intervalo $(0, T)$.

---

**Mini‑glosario:**

- **Estadístico Muestral:** Función de los datos observados cuya distribución es conocida bajo $H_0$.
- **Rango:** Posición que ocupa un dato en el ordenamiento total de la muestra combinada.
- **Clases Comunicantes:** (Concepto de Cadenas de Markov, no confundir con las clases de frecuencia en Chi-cuadrado).

---

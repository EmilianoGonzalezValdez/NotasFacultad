
Una **prueba de bondad de ajuste** es un procedimiento estadístico (test de hipótesis) diseñado para determinar si un conjunto de observaciones $x_1, x_2, ..., x_n$ (ya sean reales o simuladas) proviene de una distribución de probabilidad específica $F$. En el contexto de modelos y simulación, estas pruebas actúan como un **validador de entrada**: antes de confiar en los resultados de un modelo, debemos asegurar que las variables aleatorias que lo alimentan representan fielmente la realidad.

### El marco teórico del test de hipótesis

Para realizar la validación, se establecen dos afirmaciones contrapuestas:

- **Hipótesis Nula ($H_0$):** Los datos provienen de la distribución $F$ especificada.
- **Hipótesis Alternativa ($H_1$):** Los datos _no_ provienen de dicha distribución.

#### Procedimiento y Estadístico de Prueba

Se define un **estatístico muestral** $T = T(X_1, ..., X_n)$, que es una función de los datos cuya distribución bajo $H_0$ es conocida. El valor de $T$ mide la "distancia" o discrepancia entre lo observado y lo esperado por la teoría. Una vez evaluado $T = t$ en nuestra muestra, calculamos el **p-valor**, que indica la probabilidad de obtener un resultado tan extremo como el observado si la hipótesis nula fuera cierta.

> [!warning] Regla de Decisión Se fija un nivel de significación $\alpha$ (usualmente $0.05$ o $0.01$).
> 
> - Si $p-valor \leq \alpha$: Se **rechaza $H_0$** (los datos no ajustan).
> - Si $p-valor > \alpha$: **No hay evidencia suficiente** para rechazar $H_0$ (el ajuste es aceptable).

#### El p-valor en la práctica

Existen dos formas de calcularlo según el tipo de test:

1. **Cola derecha:** Se busca si el valor es demasiado alto, $p = P_{H_0}(T \geq t)$.
2. **Dos colas:** Se busca si el valor es inusual por ser muy bajo o muy alto, $p = 2 \cdot min{P_{H_0}(T \geq t), P_{H_0}(T \leq t)}$ [97, 453; 98, 498].

### Clasificación de las pruebas de ajuste

Dependiendo de la naturaleza de los datos, seleccionamos la herramienta matemática adecuada. La elección es crítica para no perder información durante el proceso de validación.

#### Datos discretos o agrupados

Cuando los datos toman valores finitos o han sido categorizados en intervalos (bins), se utiliza el **Test Chi-Cuadrado de Pearson**. Este método compara frecuencias observadas contra frecuencias esperadas.

- Para profundizar en este método, sus grados de libertad y el cálculo del estadístico, ver: [[Test Chi-Cuadrado de Pearson]].

#### Datos continuos

Cuando se trabaja con variables continuas (como tiempos de servicio o permanencia), agrupar los datos en intervalos puede ser ineficiente porque se pierde el detalle de la distribución dentro del rango. En estos casos, se prefiere el **Test de Kolmogorov-Smirnov**, que se basa en la distancia máxima entre la función de distribución acumulada empírica y la teórica.

- Para entender el cálculo de las distancias y la propiedad de independencia de la distribución, ver: [[Test de Kolmogorov-Smirnov]].

> [!info] Nota sobre parámetros no especificados En muchos ejercicios, no conocemos los parámetros de antemano (ej: sabemos que es Poisson pero no conocemos su $\lambda$). En esos casos, debemos estimarlos a partir de la muestra (usando $\bar{X}$ o $S^2$) antes de realizar el test, lo cual suele requerir el uso de **simulación para obtener un p-valor más preciso** [97, 464-466; 98, 490].

---

**Mini‑glosario:**

- **p-valor:** Probabilidad de que la discrepancia observada se deba simplemente al azar bajo la hipótesis nula.
- **Estadístico Muestral:** Variable aleatoria que sintetiza la información de la muestra para compararla con la teoría.
- **Nivel de significación ($\alpha$):** Riesgo máximo que estamos dispuestos a correr de rechazar un ajuste que en realidad era correcto.

---

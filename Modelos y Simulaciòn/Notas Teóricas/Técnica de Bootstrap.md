
El Bootstrap es una técnica de remuestreo que permite inferir propiedades de un estimador (como su varianza o su error) utilizando únicamente la información contenida en los datos observados, sin necesidad de asumir que provienen de una distribución teórica específica (como la Normal o la Exponencial).

### Fundamento y Muestras Bootstrap

La idea central es que la **distribución empírica** $F_e$ de nuestros datos observados es la mejor representación que tenemos de la población real.

#### Definición de Muestra Bootstrap

Dada una muestra original de tamaño $n$ ($x_1, x_2, \dots, x_n$), una **muestra bootstrap** es una nueva muestra, también de tamaño $n$, obtenida mediante **muestreo con reposición** de los datos originales. Esto significa que en una nueva muestra, algunos datos originales pueden aparecer varias veces y otros pueden no aparecer.

> [!example] Ejemplo visual Si tus datos son ${1.4, 2.5, -0.5}$, una muestra bootstrap válida sería ${2.5, -0.5, 2.5}$. Notá que el $2.5$ se repitió y el $1.4$ desapareció.

#### Procedimiento para ejercicios (Remuestreo Monte Carlo)

Cuando $n$ es grande, es imposible calcular todas las $n^n$ combinaciones posibles (Bootstrap Ideal). En la práctica, aplicamos **Bootstrap Monte Carlo** siguiendo estos pasos:

1. **Generar $B$ muestras bootstrap:** Seleccionar aleatoriamente $B$ conjuntos (típicamente $B \geq 1000$) de tamaño $n$ con reposición de la muestra original.
2. **Calcular replicaciones:** Para cada una de las $B$ muestras, calcular el valor del estimador que estamos estudiando ($\hat{\theta}^*_1, \hat{\theta}^*_2, \dots, \hat{\theta}^*_B$).
3. **Estimar la métrica:** Promediar los resultados para obtener la varianza, el ECM o una probabilidad.

### Aplicaciones: Estimación de Error y Varianza

El Bootstrap brilla cuando el estimador es complejo (como el cociente de dos medias) y no existen fórmulas matemáticas cerradas para calcular su precisión.

#### Estimación del Error Cuadrático Medio (ECM)

Para medir qué tan lejos está nuestro estimador $\hat{\theta}$ del parámetro real $\theta$, usamos la aproximación bootstrap del ECM:

1. Calculamos el parámetro en la muestra original (parámetro de la distribución empírica), denotado como $\theta(F_e)$.
2. Calculamos el ECM como el promedio de las diferencias al cuadrado entre cada replicación bootstrap y ese parámetro inicial: $$ECM \approx \frac{1}{B} \sum_{j=1}^{B} (\hat{\theta}^*_j - \theta(F_e))^2$$

#### Estimación de la Varianza de un Estimador

Si queremos saber cuánto varía nuestro estimador, calculamos la **varianza muestral de las replicaciones bootstrap**:

1. Calculamos la media de todas las replicaciones: $\hat{\theta}_m = \frac{1}{B} \sum_{j=1}^{B} \hat{\theta}^*_j$.
2. La varianza estimada es: $$\hat{Var}_{Fe}(\hat{\theta}) = \frac{1}{B-1} \sum_{j=1}^{B} (\hat{\theta}^*_j - \hat{\theta}_m)^2$$

> [!tip] Caso de uso: Cociente de medias Es muy común usar Bootstrap para estimar el tiempo promedio de permanencia de clientes cuando los arribos diarios ($n_i$) y los tiempos totales ($D_i$) varían. El estimador es $\hat{\theta} = \bar{D} / \bar{n}$, y el Bootstrap es la única forma sencilla de hallar su ECM sin conocer la distribución conjunta de arribos y tiempos.

---

**Mini-glosario:**

- **Muestra con reposición:** Técnica donde cada elemento extraído se devuelve al conjunto antes de la siguiente extracción.
- **Replicación bootstrap:** El valor que toma el estimador cuando se aplica sobre una muestra generada por remuestreo.
- **Distribución Empírica ($F_e$):** Distribución que asigna probabilidad $1/n$ a cada dato observado en la muestra.

---

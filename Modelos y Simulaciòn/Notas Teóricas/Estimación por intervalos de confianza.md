
La estimación puntual entrega un único valor como resultado (ej. la media muestral $\bar{X}(n)$), pero no informa sobre el grado de incertidumbre de esa cifra. Un **estimador por intervalo** define un rango de valores dentro del cual se encuentra el parámetro real $\theta$ con una probabilidad determinada, denominada _nivel de confianza_ $1-\alpha$.

### Construcción de intervalos para el valor esperado ($E[X]$)

Para muestras grandes ($n \geq 100$), el Teorema Central del Límite asegura que la media muestral se distribuye de forma aproximadamente normal.

Para construir un intervalo con una confianza del $100(1-\alpha)\%$, utilizamos los valores $z_{\alpha/2}$ de la tabla de distribución normal estándar. El intervalo resultante es: $$\left( \bar{X}(n) - z_{\alpha/2} \frac{S(n)}{\sqrt{n}} \ , \ \bar{X}(n) + z_{\alpha/2} \frac{S(n)}{\sqrt{n}} \right)$$

> [!info] Valores críticos comunes ($z_{\alpha/2}$)
> 
> - **90% de confianza:** $z_{0.05} = 1.64$
> - **95% de confianza:** $z_{0.025} = 1.96$
> - **99% de confianza:** $z_{0.005} = 2.58$

#### Control de la longitud del intervalo ($L$) en la práctica

En simulación, a menudo se exige que el resultado final tenga una precisión específica, es decir, que el intervalo no sea más ancho que una longitud $L$. Dado que la longitud es $2 \cdot z_{\alpha/2} \frac{S(n)}{\sqrt{n}}$, para lograr una amplitud menor a $L$, se deben generar datos hasta que se cumpla la condición de parada con un desvío estándar del estimador $d$ definido como: $$d = \frac{L}{2 \cdot z_{\alpha/2}}$$

> [!code] Algoritmo para simular con amplitud $L$ fija
> 
> ```
> def Media_Muestral_Con_L(z_alfa_2, L):
>     d = L / (2 * z_alfa_2) # Definir precisión requerida
>     Media = simular_X()
>     Scuad, n = 0, 1
>     while n <= 100 or sqrt(Scuad / n) > d:
>         n += 1
>         X_nuevo = simular_X()
>         Media_Ant = Media
>         Media = Media_Ant + (X_nuevo - Media_Ant) / n
>         Scuad = Scuad * (1 - 1/(n-1)) + n * (Media - Media_Ant)**2
>     return Media
> ```

### Intervalos para proporciones (Casos Bernoulli)

Cuando la simulación estima la probabilidad $p$ de un evento (éxito/fracaso), la variable $X_i$ es Bernoulli. En este caso, la varianza se estima directamente como $\bar{X}(n)(1-\bar{X}(n))$.

El intervalo de confianza del $100(1-\alpha)%$ para la proporción es: $$\left( \bar{X}(n) - z_{\alpha/2} \sqrt{\frac{\bar{X}(n)(1-\bar{X}(n))}{n}} \ , \ \bar{X}(n) + z_{\alpha/2} \sqrt{\frac{\bar{X}(n)(1-\bar{X}(n))}{n}} \right)$$

> [!warning] Nota sobre el tamaño de muestra Esta aproximación normal para proporciones solo es válida si $n$ es lo suficientemente grande como para que la varianza estimada sea estable.

---

**Mini-glosario:**

- **$1-\alpha$:** Nivel de confianza; probabilidad de que el intervalo contenga el parámetro real.
- **$z_{\alpha/2}$:** Valor crítico de la normal que deja un área de $\alpha/2$ en cada extremo.
- **Amplitud ($L$):** El ancho total del intervalo de confianza ($L = L_{sup} - L_{inf}$).

---


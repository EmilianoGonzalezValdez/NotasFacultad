
En simulación, cada corrida del modelo genera una observación de una variable aleatoria. El desafío es determinar cuántas simulaciones ($n$) son necesarias para que el promedio obtenido ($\bar{X}(n)$) sea una estimación precisa del valor esperado real ($\mu$).

### Criterio de parada para el número de simulaciones

Dado que el costo computacional aumenta con cada corrida, necesitamos un criterio estadístico para detenernos apenas alcancemos la precisión deseada.

#### Fundamento Teórico

Según el **Teorema Central del Límite (TCL)**, si las observaciones $X_1, X_2, \dots, X_n$ son independientes e idénticamente distribuidas, para un $n$ suficientemente grande ($n \geq 100$), la media muestral $\bar{X}(n)$ se distribuye de forma aproximadamente normal con media $\mu$ y varianza $\sigma^2/n$.

#### Aplicación Práctica

El criterio estándar consiste en fijar una **precisión deseada $d$** (el desvío estándar máximo tolerable para nuestro estimador) y seguir simulando mientras se cumpla que:

1. Hayan ocurrido al menos 100 simulaciones ($n \geq 100$) para asegurar normalidad.
2. El desvío estándar del estimador sea mayor a $d$: $$\frac{S(n)}{\sqrt{n}} > d$$

> [!info] Interpretación de la precisión Alcanzar un desvío estándar del estimador igual a $d$ implica que, con un 95% de confianza, el error de nuestra estimación ($|\bar{X}(n) - \mu|$) será menor a $1.96 \cdot d$.

### Algoritmos de actualización recursiva

Para implementar el criterio de parada, el programa debe recalcular la media y la varianza en cada paso. Guardar millones de datos en memoria para calcular el promedio al final es ineficiente. Por eso, usamos fórmulas recursivas que actualizan los valores usando solo el dato anterior y el nuevo valor $X_{n+1}$.

#### Fórmulas de actualización

- **Media recursiva:** $$\bar{X}(n+1) = \bar{X}(n) + \frac{X_{n+1} - \bar{X}(n)}{n+1}$$.
- **Varianza recursiva:** $$S^2(n+1) = \left( 1 - \frac{1}{n} \right) S^2(n) + (n+1) (\bar{X}(n+1) - \bar{X}(n))^2$$.

> [!code] Estructura del algoritmo (Pseudo-Python)
> 
> ````
> def Media_Muestral_X(d):
>     # Inicialización con el primer dato
>     Media = simular_X()
>     Scuad, n = 0, 1 # Varianza inicial S^2(1) = 0
>  
>     while n <= 100 or sqrt(Scuad / n) > d:
>         n += 1
>         X_nuevo = simular_X()
>         MediaAnt = Media
>         # Actualización recursiva
>         Media = MediaAnt + (X_nuevo - MediaAnt) / n
>         # Nota: la fórmula usa el n actual y el MediaAnt
>         Scuad = Scuad * (1 - 1/(n-1)) + n * (Media - MediaAnt)**2
>  
>     return Media
> ````

#### Variación: Estimación de una proporción (Bernoulli)

Si lo que queremos es estimar la probabilidad $p$ de un evento (ej. "¿se rompe la máquina?"), cada simulación $X_i$ vale 1 si ocurre y 0 si no.

- **Varianza específica:** En el caso Bernoulli, la varianza es $p(1-p)$. Usamos nuestra media actual como estimador: $\hat{\sigma}^2 = \bar{X}(n)(1 - \bar{X}(n))$.
- **Criterio de corte:** Se simula mientras $\sqrt{\frac{\bar{X}(n)(1-\bar{X}(n))}{n}} > d$.

> [!tip] Para proporciones, no necesitás la fórmula compleja de $S^2$. Simplemente actualizás la media recursivamente y calculás la varianza directamente con $\bar{X}(n) \cdot (1 - \bar{X}(n))$ en cada iteración.

---

**Mini-glosario:**

- **$\bar{X}(n)$:** Media muestral, nuestro estimador puntual del valor esperado.
- **$S^2(n)$:** Varianza muestral, mide qué tan dispersos están nuestros datos simulados.
- **$d$:** Valor de tolerancia o precisión que define cuándo la estimación es "suficientemente buena".

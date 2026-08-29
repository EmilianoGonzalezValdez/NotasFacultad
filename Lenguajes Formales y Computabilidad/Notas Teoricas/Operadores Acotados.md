
---
### Sumatoria, Productoria y Concatenatoria Acotada

Estos operadores permiten iterar una función sobre un rango finito de números naturales $[x, y]$. Si tenemos una función $f$ que es $PR^\Sigma$, las funciones que resultan de sumar, multiplicar o concatenar sus valores en un rango acotado también pertenecen a la clase $PR^\Sigma$.

#### Definición y Lema de la Sumatoria

Sea $f$ una función con dominio rectangular y valores en $\omega$ (o $\Sigma^*$), definimos los operadores como:

- **Sumatoria:** $\sum_{t=x}^{y} f(t, \vec{x}, \vec{\alpha})$ devuelve 0 si $x > y$, y la suma acumulada en caso contrario.
- **Productoria:** $\prod_{t=x}^{y} f(t, \vec{x}, \vec{\alpha})$ devuelve 1 si $x > y$, y el producto acumulado en caso contrario.
- **Concatenatoria:** $\subset_{t=x}^{y} f(t, \vec{x}, \vec{\alpha})$ devuelve $\epsilon$ si $x > y$, y las palabras pegadas una tras otra en caso contrario.

> [!success] Lema 23 (Lema de la sumatoria) Si $f$ es $PR^\Sigma$, entonces las funciones obtenidas por sumatoria, productoria y concatenatoria acotada también son **$PR^\Sigma$**.

#### Uso Práctico en Ejercicios

Para probar que una función compleja es $PR^\Sigma$ usando estos operadores, el procedimiento es:

1. **Encontrar la función base ($f$):** Identificar qué es lo que se está sumando o multiplicando en cada paso.
2. **Verificar que $f$ sea $PR^\Sigma$:** Generalmente es una composición de funciones iniciales o ya probadas.
3. **Definir los límites:** El rango de la sumatoria debe estar acotado por variables de la entrada o funciones $PR^\Sigma$.
4. **Concluir:** Invocar el Lema 23 para asegurar que el resultado final es $PR^\Sigma$.

> [!example] Ejemplo: Potencia $x^y$ La potencia se puede ver como una productoria: $x^y = \prod_{t=1}^{y} x$. Como la función constante $x$ (proyección) es $PR^\Sigma$, la productoria acotada garantiza que la potencia también lo es.

### Cuantificación Acotada y Predicados

La cuantificación acotada nos permite verificar si una propiedad se cumple para _todos_ ($\forall$) o para _al menos uno_ ($\exists$) de los elementos en un rango finito. Es la herramienta principal para construir predicados lógicos complejos.

#### Definición y Lema de Cuantificación

Dada una propiedad (predicado) $P$ que es $PR^\Sigma$, podemos definir:

- **Universal ($\forall$):** $(\forall t \in \bar{S})_{t \le x} P(t, \vec{x}, \vec{\alpha})$ vale 1 si $P$ es verdadero para todo $t$ en el conjunto $\bar{S}$ menor o igual a $x$.
- **Existencial ($\exists$):** $(\exists t \in \bar{S})_{t \le x} P(t, \vec{x}, \vec{\alpha})$ vale 1 si existe al menos un $t$ que cumpla la condición.

> [!important] Lema 24 Si el predicado $P$ y el conjunto de búsqueda $\bar{S}$ son $PR^\Sigma$, entonces los predicados obtenidos por cuantificación acotada (tanto numérica como alfabética) son **$PR^\Sigma$**.

> [!warning] La Trampa de lo Infinito La cuantificación **no acotada** (sobre todo el conjunto $\omega$ o $\Sigma^*$) **no preserva** la propiedad de ser $PR^\Sigma$. Esto se debe a que un humano no podría revisar infinitos casos en tiempo finito para dar una respuesta.

### Uso Práctico: Regla CP (Caracterizar Pertenencia)

Cuando tenés que probar que un conjunto $S$ es $PR^\Sigma$, lo más efectivo es usar la **Regla CP**.

**Procedimiento:**

1. **Definir la condición:** Escribir $(x, \alpha) \in S \iff \dots$ usando lenguaje matemático.
2. **Acotar la búsqueda:** Si la definición usa un "existe", buscá una cota superior natural (por ejemplo, si buscás un divisor de $x$, sabés que no puede ser mayor que $x$).
3. **Componer:** Mostrar que la condición es una combinación de predicados $PR^\Sigma$ y cuantificadores acotados.

> [!example] Ejemplo: El predicado "x es primo" Se puede caracterizar como: $x > 1 \wedge (\forall t \in \omega)_{t \le x} (t = 1 \vee t = x \vee \neg(t \text{ divide } x))$. Como todas las piezas (comparación, disyunción, división acotada) son $PR^\Sigma$, ser primo es un predicado $PR^\Sigma$.

---


---
### El Pegamento Funcional: Composición

La **composición** es el constructor más intuitivo: consiste en usar el resultado de una o varias funciones como entrada de otra. En el contexto de funciones $\Sigma$-mixtas, debemos ser cuidadosos con los **tipos** para que la "tubería" de datos encaje perfectamente.

Dada una función $f$ de tipo $(n, m, s)$ y una lista de funciones $f_1, \dots, f_{n+m}$, la composición $f \circ [f_1, \dots, f_{n+m}]$ se define como:

- **Dominio:** Es el conjunto de entradas $(\vec{x}, \vec{\alpha})$ tales que cada $f_i$ está definida para esa entrada, y la $(n+m)$-upla resultante de los valores $(f_1, \dots, f_{n+m})$ cae dentro del dominio de $f$.
- **Regla:** $f \circ [f_1, \dots, f_{n+m}](\vec{x}, \vec{\alpha}) = f(f_1(\vec{x}, \vec{\alpha}), \dots, f_{n+m}(\vec{x}, \vec{\alpha}))$.

> [!info] Tipado Correcto Para que la composición no sea la función vacía, las primeras $n$ funciones ($f_1, \dots, f_n$) deben devolver números ($\#$) y las siguientes $m$ funciones ($f_{n+1}, \dots, f_{n+m}$) deben devolver palabras ($*$).

### El Motor Inductivo: Recursión Primitiva

La **Recursión Primitiva (RP)** es la herramienta para definir funciones mediante inducción. Nos permite calcular el valor de una función para un dato "grande" basándonos en el valor que tomó para un dato "más chico". Dependiendo de si la variable que comanda la inducción es un número o una palabra, y de si el resultado es un número o una palabra, tenemos cuatro variaciones.

#### Recursión sobre Variable Numérica

Se usa para funciones que dependen de un parámetro $t \in \omega$. Necesitamos una función base $f$ (para el caso $t=0$) y una función de paso $g$ (que dice cómo saltar de $t$ a $t+1$).

- **Valores Numéricos ($R(f, g) \to \omega$):**
    1. $R(f, g)(0, \vec{x}, \vec{\alpha}) = f(\vec{x}, \vec{\alpha})$
    2. $R(f, g)(t+1, \vec{x}, \vec{\alpha}) = g(R(f, g)(t, \vec{x}, \vec{\alpha}), t, \vec{x}, \vec{\alpha})$.
- **Valores Alfabéticos ($R(f, g) \to \Sigma^*$):**
    1. $R(f, g)(0, \vec{x}, \vec{\alpha}) = f(\vec{x}, \vec{\alpha})$
    2. $R(f, g)(t+1, \vec{x}, \vec{\alpha}) = g(t, \vec{x}, \vec{\alpha}, R(f, g)(t, \vec{x}, \vec{\alpha}))$.

> [!example] Ejemplo: Suma como RP La suma $\lambda tx [t+x]$ se define con $f = p_{1,0}^1$ (caso base: $0+x=x$) y $g = Suc \circ p_{3,0}^1$ (paso: $(t+1)+x = Suc(t+x)$).

#### Recursión sobre Variable Alfabética

Se usa cuando la inducción sigue la estructura de las palabras en $\Sigma^*$. Aquí el paso inductivo requiere una **familia $\Sigma$-indexada de funciones** $G = {G_a : a \in \Sigma}$, es decir, una función de paso distinta por cada símbolo del alfabeto,.

- **Valores Numéricos ($R(f, G) \to \omega$):**
    1. $R(f, G)(\vec{x}, \vec{\alpha}, \epsilon) = f(\vec{x}, \vec{\alpha})$
    2. $R(f, G)(\vec{x}, \vec{\alpha}, \alpha a) = G_a(R(f, G)(\vec{x}, \vec{\alpha}, \alpha), \vec{x}, \vec{\alpha}, \alpha)$.
- **Valores Alfabéticos ($R(f, G) \to \Sigma^*$):**
    1. $R(f, G)(\vec{x}, \vec{\alpha}, \epsilon) = f(\vec{x}, \vec{\alpha})$
    2. $R(f, G)(\vec{x}, \vec{\alpha}, \alpha a) = G_a(\vec{x}, \vec{\alpha}, \alpha, R(f, G)(\vec{x}, \vec{\alpha}, \alpha))$.

> [!tip] Regla de Cosmética Para que las funciones encajen en los moldes de RP, a veces necesitamos renombrar variables. La **Regla de Cosmética** dice que podemos cambiar los nombres de las variables en una expresión $\lambda$ sin alterar la función que representa.

### Propiedad de Robustez

Un resultado fundamental (que constituye parte de los **Combos de Teoremas**) es que estos constructores preservan la computabilidad efectiva: si las funciones de entrada ($f, g, G_a$) son $\Sigma$-efectivamente computables, entonces la función resultante por composición o recursión primitiva también lo es.

---



---
### El Motor de las Pruebas: La Regla de Inducción

La inducción es el método fundamental para demostrar que una propiedad vale para **todos** los números naturales ($\omega$). Dado que la computabilidad se basa en pasos discretos (pasos de una máquina, líneas de un programa o constructores de funciones), casi todas nuestras demostraciones "vencen a Leibniz" usando esta lógica.

#### La Regla de Inducción Estándar

Supongamos que tenemos una sucesión de enunciados $Enu_0, Enu_1, Enu_2, \dots$ que queremos probar como verdaderos. La regla nos dice que basta con cumplir dos tareas concretas:

1. **Caso Base:** Probar que $Enu_0$ es verdadero.
2. **Paso Inductivo:** Probar que para cada $n \in \omega$, si asumimos que $Enu_n$ es verdadero (Hipótesis Inductiva), entonces podemos demostrar que $Enu_{n+1}$ también lo es.

> [!tip] Inducción desde $n_0$ No siempre empezamos desde el cero. Si una propiedad vale solo a partir de un número fijo $n_0$, el caso base será $Enu_{n_0}$ y el paso inductivo se prueba para todo $n \ge n_0$.

#### La Regla de Inducción Completa

A veces, saber que la propiedad vale para $n$ no es suficiente para saltar al $n+1$. En esos casos usamos la **Inducción Completa**.

- **Diferencia clave:** En el paso inductivo, en lugar de suponer que solo $Enu_n$ es cierto, suponemos que **todos** los enunciados anteriores ($Enu_j$ para cada $j \le n$) son verdaderos.
- **Uso común:** Es vital para demostrar el _Teorema Fundamental de la Aritmética_ (existencia de la codificación) porque un número no se construye solo sumándole 1 al anterior, sino multiplicando factores más chicos.

> [!example] Ejemplo: Primos y Factores Para probar que todo $n \ge 2$ se descompone en primos, si $n+1$ no es primo, se descompone en $a \cdot b$. Como $a, b \le n$, la Hipótesis Inductiva Completa nos asegura que $a$ y $b$ ya tienen su descomposición, y así probamos $n+1$.

### Aplicación en Computabilidad

En esta materia, la inducción no es solo para fórmulas matemáticas; se aplica a la **estructura** de los objetos:

- **Inducción sobre Programas:** Probamos que una propiedad vale para programas de 1 instrucción, y luego que si vale para programas de $n$ instrucciones, vale para los de $n+1$.
- **Inducción sobre Funciones Recursivas:** Probamos que algo vale para las funciones iniciales y luego que los constructores (composición, recursión) preservan esa propiedad.

> [!info] La Ficción de la Prueba Al hacer una inducción, creamos una "ficción" donde los objetos cumplen las hipótesis. Dentro de esa película, el Principio de Inducción es el que nos permite concluir que el resultado es una verdad universal.

---

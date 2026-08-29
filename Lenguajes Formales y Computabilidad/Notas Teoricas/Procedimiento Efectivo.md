
---
### Definición y Propiedades del Método Mecánico

Un **procedimiento efectivo** es la formalización de la idea de "receta" o "algoritmo manual". Se trata de una secuencia de pasos para realizar una tarea determinada que debe ser **precisa**, **inambigua** y **repetible**. La "gracia" es que si hacés el procedimiento dos veces con el mismo dato de entrada, las ejecuciones deben ser idénticas: hacés las mismas tareas y en el mismo orden.

Para que un procedimiento $P$ sea considerado "efectivo", debe cumplir estas cinco características:

1. **El Intérprete Humano:** El ejecutor es una persona que trabaja exclusivamente con **lápiz y papel**, contando con estos recursos de forma ilimitada.
2. **Tareas Simples:** Cada paso que el procedimiento ordene debe ser tan sencillo que cualquier persona lo pueda realizar de forma efectiva y fácil.
3. **Mecanicidad:** No es necesario "entender" qué se está haciendo para llegar al resultado; basta con seguir las instrucciones de forma ciega.
4. **Criterio de Terminación:** Al arrancar con un dato de entrada, solo existen dos caminos posibles:
    - **Se detiene:** El procedimiento para y devuelve un dato de salida.
    - **No se detiene:** El proceso sigue pidiendo realizar nuevas tareas de forma sucesiva e indefinida (entra en un "loop" infinito).
5. **Dominio Definido:** Las entradas deben ser objetos $\Sigma$-mixtos, es decir, de la forma $\omega^n \times \Sigma^{*m}$.

> [!info] El conjunto de salida Mientras que el conjunto de entrada es claro, el **conjunto de datos de salida** de un procedimiento puede ser muy difícil o incluso imposible de determinar con precisión en términos generales.

#### Uso Práctico: El ejemplo de la Suma Escolar

El procedimiento efectivo más famoso es el método para **sumar números naturales** en notación decimal que nos enseñaron en la escuela.

- **Entrada:** Dos números naturales ($\omega^2$).
- **Procedimiento:** Alinear los números, sumar columna por columna y "llevarse" una unidad a la columna siguiente si la suma supera 9.
- **Efectividad:** Solo usás lápiz, papel y reglas mecánicas. No necesitás ser un experto en teoría de números para obtener el resultado correcto.

> [!tip] La colgada es legal Acordate que un procedimiento que nunca para (que "no se detiene") es un procedimiento efectivo perfectamente válido. Simplemente nos está diciendo que para esa entrada no hay una respuesta finita.

> [!example] Procedimientos típicos
> 
> - Restar 1 a un número no nulo ($x - 1$).
> - Comparar dos palabras para ver cuál es menor.
> - Contar la longitud de una palabra borrando símbolos de a uno.

---


---
### El Concepto de Computabilidad en Funciones

Una función **$\Sigma$-mixta** se dice **$\Sigma$-efectivamente computable** si existe un _procedimiento efectivo_ $P$ capaz de resolverla. Este concepto une la abstracción matemática de la función (el conjunto de pares ordenados) con la realidad física del cálculo manual.

Decimos que un procedimiento $P$ **computa** a una función $f: D_f \subseteq \omega^n \times \Sigma^{_m} \to O$ (donde $O$ es $\omega$ o $\Sigma^*$) si se cumplen estrictamente estas cuatro condiciones:

1. **Datos de entrada:** El conjunto de entradas de $P$ coincide con el tipo del dominio de la función ($\omega^n \times \Sigma^{*m}$).
2. **Datos de salida:** El resultado que devuelve $P$ pertenece al conjunto de llegada $O$ (números o palabras).
3. **Convergencia (Éxito):** Si tomamos una entrada $(x, \alpha)$ que está en el dominio ($Df$), el procedimiento **debe detenerse** y devolver exactamente el valor $f(x, \alpha)$.
4. **Divergencia (Colgada legal):** Si la entrada $(x, \alpha)$ **no está** en el dominio, el procedimiento **no debe detenerse nunca**.

> [!danger] La importancia de la "colgada" Para Leibniz, que una función sea computable exige que el procedimiento sea "sincero": si la función no está definida para un dato, el procedimiento debe entrar en un bucle infinito. Si el procedimiento se detuviera y diera un error o un resultado cualquiera, **no estaría computando** a esa función específica.

#### Uso Práctico: Ejemplos de Computabilidad Efectiva

Para probar que una función es $\Sigma$-efectivamente computable en un examen, debemos ser capaces de describir (aunque sea coloquialmente) el procedimiento manual:

- **Suma ($\lambda xy [x+y]$):** Es efectivamente computable porque el método escolar de alinear columnas y "llevarse una" es un procedimiento efectivo que siempre da la suma.
- **Sucesor ($Suc$):** Basta con sumarle 1 al número usando el algoritmo decimal.
- **Predecesor ($Pred$):** Si la entrada es 0, el procedimiento debe entrar en un bucle infinito (ya que $Pred(0)$ es indefinido). Si es $x > 0$, se aplica el algoritmo de resta escolar para obtener $x-1$.
- **Longitud de palabra ($\lambda \alpha [|\alpha|]$):** Se puede computar borrando símbolos de a uno y sumando 1 a un contador cada vez, hasta que la palabra sea $\epsilon$.

> [!info] Leibniz vence a todos En la jerga de la materia, decimos que **"Leibniz vence a Turing"** (o a Neumann/Gödel) para expresar que cualquier función que pueda ser calculada por un modelo formal (como una Máquina de Turing) es, por definición, efectivamente computable para un humano con los pasos adecuados.

> [!warning] La función vacía ($\emptyset$) La función vacía es $\Sigma$-efectivamente computable para cualquier alfabeto. El procedimiento es simple: no detenerse nunca, independientemente de la entrada.

---

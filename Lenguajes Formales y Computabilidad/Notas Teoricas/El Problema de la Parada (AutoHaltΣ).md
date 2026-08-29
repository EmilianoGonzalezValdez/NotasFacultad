
---

En esta nota abordamos el resultado más famoso de la computabilidad: la demostración de que existen problemas que ninguna máquina (ni humana ni electrónica) puede resolver. El **Problema de la Parada** se formaliza mediante el predicado $AutoHalt_\Sigma$.

Para que este predicado tenga sentido, suponemos que el alfabeto es lo suficientemente grande como para que los programas sean palabras válidas del mismo ($\Sigma \supseteq \Sigma_p$). Esto nos permite pasar un programa como argumento a otro programa.

**Definición formal:** $$AutoHalt_{\Sigma} = \lambda P [ (\exists t \in \omega) Halt_{0,1}(t,P,P) ]$$

- **Dominio:** $Pro_\Sigma$ (el conjunto de todos los programas del lenguaje).
- **Interpretación:** El predicado vale 1 si el programa $P$ se detiene al ser ejecutado con su propio código fuente como entrada (estado initial $|P|$), y vale 0 si se queda "colgado" para siempre.

> [!danger] La trampa de la cuantificación Notá que $AutoHalt_\Sigma$ usa un cuantificador existencial **no acotado** ($\exists t$). A diferencia del predicado $Halt$ (que es $p.r.$ porque el tiempo es un dato), acá tenemos que buscar en _todo_ el tiempo infinito. Esto es lo que lo hace "sospechoso" de no ser computable.

#### Demostración de Indecidibilidad (Lema 6)

El teorema fundamental establece que **$AutoHalt_\Sigma$ no es $\Sigma$-recursivo**. La prueba se realiza por el absurdo mediante una técnica llamada _diagonalización_:

1. **Suposición:** Supongamos que $AutoHalt_\Sigma$ _es_ $\Sigma$-recursivo.
2. **Construcción:** Si es recursivo, por el **Segundo Manantial de Macros** existe un macro legal en $S_\Sigma$ para usarlo. Diseñamos entonces el programa paradójico $P_0$:
    
    ```
    L1 [ IF AutoHaltΣ(P1) GOTO L1 ]
    ```
    
3. **Análisis:** ¿Qué pasa si corremos $P_0$ con su propio código ($P_1 = P_0$)?
    - Si $AutoHalt_\Sigma(P_0) = 1$ (debería parar): El macro dice "sí", salta a `L1` y entra en un bucle infinito. **Contradicción** (no paró).
    - Si $AutoHalt_\Sigma(P_0) = 0$ (no debería parar): El macro dice "no", el programa sigue de largo y termina (SKIP implícito). **Contradicción** (sí paró).
4. **Conclusión:** Como ambas opciones llevan a un absurdo, nuestra suposición inicial era falsa: el predicado no puede ser recursivo.

#### Imposibilidad Efectiva y Tesis de Church

Este resultado matemático tiene un impacto total en la realidad gracias a la **Tesis de Church**.

- **Teorema 7:** $AutoHalt_\Sigma$ no es $\Sigma$-efectivamente computable.
- **Significado práctico:** No importa cuánto avance la tecnología o qué lenguaje de programación inventemos; **jamás** existirá un algoritmo o procedimiento efectivo capaz de decirnos si un programa cualquiera va a terminar o no.

> [!info] Ejemplo de límite absoluto Este es el ejemplo natural de que la cuantificación no acotada de un predicado recursivo primitivo ($Halt$) puede dar como resultado algo que no es computable por el hombre.

---


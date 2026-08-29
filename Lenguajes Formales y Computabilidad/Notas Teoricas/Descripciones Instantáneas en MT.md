
---
### La "Foto" del Cómputo: Sintaxis y Semántica de la DI

Para formalizar el funcionamiento de una Máquina de Turing (MT), usamos las **Descripciones Instantáneas (DI)**. Una DI es una palabra que condensa tres datos clave: el contenido de la cinta, la posición del cabezal y el estado actual de la máquina.

Se escribe como una palabra de la forma $\alpha q \beta$, donde:

- **$q \in Q$**: Es el estado actual de la máquina.
- **$\alpha \in \Gamma^*$**: Representa lo que hay en la cinta a la **izquierda** del cabezal.
- **$\beta \in \Gamma^*$**: Representa lo que hay en la cinta desde la posición del cabezal hacia la **derecha**.

> [!info] ¿Dónde está parado el cabezal? Por convención, el cabezal siempre está leyendo el **primer símbolo de $\beta$**. Si $\beta = \epsilon$ (palabra vacía), el cabezal está leyendo un símbolo **blanco** ($B$). En resumen, el símbolo escaneado es $[\beta B]_1$.

#### Regla de Unicidad y Función Piso ($\lfloor \dots \rfloor$)

Para que a cada situación real de la máquina le corresponda **una única** DI, exigimos que $\beta$ no termine en el símbolo blanco $B$ (a menos que sea $\epsilon$). Para mantener las palabras "limpias", usamos la función **Piso** ($\lfloor \dots \rfloor$), que elimina todos los blancos del final de una palabra:

- $\lfloor \epsilon \rfloor = \epsilon$
- $\lfloor \alpha \sigma \rfloor = \alpha \sigma$ (si $\sigma \neq B$)
- $\lfloor \alpha B \rfloor = \lfloor \alpha \rfloor$

### El Movimiento de la Máquina: La Relación $\vdash$

La relación de transición elemental ($\vdash$) define cómo pasamos de una foto ($d_1$) a la siguiente ($d_2$) en un solo paso, basándonos en la función de transición $\delta$.

Si tenemos $d_1 = \alpha p \beta$, el comportamiento depende de $\delta(p, [\beta B]_1) = (q, \sigma, m)$:

1. **Caso Derecha ($R$):** La máquina escribe $\sigma$, se mueve a la derecha y pasa al estado $q$. $$d_2 = \alpha \sigma q \text{ } ↷\beta$$
2. **Caso Izquierda ($L$):** Si el cabezal **no** está en la primera casilla ($\alpha \neq \epsilon$), escribe $\sigma$, se mueve a la izquierda y pasa a $q$. $$d_2 = \lfloor \alpha↶ q \text{ } [\alpha]_{|\alpha|} \sigma \text{ } ↷\beta \rfloor$$
3. **Caso Quieto ($K$):** Escribe $\sigma$, se queda en el lugar y pasa a $q$. $$d_2 = \lfloor \alpha q \sigma \text{ } ↷\beta \rfloor$$

> [!warning] El límite izquierdo Si la máquina recibe la orden de moverse a la izquierda ($L$) pero está en la primera casilla de la cinta ($\alpha = \epsilon$), la máquina **no puede hacer nada y se detiene**.

#### Cómputo y Relación Estrellada ($\vdash^*$)

Para hablar de una ejecución completa (muchos pasos), usamos estas notaciones:

- **$d \vdash^n d'$**: Significa que la máquina llega de la configuración $d$ a $d'$ en exactamente $n$ pasos.
- __$d \vdash^* d'$_*: Es la relación "estrellada". Significa que existe algún $n \in \omega$ tal que $d \vdash^n d'$. Representa el hecho de que $d'$ es alcanzable desde $d$ tras un tiempo finito de cómputo.

### Criterio de Detención

Decimos que una Máquina de Turing **se detiene** partiendo de una DI $d$ si llega a una configuración $d'$ desde la cual no hay ninguna transición posible ($d' \nvdash d''$ para todo $d''$).

Esto pasa en dos situaciones:

1. **Por falta de instrucción:** El par (estado, símbolo leído) no pertenece al dominio de $\delta$.
2. **Por movimiento imposible:** La instrucción pide ir a la izquierda ($L$) pero el cabezal está en la primera casilla ($\alpha = \epsilon$).

> [!example] Ejemplo de paso a paso Si $\delta(q_0, a) = (q_1, B, R)$, entonces la DI $a q_0 a b$ pasará en un paso a $a B q_1 b$. El cabezal escribió un blanco sobre la 'a', se movió a la derecha y ahora lee la 'b' en estado $q_1$.

---

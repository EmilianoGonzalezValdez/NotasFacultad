
---

En esta nota vamos a desglosar las diferentes formas en las que podemos entender y probar que un conjunto es **$\Sigma$-recursivamente enumerable** ($\Sigma-r.e.$). Este tema es central porque conecta la capacidad de "listar" elementos con la noción de ser el "dominio" de una función, lo que nos da herramientas variadas para enfrentar ejercicios según lo que nos convenga.

### El Teorema de las 4 Caras (Teorema 5)

Este teorema establece que, para cualquier conjunto $S \subseteq \omega^n \times \Sigma^{*m}$, las siguientes cuatro afirmaciones son equivalentes. Esto significa que si probás cualquiera de ellas, ya demostraste que el conjunto es $\Sigma-r.e.$:

1. **$S$ es $\Sigma$-recursivamente enumerable:** Existe una función recursiva que lo enumera (definición original).
2. **$S$ es la imagen de una función recursiva ($S = I_F$):** Existe una función $F$ cuyos componentes son todos recursivos tal que su imagen es exactamente $S$.
3. **$S$ es el dominio de una función recursiva ($S = D_f$):** Existe una función recursiva $f$ que está definida "justo" para los elementos de $S$ y se cuelga para el resto.
4. **$S = \emptyset$ o $S$ es la imagen de una función $\Sigma$-p.r.:** Esta es la versión más restrictiva; alcanza con una función primitiva recursiva para listar un conjunto enumerable.

> [!success] La cara más útil para las pruebas La equivalencia **(1) $\iff$ (3)** es la que más vas a usar. Para probar que un conjunto es r.e., te basta con mostrar que es el **dominio de una función recursiva**. Si lográs definir una función (o programa) que termine para los elementos de $S$ y no para los demás, ya ganaste.

#### Procedimiento para probar (2) $\implies$ (3)

Si tenés un conjunto que es la imagen de una función recursiva $F$, para probar que es el dominio de otra función $f$, el procedimiento consiste en crear un programa que realice una **búsqueda sistemática**:

1. Recibís un candidato $e$.
2. Generás un bucle que recorra todos los posibles índices $x = 0, 1, 2, \dots$.
3. Para cada $x$, calculás $F(x)$ y comparás el resultado con tu candidato $e$.
4. Si encontrás un $x$ tal que $F(x) = e$, el programa se detiene (aceptando a $e$ en su dominio).
5. Si $e$ no está en la imagen, el programa se quedará buscando para siempre, lo que es correcto para la definición de dominio.

### Relación entre Enumerabilidad y Decidibilidad (Lema 4)

Un resultado fundamental de este pilar es que un conjunto es **$\Sigma$-recursivo** (decidible) si y solo si tanto él como su **complemento** son $\Sigma-r.e.$.

$$S \in \Sigma-rec \iff S \in \Sigma-r.e. \text{ y } ((\omega^n \times \Sigma^{*m}) - S) \in \Sigma-r.e.$$

> [!tip] La técnica de las dos listas (Paralelismo) Si sabés que $S$ y $\bar{S}$ son enumerables, tenés dos "maquinitas" que listan elementos. Para decidir si un dato $x$ está en $S$, el algoritmo es:
> 
> 1. Ponés a correr los dos enumeradores al mismo tiempo (o alternando un paso cada uno).
> 2. Como $x$ tiene que estar en una de las dos listas (porque $S \cup \bar{S} = Universo$), tarde o temprano va a aparecer.
> 3. Si aparece en la lista de $S$, decís "SÍ" (1). Si aparece en la de $\bar{S}$, decís "NO" (0).
> 4. Como el proceso siempre termina, acabás de construir una función característica recursiva total.

> [!warning] La trampa de la enumerabilidad Recordá siempre que todo conjunto recursivo es r.e., pero **no todo r.e. es recursivo**. El conjunto $A$ (Aceptación) será nuestro ejemplo estrella de un conjunto que se puede listar pero no se puede decidir.

---

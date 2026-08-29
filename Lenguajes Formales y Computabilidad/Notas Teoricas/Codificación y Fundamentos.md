
---

Esta nota establece las bases matemáticas y la notación técnica necesaria para formalizar la computabilidad. Su objetivo es definir los objetos con los que trabajamos (números y palabras) y, sobre todo, cómo construir un **puente** entre ellos mediante la codificación.

### [[Sintaxis y el Universo de Objetos Matemáticos]]

Antes de operar, necesitamos definir el tablero. En esta materia, trabajamos con un enfoque **orientado a objetos**, donde cada elemento tiene un tipo disjunto y bien definido.

- **Alfabetos y Palabras ($\Sigma$ y $\Sigma^*$):** Definimos $\Sigma$ como un conjunto finito de símbolos y $\Sigma^*$ como el conjunto de todas las palabras posibles, incluyendo la _palabra vacía_ $\epsilon$.
- **Categorías Disjuntas:** Es fundamental entender que un **Número** ($\omega$), una **Palabra**, un **Conjunto**, una **n-upla** y una **Infinitupla** son objetos de distinta naturaleza; nunca se mezclan ni se confunden (por ejemplo, $0 \neq \emptyset \neq \epsilon \neq \diamond$).
- **Numerales:** Distinguimos entre el concepto matemático de número y el símbolo (numeral) que lo representa en una cinta o programa, concretamente, un numeral sera la palabra que denota al número referido. Si tengo el número 5, su numeral será **5, (cinco)**. donde cualquiera de las 2 formas referirá a la palabra/símbolo que denota al número 

> [!note] El rol de $\omega$ Usamos el símbolo $\omega$ para denotar el conjunto de los números naturales incluyendo el cero ($\mathbb{N} \cup {0}$).

### [[El Lenguaje Sigma-Mixto]]

Es la estructura central de la materia. Permite que las funciones procesen simultáneamente números y palabras, que es la base de cualquier lenguaje de programación real.

- **Funciones $\Sigma$-mixtas:** Son funciones cuyo dominio combina naturales y palabras ($D_f \subseteq \omega^n \times \Sigma^{*m}$) y cuyo resultado es, o bien un número, o bien una palabra.
- **Clasificación por Tipo $(n, m, s)$:** Identificamos las funciones según cuántas entradas de cada tipo reciben y si su salida ($s$) es numérica (#) o alfabética (*).
- **Predicados $\Sigma$-mixtos:** Funciones mixtas cuya imagen está restringida a ${0, 1}$, representando la veracidad o falsedad de una propiedad.

> [!info] Funciones Iniciales Partimos de bloques básicos computables como el Sucesor ($Suc$), Predecesor ($Pred$), Constantes ($C_{n,m}^k$) y Proyecciones ($p_{n,m}^i$).

### [[Inducción|Herramientas de Demostración: Inducción]]

Para probar que un modelo de computación es equivalente a otro, recurrimos a la estructura de los números naturales.

- **Regla de Inducción:** Probar para el caso base y demostrar que si vale para $n$, vale para $n+1$.
- **Inducción Completa:** Útil cuando la prueba de un caso requiere apoyarse en _todos_ los casos anteriores, no solo en el inmediato.

### [[Codificación, Infinituplas y Ordenes Naturales]]

Esta es la parte técnica más pesada pero la más importante. Permite tratar cualquier estructura compleja como un simple número natural.

- **Codificación de Infinituplas ($\langle ... \rangle$):** Usamos el _Teorema Fundamental de la Aritmética_ para asignar a cada secuencia finita de números un único número natural mediante el producto de potencias de primos.
- **Descodificación y Longitud:** Definimos la "bajada i-ésima" $(x)_i$ para recuperar el dato original y la función $Lt(x)$ para saber cuántos elementos hay codificados.
- __Órdenes Naturales ($\#_\le$ y $*_\le$):_* Establecemos biyecciones entre palabras y números. Esto nos permite decir, por ejemplo, que la palabra $\alpha$ es "la número n" de una lista infinita ordenada de forma lexicográfica.

---

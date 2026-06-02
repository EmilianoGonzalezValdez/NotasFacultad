
# Teoría de Macros en $S_\Sigma$

Un **macro** es un "molde" de programa que permite simular instrucciones complejas que no existen de forma básica en el lenguaje $S_\Sigma$. Esta técnica es fundamental para la computabilidad, ya que permite reutilizar lógica (como sumas, productos o comparaciones) garantizando que la función resultante siga siendo computable en el paradigma imperativo.

### Concepto de Macro y Expansión

Desde un punto de vista formal, un macro es simplemente una palabra (una secuencia de instrucciones) donde ciertas variables y etiquetas actúan como parámetros.

- **Expansión:** Es el proceso de reemplazar los componentes del macro por variables y etiquetas concretas para insertarlas en un programa principal.
- **Simulación:** Decimos que un macro "simula" una instrucción compleja si, al ejecutarse la expansión, el estado final de las variables coincide con el resultado esperado de dicha instrucción sin generar efectos colaterales no deseados.

### Estructura del Macro: Variables y Labels

Para que un macro funcione correctamente dentro de cualquier programa, sus componentes se dividen en dos categorías según su rol durante la expansión:

#### Componentes Oficiales vs. Auxiliares

- **Variables/Labels Oficiales ($V1, W1, A1$):** Son los parámetros del macro. Durante la expansión, se reemplazan por las variables "protagonistas" del programa (las que contienen las entradas o el destino de un salto).
- **Variables/Labels Auxiliares ($V4, A2$):** Son elementos necesarios para el funcionamiento interno del macro (contadores, puntos de salto intermedio).
    - **Regla de Seguridad:** Al expandir, estas deben reemplazarse por variables y etiquetas que **no se usen** en ninguna otra parte del programa principal para evitar que el macro "rompa" otros datos.

> [!warning] La importancia del SKIP Por convención, la primera instrucción de un macro nunca debe estar etiquetada. Si necesitamos que la expansión sea el destino de un salto, se suele anteponer un `SKIP` para que sirva de ancla sin alterar la lógica interna.

### Tipos de Macros

Existen dos grandes familias de macros según la tarea que simulan:

#### Macros de Asignación (Asociados a funciones)

Simulan una instrucción de la forma $Nk \leftarrow f(Nn, \dots, Pm)$.

- **Comportamiento:** Si los argumentos están en el dominio de $f$, la expansión debe detenerse y dejar el resultado en la variable destino. Si no están en el dominio, el programa **no debe detenerse** (bucle infinito) para ser fiel a la definición de función parcial.
- **Preservación:** Excepto la variable destino y las auxiliares, ninguna otra variable del programa debe ser modificada.

#### Macros de tipo IF (Asociados a predicados)

Simulan un salto condicional basado en un predicado $P$, denotado como `[IF P(...) GOTO Ln]`.

- **Comportamiento:** Si el predicado es verdadero, la ejecución debe saltar al label oficial ($Ln$); si es falso, el programa debe continuar con la instrucción inmediatamente posterior a la expansión.
- **Transparencia:** Estos macros no deben modificar ninguna variable del programa principal al finalizar su ejecución.

### El Primer Manantial de Macros

Este es el teorema central que justifica el uso de macros en la materia.

> [!success] Primer Manantial de Macros Si una función $f$ (numérica o alfabética) o un predicado $P$ son **$\Sigma$-computables**, entonces existe un macro en $S_\Sigma$ que permite utilizarlos como si fueran instrucciones básicas.

Este resultado es vital porque nos permite "importar" todo lo que probamos en los paradigmas de Turing o Gödel hacia Neumann: si algo es computable de cualquier forma efectiva, podemos usarlo como un bloque de construcción en nuestros programas.

---

**Glosario de Macros**

- **Expansión:** Programa resultante de reemplazar los moldes por variables reales.
- **Variable Protagonista:** Variable del programa principal que interactúa con el macro.
- **Efecto Colateral:** Modificación accidental de una variable que no es el objetivo del macro.


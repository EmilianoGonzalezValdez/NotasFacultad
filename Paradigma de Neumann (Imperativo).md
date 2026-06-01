
Este modelo de computabilidad, desarrollado por Von Neumann, formaliza el concepto de procedimiento efectivo mediante un lenguaje de programación teórico denominado $S_{\Sigma}$. A diferencia de los modelos funcionales, aquí el foco está en la **manipulación de estados** a través de una secuencia de instrucciones.

### [[Sintaxis del Lenguaje]] $S_{\Sigma}$

El lenguaje se construye sobre un alfabeto de programa $\Sigma_{p}$ que incluye numerales, símbolos de asignación ($\leftarrow$), operaciones aritméticas básicas y de control de flujo.

- **Variables Numéricas ($Nk$):** Almacenan números naturales ($x \in \omega$).
- **Variables Alfabéticas ($Pk$):** Almacenan palabras del alfabeto dado ($\alpha \in \Sigma^{*}$).
- **Labels ($Lk$):** Etiquetas numéricas que identifican instrucciones específicas para permitir saltos.

#### Instrucciones y Programas

Existen instrucciones básicas (asignaciones, incrementos, saltos condicionales y SKIP) e instrucciones etiquetadas ($LnI$). Un **programa** es una concatenación de instrucciones que debe cumplir la **Ley de los GOTO**:

> [!danger] Ley de los GOTO Todo tramo final de la forma $GOTO\ Ln$ dentro de una instrucción debe tener un label correspondiente $Ln$ definido en alguna instrucción del programa.

### [[Semántica y Función Sucesora]] $S_{P}$

La semántica define qué sucede durante la ejecución. Se basa en el concepto de **estado**, que es un par de infinituplas $((s_{1}, s_{2}, \dots), (\sigma_{1}, \sigma_{2}, \dots))$ que representan los contenidos de todas las variables en un momento dado.

- **Descripción Instantánea (DI):** Es una terna $(i, \vec{s}, \vec{\sigma})$ donde $i$ indica la instrucción a realizar, y $(\vec{s}, \vec{\sigma})$ es el estado actual.
- **Función $S_{P}$:** Determina la DI sucesora. Si $i$ está fuera del rango del programa, la máquina se detiene.

#### Detención del Programa

Un programa $P$ se detiene partiendo de un estado inicial cuando la primera coordenada de la DI (el puntero de instrucción) alcanza el valor $n(P)+1$.

### [[Funciones Computables|]]Funciones $\Sigma$-computables y Operador $\Psi$

Una función se considera **$\Sigma$-computable** si existe un programa en $S_{\Sigma}$ que la compute. Para formalizar el resultado de un programa, usamos los operadores $\Psi$.

#### Operadores de Salida

- **$\Psi_{n,m,\#}\ P$:** El resultado de la computación es el valor final de la variable $N1$.
- **$\Psi_{n,m,*}\ P$:** El resultado de la computación es el valor final de la variable $P1$.

> [!note] Configuración Inicial El estado inicial estándar para computar una función con $n$ entradas numéricas y $m$ alfabéticas se denota $||x_{1}, \dots, x_{n}, \alpha_{1}, \dots, \alpha_{m}||$, donde el resto de las variables se inicializan en 0 o $\epsilon$.

### [[Ingeniería de Macros y Expansión]]

Un **macro** es un "molde" de programa que permite simular instrucciones complejas (como sumas o comparaciones) que no existen de forma básica en $S_{\Sigma}$.

- **Variables/Labels Oficiales:** Son los parámetros del macro que serán reemplazados por las variables protagonistas del programa principal.
- **Variables/Labels Auxiliares:** Se usan para el funcionamiento interno del macro y deben ser reemplazados por elementos que no se utilicen en ninguna otra parte del programa principal para evitar efectos colaterales.

#### Tipos de Macros

1. **De Asignación:** Simulan una instrucción del tipo $V1 \leftarrow f(V2, \dots)$. Si la función no está definida para la entrada, el macro no debe detenerse.
2. **De Tipo IF:** Simulan un salto condicional basado en un predicado $P$. Si el predicado es verdadero, direcciona al label oficial; si es falso, continúa con la siguiente instrucción.

### [[El Primer Manantial de Macros]]

Este teorema es el puente entre el paradigma funcional y el imperativo. Establece que:

> [!success] Teorema del Manantial Si una función $f$ (o predicado $P$) es $\Sigma$-computable, entonces existe un macro en $S_{\Sigma}$ que permite utilizarla como si fuera una instrucción básica de asignación o salto condicional.

### [[Enumerabilidad y Decisión de Conjuntos]]

Un conjunto $S$ puede relacionarse con el paradigma de Neumann de dos formas:

- **$\Sigma$-computable (Decidible):** Existe un programa que, dado un elemento, devuelve 1 si pertenece a $S$ y 0 si no.
- **$\Sigma$-enumerable:** Existe un programa que puede generar (listar) todos los elementos del conjunto $S$ a partir de entradas naturales.

---

**Glosario de Neumann**

- **Estado:** Infinitupla con los valores de todas las variables.
- **Expansión:** El programa resultante de reemplazar los moldes de un macro por variables y labels concretos.
- **Ley de los GOTO:** Regla sintáctica que obliga a que todo destino de salto exista dentro del programa.
- **Realizarp:** Verbo técnico que significa "realizar la instrucción si es posible o quedarse igual si no lo es".




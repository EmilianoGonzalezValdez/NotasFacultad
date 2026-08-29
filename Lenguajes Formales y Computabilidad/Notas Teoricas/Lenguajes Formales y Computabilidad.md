
---
### La Formalización de la Intuición y sus Límites

El objetivo fundacional de esta materia es proporcionar un **modelo matemático preciso** para la noción intuitiva de _computación_. Esta búsqueda del "piso matemático" nos permite definir qué es computable y, fundamentalmente, demostrar mediante el rigor lógico qué problemas están fuera del alcance de cualquier algoritmo (indecidibilidad).

> [!info] El Desafío: "Vencer a Leibniz" Llamamos **Paradigma de Leibniz** al concepto intuitivo de _procedimiento efectivo_ (métodos mecánicos con papel y lápiz). Los paradigmas de Turing, Gödel y Neumann son formalismos que intentan capturar esa intuición. Se dice que un paradigma "vence a Leibniz" si logra modelar todo lo que intuitivamente consideramos computable.

### Índice de Pilares (Mapa de Contenido)

Esta nota conecta los seis ejes fundamentales de la materia. Cada pilar representa un tema importante de la materia a ser estudiado:

#### Pilar 1: Codificación y Fundamentos

En este nodo se definen las bases de la materia. Sin este lenguaje común, no podríamos mezclar números y palabras en una misma función.

- **Contenidos:** Alfabetos $\Sigma$, palabras $\Sigma^*$, objetos $\Sigma$-mixtos y funciones iniciales.
- **Técnicas clave:** Codificación de infinituplas $\langle s_1, s_2, \dots \rangle$ y órdenes naturales ($\#_\le, *_\le$) para biyectar el mundo de las palabras con el de los números.

#### Pilar 2: Paradigma de Leibniz (El Mundo Intuitivo)

Representa la computabilidad antes del rigor matemático. Es el paradigma filosófico que los otros modelos deben intentar formalizar.

- **Contenidos:** Procedimientos efectivos, funciones $\Sigma$-efectivamente computables y conjuntos decidibles/enumerables.

#### Pilar 3: Paradigma de Turing (El Enfoque Mecánico)

La primera formalización exitosa, basada en la abstracción de una máquina física.

- **Contenidos:** Máquinas de Turing (MT), descripciones instantáneas, aceptación de lenguajes $L(M)$.

#### Pilar 4: Paradigma de Gödel (El Enfoque Funcional)

Un modelo puramente matemático que construye la computabilidad a través de la arquitectura de funciones.

- **Contenidos:** Funciones $\Sigma$-primitivas recursivas ($\Sigma$-p.r.), constructores (composición y recursión) y el operador de minimización $M(P)$ para funciones recursivas generales.

#### Pilar 5: Paradigma de Neumann (El Enfoque Imperativo)

Modela la computación mediante un lenguaje de programación teórico ($S_\Sigma$) cercano a la arquitectura de Von Neumann.

- **Contenidos:** Sintaxis de instrucciones, programas, estados de memoria, macros y el operador de salida $\Psi$.

#### Pilar 6: Teoría de la Computabilidad (Integración y Límites)

El cierre de la materia donde se demuestra que todos los modelos son uno solo y se descubren las fronteras del conocimiento.

- **Contenidos:** Tesis de Church-Turing, teoremas de equivalencia ("batallas" entre paradigmas), el problema de la parada (_AutoHalt_) e indecidibilidad.

> [!success] Tesis de Church-Turing Es el postulado que afirma que los modelos de Turing, Gödel y Neumann son **equivalentes** entre sí y capturan perfectamente la esencia de la computabilidad efectiva de Leibniz.

---


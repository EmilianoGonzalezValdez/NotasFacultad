
---

En este bloque unificamos los tres modelos matemáticos (Turing, Gödel y Neumann) y demostramos que capturan exactamente la misma noción de "computabilidad" que la intuición de Leibniz.

### [[Neumann vence a Godel|Las Batallas de Equivalencia I: Neumann vence a Gödel]]

Esta nota trata sobre cómo el lenguaje imperativo puede replicar todo lo que hace el mundo funcional.

- **Teorema de Neumann vence a Gödel:** Demostración por inducción de que toda función $\Sigma$-recursiva es $\Sigma$-computable.
- **Simulación de Constructores:** Cómo programar la minimización (Caso 1) y la recursión (Caso 2) usando instrucciones de $S_\Sigma$.
- **El Segundo Manantial de Macros:** La justificación legal para usar cualquier función recursiva (suma, producto, etc.) como una instrucción simple en nuestros programas.

### [[Funciones Universales|Funciones Universales de Simulación]] ($i, E, Halt$)

Acá definimos las herramientas para que el paradigma de Gödel pueda "observar" y "describir" lo que pasa dentro de una computadora de Neumann.

- **Funciones de Estado ($i_{n,m}$ y $E_{n,m}$):** Funciones que capturan el número de instrucción y el contenido de las variables tras exactamente $t$ pasos.
- **El Predicado de Parada Acotada ($Halt_{n,m}$):** Definición formal de "parar en $t$ pasos". Es crucial saber que este predicado es **$\Sigma$-recursivo primitivo**.
- **Tiempo de Detención ($T_{n,m}$):** La función de minimización que mide cuánto tarda un programa en terminar. Es recursiva, pero **no** es primitiva recursiva.

### [[Godel Vence a Neumann|Las Batallas de Equivalencia II: Gödel vence a Neumann]]

El cierre del círculo entre el software y las funciones matemáticas.

- **Teorema de Gödel vence a Neumann:** Demostración de que toda función $\Sigma$-computable es $\Sigma$-recursiva.
- **La Simulación Matemática:** Cómo expresar el resultado final de un programa como una composición de funciones de estado y el tiempo de detención.

### [[Fortalecimiento Del Lenguaje|Fortalecimiento del Lenguaje y Aplicaciones Prácticas]]

Cómo el Segundo Manantial y las Funciones Universales permiten crear programas que analizan otros programas.

- **Programas que analizan el tiempo:** Uso de macros de Halt y E para enumerar dominios e imágenes de funciones computables.
- **Enumeración de conjuntos de programas:** Cómo enumerar subconjuntos de ProΣ​ (ej: programas que dan 10 como salida) usando el lenguaje SΣ∪Σp​​.
- **Introducción a la Autorreferencia:** El conjunto A (programas que paran con su propio código) y los teoremas de Recursión de Kleene y Smullyan (programas que se autopropagandean)

### [[Batallas Con Turing|Equivalencia Final y las Batallas con Turing]]

El hardware de cinta entra en el juego de las equivalencias.

- **Gödel vence a Turing:** Toda función Turing-computable es recursiva.
- **Turing vence a Neumann:** Una Máquina de Turing puede simular cualquier programa de $S_\Sigma$.
- **El Teorema de Equivalencia (Teorema 14):** El resultado final que declara el "empate técnico" entre los tres modelos.

### [[Tesis de Church-Turing|La Tesis de Church-Turing]]

La conclusión conceptual que trasciende la matemática.

- **El Postulado:** La afirmación de que toda función efectivamente computable por un humano (Leibniz) es capturada por estos modelos.
- **Consecuencias:** Por qué aceptamos que no existe (ni existirá) un modelo de cómputo más potente que lo que ya vimos.

---

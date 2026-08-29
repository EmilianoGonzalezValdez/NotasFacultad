
Este tema formaliza la computación a través de un modelo mecánico de estados finitos que opera sobre una cinta infinita. Alan Turing propuso este diseño para capturar matemáticamente la noción intuitiva de _procedimiento efectivo_.

### [[Máquina de Turing|La Máquina de Turing (MT) como Objeto Matemático]]

Esta nota define el "hardware" abstracto de la máquina.

- **La 7-upla:** Definición formal de $M = (Q, \Sigma, \Gamma, \delta, q_0, B, F)$.
- **Alfabetos y Estados:** La distinción entre el alfabeto de entrada $\Sigma$ y el de cinta $\Gamma$, y el rol del símbolo blanco $B$.
- **Función de Transición ($\delta$):** Las reglas de movimiento ($L, R, K$) que definen el comportamiento de la máquina,.

### [[Descripciones Instantáneas en MT|Configuración y Semántica: Descripciones Instantáneas (DI)]]

Representa el estado del cómputo en un momento preciso.

- **Sintaxis de la DI:** El formato $\alpha q \beta$ para ubicar el cabezal y el contenido de la cinta.
- **Dinámica de Cómputo:** Las relaciones de transición elemental ($\vdash$) y la relación estrellada ($\vdash^*$) para sucesiones de pasos,,.
- **Criterio de Detención:** Cuándo una máquina para efectivamente por falta de instrucciones o movimientos imposibles.

### [[El Conjunto LM|Aceptación de Lenguajes: El conjunto L(M)]]

Define a la MT como un reconocedor de patrones.

- **Aceptación por alcance:** Una palabra es aceptada si la máquina llega a un estado final $q \in F$,.
- **Lenguaje $L(M)$:** El conjunto de todas las palabras de $\Sigma^*$ que la máquina acepta,.

### [[Cómputo de Funciones en MT|Cómputo de Funciones y el Símbolo Unit (p)]]

Transforma el modelo mecánico en una calculadora de funciones mixtas.

- **Máquina con Unit:** Incorporación del símbolo $p$ para representar números naturales en la cinta ($px$ para el número $x$),.
- **Funciones $\Sigma$-Turing computables:** Configuración de la cinta de entrada y la cinta de salida para obtener el resultado de una función,.

### [[Robustez del Modelo de Turing|El Vínculo con Leibniz: Robustez del Modelo]]

Establece la relación entre la máquina y la intuición filosófica.

- **Leibniz vence a Turing:** La prueba de que cualquier proceso de una MT es un procedimiento efectivo realizable por un humano,.
- **Completitud del Modelo:** La postulación de que el modelo de Turing captura la totalidad de lo computable.

---

Existen **Principios fundamentales** los cuales nos guían en el proceso del diseño:
- Partición y jerarquía
- Abstracción
- Modularidad


***Partición y Jerarquía:*** Se basa en Divide y vencerás. Trata de dividir el problema en varias partes pequeñas manejables, donde cada una de estas debe poder solucionarse y modificarse separadamente del resto. Esta partición del problema determina una jerarquía de componentes en el diseño 

***Abstracción:*** La abstracción de un componente describe el comportamiento externo sin dar detalles de cómo se produce dicho comportamiento, representando a los componentes como cajas negras. Existen:
- Abstracción funcional: Especifica el comportamiento funcional de un modulo, tratando a estos como funciones de entrada y salida
- Abstracción de datos: Los datos se tratan como objetos junto a sus operaciones, las cuales sólo pueden realizarse sobre este mismo objeto. Desde fuera los detalles internos de los objetos permanecen ocultos y sólo sus operaciones son visibles

***Modularidad:*** Un sistema se dice modular si consiste de componentes discretas tal que puedan implementarse separadamente y un cambio a una de ellas apenas tenga un mínimo impacto sobre las otras. Ventajas:
- Provee la abstracción en el software
- Es el soporte de la estructura jerárquica de los programas
- Mejora la claridad del diseño y facilita la implementación 
- Reduce el costo de testing, debugging y el mantenimiento 
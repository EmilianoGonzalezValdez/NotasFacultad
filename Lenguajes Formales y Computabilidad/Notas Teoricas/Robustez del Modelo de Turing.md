
---
### La Validación del Modelo: Leibniz vence a Turing

Para que el paradigma de Turing sea una formalización válida de la computabilidad, lo primero que debemos asegurar es que no sea "demasiado potente". Es decir, que cualquier cosa que haga una Máquina de Turing (MT) pueda ser replicada por un humano siguiendo un procedimiento efectivo.

#### Proposición 1: Leibniz vence a Turing

Si una función $f$ es computada por una máquina de Turing con unit $M$, entonces $f$ es **$\Sigma$-efectivamente computable**.

**Idea de la Demostración (Simulación):** Para probar esto, diseñamos un procedimiento efectivo $P$ (para un humano) que simule a la máquina $M$ paso a paso:

1. **Estado Inicial:** El humano escribe en su papel la descripción instantánea inicial $\lfloor q_0 B p^{x_1} B \dots B \alpha_m \rfloor$.
2. **Ciclo de Cómputo:** En cada paso, el humano mira el estado actual y el símbolo bajo el "cabezal" (el primer símbolo de la palabra a la derecha del estado).
3. **Aplicación de Reglas:** Busca en la tabla de la función de transición $\delta$ qué debe hacer. Como $\delta$ es una función finita, el humano puede encontrar la instrucción fácilmente.
4. **Actualización:** Borra, escribe y se mueve en el papel según indique la regla ($L, R, K$), obteniendo una nueva descripción instantánea.
5. **Finalización:** Si el humano llega a una configuración donde no hay más reglas (detención), limpia el papel dejando solo el resultado.

> [!success] Conclusión de la Proposición Como cada paso de la simulación es una tarea simple y mecánica, el proceso completo es un procedimiento efectivo. Por lo tanto, todo lo que computa Turing es computable para Leibniz.

### La Hipótesis de Completitud: Turing vence a Leibniz

Mientras que "Leibniz vence a Turing" es un teorema demostrable, la inversa es una postulación fundamental: la idea de que el modelo de Turing es lo suficientemente robusto como para no dejar nada afuera de la computación efectiva.

- **Turing vence a Leibniz:** Se postula que si existe un procedimiento efectivo para calcular una función, entonces existe una Máquina de Turing que la computa.
- **Robustez:** A lo largo de la materia veremos que, aunque agreguemos más cintas, más cabezales o alfabetos gigantes, la potencia del modelo no cambia. Siempre se puede volver a la MT estándar de una sola cinta.

> [!info] Los Tres Vencedores El objetivo final de la materia es ver cómo **Turing, Gödel y Neumann** intentan "vencer a Leibniz" (formalizar la intuición) y cómo, al final, los tres modelos terminan siendo equivalentes entre sí.

---


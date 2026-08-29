
---

Este tema, también llamado _Paradigma Funcional_ o _Recursivo_, formaliza la computabilidad construyendo funciones complejas a partir de un conjunto de funciones iniciales ultra simples. Kurt Gödel postuló que cualquier proceso computable puede expresarse como una función obtenida mediante la aplicación finita de ciertos constructores.

### [[Funciones Básicas Primitivas Recursivas|El Paradigma de Gödel y Funciones Iniciales]]

Esta nota establece el punto de partida: las funciones "obviamente" computables que no necesitan demostración.

- **Ladrillos iniciales:** Sucesores ($Suc$), predecesores ($Pred$), constantes ($C_{n,m}^k$, $C_{n,m}^\alpha$), proyecciones ($p_{n,m}^j$) y funciones derecha ($d_a$).
- **Filosofía:** La computación vista como una estructura de capas sobre estos elementos básicos.

### [[Constructores Recursivos|Constructores: Composición y Recursión Primitiva]]

Acá se explican las reglas para pegar los ladrillos iniciales.

- **Composición:** Cómo anidar funciones preservando la naturaleza mixta.
- **Recursión Primitiva ($R$):** La herramienta central para definiciones inductivas. Incluye los **cuatro casos** fundamentales: sobre variables numéricas o alfabéticas, con resultados numéricos o alfabéticos.

### [[Funciones y Conjuntos Sigma-Recursivos|Funciones y Conjuntos Σ-primitivos recursivos (PRΣ)]]

Define la primera gran clase de funciones donde todos los programas terminan.

- **Definición de $PR_\Sigma$:** Funciones obtenidas solo con composición y recursión primitiva.
- **Predicados y Operaciones Lógicas:** Cómo construir condiciones ($\vee, \wedge, \neg$) que sigan siendo primitivas recursivas.
- **Lema de División por Casos:** El mecanismo para definir funciones "por tramos".

### [[Operadores Acotados|Operadores Acotados (Sumatoria, Productoria y Cuantificación)]]

Herramientas avanzadas para no tener que usar recursión primitiva a mano en cada ejercicio.

- **$\sum$ y $\prod$ acotadas:** Cómo iterar procesos en rangos finitos.
- **Cuantificación Acotada ($\forall, \exists$):** Cómo buscar propiedades en subconjuntos finitos de $\omega$ o $\Sigma^*$ sin perder la propiedad de ser $PR_\Sigma$.

### [[Minimización y Funciones Sigma-Recursivas|Minimización y Funciones Σ-recursivas (RΣ)]]

El salto hacia la potencia total del modelo, permitiendo procesos que pueden no terminar (funciones parciales).

- **Operador de Minimización ($\mu$):** La búsqueda del menor elemento que cumple una propiedad.
- **Clase $R_\Sigma$:** Funciones obtenidas usando también la minimización sobre predicados totales.
- **Vínculo final:** La demostración de que toda función recursiva es efectivamente computable (Leibniz vence a Gödel).

---

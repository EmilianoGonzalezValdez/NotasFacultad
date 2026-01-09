Usualmente los códigos se modifican con el fin de aumentar su funcionalidad, con el tiempo estos cambios deterioran el diseño impuesto en un principio, lo cual provoca que el código comience a hacerse mas complicado de modificar y mas susceptible a errores(lo cual conduce a una disminución de la productividad y calidad). La **Refactorización** es una técnica para mejorar el diseño del código existente, se realiza durante la codificación, pero el propósito no es agregar nuevas características, sino mejorar el diseño actual  
La **Refactorización** es la tarea que permite realizar cambios en un programa con el fin de simplificarlo mejorar su comprensión, hacerlo testeable y mantenible sin cambiar el comportamiento observacional de este. Es decir, la estructura interna del programa cambio, pero su comportamiento externo permanece igual. Esta intenta lograr una o mas de las siguientes cosas:

- Reducir acoplamiento
- Incrementar cohesión
- Mejorar respuesta del principio abierto-cerrado

Estos cambios se realizan separadamente de la codificación normal. Esto presenta un gran riesgo de romper la funcionalidad existente, por ello, para disminuir la posibilidad de que esto ocurra:

- Se refactoriza de a pequeños pasos
- Se dispone de scripts para test automatizados para testear la funcionalidad existente

Existen los denominados **MALOS OLORES**, los cuales son signos fáciles de localizar en el código que indican la posible necesidad de refactorización, aunque no se debe cumplir a rajatabla, hay que analizar cada caso  
Posibles malos olores:

- Código duplicado
- Método muy largo
- Clase muy grande
- Lista larga de parámetros
- Sentencia Switch
- Generalidad especulativa
- Demasiada comunicación entre objetos
- Encadenamiento de mensajes

Hay muchas formas para mejorar el diseño de los programas, pero todos se enfocan en mejorar:

- Métodos
- Clases
- Jerarquía de clases
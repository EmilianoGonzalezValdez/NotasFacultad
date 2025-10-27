# Diseño detallado 

El diseño detallado tiene como objetivo especificar la lógica de los distintos módulos especificados en el diseño del sistemas . Para ello utilizamos una notación textual, el problema es que como queremos un documento formal y claro no podemos usar un Lenguaje Natural para esto, ya que este es impreciso, ambiguo y conduce a problemas de comprensión. Entonces uno pensaría que podríamos optar por un Lenguaje Formal...
Bueno, no realmente ya que estos usualmente tienen mucho detalle sobre la implementación, la cual no es importante para comunicar el diseño, los cuales terminan siendo un estorbo para la comprensión.
A causa de esta falta de un lenguaje optimo es que existe **PDL** . Este tiene la sintaxis externa de un lenguaje de programación estructurado, pero su vocabulario es de lenguaje natural, lo cual nos da la libertad de ser tan específicos como nos parezca con el grado de detalle. Ahora veamos concretamente:
- Ventajas PDL:
	- Se puede integrar con código fuente, por lo que es fácil de mantener
	- Permite declaración de datos así como del procedimiento 
	- Es la forma más barata y efectiva de cambiar la arquitectura del programa 
- Desventajas del PDL:
	- No es capaz de expresar la funcionalidad de una manera comprensible 
	- La notación es comprensible para personas que manejan PDL

snipet de PDL:
```
minmax (in file) ARRAY a 
DO UNTIL end of input 
	READ an item into a 
ENDDO 
max, min := first item of a 
DO FOR each item in a 
	IF max < item THEN set max to item 
	IF min > item THEN set min to item 
ENDDO END
```

PDL logra capturar la lógica completa del procedimiento, pero revela pocos detalles de la implementación. Para llevarlo a una implementación necesitamos que cada pseudo-sentencia de PDL sea convertida a una sentencia de lenguaje de programación. En PDL el diseño puede expresarse en el nivel de detalle mas adecuado para el problema, este permite un enfoque de refinamientos sucesivos 
A este método se lo llama **Refinamiento Paso a Paso**, donde en cada paso descomponemos una sentencia o mas del algoritmo actual en instrucciones mas detalladas hasta que todas las instrucciones sean lo suficientemente detalladas como para llevarlas fácilmente al lenguaje de programación

###### ¿Cómo sabemos que el diseño detallado tiene sentido?

Bueno, para ello existe la **Verificación** la cual tiene como objetivo mostrar que el diseño detallado cumple con las especificaciones dadas por el diseño del sistema. Hay 3 métodos:
- Recorrido del diseño: Reunión informal entre el diseñador y el líder donde el autor explica el diseño paso a paso
- Revisión critica del diseño: Solo si el diseño de realiza en PDL o en algún lenguaje formal
- Verificadores de consistencia: Sigue un proceso de revisión estándar

###### Métricas
El diseño detallado provee muchos detalles de lógica de control y estructura de datos, solo omite detalles de implementación especifico del lenguaje de programación utilizado. Por ende muchas de las métricas dedicadas al código son también útiles en el diseño detallado, como por ejemplo:
- Complejidad ciclomática 
- Vínculos de datos
- Métrica de cohesión 


# Codificación 

El objetivo de la codificación es *implementar el diseño de la mejor manera posible*, escribiendo código el cual logre reducir los costos de testing y mantenimiento  siendo fácil de leer y comprender, aunque no necesariamente de escribir 

Dado que objetivo de un programador es escribir programas simples y fáciles de leer con la menor cantidad de bugs en el menor tiempo posible, existen principios y pautas para la programación que pueden ayudar a escribir de alta calidad

###### Programación estructurada 
La programación estructurada se origino en los '70 en contra del uso de constructores de control como los "gotos". Su objetivo es simplificar la estructura de los programas de manera que sea fácil razonar sobre ellos.

Un programa tiene una **estructura estática**, la cual es el orden de las sentencias en el código y una **estructura dinámica** la cual es el orden en el cual las sentencias se ejecutan. 
Para mostrar que un programa es correcto debemos mostrar que su comportamiento dinámico es el esperado, pero para ello debemos razonar sobre el código del programa, es decir sobre su estructura estática. Esto seria mucho mas fácil si ambas estructuras fuesen similares. Esto es lo que le da fundamento a la programación estructurada. Es decir, el objetivo de la programación estructurada es *escribir programas cuya estructura dinámica es la misma que la estática* 

Los constructores de la programación estructurada son de una única entrada y una única salida, de esta forma la ejecución de las sentencias se realizan en el orden en el que aparecen en el código. Las soluciones de software contienen estructuras de datos donde se guarda la información en las cuales los programas trabajan para realizar ciertas funciones. En general solo ciertas operaciones se realizan sobre la información , de modo tal que esta información debería ocultarse de manera que solo quede expuesta a esas operaciones. Este ocultamiento de información reduce el acoplamiento.

###### El proceso de codificación
La codificación comienza ni bien está disponible la especificación del diseño de los módulos. Normalmente los módulos se asignan a programadores individuales. Acá también existe la noción de desarrollo Top-Down o Bottom-Up dependiendo de que nivel de módulo se desarrolla primero.

Hay 2 principales procesos de codificación:
1. Proceso Básico: 
	- Escribir el código del modulo
	- Realizar test de unidad
	- Si hay algún error, arreglar bugs y repetir tests
2. **TDD**(Test Driven Development):
	- Primero se escriben los test y luego el código para que este pase los tests
	- Se realiza incrementalmente
	- La complejidad del código depende de que tan exhaustivos sean los tests 
	- Normalmente el código necesitara una refactorización 
	- Lo ideal seria que los test no sean mockeados
	- Selftesting code

Otra practica del Extreme Programming (además del TDD) es la programación de a pares, donde el código se escribe por dos programadores en vez de uno solo, mientras uno tipea, el otro va revisando tipeado. Estos roles se alternan periódicamente.

Otro paso esencial que los programadores deben realizar es el control de código fuente, donde normalmente se utilizan herramientas como SVN, CVS, VVS. Prácticamente esta herramienta es un repositorio donde se almacenan los archivos del código y de donde se construirá el sistema. Estas herramientas mantienen una historia completa de los cambios t todas las versiones viejas pueden recuperarse 

###### Refactorización
Usualmente los códigos se modifican con el find e aumentar su funcionalidad, con el tiempo estos cambios deterioran el diseño del principio, lo cual provoca que el código comience a hacerse mas complicado de modificar y mas susceptible a errores(lo cual conduce a una disminución de la productividad y calidad). La **Refactorización** es una técnica para mejorar el diseño del código existente, se realiza durante la codificación, pero el propósito no es agregar nuevas características, sino mejorar el diseño 
La **Refactorización** es la tarea que permite realizar cambios en un programa con el fin de simplificarlo  mejorar su comprensión, hacerlo testeable y mantenible sin cambiar el comportamiento observacional de este. Es decir, la estructura interna del programa cambio, pero su comportamiento externo permanece igual. Esta intenta lograr una o mas de las siguientes cosas:
- Reducir acoplamiento 
- Incrementar cohesión
- Mejorar respuesta del principio abierto-cerrado
Estos cambios se realizan separadamente de la codificación normal. Esto es un gran riesgo, por ello, para disminuir esta posibilidad:
- Se refactoriza de a pequeños pasos
- Se dispone de scripts para test automatizados para testear la funcionalidad existente

Existen los denominados **MALOS OLORES**, los cuales son signos fáciles de localizar en el código que indican la posible necesidad de refactorización, aunque no se debe cumplir a rajatabla, hay que analizar cada caso
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

###### Mejoras de métodos
**Extracción de métodos:** Se realiza si un método es demasiado largo, su objetivo es separar el método largo en otros métodos cortos cuya signatura indique lo que el método hace:
- Partes del código se extraen como nuevos métodos
- Variables referenciadas en estas partes se transforman en parámetros 
- Variables declaradas en esta parte pero utilizadas en otras partes deben definirse en el método original
- También se realiza si hay un método que retorna un valor Y cambia ele estado del objeto

**Agregar/eliminar parámetros:** Sirve para simplificar las interfaces donde sea posible:
- Agregar sólo si los parámetros existentes no proveen toda la información necesaria 
- Eliminar si los parámetros se agregaron originalmente "por las dudas" y/o no se utilizan

###### Mejoras de Clases
**Desplazamiento de métodos:** Mover un método de una clase a otra, se realiza cuando el método actúa demasiado con los objetos de otra clase, normalmente puede convenir dejar un método en la clase inicial que delegue al nuevo

**Desplazamiento de Atributos:** Si un atributo se usa en más de una clase, moverla a estas clases, mejorando la cohesión y acoplamiento 

**Extracción de clases:** Si una clase agrupa múltiples conceptos, separa cada concepto en una clase distinta, mejorando la cohesión 

**Remplazar valores de datos por objetos:** Algunas veces una colección de atributos se transforma en una entidad lógica, en estos casos, vale la pena separar esta colección como una clase propia

###### Mejoras de Jerarquías 
**Remplazar condicionales con polimorfismos:** Si el comportamiento depende de algún indicador de tipo, no se esta explotando el poder de la OO, entonces se debe remplazar tal análisis de casos a través de una jerarquía de clases apropiada

**Subir métodos/atributos:** Los elementos comunes deben perteneces a la superclase para que las clases hijas no deban definir la misma funcionalidad muchas veces 

###### Verificación 

El código necesita ser verificado antes de ser utilizado por otros. Para ello hay diferentes técnicas:
- Inspección de código
- Test de Unidad
- Verificación de programa

La inspección de código  es un proceso de revisión como cualquier otro, se aplica luego de que el código fue compilado, testeado algunas veces y chequeado con herramientas de análisis estático. Se utilizan listas de control para enfocar la atención en puntos clave ya que es caro(es perder una persona para que se ponga a revisar)

El test de unidad es simplemente un test que se enfoca solo en el módulo escrito por un programador, el cual es también responsable de hacerlo (normalmente). Este test consta de varios casos y "drivers", los cuales ejecutan el módulo con sus test para automatizarlos

En el análisis estático se utilizan herramientas para analizar los programas fuentes y verificar la existencia de problemas, aunque muchas veces estos dan falsos positivos. Son muy útiles para encontrar pequeños bugs como memory leaks

# Procesos de Desarrollo

La ingeniería del software se enfoca en el proceso antes que en el producto debido a que:

> [!quote] Un proceso adecuado ayuda a lograr los objetivos del proyecto con alta CyP

Un proyecto exitoso es el que satisface las expectativas en costo, tiempo y calidad. Un modelo de proceso especifica un proceso en general, usualmente con fases en las que el proceso debe dividirse, conjuntamente con otras restricciones y condiciones para la ejecución de dichas fases.
Estos modelos de proceso no se traducen directamente al proceso a usar en el proyecto, mas bien el proyecto realmente utilizado es una adaptación de algún modelo dependiendo la circunstancia y elección. Normalmente este proceso es que guía al proyecto.

Hay 2 procesos fundamentales que son ejecutados por diferentes personas:
- **Proceso de Desarrollo**: Es el corazón del proceso de software, los otros procesos giran alrededor de el . Se enfoca en las actividades para el desarrollo y garantizar la calidad necesarias
- **Administración del Proyecto**: Se enfoca en el planeamiento y control del proceso de desarrollo con el fin de cumplir los objetivos 

Como dijimos antes normalmente el proceso es un conjunto de fases cada una con una tarea bien definida que produce una salida, las salidas intermedias se las conoce como *producto de trabajo* y cada una de estas es una entidad formal y tangible capaz de ser verificada

Cada una de dichas fases sigue el enfoque **ETVX**:
- E(Entry): que condiciones deben cumplirse al iniciar la fase 
- T(Task): Lo que debe realizar la fase 
- V(Verification): Las inspecciones/controles/revisiones/verificaciones que deben realizarse a la salida de la fase
- X(Exit): Cuando puede considerarse que la fase fue realizada exitosamente

Las características son las mismas que siempre: Proveer alta CyP. Para ello existen Controles de Calidad (CC) que tienen como objetivo prevenir defectos. Los procesos deben conseguir repetir el desempeño cuando se utilizan en distintos proyectos, es decir que el resultado de un proceso debe ser predecible bajo control estadístico. Además todo proceso debe lograr adaptarse a cambios repentinos.

Ahora si podemos definir el objetivo del **Proceso de Desarrollo de Software** el cual es construir sistemas de software dentro de los costos y el tiempo planeado, cronograma y que posea la calidad apropiada, satisfaciendo al cliente, alta CyP. Aunque para ello se necesita un proceso adecuado para alcanzar los objetivos.

Normalmente este proceso esta compuesto por las siguientes fases:
- Análisis de requerimientos y especificación: Tiene como objetivo comprender precisamente el problema, especifica el "que". Su salida es la SRS
- Diseño:  Involucra 3 subfases, las cuales se van alejando cada vez mas del "que" para ir cambiando su enfoque en el "como". Cada una tiene su salida correspondiente
	- Diseño arquitectónico: Establece componentes y los conectores que conforman al sistema
	- Diseño de alto nivel:  Establece los módulos y estructuras de datos necesarios para implementar la arquitectura 
	- Diseño detallado: establece la lógica de los módulos
- Codificación: Su objetivo es implementar el diseño con código simple  y fácil de comprender. Tiene mucho impacto en el mantenimiento y testing. Su salida es el código
- Testing: Su objetivo es identificar la mayoría de los defectos, es una tarea muy cara. Su salida es un plan de test conjuntamente con los resultados y el código final testeado y confiable 

Ahora veremos los demás procesos que orbitan alrededor del proceso de desarrollo:

###### Proceso para la administración del proyecto 
Este proceso se encarga de la asignación y administración de los recursos entre las fases del proceso de desarrollo, observar su progreso, tomar acciones correctivas al respecto, etcétera. Tiene 3 fases:
- Planeamiento: Se realiza antes de comenzar el proyecto. Sus tareas claves:
	- Estimación de costos y tiempos
	- Seleccionar Personal
	- Planear el seguimiento
	- Planear el control de Calidad
- Seguimiento y control: Acompaña al proceso de desarrollo, sus tareas son:
	- Seguir y observar parámetros claves como costo, tiempos, riesgos, así como los factores que los alteran(esto a través de las métricas )
	- Tomar acciones correctivas de ser necesario 
- Análisis de terminación: Se realiza al finalizar el proceso de desarrollo. Su propósito fundamental es analizar el desempeño del proceso e identificar las lecciones aprendidas, aunque en algunos procesos iterativos, el análisis de terminación se realiza al final de cada iteración 

###### Proceso de inspección
El objetivo principal de este proceso es **Detectar los defectos en los productos de trabajo**. Actualmente es utilizado en todos los productos de trabajo, mejora tanto la calidad como la productividad. Estas inspecciones pueden realizarse sobre cualquier documento, sean requerimientos, planificaciones, diseños, etc. 

Realizado por el personal técnico para el personal técnico, es decir, es una revisión hecha por pares. Tiene 4 fases bien estructuradas con toles definidos para cada participante y su foco es encontrar problemas, no su resolución. Los roles presentes son:
- Moderador: Tiene la responsabilidad general
- Autor: Quien realizó el producto de trabajo
- Revisor: Quien identifica los defectos
- Lector: Lee línea a línea el producto de trabajo para enfocar el progreso de la reunión 
- Escriba: Registra las observaciones indicadas 

Las 4 fases son:
- Planeamiento: Se selecciona el equipo de revisión y se prepara el paquete para la distribución
- Preparación y repaso previo: Puede haber  una breve reunión opcional para repartir el paquete. Pero principalmente en esta etapa todos los miembros del equipo revisan individualmente el producto de trabajo para identificar defectos potenciales en un registro individual 
- Reunión de revisión grupal: Su propósito es definir la lista final de defectos en base a las revisiones individuales de cada miembro, los cuales son revisados por el moderador. El moderador está a cargo de la reunión y juega un rol central, asegurando que el foco permanezca en la identificación de defectos y evitando que se prolongue o que se estén discutiendo soluciones. También controla que se este revisando el producto de trabajo y no al autor de este, asegurando que la reunión se haga de forma ordenada y amigable. En la reunión
	- El lector lee línea a línea el producto de trabajo
	- En cualquier línea se puede efectuar alguna observación nueva o que ya hubiere
	- Se discute para identificar un defecto y la decisión es registrada por el escriba
	- Al final de la reunión el escriba presenta la lista final de defectos, si hay pocos de estos, el trabajo es aceptado. El grupo no propone soluciones, aunque se podrían dar recomendaciones 
- Corrección y seguimiento: Los defectos en la lista de defectos son posteriormente corregidos por el autor. Una vez corregidos el autor obtiene el visto bueno del moderador o el producto de trabajo se somete a una nueva revisión

###### Proceso de administración de configuración

Un proyecto de software produce muchos ítems: programas, documentos, datos, manuales, etcétera 


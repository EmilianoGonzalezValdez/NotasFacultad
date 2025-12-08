# Diseño detallado 

El diseño detallado tiene como objetivo especificar la lógica de los distintos módulos especificados en el diseño del sistemas . Para ello utilizamos una notación textual, el problema es que como queremos un documento formal, no podemos usar un Lenguaje Natural para esto, ya que este es impreciso, ambiguo y conduce a problemas de comprensión. Entonces uno pensaría que podríamos optar por un Lenguaje Formal...
Bueno, no realmente ya que estos usualmente tienen mucho detalle para la implementación, la cual no es importante para comunicar el diseño, los cuales terminan siendo un estorbo para la comprensión.
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
	ENDDO 
END
```

PDL logra capturar la lógica completa del procedimiento, pero revela pocos detalles de la implementación. Para llevarlo a una implementación necesitamos que cada pseudo-sentencia de PDL sea convertida a una sentencia de lenguaje de programación. En PDL el diseño puede expresarse en el nivel de detalle mas adecuado para el problema, este permite un enfoque de refinamientos sucesivos.
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

Dado que objetivo de un programador es escribir programas simples y fáciles de leer con la menor cantidad de bugs en el menor tiempo posible, existen principios y pautas para la programación que pueden ayudar a escribir código de alta calidad

##### Programación estructurada 
La programación estructurada se origino en los '70 en contra del uso de constructores de control como los "gotos". Su objetivo es simplificar la estructura de los programas de manera que sea fácil razonar sobre ellos.

Un programa tiene una **estructura estática**, la cual es el orden de las sentencias en el código y una **estructura dinámica** la cual es el orden en el cual las sentencias se ejecutan. 
Para mostrar que un programa es correcto debemos mostrar que su comportamiento dinámico es el esperado, pero para ello debemos razonar sobre el código del programa, es decir sobre su estructura estática. Esto seria mucho mas fácil si ambas estructuras fuesen similares. Esto es lo que le da fundamento a la programación estructurada. Es decir, el objetivo de la programación estructurada es *escribir programas cuya estructura dinámica es la misma que la estática* 

Los constructores de la programación estructurada son de una única entrada y una única salida, de esta forma la ejecución de las sentencias se realizan en el orden en el que aparecen en el código. Las soluciones de software contienen estructuras de datos donde se guarda la información en las cuales los programas trabajan para realizar ciertas funciones. En general solo ciertas operaciones se realizan sobre la información , de modo tal que esta información debería ocultarse de manera que solo quede expuesta a esas operaciones. Este ocultamiento de información reduce el acoplamiento.

##### El proceso de codificación
La codificación comienza ni bien está disponible la especificación del diseño de los módulos. Normalmente los módulos se asignan a programadores individuales. Acá también existe la noción de desarrollo Top-Down o Bottom-Up dependiendo de que nivel de módulo se desarrolla primero.

Hay 2 principales procesos de codificación:
1. Proceso Básico o programación incremental: 
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

Otra practica del Extreme Programming (además del TDD) es la programación de a pares, donde el código se escribe por dos programadores en vez de uno solo, mientras uno tipea, el otro va revisando lo tipeado. Estos roles se alternan periódicamente.

Otro paso esencial que los programadores deben realizar es el control de código fuente, donde normalmente se utilizan herramientas como SVN, CVS, VVS. Prácticamente esta herramienta es un repositorio donde se almacenan los archivos del código y de donde se construirá el sistema. Estas herramientas mantienen una historia completa de los cambios, permitiendo que todas las versiones viejas pueden recuperarse 

##### Refactorización
Usualmente los códigos se modifican con el fin de aumentar su funcionalidad, con el tiempo estos cambios deterioran el diseño impuesto en un principio, lo cual provoca que el código comience a hacerse mas complicado de modificar y mas susceptible a errores(lo cual conduce a una disminución de la productividad y calidad). La **Refactorización** es una técnica para mejorar el diseño del código existente, se realiza durante la codificación, pero el propósito no es agregar nuevas características, sino mejorar el diseño actual
La **Refactorización** es la tarea que permite realizar cambios en un programa con el fin de simplificarlo  mejorar su comprensión, hacerlo testeable y mantenible sin cambiar el comportamiento observacional de este. Es decir, la estructura interna del programa cambio, pero su comportamiento externo permanece igual. Esta intenta lograr una o mas de las siguientes cosas:
- Reducir acoplamiento 
- Incrementar cohesión
- Mejorar respuesta del principio abierto-cerrado

Estos cambios se realizan separadamente de la codificación normal. Esto presenta un gran riesgo de romper la funcionalidad existente, por ello, para disminuir la posibilidad de que esto ocurra:
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
- También se realiza si existe un método que retorna un valor y además cambia el estado del objeto

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

**Subir métodos/atributos:** Los elementos comunes deben pertenecer a la superclase para que las clases hijas no deban definir la misma funcionalidad muchas veces 

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
- **Proceso de Desarrollo**: Es el corazón del proceso de software, los otros procesos giran alrededor de el. Se enfoca en las actividades para el desarrollo y garantizar la calidad necesarias
- **Administración del Proyecto**: Se enfoca en el planeamiento y control del proceso de desarrollo con el fin de cumplir los objetivos 

Como dijimos antes normalmente el proceso es un conjunto de fases cada una con una tarea bien definida que produce una salida, las salidas intermedias se las conoce como *producto de trabajo* y cada una de estas es una entidad formal y tangible capaz de ser verificada

Cada una de dichas fases sigue el enfoque **ETVX**:
- E(Entry): que condiciones deben cumplirse al iniciar la fase 
- T(Task): Lo que debe realizar la fase 
- V(Verification): Las inspecciones/controles/revisiones/verificaciones que deben realizarse a la salida de la fase
- X(Exit): Cuando puede considerarse que la fase fue realizada exitosamente

Las características deseadas en el software son las mismas que siempre: Proveer alta CyP. Para ello existen Controles de Calidad (CC) que tienen como objetivo prevenir defectos. Los procesos deben conseguir repetir el desempeño cuando se utilizan en distintos proyectos, es decir que el resultado de un proceso debe ser predecible bajo control estadístico. Además todo proceso debe lograr adaptarse a cambios repentinos.

Ahora si podemos definir el objetivo del **Proceso de Desarrollo de Software** el cual es construir sistemas de software dentro de los costos y el tiempo planeado, respetando el cronograma, y que posea la calidad apropiada, satisfaciendo al cliente, alta CyP. Aunque para ello se necesita un proceso adecuado para alcanzar los objetivos.

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

Realizado por el personal técnico para el personal técnico, es decir, es una revisión hecha por pares. Tiene 4 fases bien estructuradas con roles definidos para cada participante y su foco es encontrar problemas, no su resolución. Los roles presentes son:
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

Un proyecto de software produce muchos ítems: programas, documentos, datos, manuales, etcétera. Cualquiera de ellos puede cambiar fácilmente por lo cual es necesario saber el progreso del estado de cada uno. Esto le da motivo a este proceso

Para dejarlo claro, la administración de configuración del software (SCM) controla sistemáticamente los cambios producidos. Se enfoca en los cambios durante la evolución, los cambios de requerimientos se manejan aparte. Este proceso requiere tanto disciplina como herramientas.

SCM es usualmente independiente del proceso de desarrollo, a medida que los ítems se producen, estos se introducen en la SCM. Cabe aclarar que SCM solo controla los ítems del proceso de desarrollo. De esta forma *la administración de configuración debe asegurar que las distintas versiones se combinen apropiadamente sin perdidas*

Las funcionalidades necesarias son:
- Recolectar todos las fuentes, documentos y otra información del sistema actual
- Evitar cambios o eliminaciones desautorizadas 
- Deshacer cambios o revertir a una versión especifica 
- Hacer disponible la última versión del programa 

Sus mecanismos principales son:
- Control de Acceso
- Control de Versiones
- Identificación de la configuración
- Otros Mecanismos incluyen convenciones de nombres, estructuras de directorios, etc.


Una baseline es  un arreglo apropiado de ítems de configuración. Esta establece puntos de referencia a lo largo del desarrollo del sistemas capturando el estado lógico del sistema y forma la base de cambios posteriores 

Entonces, en el **Proceso de Administración de Configuración** primero definimos las actividades que requieren control de cambio, una vez definidas siguen las siguientes fases:
- Planeamiento: Identificar ítems, definir la estructura del repositorio, definir el control de acceso, puntos de referencia, reconciliación, procedimientos, definir procedimiento de publicación
- Ejecución: Realizar los procedimiento según lo establecido en el planeamiento 
- Auditoría: Para verificar que no se estén cometiendo errores

###### Proceso de Administración de Cambios de Requisitos 

Dado que los requerimientos pueden cambiar en cualquier momento durante el desarrollo y pueden producir impactos muy grandes en los productos de trabajo e ítems de configuración si no son controlados, existe un proceso entero para su manejo adecuado

Este proceso debe:
- Registrar los cambios
- Realizar análisis de impacto sobre los productos de trabajo y los ítems
- Estimar el impacto en esfuerzo y en cronograma
- Analizar el impacto con las personas involucradas 
- Reprocesar los productos de trabajo y los ítems
Estos cambios se inician a través de un requerimiento de cambio. Existe un registro de requerimientos de cambio y de los cambios acumulativos. El impacto del cambio en el proyecto es analizado para decidir si hacerlo efectivo o no 

###### Proceso de Administración de Procesos
La administración de procesos se enfoca en la *evaluación y mejora del proceso* en si. (**NO CONFUNDIR CON ADMINISTRACIÓN DEL PROYECTO**)

Para lograr mejorar el proceso se debe comprender el proceso actual:
- Requiere que el proceso este bien documentado
- Que sea apropiadamente ejecutado en los proyectos 
- Recolectar datos de los proyectos para comprender el desempeño del proceso en los proyectos
Como todo cambio, es mejor que se haga incrementalmente de a pasos pequeños cuidadosamente seleccionados. Existen marcos que sugieren formas de proceder en la mejora del proceso, como por ejemplo **CMM** (Capability Maturity Model).
CMM tiene 5 niveles, en cada nivel se dan ciertas capacidades y se establecen las bases para pasar al siguiente nivel. Para pasar de un nivel a otro CMM especifica en que áreas enfocarse. Los niveles son:
- Nivel 1: Ad-HOC
- Nivel 2: Repetible
	- Administración de requerimientos del SW
	- Administración de configuración del SW
	- Planeamiento del Proyecto
	- Control y Monitoreo del proyecto
- Nivel 3: Definido
	- Organización en definición del proceso
	- Programa de entrenamiento
	- Revisión de pares
	- Administración integrada del SW
- Nivel 4: Administrado
	- Administración de la calidad del SW
	- Administración cuantitativa del proceso
- Nivel 5: Optimizado
	- Administración de cambio de proceso
	- Administración de cambio de Tecnología 
	- Prevención de defectos

# Planeamiento del Proyecto del Software
Un tercio de los proyectos se desbocan con costos superiores al 125% de los estipulados. Normalmente hay 5 razones que conllevan a esto:
1. Objetivos poco claros
2. Mal planeamiento
3. Administración del proyecto sin metodología
4. Nueva tecnología 
5. Personal insuficiente.
Todas estas razones están relacionadas con la administración del proyecto

###### Estimación del esfuerzo 
Dado un conjunto de requerimientos es deseable/necesario saber cuanto costara en tiempo y dinero el desarrollo del software. Normalmente el esfuerzo se mide en Persona/Mes. Lamentablemente no hay una forma fácil de estimar, normalmente la estimación mejora a medida que se incrementa la información sobre el proyecto.
**Un modelo intenta determinar la estimación del esfuerzo a partir de valores de ciertos parámetros**, los cuales dependen del proyecto. De esta forma el modelo reduce el problema de estimar el esfuerzo del proyecto al de estimar ciertos **parámetros claves** del proyecto, los cuales deben poder medirse en etapas muy tempranas del proyecto. Hay 2 enfoques:

- Estimación Top-Down: Se intenta determinar el esfuerzo total y luego calcular el esfuerzo de cada parte del proyecto. Primero se estima el tamaño global del proyecto en KLOC, luego se calcula $\text{esfuerzo} = a * \text{tamaño}^b$ donde a y b se determinan a través de análisis de regresión sobre proyectos pasados
- Estimación Bottom-Up: Primero identificamos los módulos del sistema y los clasificamos como simples, medios o complejos. Luego determinamos el esfuerzo total de codificación para cada tipo de módulo, obtenemos el esfuerzo total de codificaciones en base a la clasificación anterior y al conteo de cada tipo. Utilizamos la distribución de esfuerzos de proyectos similares para estimar el esfuerzo de cara tarea y por ultimo refinamos los estimadores anteriores en base a factores específicos del proyecto
- COCOMO:
	- Tiene enfoque top-down
	- Utiliza tamaño ajustado con algunos factores 
	- Procedimiento:
		- Obtener el estimador inicial usando el tamaño
		- Determinar un conjunto de  factores de multiplicación representando distintos tributos
		- Ajustar el estimador de esfuerzo escalándolo según el factor de multiplicación final
		- Calcular el estimador de esfuerzo de cada fase principal

Los factores de ajuste son:
- Atributos del software:
	- RELY: confiabilidad
	- DATA: tamaño de la base de datos
	- CPLX: complejidad de las funciones, datos, interfaces...
- Atributos del hardware:
	- TIME: limitaciones en el porcentaje del uso de la CPU
	- STOR: limitaciones en el porcentaje en el uso de la memoria
	- VIRT: volatilidad de la maquina virtual
	- TURN: frecuencia de cambio en el modelo de explotación 
- Atributos del personal 
	- ACAP: calificación de los analistas
	- AEXP: experiencia del personal en aplicaciones similares
	- PCAP: CALIFICACIÓN DE LOS PROGRAMADORES
	- VEXP: experiencia del personal en la maquina virtual 
	- LEXP: experiencia en el lenguaje de programación a usar
- Atributos del Proyecto:
	- MODP: uso de practicas modernas de programación 
	- TOOL: uso de herramientas de desarrollo de software
	- SCED: limitaciones en el cumplimiento de la planificación 

###### Planificación y recursos humanos
Hay 2 niveles de planificación:
- Planificación global
- Planificación detallada 

La *planificación global* depende fuertemente del esfuerzo estimado, hay una cierta flexibilidad ,dependiendo de los recursos asignados, para una cierta estimación. Un método es estimar el tiempo programado del proyecto en meses como una función del esfuerzo en personas/mes
$\text{Rule of thumb:} \space M =  \sqrt{esfuerzo}$

Seguidamente determinar la duración de cada meta parcial principal del proyecto. Luego distribuir los recursos, aunque la distribución de los RRHH no es homogénea, sigue aproximadamente una curva de Rayleigh. Con dicha curva y la distribución de esfuerzos se puede determinar el tiempo de las metas parciales. Cabe aclarar que la distribución de esfuerzo y la distribución de los tiempos en las fases son 2 cosas distintas

En la *planificación detallada*  se pueden utilizar herramientas como ayuda. En la teoría cualquier actividad a realizarse debe quedar reflejada en la planificación detallada, donde cada tarea tiene asignado un nombre, esfuerzo, fecha, duración, recursos, etc. Esta planificación debe ser consistente con las metas, dado que las tareas son subactividades de las actividades a nivel de metas, así que el esfuerzo individual sebe sumar apropiadamente preservando la duración total de la meta 

###### Estructura del equipo de trabajo
Para asignar las tareas en la planificación detallada es necesario un equipo de trabajo estructurado.
- Organización Jerárquica:
	- Es la más común
	- Hay un administrador de proyecto con la responsabilidad global, realiza diseño, asigna recursos, etc.
	- Tiene programadores, testers y administrador de configuración para ejecutar las tareas detalladas 
	- Una persona podría cumplir mas de un rol
- Equipos democráticos:
	- Funciona en pequeños grupos
	- El liderazgo es rotativo
	- ALTERNATIVA:
		- Reconoce tres tareas principales: Desarrollo, testing y administración del programa
		- Cada una tiene su propio equipo y cada equipo su líder
		- Todos reportan a un líder general
		- Se utiliza para el desarrollo de grandes productos 

###### Planeamiento de la administración de la configuración del software

Se deben identificar los ítems de configuración y especificar los procedimientos a usar para controlar e implementar los cambios de estos ítems. El planeamiento de la administración de configuración se realiza cuando el proyecto ha sido iniciado y ya se conoce la especificación de los requerimientos y el entorno de operación 

###### Planeamiento del Control de Calidad
Objetivo básico: entregar un software de alta calidad .

Defecto: Algo que causa que el software se comporte de manera inconsistente, con respecto a los requerimientos o necesidades del cliente

El desarrollo de software es una actividad altamente dependiente de personas, por lo cual es propensa a errores. Estos defectos se pueden introducir en cualquier etapa. Como el objetivo de calidad es la baja densidad de defectos, los defectos deben eliminarse. Normalmente esto se hace mediante las actividades de control de calidad incluyendo revisiones y testing

Hay varios enfoques para la administración del Control de Calidad
- Enfoque ad-hoc:
	- Se hacen test y revisiones de acuerdo a cuando y como se necesitan
- Enfoque de procedimiento:
	- El plan define que tareas de Control de calidad se realizarán y cuando
	- Principales tareas del control de calidad: revisión y testing
	- Provee procedimientos y lineamientos a seguir en el testing y en la revisión 
	- Durante la ejecución del proyecto se asegura el seguimiento del plan y los procedimientos
- Enfoque Cuantitativo:
	- Va mas allá de requerir que se ejecute ejecute el procedimiento 
	- Analiza los datos recolectados de los defectos y establece juicios sobre la calidad: métricas, densidad de defectos 
	- La información del pasado es muy importante para predicciones de defectos
	- Parámetros claves: tasas de introducción y eliminación de defectos

El **plan de calidad** establece qué actividades deber realizarse. El nivel del plan depende de los modelos de predicción disponibles. De mínima debe definir las tareas del control de calidad que deben realizarse durante el proyecto, aunque también puede especificar los niveles esperados de defectos que cada tarea de control de calidad debe encontrar 

###### Administración de Riesgos 
Cualquier evento puede fallar debido a eventos no previstos. La administración de riesgo es un intento de minimizar las chances de fallas, pero que es el riesgo?
Riesgo: Cualquier condición o evento de ocurrencia incierta que puede causar la falla del proyecto. El objetivo de la **administración del riesgo** es minimizar el impacto de la materialización de los riesgos 

Durante el planeamiento del proyecto se realiza una *Evaluación de Riesgos*. Esta esta compuesta por 3 tareas, la Identificación de riesgos, la Definición de prioridades de los riesgos y el análisis de riesgos. Mientras que durante la realización del proyecto se realiza el *Control de Riesgos*, el cual esta compuesto por el Planeamiento de la Administración de riesgos, la Resolución de riesgos y el Seguimiento de riesgos. Ahora veremos estas tareas una a una

*Tareas de Evaluación de Riesgos*

**Identificación del riesgo**: Se identifican los posibles riesgos del proyecto, es decir, aquellos eventos que podrían ocurrir y causar la falla del proyecto. Los 9 factores de riesgo más importantes: 
1. Personal: insuficiente o inapropiadamente entrenado
2. Tiempos y costos irreales
3. Componentes externas: incompatibles o de baja calidad
4. Discrepancia con la interfaz del usuario
5. Discrepancia con los requerimientos
6. Arquitectura, desempeño, calidad: inadecuada o insuficiente evaluación
7. Flujo continuo en los cambios de requerimientos
8. Software legado
9. Tareas desarrolladas externamente: inadecuadas o demoradas

La cantidad de riesgos puede ser grande, por ello se deben priorizar para enfocar la atención en las áreas de alto riesgo 

**Definición de prioridades y Análisis de los riesgos**: Establecer la probabilidad de materialización de los riesgos identificados y la pérdida que éstos originarían. Ordenas de acuerdo al "valor de exposición al riesgo (RE)"
Es decir, RE es el valor esperado de la perdida debido a un riesgo. Siempre queremos realizar planes para tratar con los riesgos de mayor RE, clasificando las probabilidades de ocurrencia como Bajas, Medias o Altas, luego clasificar los impactos de los riesgos como Bajos, Medios o Altos para poder enfocarnos solamente en todos los riesgos AA y AM/MA

*Tareas de Control de Riesgos*

Si es posible evitar el riesgo, lo evitamos. En los casos que no se puedan evitar se debe planear y ejecutar los pasos necesarios para mitigar los riesgos y que su impacto sea mínimo, esto claramente, involucra costo extra

**Plan de mitigación de riesgos**
La mitigación de riesgos incluye los pasos a  realizar, en consecuencia, a costo extra. Estos pasos deben planificarse en el tiempo y ejecutarse, además estos son distintos de los que se deben realizar si el riesgo se materializa, los cuales se efectúan solo si es necesario. Los riesgos deben revisarse periódicamente

###### Planificación del seguimiento del proyecto 
El plan de administración del proyecto es meramente un documento que sirve como guía. Este debe ejecutarse para asegurar que la ejecución se realiza como se planeó, ésta debe seguirse y controlarse. Este seguimiento requiere mediciones y métodos que las interpreten. El plan de seguimiento incluye:
- Planificar qué medir, como y cuando 
- Como analizar y reportar estos datos
**Principales medidas:**
- Tiempo: es la mas importante de las medidas
- Esfuerzo: Es el principal recurso
- Defectos: Determinan calidad
- Tamaño:: Mucha información se normaliza respecto al tamaño

El objetivo del seguimiento del proyecto es hacer visible la ejecución del proyecto de manera de realizar acciones correctivas cuando sea necesario con el fin de asegurar el éxito del proyecto. hay distintos niveles de seguimientos:
- Nivel de actividad:
	- Asegura que cada actividad se realiza apropiadamente y a tiempo
	- Realizado diariamente por los administradores de proyecto 
	- Una tarea realizada se marca con un %100
- Reportes de estado
	- Usualmente se prepara semanalmente
	- Contiene un resumen de actividades completadas y pendientes desde el ultimo reporte y cuestiones que necesitan atención o deben ser resueltas
- Análisis de metas parciales:
	- Se realiza una mayor revisión con cada meta parcial
	- Análisis de esfuerzos y tiempos reales vs estimados
	- Si la desviación es amplia se realizan medidas correctivas
	- Revisión de los riesgos


# Testing 

###### Defecto y Desperfecto 

Desperfecto(failure) =  Un desperfecto de software ocurre si el comportamiento de éste es distinto del esperado/especificado 

Defecto(Fault) = Es la causa del desperfecto = BUG

Un desperfecto implica la presencia del defecto, pero la existencia de un defecto no implica la ocurrencia de un desperfecto 

Las revisiones son procesos humanos, no pueden encontrar todos los defectos. En consecuencia habrán defectos en los requerimientos, en el diseño y en la codificación, los cuales deben identificarse por medio del testing. Por esto mismo, el testing juega un rol critico a la hora de garantizar la calidad

Durante el testing un programa se ejecuta siguiendo un conjunto de casos de tests, si hay algún desperfecto en los test entonces hay algún defecto en el software. Si no aparecen desperfectos aumenta la confianza en el software, pero esto no nos garantiza que no haya algún defecto. Para detectar los defectos debemos causar desperfectos durante el testing y para identificar el defecto real que causa el desperfecto, debemos recurrir al debugging 

###### Conceptos fundamentales 
Para verificar la ocurrencia de un desperfecto en la ejecución de un caso de test, necesitamos conocer el comportamiento correcto para este caso, por ende necesitamos un *oráculo de test*. Esto oráculo de test es un ente el cual pretendemos que siempre dé el resultado correcto. Muchas veces el oráculo puede generarse directamente desde la especificación

Si existen diferentes defectos, queremos tener varios casos de tests que los evidencien a través de fallas tal que la correcta ejecución de dicha "suit" de test, implique la ausencia de defectos. Como el testing es costoso queremos que este conjunto de casos sea lo mínimo posible. Por ello usamos *criterios de selección de tests*, el cual especifica las condiciones que el conjunto de casos de test debe satisfacer con respecto al programa y/o a la especificación. Normalmente siempre esperamos de los criterios de test Confiabilidad y Validez (con estas podríamos decir que el test es exhaustivo), lo cual es prácticamente imposible si le sumamos que queremos una cantidad manejable de tests 

Como queremos sacar a la luz los defectos mediante tests, estos deben ser destructivos. Hay 2 enfoques de tests:
- Testing caja Negra
- Testing caja Blanca

##### Testing Caja Negra

El software a testear se trata como una caja negra, donde la especificación de esta es dada y para testear se utiliza el comportamiento esperado del sistema. Es decir que los casos de test se seleccionan solo a partir de la especificación de la caja negra
Como solo tenemos la especificación, el testing funcional mas minucioso es el mas exhaustivo, puesto que como el software esta diseñado para trabajar sobre ciertas entradas, lo mas exhaustivo que se puede ser es testearlo junto a todos sus elementos de entrada. Lo cual es muy costoso, si es que no es imposible. A cusa de esto veremos mejores métodos de selección de tests

###### Particionado por clase de equivalencia 

Se intenta dividir el espacio de entrada en clases de equivalencia. Este método parte de la idea de que si el software funciona para un caso de test en una clase, entonces muy probablemente funcione de la misma manera para todos los elementos de la misma clase. La base lógica de este método es que la especificación requiere el mismo comportamiento en todos los elementos de una misma clase. Cada condición especificada como entrada es una clase de equivalencia, para lograr robustez se deben armar clases de equivalencias para entradas invalidas.
También se deben considerar las clases de equivalencia de los datos de salida. Generar los casos de test para estas clases eligiendo apropiadamente las entradas. Una vez elegidas las clases de equivalencia se deben seleccionar los casos de test:
- Seleccionar cada caso de test cubriendo tantas clases como sea posible
- O dar un caso de test que cubra a lo sumo una clase válida por cada entrada

En otras palabras, lo que hacemos es separar acada entrada del programa en clases, donde cada clase tiene una propiedad de esta entrada que el programa puede procesar sin problema(si mi programa suma 2 números positivos, una clase seria los números mayores o iguales a 0), luego hacer lo mismo pero con las que no puede procesar, y en base a esto elegir los casos de test

###### Análisis de valores límites 

Muchos de los programas generalmente fallan sobre valores especiales los cuales se encuentran normalmente en los limites de las clases de equivalencia, por ello vamos a hacer un caso de test sobre los valores limites, los cuales simplemente son un conjunto de datos de entrada que se encuentran en el borde de las clases de equivalencias de la entrada o salida(testear casos borde).Para el caso de múltiples entradas hay dos estrategias para combinarlas en un caso de test:
- Para cada clase de equivalencia se elegirán 6 casos limite + 1 normal, de estos 6 tenemos:
	- Los 2 casos de los limites
	- 2 casos que estén apenas adentro de los limites
	- 2 casos que estén apenas afuera de los limites
- Ejecutar todas las combinaciones posibles de las distintas variables
	- Por ende si tenemos n variables, tenemos $7^n$ casos de test

###### Grafo de Causa Efecto

Los análisis de clase de equivalencia y valores límites consideran cada entrada separadamente. Para manipular las entradas distintas combinaciones de las clases de equivalencia deben ser ejecutadas, cuya cantidad puede ser muy grande ya que si hay n condiciones distintas en la entrada que puedan hacerse validas o invalidas, entonces tenemos $2^n$ clases de equivalencia 

El grafo de causa-efecto ayuda a seleccionar las combinaciones como condiciones de entrada. 
Primero debemos identificar las Causas y Efectos y cuales causas pueden producir qué efectos(las causas se pueden combinar).
- Causa: distintas condiciones en la entrada que pueden ser verdaderas o falsas
- Efecto: distintas condiciones de salidas: verdaderas/falsas también 

Las causas y efectos son nodos del grafo, y las aristas determinan dependencia. Hay aristas positivas y negativas, además existen nodos and y or para combinar causalidad.
A partir del grado causa-efecto se puede armar una tabla de decisión, la cual lista las combinaciones de condiciones que hacen efectico cada efecto, esta puede usarcé para armar los distintos casos de test 

###### Testing de a Pares

Usualmente muchos parámetros determinan el comportamiento del sistema y muchos defectos involucran sólo una condición, esto se le llama defecto de modo simple
Pero no todos los defectos son de modo simple, ya que el software puede fallar en combinaciones especificas de estos parámetros. Estos defectos se revelan con casos de test que contemplen combinaciones apropiadas. Esto se denomina test combinatorio, el cual por obvias razones no es factible, es muy costoso. Por ello se investigo que la mayoría de tales defectos se revelan con la interacción de pares de valores, por lo cual solo necesitamos testear cada par, esto se conoce como testing de a pares. Un caso de test consiste en algún seteo de los n parámetros, el menor conjunto de test se obtiene cuando cada par es cubierto solo una vez  

###### Casos Especiales 

Los programas usualetne fallan en casos especiales. Estos dependen de la naturaleza de la entrada, tipos de estructuras de datos, etcétera.
No hay buenas regalas para identificarlos, una forma es adivinar cuando el software puede fallar y crear esos casos de test. Los casos especiales pueden ocurrir debido a suposiciones sobre la entrada, usuario, entorno operativo, negocio, etcétera 

###### Testing Basado En Estados

El test basado en estados se enfoca en el testing de estados y transiciones, se testean distintos escenarios que de otra manera podrían pasarse por alto. El modelo de estado se realiza usualmente luego de que la información de diseño se hace disponible, en este sentido, se habla a veces de testing de caja gris, dado que no es de caja negra puro.
Estos test se originan debido a que en algunos programas el comportamiento y la salida depende tanto de la entrada como del estado actual del sistema.  Para lograr testear esto un sistema se modela como una maquina de estados, donde cada estado representa un estado lógico de interés del sistema. Un modelo de estado tiene 4 componentes :
- Un conjunto de estados: son estados lógicos representando el impacto acumulativo del sistema
- Un conjunto de transiciones: representa el cambio de estado en respuesta a algún evento de entrada
- Un conjunto de eventos: son las entradas del sistema
- Un conjunto de acciones: son las salidas producidas en respuesta a los eventos de acuerdo al estado actual

##### Testing de Caja Blanca
El testing de caja negra se enfoca solo en la funcionalidad, mientras que el testing de caja blanca se enfoca en el código, el objetivo es ejecutar las distintas estructuras del programa con el fin de descubrir errores. Por ende, los casos de test se derivan del código

Tipos de testing estructural(test de caja blanca):
- Criterio basado en el flujo de control: Observa la cobertura del grafo de control
- Criterio basado en el flujo de datos: Observa la cobertura de la relación definición-uso en las variables 
- Criterio basado en mutación

###### **Criterio basado en flujo de control**
Considerar el programa como un grafo de flujo de control donde los nodos representan bloques de código y las aristas representan posibles transferencia de control del nodo i al j. Presenta 3 criterios:
- Criterio de cobertura de setnencia
- Criterio de cobertura de ramificaciones
- Criterio de cobertura de caminos 

**Criterio de cobertura de sentencias:** Cada sentencia se ejecuta al menos una vez durante el testing, por ende el conjunto de caminos ejecutados debe recorrer todos los nodos. Su limitación es que puede no requerir que una decisión evalúe a falso en un if si no hay else. Puede haber nodos inalcanzables 

**Criterio de cobertura de ramificaciones:** Cada arista debe ejecutarse al menos una vez en el testing, por ende cada decisión debe ejercitarse como verdadera y como falsa durante el testing. La cobertura de ramificaciones implica cobertura de sentencias. Si hay múltiples condiciones en una decisión no todas las condiciones se ejercitaran como verdadera y falsa

**Criterio cobertura de caminos:** Todos los posibles caminos del estado inicial al final deben ser ejercitados, esta cobertura implica cobertura de bifurcación. El problema es que la cantidad de caminos puede ser infinita, además que puede haber caminos no realizables 

###### Criterio basado en flujo de datos 

Se construye un grafo de definición-uso etiquetando apropiadamente el grafo de flujo de control. Hay 3 tipos de sentencias en el grafo de control:
- def: representa definiciones de una variable o reasignaciones 
- uso-c: cuando una variable se usa para computo
- usp-p: cuando una variable se usa en un predicado de transferencia de control

El grafo de def-uso se construye asociando variables a nodos y aristas del grafo de flujo de control:
- Por cada nodo i, def(i) es el conjunto de variables para el cual hay una definición en i
- Por cada nodo i, c-use(i) es el conjunto de variables para el cual hay un uso-c  en i
- Por cada arista (i,j),p-use(i,j) es el conjunto de variables para el cual hay un uso-p

Un camino puede estar libre de definiciones con respecto a una variable x en un camino i a j

Los criterios son bastante subjetivos ya que pueden ser del tipo:
- Todas las definiciones
- Todos los uso-p
- Todos los usos-c
- Algunos usos-c
- Algunos usos-p

##### Soporte con herramientas

Una vez elegido el criterio surgen dos problemas:
- ¿El test suite satisface el criterio?
- ¿Cómo generar el test suite que asegure cobertura?

Para determinar cobertura se pueden usar herramientas que normalmente son de asistencia, ayudando a visibilizar las sentencias o ramificaciones que quedan sin cubrir, por lo que el proceso de selección de caso de test sigue siendo mayormente manual 

##### Comparación y uso

Se deben utilizar tanto test funcionales de caja negra, como estructurales de caja blanca ya que ambas técnicas son complementarias:
- Caja blanca: Bueno para detectar errores en la lógica del programa o errores estructurales
- Caja negra: Bueno para detectar errores de entrada/salida o errores funcionales
Hay que tener en cuenta igualmente que los métodos estructurales son útiles a bajo nivel solamente ya que el programa es "manejable". Mientras que los métodos funcionales son útiles a alto nivel, donde se busca analizar el comportamiento funcional del sistema o partes de éste 

##### Testing Incremental

Hay objetivos contrapuestos, ya que el objetivo del testing es detectar defectos con un bajo costo, pero el incrementarlo para encontrar aun mas defectos aumenta el costo. La idea es ir agregando test a partes no testeadas incrementalmente, siendo esto esencial para conseguir:
- encontrar mas defectos
- identificación y eliminación  de defectos
En grandes empresas siempre se hace incrementalmente el testing 

##### Niveles de Testing 

Como dijimos anteriormente el código contiene defectos de requerimientos, diseño y codificación, donde la naturaleza de cada defecto es diferente dependiendo de en que etapa fue introducido. Por lo tanto se utilizan distintos niveles de testing para revelar los distintos tipos de defectos:

- Testing de unidad: Los distintos módulos del programa se testean separadamente contra el diseño, que actúa como especificación del módulo. Se enfoca en los defectos inyectados durante la codificación. Normalmente realizado por el mismo programador que realizo el módulo 
- Testing de integración: Se enfoca en la interacción de módulos de un subsistema, combinando módulos que ya fueron testeados unitariamente para formarlo, siendo este sujeto a testing de integración. Los casos de test deben generarse con el objeto de ejercitas de distinta maneta la interacción entre módulos 
- Testing del sistema: El sistema completo es testeado verificando si el sistema implementa los requerimientos. Normalmente es la etapa final del testing antes de la entrega del software 
- Testing de aceptación: Se enfoca en verificar que el software satisfaga las necesidades del usuario, Generalmente se realiza por el usuario en en su entorno y con datos reales. Solo después de que el testing de aceptación resulte satisfactorio, el software es puesto en ejecución
- Testing de desempeño: Requiere herramientas para medir desempeño 
- Testing de estrés: El sistema se sobrecarga al máximo, requiere herramientas de generación de cargas 
- Testing de regresión: Se realiza cuando se introduce algún cambio al software, verificando que las funcionalidades previas no se rompieron con la nueva incorporación


##### El Plan de Test:

El testing usualmente comienza con la realización del plan de test y finaliza con el testing de aceptación.
El plan de test es un documento general que define el alcance y el enfoque del testing para el proyecto completo, utilizando como entradas la SRS, el plan del proyecto y el diseño, e identificando que niveles de testing se realizaran, que unidades serán testeadas, etc. 

Es necesario hacerlo para asegurar que el plan de test es consistente con el plan de calidad del proyecto y que el cronograma de testing es consistente con el del proyecto

Usualmente contiene:
- Especificación de la unidad de test: Que unidad necesita testearse separadamente
- Características a testear: Esto incluye funcionalidad, desempeño, usabilidad, restricciones de diseño, etc.
- Enfoque: Criterios a utilizarse, cuando detenerse, como evaluar, etc.
- "Entregables": lista de casos de test utilizados, resultados detallados del testing, reporte resumido, etc.
- Cronograma y asignación de tareas 

##### Especificación de los casos de test

El plan de test se enfoca en cómo proceder y que testear, pero no trata con los detalles del testeo manual de una unidad. La especificación de casos de test se tiene que realizar separadamente para cada unidad determinando los casos de test de acuerdo con el plan. Conjuntamente con cada caso de test se especifica (esta es la justificación del caso de test):
- las entradas a utilizar
- las condiciones que este testeara
- el resultado esperado

La efectividad y costo del testing dependen del conjunto de casos de test seleccionado. Normalmente los caso de test elegidos son revisados por expertos, lo cual es otra razón para tener especificaciones de casos de test ya definidas(para ello es importante la justificación del test)

Para cada testeo se desarrolla una especificación de casos de test que se revisa y se ejecuta. La preparación de la especificación de los casos de test es una tarea exigente y que demanda tiempo ya que se pueden utilizar criterios para casos de test además de casos especiales y escenarios. Una vez especificados, la ejecución y verificación del resultado se pueden automatizar en scripts, lo cual es deseado si se necesita repetir el testing 

##### Registro de defectos y seguimiento

Un software grande puede tener miles de defectos, encontrados por muchas personas distintas, donde quien lo corrige no es necesariamente quien lo encontró. Debido a este gran alcance, el registro y la corrección de los defectos no puede realizarse informalmente. Normalmente los defectos encontrados se registran en un sistema seguidos de defectos que permite rastrearlos hasta que se cierren

Los defectos tienen su ciclo de vida durante el cual se registra información sobre el defecto en sus distintas etapas para ayudar al debugging y al análisis. Además normalmente los defectos se categorizan  en alguno tipos junto con la severidad de este en términos de su impacto en el software en:
- Critico: Puede demorar el proceso, afecta a muchos usuarios
- Mayor: Tiene mucho impacto pero posee soluciones provisorias 
- Menor: Defecto aislado que se manifiesta raramente y que tiene poco impacto
- Cosmético: Pequeños errores sin impacto en el funcionamiento correcto del sistema
Idealmente todos los defectos deben cerrarse, aunque algunas veces las organizaciones entregan software con defectos conocidos dependiendo de sus estándares de cuando un producto puede entregarse
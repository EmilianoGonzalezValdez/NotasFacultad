## Introducción

El software => Colección de programas,procedimientos,documentación y datos asociados que determinan la operación de un sistema de computación 

Las fallas de software siempre estuvieron presentes desde su desarrollo. No así las fallas mecánicas o eléctricas que son por el deterioro del tiempo. Es decir que la falla de software estuvo presente desde el principio, solo que nunca se había manifestado

El mantenimiento del software suele costar mas que el desarrollo y su motivo es para:
- Corregir errores residuales (Updates) => Mantenimiento Correctivo
- Mejorar funcionalmente el software y adaptarlo a los cambios del entorno (Upgrades) => Mantenimiento Adaptativo

La *Ingeniería del Software* es una aplicación de un enfoque sistemático,disciplinado y cuantificable al desarrollo,operación y mantenimiento del software
Un **Enfoque Sistemático** es una metodología y practicas existentes para solucionar un problema dentro de un dominio determinado. De esta forma podemos repetir dicho procedimiento y estimar los resultados


#### Enfoque

El enfoque de la *Ingeniería del Software* viene del problema de producir un software determinado por la idea de satisfacer las necesidades del cliente. El objetivo básico de la *IS* es buscar el **CYP**(calidad y productividad), los cuales estan rodeados del triangulo de hierro formado por la tecnología, la gente y el proceso. Pero tenemos otros factores que también modifican este enfoque:
1. Escala
2. Calidad
3. Productividad
4. Consistencia
5. Cambios

#### Escala
La *Ingeniería del software* debe tener en cuenta la escala del software a desarrollar, ya que no siempre los métodos para solucionar pequeños problemas funcionan con problemas de mayor magnitud. Por ende, estos métodos deben tener la capacidad de adaptación y respuesta del mismo a medida que aumenta la cantidad de usuarios o requerimientos al mismo. Para ello hay 2 claras dimensiones a considerar:
- Métodos de Ingeniería
- Administración del Proyecto
Los cuales en sistemas pequeños ambos pueden ser informales, pero al tratarse de un sistema grande, ambos deben ser formales 

**¿Que es un sistema grande o chico?**

| Pequeño   | Mediano         | Grande            | Muy Grande  |
| --------- | --------------- | ----------------- | ----------- |
| < 10 KLOC | < 10 a 100 KLOC | < 100 a 1000 KLOC | > 1000 KLOC |

#### Productividad
Un software que demora mucho tiempo en ser entregada o uno barato y de mala calidad son inaceptables. El costo del software se mide en Persona/Mes. La productividad asocia estas 2 ideas de forma tal que $\text{Si es mas alta} => \text{menor costo}/\text{Menor Tiempo}$ (aunque también dependa de la cantidad de personas)

#### Calidad
Claramente desarrollar software de alta calidad es otra motivación de la *Ingeniería del Software*, aunque la calidad de un software es difícil de definir. Su definición estándar se basa en 6 aspectos:
1. Funcionalidad: Capacidad de proveer funciones que cumplen las necesidades establecidas
2. Confiabilidad: Capacidad de realizar las funciones necesitadas en un tiempo determinado 
3. Usabilidad: Capacidad de ser comprendido, aprendido y usado
4. Eficiencia: Capacidad de proveer desempeño apropiado en base a la cantidad  de recursos usados 
5. Mantenibilidad: Capacidad de ser modificado con el propósito de corregir,mejorar o adaptar
6. Potabilidad: Capacidad de ser adaptado a otro entorno sin necesidad de realizar muchos cambios

Este concepto de realidad tiene muchas dimensiones como para reducirlo a un solo número, por ello cada en proyecto se elige que sera calidad para este, enfocándose en uno de los aspectos anteriores como principal. Normalmente se elige Confiabilidad. Se tienen 2 formas de medir la Confiabilidad
1. $\text{+fallas} = -\text{confiable}$
2. $\text{Calidad} = \text{Cantidad de defectos en software}/\text{tamaño}$

Normalmente el calculo seria  < 1 defecto /KLOC

#### Consistencia y repetitividad
Algunas veces un grupo puede desarrollar un software de buena calidad. Un objetivo clave de la *Ingeniería del software* es la sucesiva producción de sistemas de alta calidad y con alta productividad. Esta consistencia es la que nos permite predecir el resultado del proyecto con certeza razonable. Sin esta consistencia seria imposible estimar costos 

#### Cambios
El software debe cambiar para adaptarse a los cambios de la institución/empresa. Las practicas de la *IS* deben preparar al software para que estos cambios no sean abruptos, es decir que este sea fácilmente modificable. Los métodos que producen alta calidad, si no permiten cambios, no son útiles


La *IS* se enfoca mayormente en el proceso para conseguir los objetivos de calidad y productividad, siendo el **enfoque sistemático** el proceso que se utiliza.
La *IS* separa el proceso para desarrollar software del producto en si desarrollado. El proceso es quien determina en gran medida la **CYP**. Diseñar el proceso apropiado y su control es el desafió clave de la *IS*

#### El proceso de desarrollo en fases
El proceso de desarrollo consiste en varias fases, las cuales tienen una salida definida. Estas fases se realizan en el orden especificado por el modelo de procesos que se elija seguir. EL motivo de separar el desarrollo en fases es la *separación de incumbencias*: donde cada fase manipula distintos aspectos del desarrollo de software. Ademas cada fase permite verificar la calidad y el progreso al terminar. Este enfoque de desarrollo en fases es central en el enfoque de la *IS* para solucionar la solucionar la crisis de software

Estas fases en general son:
1. Análisis y especificación de los requerimientos
2. Arquitectura
3. Diseño
4. Codificación
5. Testing
6. Entrega y instalación 

Los enfoques sistemáticos necesitan que cada etapa se realice de forma rigurosa y formalmente

#### Administración del Proceso 
La administración del proceso establece cómo asignar los recursos a las distintas tareas, cómo organizarlas temporalmente, cómo asegurar que cada fase se desarrollo apropiadamente,etc. Sin la administración del proceso es virtualmente imposible cumplir con los objetivos de **CYP**. El planeamiento del proyecto es central en la administración del proyecto para poder determinar cuestiones como:
- ¿El proyecto se está desarrollando a término?
- ¿El proyecto procede acorde al presupuesto?
- ¿Se esta cumpliendo con los objetivos de calidad?
Las cuales son importantes para poder planear y administrar las métricas y medidas 

## Análisis y especificación de los requerimientos

En problemas pequeños es mas fácil comprender y especificar los requerimientos, en problemas grandes, en cambio, es mas difícil ya que hay grandes posibilidades de cometer un error

*Identificar y especificar* los requisitos necesariamente involucra interacción con la gente, no puede automatizarse. La fase de requisitos termina produciendo un documento con la especificación de los requerimientos del software(**SRS**). Es decir que esta **SRS** especifica lo que el sistema propuesto debe hacer 

##### ¿Pero, por que es tan importante la SRS?

La *SRS* establece las bases para el acuerdo entre el cliente/usuario y el desarrollador. En esta tenemos 3 partes involucradas:
- Cliente => Tiene necesidades
- Usuario => Tiene consideraciones 
- Desarrollador  => Debe entender lo que intentan comunicar el cliente y el usuario

Normalmente hay una brecha comunicacional entre estas partes ya que el:
- Cliente: No comprende el proceso de desarrollo de software
- Desarrollador: NO conoce el problema del cliente ni su área de aplicación 

La SRS es el medio para reconciliar las diferencias y especificar las necesidades del
cliente/usuario de manera que todos entiendan.

>[!INFO]- *Requerimiento* 
>- Una condición o capacidad necesaria de un usuario para solucionar un problema o alcanzar objetivos
>- Una condición o capacidad que debe poseer o cumplir un sistema

Estos requerimientos son difíciles de entender/discernir ya que visualizar el futuro sistema es complicado, al igual que visualizar sus capacidades. Además estos requerimientos cambian con el tiempo, por lo cual es muy importante realizar correctamente la SRS 

Principalmente por las siguientes 5 razones:
1. Ayuda al usuario a comprender sus necesidades
2. Los usuarios no siempre saben lo que quieren o necesitan. Deben analizar y comprender el potencial del sistema
3. EL proceso de requerimientos ayuda a aclarar las necesidades 
4. La SRS provee una referencia para la validación del producto final
5. Debería dar una clara comprensión de lo que se espera

>[!attention] Una SRS de alta calidad es esencial para obtener software de alta calidad

Los errores de requerimiento sólo se manifiestan en el software final. Para satisfacer los objetivos de calidad, se debe comenzar con una SRS de calidad 

Una buena SRS reduce los costos de desarrollo ya que a medida que avanza el proyecto, corregir los errores en la SRS es mas caro llegando a costar hasta un %40.

|            Phase            | Cost(person/hours) |
| :-------------------------: | :----------------: |
|       Requerimientos        |         2          |
|           Diseño            |         5          |
|        Codificación         |         15         |
|           Testing           |         50         |
| Instalación y mantenimiento |        150         |

#### Proceso de Requerimientos
*Proceso de Requerimientos* => Secuencia de pasos que se realizan para convertir las necesidades del usuario en una SRS. Este proceso debe recolectar las necesidades y los requerimientos y especificarlos claramente. Se puede dividir en 3 actividades:
1. ==Análisis del problema o requerimientos== => Más difícil ya que exige la recolección y extracción de estos
2. Especificación de los requerimientos
3. Validación 

Este proceso no es lineal, es iterativo y en paralelo. Hay superposición entre las fases (algunos requerimientos pueden estar siendo especificados mientras otros son analizados). Muchas veces especificar un requerimiento ayuda a su análisis; mientras que la validación puede mostrar brechas entre el análisis y su especificación 

```mermaid 
graph TD;
	Necesidades_del_Cliente --> Análisis
	Análisis --> Especificación
	Especificación --> Validación
	Validación --> Especificación
	Validación --> Análisis
	Especificación --> Análisis
	
```

La transición del análisis a la especificación es complicada. La especificación se enfoca en el comportamiento externo, mientras que el análisis tiene como objetivo comprender la estructura del problema y su dominio, sus componentes, entradas y salidas; además que en esta se recolecta mas información de la necesaria para la especificación 

El uso del análisis y las estructuras que lo construyen puede ser indirecto, ayudando a comprender en lugar de asistir a la especificación 

#### Análisis
El análisis se enfoca en la comprensión del sistema deseado y sus requerimientos. Normalmente se aplica un *Divide y vencerás*, es decir se divide el problema en partes mas pequeñas y se intenta comprender estas mini partesitas y su relación entre ellas
Normalmente se generan grandes cantidades de información, la cual debe ser organizada para su entendimiento; para ello se suelen usar métodos como diagrama de flujo de datos, diagrama de objetos,etc.

obsidian sync: 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
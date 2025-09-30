Un caso de uso captura un contrato entre el usuario y el comportamiento del sistema como *interacción*. Útil en la recolección de requerimientos ya que a los usuarios les agrada, comprenden el formato y reaccionan a este fácilmente. Son colecciones de muchos escenarios donde estos escenarios pueden llamar a otros casos de uso, organizando así jerárquicamente los casos de uso. Los casos de uso solo forman la parte funcional de la *SRS*
**Conceptos Básicos:** 
- Actor: Una persona o sistema diferente que interactúan con el sistema propuesto para alcanzar un objetivo. Los actores son entidades lógicas, por lo cual un actor transmisor y uno receptor son diferentes, aun si hacen referencia al mismo individuo
	- Actor primario: Es quien inicia el Caso de Uso, y este debe satisfacer su objetivo
	- Actor secundario: Es alguien que puede realizar la ejecución real en vez del actor primario, pero no tiene relación directa con el objetivo del caso de uso
- Escenario: Es un conjunto de acciones realizadas con el fin de alcanzar un objetivo bajo determinadas condiciones. Un paso es una acción lógicamente completa realizada tanto por el actor como por el sistema (Es una interacción entre el usuario y el sistema)
	- Escenario exitoso principal:  cuando todo funciona correctamente y se alcanza el objetivo
	- Escenario alternativo/excepcional: Cuando algo sale mal y el objetivo no puede ser alcanzado 

**Elaboración de casos de uso:**
1. Actores y objetivos:
	- Preparar una lista de actores y objetivos
	- proveer un breve resumen de cada caso
2. Escenarios exitosos principales:
	- Por cada cado de uso extender el escenario principal, proveyendo el comportamiento principal del sistema con este (puede revisarse para ver que satisface el interés de los participantes y actores)
3. Condiciones de falla:
	- Identificar y listar condiciones de falla para cada caso de uso
4. Manipulación de Fallas (maybe lo mas dificil):
	- Especificar el comportamiento del sistema para cada condición de falla

**Errores comunes:**
- Debe haber *interacción* entre los escenarios exitosos (Entre cada paso)
- Un caso de uso nunca puede ser iniciado por el sistema
- Los escenario excepcionales siempre deben hacer referencia a un punto del exitoso donde el sistema chequea algo 
- Las precondiciones de casos generales deben implicar las de los casos que se referencias adentro
- Seguir sintaxis dada en clase
- No hay lógica de programación (If's, loops, etc.)
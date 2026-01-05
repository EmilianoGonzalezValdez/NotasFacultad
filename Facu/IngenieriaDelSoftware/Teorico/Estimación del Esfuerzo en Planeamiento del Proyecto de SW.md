Dado un conjunto de requerimientos es deseable/necesario saber cuanto costara en tiempo y dinero el desarrollo del software. Normalmente el esfuerzo se mide en Persona/Mes. Lamentablemente no hay una forma fácil de estimar, normalmente la estimación mejora a medida que se incrementa la información sobre el proyecto.
**Un modelo intenta determinar la estimación del esfuerzo a partir de valores de ciertos parámetros**, los cuales dependen del proyecto. De esta forma el modelo reduce el problema de estimar el esfuerzo del proyecto al de estimar ciertos **parámetros claves** del proyecto, los cuales deben poder medirse en etapas muy tempranas del proyecto. Hay 2 enfoques:

- Estimación Top-Down: Se intenta determinar el esfuerzo total y luego calcular el esfuerzo de cada parte del proyecto. Primero se estima el tamaño global del proyecto en KLOC, luego se calcula $\text{esfuerzo} = a * \text{tamaño}^b$ donde a y b se determinan a través de análisis de regresión sobre proyectos pasados
- Estimación Bottom-Up: Primero identificamos los módulos del sistema y los clasificamos como simples, medios o complejos. Luego determinamos el esfuerzo total de codificación para cada tipo de módulo, obtenemos el esfuerzo total de codificaciones en base a la clasificación anterior y al conteo de cada tipo. Utilizamos la distribución de esfuerzos de proyectos similares para estimar el esfuerzo de cada tarea y por ultimo refinamos los estimadores anteriores en base a factores específicos del proyecto
- COCOMO:
	- Tiene enfoque top-down
	- Utiliza tamaño ajustado con algunos factores 
	- Procedimiento:
		- Obtener el estimador inicial usando el tamaño tal que $E = a*\text{tamaño}^b$  donde tanto $a$ como $b$ los sacamos en si el sistema es ==Orgánico, Semi-rígido o Rígido==
		- Determinar un conjunto de  factores de multiplicación representando distintos atributos
		- Ajustar el estimador de esfuerzo escalándolo según el factor de multiplicación final con la formula $\text{esfuerzo} = E * \prod_{k=I}^{15} {f_k}$, donde $\prod_{k=I}^{15} {f_k}$ es el factor de ajuste    
		- Calcular el estimador de esfuerzo de cada fase principal en base al tipo de sistema, hay un cuadro para cada tipo de sistema

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
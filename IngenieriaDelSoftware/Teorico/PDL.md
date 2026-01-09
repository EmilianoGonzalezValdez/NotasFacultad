A causa de una falta de un lenguaje optimo para el diseño detallado, es que existe **PDL** . Este tiene la sintaxis externa de un lenguaje de programación estructurado, pero su vocabulario es de lenguaje natural, lo cual nos da la libertad de ser tan específicos como nos parezca con el grado de detalle. Ahora veamos concretamente:

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
A este método se lo llama **Refinamiento Paso a Paso**, donde en cada paso descomponemos una sentencia o mas del algoritmo actual en instrucciones mas detalladas hasta que todas las instrucciones sean lo suficientemente detalladas como para llevarlas fácilmente al lenguaje de programación
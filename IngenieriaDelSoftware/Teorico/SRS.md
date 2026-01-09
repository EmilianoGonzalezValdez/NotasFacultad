La ***SRS*** establece las bases para el acuerdo entre el cliente/usuario y el desarrollador, siendo estas las 3 partes involucradas, entre las cuales, normalmente hay una enorme brecha comunicacional 
La SRS es el medio para reconciliar las diferencias y especificar las necesidades del cliente/usuario de manera que todos entiendan

Principales razones por las que sirve la SRS:
- Ayuda al usuario a comprender sus necesidades
- Los usuarios no siempre saben lo que quieren o necesitan. Deben analizar y comprender el potencial del sistema
- El proceso de requerimientos ayuda a aclarar las necesidades 
- La SRS provee una referencia para la validación del producto final
- Debería dar una clara comprensión de lo que se espera

Los errores de requerimiento sólo se manifiestan en el software final. Para satisfacer los objetivos de calidad, se debe comenzar con una **SRS** de calidad

>[!attention] Una SRS de alta calidad es esencial para obtener software de alta calidad


**Características de una SRS:**
- Correcta
	- Cada requerimiento representa precisamente alguna característica deseada por el cliente en el sistema final.
- Completa
	- Todas las características deseadas por el cliente están descriptas. La característica más difícil de lograr, para conseguirla uno debe detectar las ausencias en la especificación. Corrección y completitud están fuertemente relacionadas.
- No ambigua 
	- Si para cada requerimiento existe un solo significado. Si es ambigua los errores se colarán fácilmente. La no ambigüedad es esencial para verificabilidad. Como la verificación es usualmente hecha a través de revisiones, la SRS debe ser comprensible, al menos por el desarrollador, el usuario y el cliente. Particular atención si se usa lenguaje natural. Los lenguajes formales ayudan a “desambiguar”.
- Consistente
	- Ningún requerimiento contradice a otro
- Verificable 
	- Si existe para cada requerimiento algún proceso efectivo que puede asegurar que el software final satisface el requerimiento.
- Rastreable
	- Se debe poder determinar el origen de cada requerimiento y cómo éste se relaciona a los elementos del software. Hacia adelante: dado un requerimiento se debe poder detectar en qué elementos de diseño o código tiene impacto. Hacia atrás: dado un elemento de diseño o código se debe poder rastrear que requerimientos está atendiendo.
- Modificable
	- Si la estructura y estilo de la SRS es tal que permite incorporar cambios fácilmente preservando completitud y consistencia. La redundancia es un gran estorbo para modificabilidad, puede resultar en inconsistencia.
- Ordenada en aspectos de importancia y estabilidad
	- Los requerimientos pueden ser críticos, importantes pero no críticos, deseables pero no importantes. Algunos requerimientos son esenciales y difícilmente cambien con el tiempo. Otros son propensos a cambiar. => Se necesita definir un orden de prioridades en la construcción para reducir riesgos debido a cambios de requerimientos

**¿Qué debe tener una SRS?**
- Requerimientos de Funcionalidad
- Requerimientos de desempeño
- Restricciones de diseño
- Requerimientos de interfaces externas
###### Requerimientos de Funcionalidad
Es el corazón de la *SRS*, conforma la mayor parte de la especificación. Especifica toda las funcionalidades que el sistema debe proveer. Las salidas que se deben producir para cada entrada dada y las relaciones entre ellas. También describe todas las operaciones que el sistema debe realizar, las entradas validas y las verificaciones de validez para entrada y salida. Y especifica el comportamiento del sistema en caso de entradas invalidas, errores de calculo, es decir de situaciones anormales o situaciones normales con imposibilidades de seguir operando por x razón 
###### Requerimientos de desempeño
Se dividen en *Requerimientos dinámicos* los cuales especifican restricciones sobre la ejecución como:
- Tiempo de respuesta
- Tasa de transferencia o rendimiento
- etc.
En general se especifican los rangos aceptables de distintos parámetros, en casos normales y extremos

Y en los *Requerimientos estáticos* o de capacidad los cuales no imponen restricción en la ejecución como:
- Cantidad de terminales admitidas
- Cantidad de usuarios en simultaneo
- Etc.
Todos estos requisitos se especifican en términos medibles para ser verificados 

###### Restricciones de diseño
Existen factores en el entorno del cliente que pueden restringir las elecciones de diseño como limitaciones de hardware por ejemplo. 
###### Restricciones de interfaces externas 
Todas las interacciones del software con gente, hardware, y otro software debe especificarse claramente. Cabe recalcar que la interfaz del usuario debe recibir atención adecuada creando un manual preliminar indicando los comandos del usuario, los formatos de las pantallas, etc. Estos requerimientos también deben ser precisos para asegurar la verificabilidad.
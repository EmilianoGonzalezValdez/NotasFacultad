La idea de inundación dice que para enviar un paquete de un origen $u$ a un destino $v$ los caminos usados son aquellos que respetan las siguientes reglas:
- $u$ manda el mensaje por todas las líneas de salida
- Cada paquete que llega a un enrutador distinto de $v$ se reenvpia por cada una de las lpineas excepto aquella por la que llegó

Hay algunos problemas con la idea anterior:
- La inundación genera grandes cantidades de paquetes duplicados, a menos que se tomen algunas medidas para limitar el proceso
- Árbol de envío de paquetes. Cada arco representa un paquete que se envia
- Árbol de envío de paquetes es infinito con infinitos duplicados. O sea, se generan infinitas rutas. La causa es la presencia de ciclos en el grafo de la subred

Por eso, ahce falta limitar un poco el proceso de inundación dado en la idea anterior para resolver el problema. La solución es que cada enrutador recuerda *los paquetes difundidos* previamente por 'el para decidir si acepta un paquete
  

**Refinamiento de la solución de registro de paquetes difundidos:**
- El enrutador de origen pone *número de secuencia en cada paquete que recibe de sus host (así se distingue entre paquetes distintos del mismo enrutador de origen)*
- Un enrutador recuerda para cada enrutador de origen los números de secuencia recibidos
- Si llega un paquete a un enrutador con par <enrutador de origen, número de secuencia> recibido antes, no se lo reenvía

En la implementación para cada enrutador se usa una *tabla de registro de paquetes difundidos*.
Con esto podemos limitar que las listas enlazadas crezcan sin limites. ¿Como? Bueno vamos a agregar una columna llamada contador que indica el mayor número de secuencia tal que llegaron paquetes con todos los números de secuencia anteriores desde ese enrutador de origen.

Tambien existe **inundación con contador de saltos:** el cual integra un contador de saltos en el encabezado de cada paquete, que disminuye con cada salto y el paquete se descarta cuando el contador llega a 0.
**¿Como se determina el contador de saltos?**
Lo dieal es inicializar el contador de saltos a la *longitud de la ruta entre el origen y el destino*. Si el emisor desconoce el tamaño de la ruta, puede inicializar el contador en el peor caso, es decir, el *diametro total de la subred*

Y por ultimo **Inundación selectiva:** Es una idea para la inundación bastante práctica en donde:
- Los enrutadores no envían cada paquete de entrada por todas las lineas, sino solo por aquellas que van aproximadamente en la dirección correcta.
- El enrutador necesita almacenar información para poder aplicar inundación selectiva, especificamente:
- 	Se necesita saber en que dirección va cada linea
- 	Se necesita saber en qué dirección está el destino
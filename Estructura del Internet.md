La *internet*  está formada por billones de dispositivos de computación conectados entre si, pues esta es una red de redes que a su vez interconecta redes entre sí, donde para el envío y recepción de mensajes entre computadoras se usan *protocolos*  

Los hosts acceden a la internet a través de un *ISP de acceso* de alguno de los siguientes tipos:
- *ISP residenciales*
- *ISP empresarial*
- *ISP universitario*
- Celulares
- *ISP que proveen acceso a WiFi*

Para que 2 hosts que están conectados a diferentes ISP de acceso puedan enviarse paquetes entre si es necesario que dichos ISPs estén interconectados. Para eso las ISP de acceso son interconectadas a través de redes ISP nacionales e internacionales de más alto nivel llamados *ISPs de capa superior* o *globales de tránsito*. Estas mismas son ISP que proveen *servicios de tránsito* compitiendo entre si. Las mismas consisten en enrutadores de alta velocidad interconectados con enlaces de fibra óptica de alta velocidad.
Las ISP global de transito deben estar interconectadas entre si, y cada ISP debe ser manejada independientemente.
Como no todas los ISP globales de tránsito tienen presencia en cada ciudad o región del mundo, existen los *ISP regionales* a los cuales se conectan los *ISP de acceso de dicha región*, para luego conectar el ISP regional a los ISP globales de tránsito. En esta solución los ISP de acceso le pagan a su respectivo ISP regional, los cuales a su vez le pagan al ISP global de tránsito al que estén conectados.
Finalmente tenemos las redes proveedoras de contenido, las cuales se usan para reducir pagos a redes de tránsito global y para tener control sobre cómo sus servicios son entregados a los usuarios finales. Estas redes se conectan a las ISP regionales e ISP de acceso, y como ultima opción a una ISP de tránsito si no tiene de otra  

Si pensamos al internet como una red formada por niveles de jerarquía veríamos claramente 3 niveles tal que:
- En el **Nivel 1** tenemos: *ISP comerciales(globales de tránsito)* y *Redes proveedoras de contenido* 
- En el **Nivel 2** tenemos: *ISP regionales*
- En el **Nivel 3** tenemos: *ISPs de acceso*

Otra forma de ver la estructura del internet es como un conjunto de redes de distintos tamaños interconectadas entre si. Así las redes pueden tener diferentes tamaños, formas y cumplir distintos propósitos, donde varias redes pueden interconectarse entre sí para formar redes más grandes 
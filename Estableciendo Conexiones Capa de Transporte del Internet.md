Como al establecer una conexión se usan segmentos, una conexión debería tener un número de secuencia con el que comienza a operar.
La idea sigue siendo la misma, vincular el número inicial de secuencia de algún modo al tiempo y para medir el tiempo usar un reloj

La implementación de la idea de Tomlinson dice que:
- Cada host tiene un reloj de hora del dia. Los relojes de los host no necesitan ser sincronizados, se supone que cada reloj es un contador binario que se incrementa a si mismo en intervalos uniformes. El reloj continua operando aun ante la caída del host
- Cuando se establece una conexíon los k bits de orden mayor del reloj = *número inicial de secuencia*


Cuando un host se cae, al reactivarse sus ET no saben dónde estaban en el espacio de secuencia. Este es un problema porque para el siguiente segmento a enviar no se sabe qué números de secuencia generar; si se genera mal, entonces el nuevo segmento podría tener el mismo número de secuencia que otro segmento distinto circulando por la red.
Para solucionar esto vamos a requerir que las ET estén inactivas durante T segundos tras una recuperación para permitir que todos los segmentos viejos expiren (entonces no vamos a tener dos segmentos diferentes con el mismo número de secuencia)

**¿Cómo hacer para establecer una conexión entre dos host?**
Para establecer conexión el host de origen envía un segmento *CONNECTION REQUEST* al destino y espera una respuesta *CONNECTION ACCEPTED*.
Supongamos que se establecen conexiones haciendo que un host 1 envía segmento S = CR N, P a host 2 donde N es el número de secuencia y P es el número de puerto. Host 2 confirma ese pedido con segmento CA N

En este contexto puede pasar que S se demora demasiado en llegar a host 2, vence el timer en host 1 y host 1 manda un duplicado S'. Luego puede psar que host 2 reciba S' y un buen tiempo despues S
El problema con esto es que no tenemos forma de saber si un segmento CR que contiene un número de secuencia inicial es un duplicado de una conexión reciente o una conexión nueva, por ende el host no sabe si mandar un segmento CA o no.
La solución a esto es el *Acuerdo de las 3 vias* de Tomlinson de 1975 donde:
- En un caso de operación normal solo hay que fijarse en el número de secuencia del segmento de datos enviado
- En un caso de segmento CR duplicado con retraso. El host 1 rechaza el primer CA del host 2, al rechazar el host 1 del intento de establecimiento de conexión del host 2, el host 2 se da cuenta de que fue engañado por un duplicado con retardo y *abandona la conexión*; de esta forma un duplicado con retardo no causa daño
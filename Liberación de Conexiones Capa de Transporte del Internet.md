**¿Como hacer un protocolo para liberación de conexiones?**

La primera idea seria hacer un protocolo en el que:
- el host 1 dice "ya termine¿terminaste también?"
- Si el host 2 responde "Ya termine también. Adios", la conexipon puede liberarse con seguridad.
En la practica un protocolo asi no siempre funciona, porque existe el *problema de los dos ejércitos*

Hay 2 ejercitos azules rodeando a un ejercito blanco. Si los dos ejércitos azules atacan simultaneamente van a ganar. Por eso quieren sincronizar su ataque. Supongamos que el comandante del ejercito azul 1 manda un mensaje  "¿que le parece que ataquemos en el horario X?", el mensaje llega y el comandante del ejercito azul 2 contesta que está de acuerdo. Aun así el ataque no va a ocurrir puesto que el comandante del ejercito azul 2 no sabe si el mensaje fu recibido por el ejercito azul 1.

**SPOILER:** No existe un protocolo que resuelva el problema de los 2 ejercitos 

Para el caso de liberación de conexiones "atacar" equivale a "desconectar". Si ninguna de las aprtes está preparada para desconectarse hasta estar convencida que la otra está preparada para desconectarse también, nunca ocurrira la desconexión

Otra idea seria permitir que cada parte decida cuando la conexión está terminada. Este es un problema mas sencillo. Veremos cuatro escenarios de liberación de conexión usando un acuerdo de 3 vias. Aunque este protocolo no es infalible, generalmente es adecuado

**La liberación de conexión en un host significa** que la ET remueve la información sobre la conexión de su tabla de conexiones abiertas y avisa de alguna manera al dueño de la conexión


El caso normal:
1. Host 1 envía un segmento DISCONNECTION REQUEST e inicia un temporizador para el caso que no llegue DR de host 2
2. Al llegar DR al host 2, éste emite un segmento DR e inicia un temporizador para el caso de que no llegue respuesta de host 1
3. Al llegar esta DR el host 1 envía de regreso un segmento ACK y libera la conexión
4. Cuando el segmento ACK llega el host 2 tambien libera la conexión

Caso 2 Si se pierde el último segmento ACK:
- Al expirar el temporizador la conexión se libera de todos modos

Caso 3 Si se pierde el segundo DR:
- El host 1 no recibira la respuesta esperada, su temporizador expirará y todo comenzará de nuevo

Caso 4, Respuesta perdida y DRs subsiguientes perdidos:
Supongamos que todos los intentos repetidos de retransmitis la DR también fallan debido a la pérdida de segmentos:
- Tras N reintentos el emisor se da por vencido y libera la conexión
- Mientras tanto tambíen termina el temporizador del receptor y también se sale

El protocolo anterior falla si se pierde la DR inicial y N retransmisiones. El emisor se dará por vencido y liberará la conexión, pero el otro lado no sabrá nada sobre los intentos de desconexión y seguirá plenamente activo. Esta situación origina una *conexión abierta a medias*

Para evitar estas *conexiones abiertas a medias* hay varias soluciones. Una es evitar que el emisor se diera por vencido tras N reintentos, sino obligandolo a seguir insistiendo hasta recibir una respuesta. 
El problema de esta solución es que si se permite que expire el temporizador en el otro lado, entonces el emisor continuará eternamente, pues nunca aparecerá una respuesta

Otra manera de matar conexiones abiertas a medias es:
- Si no ha llegado ningún segmento durante una cierta cantidad de segundos al host 2, se libera automaticamente la conexión en el host 2
- Luego el host 1 detectará la falta de actividad y también se desconectara
- Esta solución también resuelve el caso que la red "se rompio" y los host ya no pueden conectarse

Para implementar esta idea es necesario que cada ET tenga un temporizador que se detenga y se reinicie con cada envío de un segmento.
Por esto mismo no se puede garantizar absolutamente que cuando se libera una conexión no occure pérdida de datos. Pero si se puede limitar mucho que esto suceda


#### Liberación de Conexiones

La *liberación simétrica:*
- Cada parte se cierra por separado, independientemente de la otra
- Una de las partes emite un DISCONNECT porque ya no tiene más datos por enviar y aun está dispuesta a recibir datos de la otra parte
- Una conexión se libera cuando ambas partes han emitido una primitiva DISCONNECT


La liberación simetrica es ideal cuando cada proceso tiene una cantidad fija de datos por enviar y sabe con certidumbre cuándo los ha enviado
En otras situaciones la determinación de si se ha efectuado o no todo el trabajo o si debe terminarse o no la conexión no es tan obvia
TCP trabaja con liberación simetrica


#### Liberación de una conexión TCP

En TCP los encabezados tienen un campo dedicado a la liberación de conexiones.
El campo *FIN* especifica que el emisor no tiene más datos que transmitir.
Tras cerrar una conexión, un proceso puede continuar recibiendo datos indefinidamente
Ambos segmentos, SYN y FIN, tienen número de secuencia y por tanto, tienen la garantía de procesarse en el orden correcto

**Resumen:**
- Para liberar una conexión cualquiera de las partes puede enviar un segmento TCP con el bit FIN establecido, lo que significa que no tiene más datos por transmitir, pero todavía puede recibir datos del otro lado
- Al confirmarse la recepción del FIN, ese sentido se apaga. Sin embargo puede continuar un flujo de datos indefinidos en el otro sentido
- Cuando ambos sentidos se han apagado, se libera la conexión
- Normalmente se requieren 4 segmentos TCP para liberar una conexión: un FIN y un ACK para cada sentido. Sin embargo es posible que el primer ACK y el segundo FIN estén contenidos en el mismo segmento, reduciendo la cuenta total a 3
- Una vez que el cliente manda el ACK al servidor, entra en un estado de espera llamado TIMED-WAIT
- El tiempo gastado en TIMED_WAIT es de dos tiempos de vida de paquete. TCP espera esta cantidad para garantizar que todos los paquetes de la conexión han muerto, en el caso que el ACK final se haya perdido
- Luego de la espera la conexión se cierra formalmente y todos los recursos del lado del cliente son liberados.
- Ambos extremos de una conexión TCP pueden enviar segmentos FIN al mismo tiempo. La recepción de ambos se confirma de la manera normal y se apaga la conexión. No hay diferencia entre la liberación secuencial o simultanea por parte de los hosts